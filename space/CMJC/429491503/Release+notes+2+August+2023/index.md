# Release notes 2 August 2023

### August 2, 2023

We are happy to announce the release of **Configuration Manager for Jira Cloud 2.0.5**!

## Highlights

- [New product analytics](#FEATURES)
- [Improved deployment of permission schemes](#IMPROVEMENTS)
- [Migration of JSU and JMWE rules that are managed by Atlassian on Jira Cloud](#IMPROVEMENTS)
- [Third-party library upgrades](#IMPROVEMENTS)
- [Bug fixes](#RESOLVED)

![contentId-429491503](/cms_trial/assets/e30bc981-12b5-453e-9801-bcf22d5151b6.png)

[**Installation instructions**](/cms_trial/space/CMJC/194183182/Installation+guide/)

## Updates and Resolved Issues

![contentId-429491503](/cms_trial/assets/47cd2223-dc74-4457-92bc-2f16b53877ba.png)![contentId-429491503](/cms_trial/assets/e6c30702-3666-4e19-a1c1-cedd5605c66b.png)![contentId-429491503](/cms_trial/assets/6445374d-a6ff-48cd-9d6b-f2dfae70083b.png)

#### FEATURES

- We introduced **product analytics** to track and analyze how our users interact with Configuration Manager for Jira (CMJ) Cloud. The analytics data will help us determine areas to focus on, optimize performance and diagnose problems. Furthermore, it will help us put our users at the center of our product development by improving their journeys with CMJ Cloud.

#### IMPROVEMENTS

- We've changed the way we deploy permission schemes associated with **permissions that aren't supported** by the destination. In the analysis phase, you'll see a message warning you that the permissions won't be deployed in the destination Jira Cloud. The deployment can continue despite the warning.
- The *Cloud Migration Tool* and *CMJ Cloud* pair is able to migrate the [**JSU**](https://marketplace.atlassian.com/apps/5048/jsu-automation-suite-for-jira-workflows?tab=overview&hosting=cloud) **and** [**JMWE**](https://marketplace.atlassian.com/apps/292/jira-misc-workflow-extensions-jmwe?tab=overview&hosting=cloud) **Server/Data Center workflow rules** managed by Atlassian on the cloud. Check the lists of [JSU](https://appfire.atlassian.net/wiki/spaces/JSU/pages/12683782) and [JMWE](https://appfire.atlassian.net/wiki/spaces/JMWEC/pages/78481088/Feature+differences+between+JMWE+Data+Center+Server+and+Cloud) workflow rules that are now built-in and native to Jira Cloud.
- We've **upgraded the third-party libraries** used in CMJ Cloud. This will improve CMJ Cloud's overall quality and future development.

#### RESOLVED

- Fixed problems causing deployment failures.
- Security fixes.

Previous Releases...

[2.0.4 Release Notes](/cms_trial/space/CMJC/380764524/Release+notes+22+June+2023/)

[2.0.3 Release Notes](/cms_trial/space/CMJC/290357530/Release+notes+25+April+2023/)

[2.0.0 Release Notes](/cms_trial/space/CMJC/258408524/Release+notes+10+April+2023/)

---

More improvements and bug fixes will be coming soon! Thanks! Please submit your suggestions for improvements to Appfire's [**Support Portal**](https://apps.appf.re/support). We value your feedback!