# Release notes November 2023

### 3 November 2023

We are happy to announce the release of **Configuration Manager for Jira (CMJ) Cloud 2.0.8**!

## Highlights

- [Configuration Manager remembers the last used destination Jira Cloud sites](#FEATURES)
- [Bug fixes](#RESOLVED)

![contentId-578060323](/cms_trial/assets/caf35313-09b1-451d-af23-b0b9f6726a6c.png)

[**Installation instructions**](/cms_trial/space/CMJC/194183182/Installation+guide/)

## Updates and Resolved Issues

![contentId-578060323](/cms_trial/assets/86034764-fe10-4af3-9222-93068f19be31.png)![contentId-578060323](/cms_trial/assets/f9519740-161f-4b37-8fee-2c9b6110dfe3.png)

#### FEATURES

- Now, CMJ Cloud **remembers the last ten** **destination**Jira Cloud sites you had entered during deployments.

[Overview](#Remembering-the-last-used-destination-Jira-Cloud-sites)

#### RESOLVED

- Fixed a problem where deployment was failing with the *‘Permission scheme already exists’* error.
- Fixed a problem where deployment was failing with the *‘The value has to be provided’* during custom field context creation.
- Fixed a problem where deployment was failing as CMJ Cloud was attempting to delete the current user from the “site-admin” group.
- Fixed a problem where deployment was failing during board creation.
- Fixed a problem where deployment was failing with the *“Please select a valid project role”* error.
- Fixed a problem where deployment was failing during user creation with the *‘A user with that username already exists’* error.
- Fixed a problem where deployment was failing as CMJ Cloud was attempting to create a second global context.

Previous Releases...

[2.0.7 Release Notes](/cms_trial/space/CMJC/503480776/Release+notes+18+September+2023/)

[2.0.6 Release Notes](https://appfire.atlassian.net/wiki/spaces/DCMFJC/pages/439484420)

…

[2.0.0 Release Notes](https://appfire.atlassian.net/wiki/spaces/DCMFJC/pages/254574741)

---

## Remembering the last used destination Jira Cloud sites

When you enter a destination Jira Cloud site and trigger the *analysis* of a deployment, CMJ Cloud stores the destination URL. It can remember up to 10 destination Jira Cloud sites. Afterward, when you start a new migration, CMJ Cloud offers you the remembered URLs for ease and convenience.

![contentId-578060323](/cms_trial/assets/ae9175a5-275c-47d9-84ae-340546fa9b74.PNG)

---

More improvements and bug fixes will be coming soon! Thanks! Please submit your suggestions for improvements to Appfire’s [**Support Portal**](https://apps.appf.re/support). We value your feedback!