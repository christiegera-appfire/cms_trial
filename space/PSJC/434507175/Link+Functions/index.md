# Link Functions

This section contains functions that enable users to handle links. There are 2 kinds of links: structure links (like “blocks“, or “depends on“) and external links (*Web Links* also named *Remote Links*)

## Functions Summary

- [createWebLink](/cms_trial/space/PSJC/434864417/createWebLink/)
- [deleteWebLink](/cms_trial/space/PSJC/958071114/deleteWebLink/)
- [getIssueLinksDetail](/cms_trial/space/PSJC/434602750/getIssueLinksDetail/)
- [getWebLink](/cms_trial/space/PSJC/957940055/getWebLink/)
- [getWebLinksForIssue](/cms_trial/space/PSJC/958955774/getWebLinksForIssue/)
- [linkedIssues](/cms_trial/space/PSJC/434995421/linkedIssues/)
- [linkIssue](/cms_trial/space/PSJC/434799241/linkIssue/)
- [unlinkIssue](/cms_trial/space/PSJC/434995439/unlinkIssue/)
- [updateWebLink](/cms_trial/space/PSJC/958333364/updateWebLink/)

Structures used:

**JIssueLink** - the structural links

```text
integer id;
string name;
integer direction;
string description;
string issue;
```

**JRemoteIssueLink** - external (remote) links

```text
integer id;
string globalId;
string appName;
string appType;
string relationship;
string iconTitle;
string iconUrl;
string summary;
string title;
string url;
boolean statusResolved;
string statusIconTitle;
string statusIconUrl;
string statusIconLink;
```