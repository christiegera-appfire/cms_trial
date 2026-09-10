# Add a comment to a linked issue in a service management project

---

|  |  |
| --- | --- |
| **Goal** | Create a rule that adds a comment to a linked issue in a Jira service management project so the support team is aware of the status. |
| **Scenario** | You want to add a predefined comment to issues that are done so the support team is quickly notified of the status. |
| **Components** | - [Update Any Issue Field](/cms_trial/space/JSUCLOUD/12518373/Update+Any+Issue+Field+post+function/) post function |
| **Scope** | This scenario uses JQL to set the scope for related issues |

## How to configure this rule

1. Create a draft of your project workflow. If you're unsure how to get to this page, follow the onboarding steps in [Edit a Jira Workflow](https://appfire.atlassian.net/wiki/spaces/JSUCLOUD/pages/12519274). You can then view your workflow in Text or Diagram mode. The steps in this use case represent Text mode.
2. Select the transition for which you want to run the post function. In this case, we are using the Done transition.

   ![Screenshot of the draft workflow page in text view with the Done transition highlighted.](/cms_trial/assets/c6cf7e37-c54f-410a-9ab5-6fcbcfd9a36b.png)
3. On the workflow *Transition* page, select the *Post Functions* tab, then select **Add Post Function**.
4. Select the *Update any issue field (JSU)* post function, then click **Add**.
5. Complete the required fields to configure the post function:

   1. *Update field on all issues related as*: Select **JQL**. The JQL you enter here should reference the service management project. Our project is called Customer Support, so we use:  
      `issue in linkedIssues({issue.key},"relates to")and project="Customer Support"`
   2. *Perform as User*: Choose the user to initiate the rule. The comment will be associated with the user. In this example, the user is the JSU app. You can select a specific user, or select the initiating user for full transparency. The initiating user is the user who transitioned the bug to done.
   3. *Issue Field*: Select **\*\*\*new comment\*\*\***.
   4. *Field Value*: Enter the note to be added to the linked issue. For example, `The bug fix linked to this support issue is done and released.`

      ![The Update Any Issue Field Screenshot of the Update any issue field post function configured as described on this page.](/cms_trial/assets/d9821e87-d453-433e-b8a1-fd5db477bbdb.png)
6. Click **Add** at the bottom of the page. The summary of the post function is displayed.
7. Click **Publish Draft** at the top of the page.

## Test the rule

We recommend that you build and test your rules in a test project.

1. Go to the bug issue that is linked to a support ticket.
2. Move the issue to done (or the equivalent status in your workflow). The comment you created is displayed in the Comment section of the linked support issue.

   ![Screenshot of the support issue with the comment described on this page.](/cms_trial/assets/ce5c065a-3307-410b-9003-ca29d0846c86.png)

## Related pages

- [Perform As User](/cms_trial/space/JSUCLOUD/12518776/Perform+As+User/)
- [JQL use cases](/cms_trial/space/JSUCLOUD/12518307/JQL+use+cases/)
- <https://support.atlassian.com/jira-service-management-cloud/docs/use-advanced-search-with-jira-query-language-jql/>