# Forms and Wizards

The Forms and Wizards feature lets you design custom actions in Jira Cloud that enable users to modify issues and execute tasks without advancing through workflow transitions.

With this feature, you can create various interface options for users, such as:

- Interactive forms and wizards that appear in panels within the Jira issue view (in the right column or the main body of the issue screen).
- Configurable buttons that serve as multiple entry points, each opening a different form or wizard within an issue.

This streamlined approach significantly reduces maintenance costs, simplifies development and configuration, and lets you implement complex actions without duplicating configuration throughout your workflow.

Watch this video for a brief overview of the Forms and Wizards feature:

Transcript

In this video, you'll learn how to create custom interactive panels in Jira using forms and wizards, a new powers scripts feature for Jira cloud.

Let's start with a simple form. Go to Apps, then Power Apps Config, Advanced, Forms and Wizards, and click **Add form**. Give your form a name. Choose which projects and issue types should show it. Pick where it appears on the screen and hit **Save**. Now you'll configure three SIL scripts. The condition script controls when users see your form. The screen script defines what fields they'll fill out and the action script decides what happens when they submit. That's it. Your form is live.

Want multiple options? Toggle on buttons when creating your form. Each button gets its own set of those same three scripts, giving users different actions to choose from. Here's how it looks when a user opens  
the buttons enable form on the right side of the work item. Need something more complex? Just add extra steps to create a multi-step wizard instead. Users can work through your process one screen at a time. Here's how a user can access the wizard. you configured on the left side of the work item.

Whether it's a simple form, multiple buttons, or a step-by-step wizard, you now have the tools to customize Jura exactly how your team works.

---

## What you need to know about actions

Forms and Wizards is the cloud version of the Power Actions for Jira DC app.

In this context, an action refers to a customizable, interactive operation that users can execute within a Jira issue panel.

- Actions can be presented as standalone forms, multi-step wizards, or as a collection of buttons that each trigger their own form or wizard.
- An action has the same activation structure as a workflow transition and can be performed regardless of the issue status as long as the action condition is met.
- Each action is controlled by a set of SIL scripts that determine its visibility, user interface, and functional behavior.

---

## The interface options

The Forms and Wizards feature provides the following customizable interfaces within Jira issues:

- **Forms** provide a simple single-screen interface with all input fields visible at once. Forms are ideal for simple, straightforward tasks.
- **Wizards** break complex processes into manageable steps, with each screen building upon previous selections. This multi-step approach supports:

  - Integration with external databases or LDAP directories
  - Creation of sophisticated decision paths based on earlier user choices
  - Dynamic content that adapts to user inputs across multiple screens
- **Buttons** serve as distinct entry points to different forms or wizards within a single panel. Each button:

  - Acts as a gateway to its own complete form or a multi-step wizard
  - Allows administrators to organize complex functionality into intuitive, purpose-specific options
  - Enables multiple forms to coexist within the same panel without overwhelming the user.

---

## How it works

The Forms and Wizards feature is built on three essential script components that work together as building blocks to create dynamic, interactive experiences within Jira issue panels.

| **Script component** | **Description** |
| --- | --- |
| Condition script | Controls the visibility and availability of actions. You can make actions:   - Available (enabled) for users to execute - Visible but unavailable (disabled) based on specific conditions - Hidden entirely when not applicable |
| Screen scripts | Defines the user interface for gathering information. This script lets you:   - Create rich, interactive forms with various input types - Add HTML to provide context and instructions - Customize buttons, titles, and field attributes |
| Action script | The engine that performs the actual work after all information is gathered. This script can:   - Process user input from the form - Perform validations and provide feedback if errors occur - Execute complex logic using our Simple Issue Language (SIL) - Modify issue values or take conditional actions |

These three scripts operate as complementary components within a unified framework, providing a complete solution that guides Jira users through complex actions while maintaining data consistency and adhering to your business rules.

By separating the condition, interface, and execution layers, Forms and Wizards give you flexibility in designing and implementing user interactions in Jira without the traditional constraints of workflow transitions.

---