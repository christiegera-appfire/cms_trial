# Overview (App configuration)

## Security and access

Only Jira/App Admins can manage the app on the global (app) configuration level.

To access the global settings for the Overview module:

1. Click the **wrench icon** in the top right corner.
2. Select **Modules** from the dropdown.
3. You are now on the **Overview** page.

## Overview configuration

![Overview configuration on the app configuration page.](/cms_trial/assets/aeb88279-2a8e-4df0-9db7-36a15a792bd8.png)

### Box scope aggregation

Set the time interval in which the app will recalculate box scope aggregations. These settings affect boxes with [auto scope-based](/cms_trial/space/SPM/1918669073/Period+mode+and+sequentiality/) period mode.

The smaller the value, the better the app's performance. The recommended interval time is 60 seconds. To change the default interval time, enter a new value in the **Box scope aggregation re-calculation interval** field.

### Box auto-archiving

Use this function if there are many boxes that are no longer used. Archiving boxes can improve the app’s performance. By default, archived boxes will be hidden in the Overview module, making it easier to focus on current tasks. Aggregations will no longer be calculated for archived boxes.

A box is only archived if the entire cluster or branch has not been used for some time. For example, if no one interacts with the "Own" scope box for some time but its sub-boxes are still used, the box and its sub-boxes will not be archived automatically.

![Box auto-archiving setting.](/cms_trial/assets/122fa588-ae25-4373-831d-24b8808fd38f.png)

To enable box auto-archiving, toggle the switcher on and define the inactivity period required to trigger auto-archiving.