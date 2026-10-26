# Function support

Not every SIL function is compatible with Jira Product Discovery because it uses a simplified project structure with some standard Jira features removed and specialized features added. Functions that depend on missing Jira features won't work in Product Discovery projects.

A function is categorized as unsupported when it is either:

- Incompatible: should work, but has technical limitations, or;
- Not applicable: depends on features that don't exist in Product Discovery.

## Custom field and admin functions

Product Discovery custom fields use specialized configurations that differ from standard Jira custom fields. Many functions designed for standard custom field administration won't work with Product Discovery's unique field structure.

|  |  |
| --- | --- |
| **Compatible functions** | - [admAddCustomFieldAlias](/cms_trial/space/PSJC/434962801/admAddCustomFieldAlias/) - [admCreateCustomField](/cms_trial/space/PSJC/434897123/admCreateCustomField/) - [getCustomFieldNameById](/cms_trial/space/PSJC/434602668/getCustomFieldNameById/) - [getIssueFieldNames](/cms_trial/space/PSJC/435028327/getIssueFieldNames/) - [getIssueFields](/cms_trial/space/PSJC/434831740/getIssueFields/) - [lastFieldHistory](/cms_trial/space/PSJC/434799142/lastFieldHistory/) - does not work with all fields |
| **Unsupported functions** | - [admGetAllFieldConfigSchemes](/cms_trial/space/PSJC/514818850/admGetAllFieldConfigSchemes/) - [admGetFieldConfigScheme](/cms_trial/space/PSJC/515146283/admGetFieldConfigScheme/) - [admAddCustomFieldOptions](/cms_trial/space/PSJC/791282009/admAddCustomFieldOptions/) - [admUpdateCustomFieldOptions](/cms_trial/space/PSJC/790528847/admUpdateCustomFieldOptions/) - [admDeleteCustomFieldOptions](/cms_trial/space/PSJC/790627240/admDeleteCustomFieldOptions/) - [admGetCustomFieldOptions](/cms_trial/space/PSJC/791511311/admGetCustomFieldOptions/) - [admUpdateCustomField](/cms_trial/space/PSJC/792461313/admUpdateCustomField/) - [admDeleteCustomField](/cms_trial/space/PSJC/791283227/admDeleteCustomField/) - [fieldHistory](/cms_trial/space/PSJC/434766025/fieldHistory/) - [getFieldChanges](/cms_trial/space/PSJC/434930045/getFieldChanges/) - [getPriorityIdByName](/cms_trial/space/PSJC/434995343/getPriorityIdByName/) - [getPriorityNameById](/cms_trial/space/PSJC/434374256/getPriorityNameById/) |

## Issue and admin functions

Some issue functions don't work properly in Product Discovery due to unsupported custom field types. As support for additional field types is added, more issue functions should become available.

|  |  |
| --- | --- |
| **Compatible functions** | - [allLinkedIssues](/cms_trial/space/PSJC/434507143/allLinkedIssues/) - [countIssues](/cms_trial/space/PSJC/434930080/countIssues/) - [getIssueURL](/cms_trial/space/PSJC/435028396/getIssueURL/) - [isIssueContext](/cms_trial/space/PSJC/434995375/isIssueContext/) - [lastIssueChanges](/cms_trial/space/PSJC/434799219/lastIssueChanges/) - [selectIssues](/cms_trial/space/PSJC/434831783/selectIssues/) |
| **Unsupported functions** | - [cloneIssue](/cms_trial/space/PSJC/435028380/cloneIssue/) - [createIssue](/cms_trial/space/PSJC/434507110/createIssue/) - [deleteIssue](/cms_trial/space/PSJC/434507126/deleteIssue/) - [getCustomKeywordIndexValue](/cms_trial/space/PSJC/734134284/getCustomKeywordIndexValue/) - [setCustomKeywordIndexValue](/cms_trial/space/PSJC/733775542/setCustomKeywordIndexValue/) - [admArchiveIssues](/cms_trial/space/PSJC/514786357/admArchiveIssues/) - [admUnarchiveIssues](/cms_trial/space/PSJC/515178779/admUnarchiveIssues/) - [subtasks](/cms_trial/space/PSJC/434995389/subtasks/) - [getIssueEntityPropertyValue](/cms_trial/space/PSJC/434799205/getIssueEntityPropertyValue/) - [setIssueEntityPropertyValue](/cms_trial/space/PSJC/465862657/setIssueEntityPropertyValue/) |

## Project and admin functions

Product Discovery projects lack many standard Jira project features like components, versions, and complex workflows. Functions that manage these missing features are not applicable to Product Discovery projects.

|  |  |
| --- | --- |
| **Compatible functions** | - [allProjects](/cms_trial/space/PSJC/434733476/allProjects/) - [getProjectKeyByName](/cms_trial/space/PSJC/435028429/getProjectKeyByName/) - [issueTypesForProject](/cms_trial/space/PSJC/434799271/issueTypesForProject/) - [projectPM](/cms_trial/space/PSJC/434831859/projectPM/) - [projectsForPM](/cms_trial/space/PSJC/434766136/projectsForPM/) |
| **Unsupported functions** | - [getTeamLeaders](/cms_trial/space/PSJC/433654497/getTeamLeaders/) - [projectMembers](/cms_trial/space/PSJC/434930117/projectMembers/) - [admAddProjectComponent](/cms_trial/space/PSJC/733905555/admAddProjectComponent/) - [admAddProjectVersion](/cms_trial/space/PSJC/744261602/admAddProjectVersion/) - [admArchiveProjectVersion](/cms_trial/space/PSJC/746324309/admArchiveProjectVersion/) - [admDeleteProjectComponent](/cms_trial/space/PSJC/732990279/admDeleteProjectComponent/) - [admDeleteProjectVersion](/cms_trial/space/PSJC/746356959/admDeleteProjectVersion/) - [admReleaseProjectVersion](/cms_trial/space/PSJC/744165367/admReleaseProjectVersion/) - [admSetProjectVersionReleaseDate](/cms_trial/space/PSJC/744589333/admSetProjectVersionReleaseDate/) - [admSetProjectVersionStartDate](/cms_trial/space/PSJC/744589347/admSetProjectVersionStartDate/) - [admUpdateProjectComponent](/cms_trial/space/PSJC/733187152/admUpdateProjectComponent/) - [admUpdateProjectVersion](/cms_trial/space/PSJC/744065110/admUpdateProjectVersion/) - [getComponent](/cms_trial/space/PSJC/434733545/getComponent/) - [getComponents](/cms_trial/space/PSJC/434472682/getComponents/) - [getComponentsObjects](/cms_trial/space/PSJC/434831843/getComponentsObjects/) - [getProjectComponentLead](/cms_trial/space/PSJC/434864433/getProjectComponentLead/) - [getVersion](/cms_trial/space/PSJC/434733561/getVersion/) - [getVersions](/cms_trial/space/PSJC/433000678/getVersions/) - [getVersionsObjects](/cms_trial/space/PSJC/434766119/getVersionsObjects/) |

## Admin functions

Most admin functions work with Product Discovery since they operate at the instance level rather than the project level. However, functions that manage features not present in Product Discovery (like workflow administration) are not applicable.

|  |  |
| --- | --- |
| **Compatible functions** | - [Dashboard Functions](/cms_trial/space/PSJC/748683346/Dashboard+Functions/) - [Filter Administration Functions](/cms_trial/space/PSJC/722174068/Filter+Administration+Functions/) - [Group Administration Functions](/cms_trial/space/PSJC/515178984/Group+Administration+Functions/) - [Notification Administration Functions](/cms_trial/space/PSJC/531989115/Notification+Administration+Functions/) - [Permissions Administration Functions](/cms_trial/space/PSJC/532284137/Permissions+Administration+Functions/) - [System Administration Functions](/cms_trial/space/PSJC/434766189/System+Administration+Functions/) - [User Administration Functions](/cms_trial/space/PSJC/514688035/User+Administration+Functions/) - [Screen and Screen Schemes Administration Functions](/cms_trial/space/PSJC/790495364/Screen+and+Screen+Schemes+Administration+Functions/) |
| **Unsupported functions** | - [Custom Field Administration Functions](/cms_trial/space/PSJC/434897107/Custom+Field+Administration+Functions/) - [Issue Administration Functions](/cms_trial/space/PSJC/514818767/Issue+Administration+Functions/) - [Issue Type Administration Functions](/cms_trial/space/PSJC/531890890/Issue+Type+%26+IT+Screen+Scheme+Administration+Functions/) - [Project Administration Functions](/cms_trial/space/PSJC/434733529/Project+Administration+Functions/) |

## All other function categories

General SIL functions for attachments, comments, groups, links, and users work normally with Product Discovery since these are core Jira features. Functions related to agile features (workflow, worklog) are not applicable due to Product Discovery's simplified structure.

|  |  |
| --- | --- |
| **Compatible functions** | - [Attachment functions](/cms_trial/space/PSJC/434962663/Attachment+Functions/) - [Comment functions](/cms_trial/space/PSJC/434799105/Comment+Functions/) - [Group functions](/cms_trial/space/PSJC/434831757/Group+Functions/) - [Jira system functions](/cms_trial/space/PSJC/434995359/Jira+System+Functions/) - [Link functions](/cms_trial/space/PSJC/434507175/Link+Functions/) - [User functions](/cms_trial/space/PSJC/434864450/User+Functions/) |
| **Unsupported functions** | - [Workflow functions](/cms_trial/space/PSJC/434733610/Workflow+Functions/) - [Worklog functions](/cms_trial/space/PSJC/434635605/Worklog+Functions/) |