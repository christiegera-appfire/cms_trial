# SIL Listeners

SIL Listeners automatically execute custom scripts when specific Jira events occur. They serve as integration points that help synchronize your Jira instance with external systems, enforce business rules, or automate workflows.

## How listeners work

When a Jira event occurs (such as creating an issue or adding a comment), Power Scripts detects the event and executes your configured listener script.

At its core, a listener is defined by two elements:

- The script the listener executes.
- The events it's configured to react to.

Power Scripts for Jira Cloud operates independently from Jira and communicates through HTTP API calls, making all interactions inherently asynchronous. However, you can configure individual listeners to execute in two modes:

- **Synchronous execution**: The script runs immediately and can affect the triggering operation.
- **Asynchronous execution**: The script runs in the background without blocking Jira operations.

For detailed guidance on choosing the right execution mode, see [Understanding Synchronous vs Asynchronous execution](/cms_trial/space/PSJC/513278324/Understanding+listener+execution/).

---

### In this section:

- [Listener configuration](/cms_trial/space/PSJC/490998110/Listener+configuration/)
- [Understanding listener execution](/cms_trial/space/PSJC/513278324/Understanding+listener+execution/)
- [Understanding listener script context](/cms_trial/space/PSJC/490998238/Understanding+listener+script+context/)
- [Listener implementation examples](/cms_trial/space/PSJC/490998290/Listener+implementation+examples/)