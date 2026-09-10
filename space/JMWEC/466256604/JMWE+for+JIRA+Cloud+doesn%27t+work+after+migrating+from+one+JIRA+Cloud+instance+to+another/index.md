# JMWE for JIRA Cloud doesn't work after migrating from one JIRA Cloud instance to another

## Problem

When you migrate from one JIRA Cloud instance to another (using Backup/Restore), most Connect add-ons, such as JMWE for JIRA Cloud, installed in your instance will stop working. If you navigate to a JMWE screen, such as a post-function configuration screen or the Troubleshooting and Support page, you will receive an "Unauthorized" error. This is due to a known JIRA Cloud bug [AC-1528](https://ecosystem.atlassian.net/browse/AC-1528).

## Solution

If you wish to continue using the old JIRA Cloud instance (such as when you have both a production and a test instance), the only solution is to reach out to [Atlassian Support](https://support.atlassian.com/) and ask them to fix your "clientKey". Once they fix it, you should be able to [reinstall the add-on](/cms_trial/space/JMWEC/465503970/Installing+or+Uninstalling+on+Jira+Cloud/).

If you are replacing your old instance with the new (most likely to modify the URL), please [contact us](https://appfire.atlassian.net/servicedesk/customer/portal/11) so we can clear your existing registration and then you will be able to [reinstall the add-on](/cms_trial/space/JMWEC/465503970/Installing+or+Uninstalling+on+Jira+Cloud/).

Reinstalling of the add-on will not modify your configured workflows. However, while the add-on is inactive, JIRA might start failing transitions which have JMWE post-functions configured, so you want to minimize the time between un-installation and re-installation of the add-on.

## Related articles

|  |  |
| --- | --- |
| Related issues |  |