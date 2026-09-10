# Understanding listener execution

This page explains how SIL listeners execute in Power Scripts for Jira Cloud, including the choice between synchronous and asynchronous execution modes. You'll learn when to use each execution type, how to manage multiple listeners for the same event, and important considerations like avoiding infinite loops and monitoring listener performance.

## Synchronous vs Asynchronous execution

Power Scripts for Jira Cloud operates independently from Jira and communicates through HTTP API calls. Despite this asynchronous architecture, you can configure individual listeners to execute in synchronous or asynchronous modes.

| **Execution mode** | **How it works** | **Use when** |
| --- | --- | --- |
| **Synchronous** | - The script executes immediately when the event occurs. - The triggering Jira operation waits for your script to complete before proceeding.   **Use with caution in Jira Cloud**  Synchronous listeners block the triggering Jira operation, meaning Jira waits for your script to complete before proceeding with its own process. This direct dependency can significantly impact Jira's performance and responsiveness. Long-running or failing synchronous scripts may lead to user experience degradation, timeouts, or affect the integrity of data operations. | - Fast issue updates are required, and your script has a short runtime. |
| **Asynchronous** | - The script is queued for execution after the Jira operation completes. - The original Jira operation proceeds immediately without waiting. - Your script runs independently on a separate thread.   Asynchronous listeners on Cloud let you directly modify issues within Jira. This means your background scripts can still update the same issues that triggered them, but these updates happen after the original operation is complete. | - Short update time is not required, and your script has a long runtime.   When using asynchronous listeners, monitor and adjust the thread pool accordingly to ensure optimal performance.   - Go to **Runtime** > **Queued Tasks** and track queued and executing listeners for bottlenecks. - If too many listeners queue up, consider optimizing scripts or adjusting execution timing. |

### **Performance recommendations**

Regardless of execution type, consider these best practices:

- Minimize the number of HTTP API calls in your scripts.
- Keep synchronous scripts under 30 seconds execution time.
- Use asynchronous execution for any script that might take longer than 30 seconds.
- Avoid complex processing in synchronous listeners to prevent user experience degradation.

---

## Execution order and multiple listeners

You can configure multiple listeners to respond to the same event.

- For Synchronous listeners, execution order matters and affects the final result. Scripts run in the sequence you define, and each can affect the outcome for subsequent scripts.
- For Asynchrnous listeners, the order only determines the triggering sequence, not the actual execution order. Since these run on separate threads, you cannot guarantee which will complete first.

While this is possible, it's not recommended as a best practice.

It can be helpful to use multiple listeners when:

- Different teams are managing separate integrations for the same event.
- Separating concerns (for example, one for validation, another for notifications).
- Gradual migration from old listeners to new ones.

### How to define execution order

1. Navigate to the SIL Listeners configuration page (**Power Scripts** > **Configurations** > **Automations** > **Listeners**).
2. Use the **Filter by event** dropdown to select the event for which you want to order existing listeners.

![Power Scripts for Jira Cloud upload and replace configuration](/cms_trial/assets/c234f281-b9d5-4b19-853f-22e9a64711e9.png)

1. Use the arrow buttons on the right side to arrange listeners in your preferred execution sequence.

Use one script per event whenever possible. This approach:

- Consolidates all execution logic in a single file.
- Provides optimal performance.
- Eliminates complex inter-script dependencies.
- Makes debugging and maintenance much easier.

---

## Preventing infinite loops

An infinite loop can occur if a listener script performs an action that subsequently triggers the same event, creating a continuous cycle. This is particularly relevant when the script's actions are performed using user credentials that Jira recognizes as legitimate event sources.

Let’s consider an example of a listener on the **Issue Commented** event with the following script:

```text
addComment(key, currentUser(), "One new comment!");
```

Here’s how the loop is created: When you add a comment to an issue where this listener is active, the `addComment` function will post a new comment on behalf of your user. This new comment then triggers the `Issue Commented` event again, causing the script to run, post another comment, and so on, creating an infinite loop.

Power Scripts does not automatically ignore events that it generates itself, because there are legitimate scenarios where you might want Power Scripts actions to trigger other listeners.

### Prevention guidelines

To stop an infinite loop, disable the listener and review your script. Some guidelines to consider include:

- When writing listener scripts, be especially careful with functions that mimic user actions or require direct user interaction, as these are particularly prone to causing infinite loops.
- Organize your code to minimize unintended re-triggering of events by carefully considering the user context (`currentUser()` vs. a specific user).
- Carefully consider the functions you use, especially those that interact with Jira, such as `addComment` and `updateIssue`.

- It is always recommended to test thoroughly in development environments before deploying listeners.