# issue APIs

Issue APIs allow you to access field and property data for issues - both the current issue and related issues.

**Note**: It is not possible to access values directly within your scripts. This method, while once possible, is no longer supported. You must use the [getField](/cms_trial/space/JMCFC/1325137936/getField/) or [getFields](/cms_trial/space/JMCFC/1326317598/getFields/) APIs to access field values. This includes when using [getLinkedIssues](/cms_trial/space/JMCFC/1798209737/getLinkedIssues/), [getChildIssues](/cms_trial/space/JMCFC/1325072483/getChildIssues/), and [getParentIssue](/cms_trial/space/JMCFC/1326022692/getParentIssue/). To access field values of work items returned by these APIs, you must also use `getField` or `getFields` after fetching the related work items. See each page for details on how to update your scripts.

Additionally, you must always get fields using the ID or key, and not the field name or label (some Jira system fields have the same ID as their name, but this does not affect the requirement). See **Determining custom field IDs**, below, for more information.

## The script editor

You are viewing the documentation for **Jira Cloud**.

| **In this section**   - [getChildIssues](/cms_trial/space/JMCFC/1325072483/getChildIssues/) - [getField](/cms_trial/space/JMCFC/1325137936/getField/) - [getFields](/cms_trial/space/JMCFC/1326317598/getFields/) - [getFieldHistory](/cms_trial/space/JMCFC/1562447291/getFieldHistory/) - [getIssueHistory](/cms_trial/space/JMCFC/1563854403/getIssueHistory/) - [getLinkedIssues](/cms_trial/space/JMCFC/1798209737/getLinkedIssues/) - [getParentIssue](/cms_trial/space/JMCFC/1326022692/getParentIssue/) - [getProperty](/cms_trial/space/JMCFC/1326120998/getProperty/) - [getProperties](/cms_trial/space/JMCFC/1324974093/getProperties/) |
| --- |