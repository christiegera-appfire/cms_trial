# Release notes February 2024

### February 14, 2024

We are happy to announce the release of **Configuration Manager for Jira Cloud 2.0.12**!

## Highlights

- [Configuration transformations from a JSON file](#FEATURES)
- [Bug fixes](#RESOLVED)

![contentId-759791666](/cms_trial/assets/8ee40e0e-8d3d-4480-ac3e-367504e42564.png)

[**Installation instructions**](/cms_trial/space/CMJC/194183182/Installation+guide/)

## Updates and Resolved Issues

![contentId-759791666](/cms_trial/assets/317e8ddb-0067-40f0-9651-43b74d1346db.png)![contentId-759791666](/cms_trial/assets/9549724c-8390-4015-b3a0-9aec35038793.png)

#### FEATURES

- Now, you can **apply transformations from a file** to projects, other configuration elements, and users.

[Overview](#Configuration-transformations-from-a-JSON-file)

#### RESOLVED

- Fixed defects causing deployment failures.

Previous Releases...

[2.0.11 Release Notes](/cms_trial/space/CMJC/705495925/Release+notes+January+2024/)

[2.0.9 Release Notes](https://appfire.atlassian.net/wiki/spaces/DCMFJC/pages/597688762)

…

[2.0.0 Release Notes](https://appfire.atlassian.net/wiki/spaces/DCMFJC/pages/254574741)

---

## Configuration transformations from a JSON file

We’re releasing a feature that allows you to *make changes to projects, configuration elements, and users* in the deployment scope. We call these changes *transformations*. You can apply changes to the configuration by uploading a JSON file listing the desired transformations.

[See the list of elements that can be transformed](/cms_trial/space/CMJC/759496884/JSON+objects+for+configuration+element+transformations/).

This new way of applying transformations allows you to:

- **Download configuration mapping** - downloading a file holding JSON records for all configuration elements in the deployment scope, their details, and the way they’ll be deployed. The file specifies whether configuration elements, including projects and users, will be newly created or mapped to existing destination elements. [Learn more about downloading the configuration mapping](/cms_trial/space/CMJC/759824434/Download+and+customize+the+configuration+mapping/).
- **Customize configuration mapping** *-* applying transformations from a JSON file to the configurations being deployed. These transformations can come in the form of renaming and remapping configuration elements or changing project keys. Also, you can apply transformations to multiple configuration elements simultaneously. [Learn more about customizing the configuration mapping](/cms_trial/space/CMJC/759824434/Download+and+customize+the+configuration+mapping/).
- **Apply user transformations** - applying transformations from a JSON file to the deployed users. This way, you can merge users, correct emails and names, and choose different mapping between source and destination users. [Learn more about user transformations](/cms_trial/space/CMJC/760315914/User+transformations/).

Visit the [Transformations](/cms_trial/space/CMJC/759595150/Transformations/) section of the documentation and find all guides on the topic.

The following video is a short demo of using this new feature to transform configuration elements before deploying them.

![CMJC-customize-mapping-fix-problems.mp4](/cms_trial/assets/206c72db-0a90-4d4d-960e-21f8f528559c.mp4)

---

More improvements and bug fixes will be coming soon! Thanks! Please submit your suggestions for improvements to Appfire's [**Support Portal**](https://apps.appf.re/support). We value your feedback!