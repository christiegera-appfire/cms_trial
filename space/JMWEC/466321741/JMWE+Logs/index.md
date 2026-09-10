# JMWE Logs

You must be logged in as an administrator to view or use this page.

![JMWE for Jira Cloud logs administration panel with detailed logging information](/cms_trial/assets/8247dddc-05a3-4f9e-a553-c20b7b8c6b03.png)

The **JMWE Logs** administration page (Figure 1, right) details the most recent events logged by JMWE for your Jira Cloud instance. From here, you can configure the logging level for JMWE installation, configure Webhooks to receive JMWE log messages, and search for specific logs.

## Logging level

The **Logging Level** determines which types of system events are captured by JMWE. By default, events with a level below **INFO**are not stored and therefore cannot be included in the logs. However, for troubleshooting purposes, it is possible to temporarily increase the level of logging.

To set a temporary log level:

1. Select the required level from the **Temporary log level** pulldown menu.
2. Click **Apply**.
3. The new level set here will remain for *one hour*, and will thereafter revert to the default **INFO** level.
4. Click **Reset** to the right of the pulldown menu to revert the log level to the default **INFO**level.

## Send errors and/or warnings to a Webhook

A webhook can be used to send errors and warnings for your JMWE post-functions and actions to an external applications for monitoring or other processing.

To configure a webhook, enter the following:

1. **Webhook URL** - Enter the URL for the location to which any errors and/or warnings should be sent.
2. **Send** - Choose whether to send **Errors and Warnings** or **Only Errors**.
3. **Receive log entries** - Configure how to send messages to the webhook URL. The options are:

   1. **Single entry** - Log messages are sent one at a time; if a message includes more than one error and/or warning, it will be broken into multiple messages.
   2. **Grouped (when possible)** - Log messages will not be separated when they include more than one error and/or warning. Messages that include only one error or warning will still be sent as one message.
4. Click **Apply.**

When an error or warning (depending on configuration) occurs, the webhook will post the error data in real-time.

## Log viewer

By default, the logs from the last 24 hours with a level higher than **INFO** are displayed in the table. You can filter the logs based on several conditions:

- **When** - when the logs were created (when the event occurred)
- **Level** - The range of levels to include in the output. Events can be filtered on any level from **DEBUG** all the way up to **FATAL**.
- **Extension IDs** - Logs can also be filtered based on the ID of any extension that has been created, including:

  - **Post-function ID**
  - **Condition ID**
  - **Validator ID**
  - **Action ID** (for [Shared Actions](/cms_trial/space/JMWEC/466288975/Shared+actions/))

To find the ID of a post-function, condition, validator, or Shared Action, open the extension in the transition in the Workflow editor; the ID will be listed under the name of the post-function in the transition information screen.

Additional filters are available; click **More filters** to expand the list and access the following:

- **Message type** - Filter by message type, e.g. security-error, template-error, workflow-warning etc. Select a message type from the pulldown menu.
- **Post-function** - The post-function that was executed. Select a post-function name from the pulldown menu.
- **Condition** - The condition that was executed. Select a condition name from the pulldown menu.
- **Validator** - The validator that was executed. Select a validator name from the pulldown menu.
- **Workflow name** - Filter by a specific Workflow. Enter the Workflow name.
- **Transition name** - Filter by a specific transition. Enter the transition name.
- **Issue key** - Filter for a specific issue. Enter the Issue ID.
- **Username** - Filter based on the user who triggered the transition.
- **Execution ID** - Filter based on an execution ID, which can be copied from Context; see below for more information. Context; see below for more information.

Click on **Apply filters** to filter the logs.

## Entries

**Please note:** Not every tab or field listed below will be displayed at all times. Only the tabs and fields appropriate to the log will be displayed.

Only the 200 most recent events that match your filters are displayed in the table. Each entry has the following information:

- Timestamp
- Level
- Workflow Extension
- Message Type
- Message

In most cases, the failure details are displayed in the **Message**. If the Message isn't sufficient to debug the problem, click '**>'** to the left of the log entry to see the additional information:

- **Error details -** Displays any additional error details. *This tab will only appear on error logs*.

  - **Error code**
  - **Error message**
  - **Field error(s)** - Displays for errors related to specific fields.
- **Context** - Displays the context of the log entry.

  - **Account ID** - The account ID number for the user who triggered the transition, e.g. `557058:72911e75-a89c-402e-b2f4-054c6bXXXXXX`.
  - **During** - which process the entry was created, e.g. `post-function-execution`.
  - **<Extension> ID** - The ID number of the extension that encountered the error. Click **add to filters** to copy the ID value to the corresponding filter field.
  - **Execution ID** - The ID of the specific execution of a post-function. This allows you to search for all events generated by a single execution of a post-function. Click **add to filters** to copy the ID value to the filter.
  - **Transition Execution ID** - The ID of the transition execution that triggered the error.
  - **Issue key** - The ID of the Jira issue which triggered the error.
- **Timings** - Timing data related to the extension which encountered the error.

  - **Delay** - The delay before executing the extension.
  - **Execution** - The total time for executing the extension.
  - **Queue** - The total time the extension spent in the queue.
  - **Triggering** - Time spent to bootstrap the execution, in case of triggered events.
- **Jira REST API call** -Displays information on the call made to the Jira API

  - **Method** - Method used. Eg: PUT, GET, etc.
  - **Url** - REST Url.
  - **Data** - Object or value sent to Jira to set a field.
- **Post-function** or **Condition** or **Validator** - Configuration details for the extension that caused the error

  - **Post-function**/**Condition**/**Validator** - Name of the extension.
  - **Transition** - Transition name and Workflow name in which the error occurred.
  - **Configuration/Jira Expression**
- **Action** - For [Shared Actions](/cms_trial/space/JMWEC/466288975/Shared+actions/), data for the action that caused the error.

  - **Action Name**
  - **Action Id** - The ID of the Shared Action. Click **add to filters** to copy the ID value to the **Action ID** filter field.
  - **Action Execution Id** - The execution ID for the Shared Action. Click **add to filters** to copy the ID value to the **Action Execution ID** filter field.
  - **Type** - The type of Shared Action.

## Download logs

Once you have filtered the logs as needed, they can be downloaded for analysis. Follow these steps to download your filtered logs:

1. Under **Download logs**, select a format from the **Format** pulldown menu:

   - **JSON**
   - **Text (short)**
   - **Text (detailed)**
   - **Text (dev)**
2. Click **Download logs**.

The logs displayed in the table will be downloaded in the format selected. The download is limited to 200 events *at most* that match the filters selected.

## Using logs for troubleshooting

If any JMWE extensions in your workflow do not seem to be working as expected, you can investigate possible issues or failures from these logs. The example scenarios below detail how to troubleshoot.

### 1 - Failure to create an Epic using ‘Create issue(s)’ post-function

#### Filter your logs

1. Go to **JMWE Logs** page.
2. Under the **Log viewer** section, click **More filters**.
3. Select `Create issue` from the **Post-function** pulldown menu.
4. Click **Apply filters.**

The table displays your filtered logs.

#### Analyzing the logs

The first thing to do is look at the **Message** value (the last column of the table) for the specific error/warning message:

![JMWE for Jira Cloud log entry controls for filtering and management](/cms_trial/assets/cd505356-e164-4270-acc7-34b9cae3a064.png)

**Message:** The post-function failed to create the Epic because the Epic Name was not provided, which is a mandatory field when creating an Epic.

### 2 - Failure to set the Component/s field to "Backend,Testing" using the ‘Set field value’ post-function

#### Filtering your logs

1. Go to **JMWE Logs** page.
2. Under the **Log viewer** section, click **More filters**.
3. Input the Issue key in **Issue key** filter.
4. Click on **Apply filters.**

The table displays your filtered logs.

#### Analyzing the log

The first thing you need to do is look at the **Message** value (the last column of the table) for the error/warning message:

![JMWE for Jira Cloud log filtering interface with search and display options](/cms_trial/assets/72791fdb-a10d-415b-8188-e94ae6cc41ea.png)

**Message:** The post-function failed to set the Component/s field with a component name "Testing".

Click on the arrow ( **> )** for the log entry, and looking at the **Jira REST API call** will display information on what value has been passed to Jira:

![JMWE for Jira Cloud detailed log viewer with entry information and controls](/cms_trial/assets/23c4810f-613c-42f4-ac97-936368cb742d.png)

**Jira REST API call:**The Data shows that two component values -`Backend` and `Testing` - were passed to Jira instead of one (i.e. `"Backend,Testing"`). The comma(',') was considered as a delimiter in the array of values rather than a part of the component name. So you need to pass the value as JSON object (`[{"name":"Backend,Testing"}])` selecting the `"Treat value as JSON"` option in the post-function configuration.

### 3 - Determine impacted issues when using ‘Set field value of linked issues' post-function

While iterating over linked issues to set a field value using the [Set field value of linked issues](/cms_trial/space/JMWEC/465504997/Set+field+value+of+linked+issues+(Deprecated)/) post-function, there is no way of knowing which issues were impacted. In this circumstance, you might want to set the **Temporary log level** to **DEBUG** and trigger a transition that has the post-function.

#### Filtering your logs

1. Go to **JMWE Logs** page.
2. Select `DEBUG` infor **Level**.
3. Under the **Log viewer** section, click **More filters**.
4. Select `Set field value of linked issues` from the **Post-function** pulldown menu.
5. Click **Apply filters**.

The table displays your filtered logs.

#### Analyzing the log

The table now has DEBUG entries indicating the setting of the field on the impacted linked issues.

![JMWE for Jira Cloud log information controls for viewing and management](/cms_trial/assets/26233d77-071f-4d13-96e0-b6c0c3001dbd.png)

## Using error and warning data posted to a webhook

When using a webhook, the raw content is sent as a JSON file.

![JMWE for Jira Cloud JSON sample data display for configuration reference](/cms_trial/assets/8d847c02-e47c-4940-a092-857f5028b3ac.png)

You can use this raw content to construct your own logging messages in external applications.

For example, you can derive:

A ***msgType*** occurred at ***time*** during (post-function ***postFunction***) on ***issueKey*** transition ***transition.transitionName*** (from status ***transition.from\_status*** to status ***transition.to\_status***) of workflow ***transition.workflowName***. The message is: ***error.message*** and the error code is ***error.code***.

Using the sample data above, this reads:

A ***license-error*** occurred at ***2022-04-14T14:42:01.408Z*** when***post-function-triggered*** (post-function ***ClearFieldsFunction***) on ***MYPROJ-125*** transition ***Move to Backlog*** (from status ***Selected for Development***to status ***Backlog***) of workflow ***My Workflow***. The message is: ***You do not have a valid, active license, but post-functions will run because licensing is disabled****.*and the error code is ***402***.