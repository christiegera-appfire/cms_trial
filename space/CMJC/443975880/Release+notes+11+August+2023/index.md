# Release notes 11 August 2023

### August 11, 2023

We are happy to announce the release of **Configuration Manager for Jira Cloud 2.0.6**!

## Highlights

- [Suggested actions to resolve conflicts](#IMPROVEMENTS)
- [Issue type scheme transformations](#IMPROVEMENTS)
- [Bug fixes](#RESOLVED)

![contentId-443975880](/cms_trial/assets/f54812d0-69c3-4adb-99c9-899b92cc26e7.png)

[**Installation instructions**](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=cmjc&title=Installation%20and%20upgrade&linkCreation=true&fromPageId=443975880)

## Updates and Resolved Issues

![contentId-443975880](/cms_trial/assets/932102ae-4140-410c-ab1c-4805803d8a9d.png)![contentId-443975880](/cms_trial/assets/0471830c-7614-4514-870e-7bc6899ba4a9.png)

#### IMPROVEMENTS

- Actions are suggested to resolve configuration conflicts reported in the **Analyze changes** phase of deployments.  
  [Overview](#Suggested-actions-to-resolve-conflicts)
- Issue type schemes in a deployment can now be renamed in the same way as the projects, workflows, and workflow schemes.  
  [Visit documentation](/cms_trial/space/CMJC/759529597/Inline+transformations/)

#### RESOLVED

- Fixed problems causing deployment failures.

Previous Releases...

[2.0.5 Release Notes](/cms_trial/space/CMJC/429491503/Release+notes+2+August+2023/)

[2.0.4 Release Notes](/cms_trial/space/CMJC/380764524/Release+notes+22+June+2023/)

…

[2.0.0 Release Notes](/cms_trial/space/CMJC/258408524/Release+notes+10+April+2023/)

---

## Suggested actions to resolve conflicts

We’ve improved the configuration analysis to suggest an action when you run into a conflict. You’ll see them as a **Rename** or **Change key** (for projects) button in the conflict message during the **Analyze Changes** deployment phase. This way, you can fix conflicts faster, regardless if they’re between projects or configuration elements.

[Visit the documentation](/cms_trial/space/CMJC/193626781/Analyze+changes/)

When there is a conflict in the configuration element name, you can use the **Rename** action suggested in the error message (check the image below). This action is available for projects and the other configuration elements that can’t have duplicating names.

![contentId-443975880](/cms_trial/assets/b3194a53-8cd8-412e-89e2-efb8d50112fd.PNG)

When there is a project key conflict, you can use the **Change key** action suggested in the error message (check the image below).

![contentId-443975880](/cms_trial/assets/10bae399-68ff-4ca1-a448-1d64bca38033.png)

---

More improvements and bug fixes will be coming soon! Thanks! Please submit your suggestions for improvements to Appfire's [**Support Portal**](https://apps.appf.re/support). We value your feedback!