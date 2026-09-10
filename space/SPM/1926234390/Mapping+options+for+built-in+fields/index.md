# Mapping options for built-in fields

## Mapping options for built-in fields (old navigation)

Click to expand the guide

[Built-in fields](/cms_trial/space/SPM/1918832240/Built-in+fields/) can function in the following ways:

- Configurable fields (e.g., End Date)
- Non-configurable fields (e.g., summary)
- Native App fields (don’t correspond to any external tool)
- Fields that vary depending on the external platform (for example, the mapping of a field can be changed for Jira but not for Trello; or a field exists in one external platform but not in another)

## Configurable fields

For some fields, you can select the value you want to use.

For example, you define synchronization rules on the **App Configuration** > **General** > [**Fields**](/cms_trial/space/SPM/1918635376/Fields/) page. The “End date” field could be mapped to the Jira “Due date” field. In such cases, the app's built-in end date effectively displays the same value as the Jira due date.

![contentId-1926234390](/cms_trial/assets/e04da4f4-3fc6-4f7a-8905-695d579d04fa.png)

**Mapping options**

Available options vary across external platforms (something can be ‘mappable’ in Jira but not in Trello). You can change the mapping of an “End date” for Jira and decide to use the “Due date” Jira value as an end date, but you can’t change the settings for Trello.   
Effectively, the built-in “End date” field will display:

- For Jira, what has been specified in the App Configuration (in the example below, “Due date” has been used).
- Trello due date (Trello doesn’t have an “End Date” - due date will always be used to populate the built-in “End date” field).

## Non-configurable fields

For non-configurable fields, you can’t change the mapping.

For example, Summary in Jira = summary built-in, and this cannot be changed. You can’t decide that a built-in “summary” will display “description” or anything else. The built-in summary will always display the same value as the Jira summary.

![contentId-1926234390](/cms_trial/assets/8f8e123a-c7c4-4655-b86a-1affd99a5461.png)

## Native app fields

Native fields exist only in the App and can’t be found in Jira, Trello, or any other connected tool.

For example, the “Color”, and “Task ID” fields.

![contentId-1926234390](/cms_trial/assets/e680bb8e-bbbe-4f3f-8300-99c7be9f7cdf.png)

Some native fields, such as “Milestone,” can be mapped to external tools in configuration.

## Fields that vary depending on the external tool

Some fields may not have a straightforward corresponding value on the external platform. For example, Assignee is easily found in Jira (the built-in field can display the value), but Trello doesn’t have a corresponding field (members can be added to a card, but no single person is assigned). This is why a built-in Assignee column will not display any value for Trello cards. Basic Tasks also don’t have an assignee listed in the column.

![contentId-1926234390](/cms_trial/assets/56375f44-f3fa-4635-85b6-3da6af76ff2e.png)

## Mapping options for built-in fields (new navigation)

Click to expand the guide

[Built-in fields](/cms_trial/space/SPM/1918832240/Built-in+fields/) can function in the following ways:

- Configurable fields (e.g., End Date)
- Non-configurable fields (e.g., summary)
- Native app fields (don’t correspond to any external tool)
- Fields that vary depending on the external platform (for example, the mapping of a field can be changed for Jira but not for Trello; or a field exists in one external platform but not in another)

## Configurable fields

For some fields, you can select the value you want to use.

For example, you define synchronization rules on the **App Configuration** > **General** > [**Fields**](/cms_trial/space/SPM/1918635376/Fields/) page. The End Date field could be mapped to the Due Date field in Jira. In such cases, BigPicture’s built-in end date effectively displays the same value as the Jira due date.

![A dropdown with Jira fields that you can map with BigPicture's End date field.](/cms_trial/assets/21fb958b-4624-48c4-a75f-a07112055e9d.png)

Available options vary across external platforms (some fields can be synced in Jira but not in Trello). You can change the mapping of an End Date for Jira and decide to use the Due Date Jira value as an end date, but you can’t have the same settings for Trello.   
Effectively, the built-in End Date field will display:

- For Jira: The value from the field that was specified in the App Configuration.
- For Trello: Trello due date (Trello doesn’t have an End Date; a Due Date will be used to sync the built-in End date field.

## Non-configurable fields

For non-configurable fields, you can’t change the mapping.

For example, the Summary field in Jira syncs with the Summary built-in field in BigPicture, and this cannot be changed. You cannot change the mapping of a built-in Summary field to Description or any other field. The built-in Summary in BigPicture will always display the same value as the Summary in Jira.

![Summary column with a tooltip.](/cms_trial/assets/127228b3-9dd8-4543-9909-f7c1ce422d06.png)

## Native app fields

Native fields exist only in BigPicture and cannot be found in Jira, Trello, or any other connected tool.

For example, the Color and Task ID fields. When you search for them in the **Add or edit columns** dropdown, you will see that there is no equivalent field in the connected tool.

![Task ID column.](/cms_trial/assets/5a2e63c5-d5f7-410c-a5fe-2e8428558a15.png)

Some native fields, such as Milestone, can be mapped to external tools in configuration.

## Fields that vary depending on the external tool

Some fields may not have a straightforward corresponding value on the external platform.

For example, Assignee can be found in Jira (the built-in field can display the value), but Trello does not have a corresponding field (members can be added to a card, but no single person is assigned). This is why a built-in Assignee column will not display any value for Trello cards.

BigPicture tasks also do not have an assignee listed in the task structure column.