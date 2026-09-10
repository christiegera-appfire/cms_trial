# Universal Rule Builder

**A new rule builder experience is coming**

We’re updating the Universal Rule Builder with a more flexible interface for creating rules with multiple actions, conditions, and nested logic.

Configurations created in the current rule builder will be migrated automatically and will remain available in the new experience. You don’t need to recreate them or take any action before the update.

The instructions on this page describe the current beta interface and may differ from the upcoming experience.

## A new editor experience

JSU’s Universal Rule Builder BETA is a faster and simpler way to build and visualize automation rules for your Jira workflows. You can build simple or complex rules from a single place, eliminating the need to navigate through Jira multiple times to add your desired workflow changes with JSU. The Universal Rule Builder lets you review your complete rule summary in a When-if-then format, edit the component configurations, or change their order before saving the rule, so you can quickly configure and fine-tune the rules you want from the start.

## What’s in the beta release?

We have included simplified versions of two of our most popular post functions for you to try out. Don’t worry, all of your existing JSU rules remain intact. The new feature will not change or replace anything in your existing rules. You can still create and edit rules in the usual way, using individual components (post function, precondition, or conditions) in the old editor experience. New rules that you build with the Universal Rule Builder are managed strictly through the new editor.

The beta version of the Universal Rule Builder provides a new way to use the following features:

- new Clear Field Value post function
- Update Any Issue Field post function
- Trigger a Linked Transition post function
- *Related Issue Status* precondition (new IF precondition that you can add to a post function)

We will continue to release additional features to the Universal Rule Builder based on your feedback, and we will provide you with opportunities to share your thoughts directly within the app.

### Beta limitations

- **Update Any Issue Field** and **Clear Field**: These can only be performed within the *same* issue; there are no issue relation options.
- **Trigger a Linked Transition**: This post function can apply only to parent or subtask.
- **Run as User**: Rules are always executed as the JSU User.

## How can I access the Universal Rule Builder?

You can access the Universal Rule Builder through the *Add Post Function* option when editing a draft workflow in Jira. Like all JSU features, the Universal Rule Builder can only be used when working with *company-managed* projects.

1. Navigate to your project workflow and select **Edit** to create a draft.
2. In Diagram mode, select the arrow for the transition that will trigger your rule. Alternatively, in Text mode, select the transition name.
3. Select **Post Functions** from the *Options* menu. If you are in Text mode, select the *Post Functions* tab.
4. Select **Add Post Function**.
5. Select the *Access the Universal Rule Builder from JSU* post function, and then click **Add** at the bottom of the page. The Universal Rule Builder displays.

We recommend that you build and test your rules in a test project.

![Resized.mp4](/cms_trial/assets/b48c1897-0b20-42f0-ad19-d7c4db9b9e69.mp4)

---

## Build a rule with the Universal Rule Builder

On the left side of the Universal Rule Builder, you can see the rule overview, starting with a WHEN statement representing your selected transition. The components you use to build your rule are displayed on the right side. To change the triggering transition, navigate back to the workflow editor in Jira, select the transition, and then add the post function for the Universal Rule Builder again.

If you don’t see a component that you need in the URB, use the request button at the bottom of the components list and tell us about it.

![The Universal Rule Builder in JSU.](/cms_trial/assets/fa0c876e-52c8-44f0-a826-e7880e27e27b.png)

To help you get started, we will add a simple rule to trigger a transition on a linked issue.

**Step 1: Select a component**  
In the **All Components** list, select your required component. It displays in the rule overview. In this example, we selected the *Trigger a Linked Transition* post function.

![A fully configured rule using the Trigger a Linked Transition post function in the Universal Rule Builder.](/cms_trial/assets/7efd3c3e-4ffe-4116-ac0a-b6529d620273.png)

**Step 2: Configure the component**  
Set the parameters for your component to define the outcome of your rule.  
**What**: Select the type of issue that you want to transition to the new status. Here, we selected the *Subtask(s) of the parent*.  
**Where**: Select the status that you want to move the issue to. You can filter the list of available statuses by selecting a different workflow if required under *Advanced/Optional settings*.

**(Optional): Add more components**   
Select **Add Component** to display the list of available options.

To change the order of a component within the rule Overview, drag it to the desired position. To remove a component, select the **More** **options** menu (**⋮**), then select **Delete Component**.

**Step 3: Name your rule**  
 In the *Name* field, enter a name. Choose a name that helps you identify what the rule does.

**Step 4: Save your rule**  
Select **Add** below the Overview to save your rule. Your complete rule is displayed in the *Post Functions* tab on the selected transition page. To make any changes, select the **Edit** icon for the corresponding rule.

![Summary of the rule in the draft workflow showing the location of the Edit option.](/cms_trial/assets/a3b9e642-618c-4157-abda-c406dd0e6c16.png)

**Step 5: Publish your draft workflow**  
Select **Publish Draft** at the top of the draft Workflow page, and then test out your rule by creating some test issues and subtasks.

See [My Workflows](/cms_trial/space/JSUCLOUD/12519535/My+Workflows/) to learn how to view all your saved JSU rules in one place.

## Related pages

- [Use Case: Close Parent Issue When All Subtasks are Closed](https://appfire.atlassian.net/l/cp/kuimUCD0)
- [Use Case: Remove Assignee When an Issue Moves Back to To Do](/cms_trial/space/JSUCLOUD/49775577/Remove+assignee+when+an+issue+moves+back+to+To+Do/)