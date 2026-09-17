# Issue Type & IT Screen Scheme Administration Functions

This section contains functions that enable users to handle issue type administration.

## Functions Summary

- [admAppendITSSMapping](/cms_trial/space/PSJC/806158387/admAppendITSSMapping/)
- [admAssignITSSToProject](/cms_trial/space/PSJC/805667045/admAssignITSSToProject/)
- [admCreateIssueTypeScreenScheme](/cms_trial/space/PSJC/805634774/admCreateIssueTypeScreenScheme/)
- [admDeleteIssueTypeScreenScheme](/cms_trial/space/PSJC/805634802/admDeleteIssueTypeScreenScheme/)
- [admGetAllIssueTypeSchemes](/cms_trial/space/PSJC/514786551/admGetAllIssueTypeSchemes/)
- [admGetAllIssueTypeScreenSchemes](/cms_trial/space/PSJC/518324501/admGetAllIssueTypeScreenSchemes/)
- [admGetIssueTypeScheme](/cms_trial/space/PSJC/515211665/admGetIssueTypeScheme/)
- [admGetIssueTypeScreenScheme](/cms_trial/space/PSJC/518291809/admGetIssueTypeScreenScheme/)
- [admGetITSSMappings](/cms_trial/space/PSJC/805961911/admGetITSSMappings/)
- [admGetITSSProjects](/cms_trial/space/PSJC/806158401/admGetITSSProjects/)
- [admRemoveITSSMapping](/cms_trial/space/PSJC/806322241/admRemoveITSSMapping/)
- [admUpdateIssueTypeScreenScheme](/cms_trial/space/PSJC/806125616/admUpdateIssueTypeScreenScheme/)
- [admUpdateITSSDefaultScreenScheme](/cms_trial/space/PSJC/805798001/admUpdateITSSDefaultScreenScheme/)

Structures used:

### JIssueTypeScheme

```text
int id;
string name;
string description;
int defaultIssueTypeId; //the default issue type
```

### JIssueTypeScreenScheme

```text
int id;
string name;
string description;
```

### JIssueTypeScreenMapping

```text
int issueTypeId;
int screenSchemeId;
```