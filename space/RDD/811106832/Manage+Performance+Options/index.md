# Manage Performance Options

## Overview

Learn how to fine-tune your instance for optimal performance, tailored to your unique workflow.

## Global settings - Performance Options

### Set refresh time

Navigate to “Manage apps” (only admins) and to “Global Settings” under the Dashboard Hub section. Change to the “Performance Options” tab and select the **Auto refresh time interval**.

![Dashboard Hub auto refresh time interval setting](/cms_trial/assets/a8f78e6b-aa28-4d61-b7a3-6a8b4b9ef6b2.png)

Improve the performance of your instance by disabling or increasing the time of the automatic data refresh. If you **disable auto refresh**, the data will still be updated when you reload the dashboard.

- Default: All the Jira, Confluence, and monday.com gadgets are updated every 3 minutes. Opsgenie, Atlassian Marketplace, and gadgets from the “Other” category every 15 minutes. Exceptionally, the Historical Uptime from StatusPage is updated every 5 hours.
- No refresh: Stop automatically updating gadgets, recommended for large instances. Data is still updated when the dashboard is reloaded.
- [5 - 1440] minutes: All gadgets are automatically updated with the selected cadence in minutes.

[High priority](/cms_trial/space/RDD/146309328/How+to+manage+dashboards/) gadgets are not affected by this change, and are updated every minute.

If you **disable auto refresh**, the data will still be updated when you reload the dashboard.  
**Windows**: Hold down Ctrl and press F5 (*Chrome*), or hold down Ctrl and ⇧ Shift and then press R (*Firefox*).  
**Mac**: Hold down ⌘ Cmd and ⇧ Shift key and then press R (*Chrome* and *Firefox*), or hold down the Option + ⌘ Cmd key and then press the ‘E’ key (*Safari*).

### Set issue limit

Read the dedicated page to learn how to set the default maximum issue limit: [Set the Default Maximum Work Item Limit](/cms_trial/space/RDD/1069711378/Set+the+Default+Maximum+Work+Item+Limit/)

## See also