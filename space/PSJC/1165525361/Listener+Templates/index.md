# Listener Templates

Listener scripts are extremely useful because they capture a wide range of events that occur both inside and outside of the issues workflow. Listeners can capture such things as issue edits, or the creations of new objects within Jira.

The templates will add scripts to associated events within Jira.

## Setting up the Listener Templates

Listener scripts are designed to live above projects and workflows so those elements do not need to be specified with all listener scripts. However, listeners still need to be associated with events inside Jira. The first two steps to setting up a listener template is to select an event to use as a script trigger and as an associated user.

![Power Scripts for Jira Cloud alias creation dialog](/cms_trial/assets/2595c0e5-29a3-45da-b2bb-8c8c841fac6c.png)

**NOTE:** The “Run as” setting is not required. If used, the script will always run under the specified user. If not specified, the script will run as the user who triggered the event.

## Testing the Script

Testing listeners can be quite simple. In order to test you should perform an action that will trigger the specific event associated with the trigger then check to see if the desired action was performed. However, if not, troubleshooting listener scripts can be a little tricky, see this section about troubleshooting scripts.

## Templates

## Print in server log when an event is triggered

Print text in log file when an event happens.

### Inputs

| **Name** | **Required** | **Description** |
| --- | --- | --- |
| User | YES | The specific user for which the issue will be assigned. |
| Description | NO | The description text will be added to a comment at the head of the script so other users can be informed of the purpose of the script. |

### Script

```text
assignee = "jmuse";
```