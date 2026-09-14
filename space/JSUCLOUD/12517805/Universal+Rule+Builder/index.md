# Universal Rule Builder

**A new rule builder experience is coming**

We’re updating the Universal Rule Builder with a more flexible interface for creating rules with multiple actions, conditions, and nested logic.

Configurations created in the current rule builder will be migrated automatically and will remain available in the new experience. You don’t need to recreate them or take any action before the update.

The instructions on this page describe the current beta interface and may differ from the upcoming experience.

## A new editor experience

![admin-AddRule.png](/cms_trial/assets/99945761-08f9-457a-947f-7c01f37debe1.png)

JSU’s **Universal Rule Builder** is a faster and simpler way to build and visualize automation rules for your Jira workflows. You can build simple or complex rules - Actions (post functions), Conditions, and Validators - from a common interface, eliminating the need to navigate through Jira multiple times to add your desired workflow changes with JSU. The Universal Rule Builder lets you review your complete rule summary in a IF-THEN format, edit the included configurations, and change their order before saving the rule, so you can quickly configure and fine-tune the rules you want from the start.

## What’s in the release?

This revamped Rule Builder covers all functionality previously available through JSU - all Conditions, Validators, and Post Functions (now called Actions in Jira Workflows) are now available in the Rule Builder. Don’t worry, all of your existing JSU rules remain intact. The new feature will not change or replace anything in your existing rules. You can still create and edit rules in the usual way, using individual components (post function, precondition, or conditions) in the old editor experience. New rules that you build with the Universal Rule Builder are managed strictly through the new editor.

### Limitations

## Using the Universal Rule Builder

You can access the Universal Rule Builder through the Jira workflow editor; when adding a Condition, Validator, or Action (Post function), you can select the **JSU Rule Builder** component.

**Note**: Unlike previous versions of JSU, the Universal Rule Builder can be used in both team-managed and company-managed spaces.

1. Open your workflow and select the transition that will trigger your rule. Alternatively, in Text mode, select the transition name.
2. In the right-hand panel, click the **Add** button for the type of rule you want to create. For example, to add an Action (post function), click the **Add** button for **Perform actions**.
3. Select the *JSU Rule Builder - Actions* post function, and click **Select** at the bottom of the window. The Universal Rule Builder opens.

We recommend that you build and test your rules in a test project.

![Resized.mp4](/cms_trial/assets/b48c1897-0b20-42f0-ad19-d7c4db9b9e69.mp4)

---

## Build a rule with the Universal Rule Builder

On the left side of the Universal Rule Builder, you can see the rule overview, starting with a transition selector pre-populated with your selected transition (**Point 1**, **Figure 2**, below). To change the triggering transition, simply select it from the pulldown.

The exact details of the Rule Builder depend on the type of rule you’re building. Refer to the specific documentation for each type for more information.

Overall, the logic of your rule is displayed on the left - each component (a Condition, Validator, or Action) as well as any associated conditional logic (**Point 2**, **Figure 2**, below). The right panel changes based on what you have selected in the left panel:

- When you first create a rule, the right panel displays the general configuration - the rule’s name, Description, and any other options
- When adding a component, the right panel will display the list of available components (**Point 3**, **Figure 2**, below)
- When you select a component to add, or select an existing component, the right panel displays the configuration options for that component

![admin-RuleOverview.png](/cms_trial/assets/da2e19e2-4711-49f1-a346-5d2077b4278e.png)

To help you get started, several [use cases](/cms_trial/space/JSUCLOUD/12518487/Use+cases/) are available to build common automations.