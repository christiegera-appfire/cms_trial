# Resolved Issues

## Overview

This gadget displays the number of issues resolved in a specific period in a sprint. It also compares the number of resolved issues in the previous sprint, indicating the change percentage: red if the number of resolved issues is lower than the previous period, and green when there are more resolved issues than the previous sprint.

![Dashboard Hub resolved issues dashboard gadget](/cms_trial/assets/383a613c-67b8-435b-9f58-4ea0aeecc20e.png)

## Configuration

1. Provide a meaningful name for the gadget so everyone knows what information it displays.
2. Complete the remaining fields as applicable:

   1. The datasource, where **Current** indicates the Jira instance where the app is installed.
   2. The project and the board where the issues are located. By default, all the issues are displayed, no matter the active sprint they belong to, in case there are parallel sprints.
   3. Choose whether to use the current settings for all the compatible gadgets in the dashboard. This option avoids configuring the rest of the gadgets individually.

## Dashboards

This gadget appears in the following dashboard: [Scrum software team template](/cms_trial/space/RDD/146310016/Scrum+software+team+template/).