# Bottom panel

The bottom panel provides essential debugging and monitoring tools through three tabs:

- **Editor console**
- **Server log**
- **Event viewer**

Each tab offers different insights into script execution and system behavior. The panel opens automatically when you select one of the tabs.

![Power Scripts for Jira Cloud bottom panel interface with script execution tools](/cms_trial/assets/346be87f-7309-4884-9da6-4cd5d0d19955.png)

## Editor console

The **Editor console** displays output from your scripts, showing variable values, script progress, and error messages to help you understand how your code is performing.

| **Featrue** | **Description** |
| --- | --- |
| **Script output** | You can view results, such as values and calculations, using the `return` statement at the end of your script or the `runnerLog()` function anywhere within your code.  Learn more about using the `runnerLog()` function in the [runnerLog() reference page](/cms_trial/space/PSJC/433000617/runnerLog/). |
| **HTML support** | The `runnerLog()` function can display HTML content, letting you create formatted output such as tables for better data presentation. Power Scripts for Jira Cloud SIL Manager bottom panel workspace The `runnerLog()` function takes two parameters: your message (which can include HTML tags) and `treatAsHtml`(boolean). Set `treatAsHtml` to `true` to render HTML formatting. For example: `runnerLog("<b>Bold text</b>", true)`. |
| **Error display** | Runtime errors appear in the **Editor console**. Some errors are only visible in the **Editor console** or the **Server log** tab and won't appear elsewhere in the SIL Manager. These runtime errors can occur even when your script syntax is completely correct. For example, if a file path is incorrect or a file doesn't exist when using file functions, the script will fail at runtime even though the syntax checker would not detect this type of error. Power Scripts for Jira Cloud script editor execution interface |
| **Export capability** | Download console output directly to a file. This is particularly useful for exporting data from Jira, such as lists of inactive users. Power Scripts for Jira Cloud console download interface |

## Server log

The Server Log tab displays the contents of the actual Jira log file from the file system. This tool helps debug scripts that appear to be working but produce unexpected results.

![Power Scripts for Jira Cloud script execution log panel](/cms_trial/assets/6df16247-7bb1-4078-b915-90be2f10a3d3.png)

| **Featrue** | **Description** |
| --- | --- |
| **Real-time log access** | View current Jira system logs without accessing the server file system directly. |
| **Log configuration** | Use the settings icon in the **Server log** panel to configure display options: Power Scripts for Jira Cloud server log settings configuration  - **Max number of lines**: Limit how many log lines are displayed. Default: value is 500. - **Line to start from**: Specify a starting point in the log. Leave blank for newest logs. - **Log filter**: Enter a search string to filter logs by specific keywords or patterns. - **Auto reload**: Toggle automatic refreshing of log content.   These settings help you focus on relevant log entries and control the amount of data displayed for better performance and readability. |

## Event viewer

The Event Viewer tab maintains a temporary record of actions and events within the SIL Manager. It is particularly helpful in the following scenarios:

- **Comparison analysis**: Compare results from multiple script runs by reviewing previous execution records.
- **Action history**: Track what operations have been performed within the SIL Manager session.
- **Debugging support**: Review the sequence of events when troubleshooting script behavior.

![Power Scripts for Jira Cloud log viewer with filtering options](/cms_trial/assets/b029b78a-6fef-4f4c-a234-f580d6651d96.png)