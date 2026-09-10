# Build-your-own (scripted) Condition

A workflow condition that hides/shows a transition based on the result of a [Jira expression](/cms_trial/space/JMWEC/465241623/Using+Jira+Expressions/).

The transition to which the condition is added will be available only if the Jira expression returns `true`. This can be used to test or compare issue fields, to test linked issues, to check for open Sprints, etc.

![Build Your Own Condition No Code option](/cms_trial/assets/202e09eb-fe8e-4be8-831a-5cd656378c30.png)

When you add this condition to a transition, the extension checks the result of a logical test, comparing a field value to either another field value or to a set value. The logical test can be a [Jira expression](/cms_trial/space/JMWEC/465241623/Using+Jira+Expressions/) entered manually, or you can build an expression using the *No Code* option (see below). If the expression returns `true`, the transition will be available to the user; if it returns `false` or a non-Boolean value, the transition will be hidden.

To add a condition:

1. Log into your Jira Server instance as an Administrator.
2. Click on the **Settings** icon ⚙️ in the upper right corner.
3. Select **Issues**.
4. In the left-hand panel, click **Workflows**.
5. Click **Actions** ( ▢ ) for the workflow you want to edit and select **Edit**.
6. Edit the Transition:

   1. When viewing the Workflow in **Diagram** view, select the Transition and click the **Conditions** link. Click **Add condition** at the top of the list of existing conditions.
   2. When viewing the Workflow in **Text** view, click the name of the Transition then select the **Condition** tab. Click **Add condition** at the top of the list of existing conditions.

## Configure the condition

1. Follow the steps above to add a condition to a transition.
2. From the list of validators, select *Build-your-own (scripted) Condition (JMWE app)*.
3. The *Build-your-own (scripted) Condition*page will open. Configure the condition as needed:

   1. Set the **Description**.
   2. For **Choose type**, select either *No Code* or *Jira Expression* as the method of creating the logical test. See below for details on each of the configurations.
4. Click **Add**.

Note that you will need to publish the workflow for the new Condition to take effect.

![Build-your-Own Condition Jira Expression option](/cms_trial/assets/c612c99b-5db6-476a-89d9-7e5664624603.png)

The following configurations are available:

- **Description** - Give the condition a description; this will be included in the list of conditions for the transition and in the [Workflow Extensions](/cms_trial/space/JMWEC/466321411/JMWE+workflow+extensions/) administration page.
- **No Code** (Figure 1, above) - These fields will only display when **Choose type** is set to *No Code*. Select this option to create the condition without the need to write a Jira expression. Set each of the following options:

  - **Field** - Select the field to be tested.
  - **Operator** - Select the logical operation to use in the test; for example, *Equals*, *Does not equal*, *is empty*, *Less than*, or *Greater than* (among others).
  - **Value to compare type** - Select against what value the test will be evaluated:

    - *Field* - Compare the condition field against the value(s) of another field.
    - *Text* - Compare the condition field against a set value.
  - **Value to compare** - Either select a field from the pulldown menu, or enter a set value.
- **Jira Expression** (Figure 2, right) - The [Jira expression editor](/cms_trial/space/JMWEC/466225418/Jira+Expressions+Editor/) will only display when **Choose type** is set to *Jira Expression*. Enter the [Jira expression](/cms_trial/space/JMWEC/465241623/Using+Jira+Expressions/) for the logical test for the condition. If this test evaluates to `false`, the condition will fail and the transition will not be available for selection.

### Computed Expressions

![Computed Expression field showing the JavaScript result of configurations](/cms_trial/assets/8b69f7bb-8687-4c68-bd79-ba7282ee1d78.png)

If you use the *No Code* option to create your condition, the **Computed Expression** box (Figure 3, right) will populate with the equivalent Jira expression for your configurations. You will not be able to alter the script, but it is possible to test the script and to copy the script so it can be pasted elsewhere.

Click **Test** ( ▢ ) to open a window where you can select an issue against which the script should be tested.

Click **Copy** ( ▢ ) to copy the script to your clipboard.