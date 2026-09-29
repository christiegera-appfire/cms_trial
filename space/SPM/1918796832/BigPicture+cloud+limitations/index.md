# BigPicture cloud limitations

## Clear cache

Most problems with outdated information that cause errors can be resolved by clearing the cache.

Refer to the [Plugin cache](/cms_trial/space/SPM/1918635809/Plugin+cache/) page for further instructions.

## The list of missing functionalities in BigPicture Cloud – blocker on BigPicture's side

| Module | Key difference | Explanation | Preview |
| --- | --- | --- | --- |
| Risks, Board | Edit Issue dialog not available on Cloud  **Note**: inline editng allows you to edit visible card fields.  Alternatively, click on the issue key to open the issue page to make changes. | Not available at the moment. | Edit option in task view. |
| All | Online presence | Not available at the moment. |  |
| All | Enhanced JQL functionality | Jira Cloud doesn't support JQL enhancement. |  |

<https://appfire.atlassian.net/browse/ONE-38877>

<https://appfire.atlassian.net/browse/BP-4273>

<https://appfire.atlassian.net/browse/BP-9023>

## The list of missing functionalities in BigPicture Cloud – blocker on Atlassian's side

| Module | Key difference | Explanation | Preview | Issue to track |
| --- | --- | --- | --- | --- |
| Gantt | Create Jira sub-task not available on Cloud | Atlassian Connect Jira JavaScript API does not provide such functionality. | Jira sub task highlighted in a drop-down menu | Ticket on Atlassian's end - [click here](https://ecosystem.atlassian.net/browse/ACJIRA-1487). |
| Scope | Detail View not available on Cloud | Atlassian API does not provide such functionality. | Risk consequences and probability in a drop-down menu | Ticket on Atlassian's end - [click here](https://jira.atlassian.com/browse/JRACLOUD-69721). |
| BigPicture configuration | "Risk consequence" "Risk probability" and Task Mode fields are locked | Atlassian's REST API allows the plugin to add *Select List (single choice)* type of fields on installation only when they are locked.  For more information, refer to the ["Risk consequence" and "Risk probability" fields are locked](/cms_trial/space/SPM/1918829871/%22Risk+consequence%22+and+%22Risk+probability%22+fields+are+locked/) page. | Risk consequences highlighted. |  |
| BigPicture configuration | Respect Jira's Screen scheme configuration | The UI element (swiper) is not available. The Jira Cloud hosting security always requires respecting the screen scheme configuration, so the administrator has no possibility to configure the application in this regard. |  |  |
| Confluence | Gadgets | Following differences in the Confluence architecture between Jira Data Center and Jira Cloud:   - Gadgets from Jira Data Center are automatically available with the same login mechanisms; - Gadgets from Jira Cloud were removed on July 7th, 2017 (see <https://support.atlassian.com/jira/kb/removing-unsupported-external-gadgets-from-jira-cloud/>). | - |  |

If you have any further questions or are still in doubt about why certain options or features remain inaccessible, contact us via[**Service Desk**](https://appfire.atlassian.net/servicedesk/customer/portal/11)**.**

## Custom fields from third-party Jira apps in BigPicture

Depending on the functionality of a given plugin, custom fields based on third-party Jira apps may have limited or different functionality in the Cloud version of the product. For example, Traffic Lights can be displayed only as a text field.