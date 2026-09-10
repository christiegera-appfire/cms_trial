# How to transition an issue based on a custom field value using the JMWE app

This article explains how to transition an issue based on a custom field value using <https://appfire.atlassian.net/wiki/spaces/JMWE/pages/462127732> post function.

**Use case**: Based on the custom field, *Question,* with value “Yes” or “No” transition of the current issue happens. If the selected value is *Yes,* the issue shall go to Review status and if the value is selected as *No,* it shall go to Done status.

## Instructions

1. Navigate to the desired workflow transition and add the *Transition Issue* post function.
2. Add the target transition Id of the specific workflow and custom field Id based on your Jira instance.

   ![JMWE for Jira Cloud workflow configuration for custom fieldbased issue transitions](/cms_trial/assets/2b052cf9-f20c-4aea-b3c4-a5edf25dbbfd.png)
3. Enter the below Condition Execution which will make sure to execute the post function when this condition is true.

   ![JMWE for Jira Cloud custom field value display for transition workflow configuration](/cms_trial/assets/df641ef5-1108-4afe-8af2-c923ba355d49.png)
4. Add the following post function.

   ![JMWE for Jira Cloud transition configuration showing field valuebased workflow logic](/cms_trial/assets/ad1acde1-8c05-4303-b10a-63988d428831.png)
5. **Publish** the workflow and execute the scenario.