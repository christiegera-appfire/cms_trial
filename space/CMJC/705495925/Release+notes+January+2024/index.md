# Release notes January 2024

### January 22, 2024

We are happy to announce the release of **Configuration Manager for Jira Cloud** **2.0.11**!

## Highlights

- [Jira Service Management fields are treated as managed fields](#IMPROVEMENTS)
- [Bug fixes](#RESOLVED)

![contentId-705495925](/cms_trial/assets/b0ffa5bc-fe35-43e7-b0f9-aeaf6bb64961.png)

[**Installation instructions**](/cms_trial/space/CMJC/194183182/Installation+guide/)

## Updates and Resolved Issues

![contentId-705495925](/cms_trial/assets/3b5c8ad0-af7c-4870-84b3-4f12615858e7.png)![contentId-705495925](/cms_trial/assets/7f36335b-c8d5-48c3-8361-307aa32f7d37.png)

#### IMPROVEMENTS

- Some Jira Service Management fields can’t be created on the destination Jira Cloud site, and now they’re treated as **managed fields**. This means that the deployment analysis will display an error informing you that the field has been identified as managed, and you need to manually recreate it on the destination Jira Cloud site.

#### RESOLVED

- Fixed a problem where the deployment failed when it contained a suspended user in the destination Jira Cloud site.
- Fixed a problem where the deployment failed because of a missing description of a custom event in a notification scheme.
- Fixed a problem where the deployment failed when a notification couldn’t be added to a notification scheme.

Previous Releases...

[2.0.9 Release Notes](/cms_trial/space/CMJC/642187824/Release+notes+December+2023/)

[2.0.8 Release Notes](https://appfire.atlassian.net/wiki/spaces/DCMFJC/pages/575471774)

…

[2.0.0 Release Notes](https://appfire.atlassian.net/wiki/spaces/DCMFJC/pages/254574741)

---

More improvements and bug fixes will be coming soon! Thanks! Please submit your suggestions for improvements to Appfire's [Support Portal](https://apps.appf.re/support). We value your feedback!