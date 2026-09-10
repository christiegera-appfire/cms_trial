# Enable local time correspondence between Jira and Dashboard Hub

If Dashboard Hub shows a date that does not match the Jira date, it means that Dashboard Hub needs permission to view the user-configured local time parameter in Jira.

A time mismatch between Dashboard Hub and Jira becomes more evident on specific cut-off dates and when different time zones are at play.

## Example

Depending on the time zone, the JQL with dates ranging from 2023-01-01 to 2022/12/31 might exclude Jira issues with the date 2023-01-01.

To overcome the date discrepancy, you can:

1. **Verify the Dashboard Hub Data Source**:

   - Ensure that the Jira instance where you check your data is configured in the data source.
2. **Set the user local time parameter to public**:

   1. In Jira, go to **Profile and Settings**.
   2. Select **Manage Account**.

![Dashboard Hub Jira profile menu showing Manage Account option for timezone settings](/cms_trial/assets/1906d623-5459-475b-80a6-809356cd9b24.png)

c. Set the Local time parameter to **Anyone**.