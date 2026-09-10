# Jira Cloud for Salesforce (Salesforce Package on AppExchange) Release Notes

Find the Salesforce Package on [AppExchange](https://appexchange.salesforce.com/listingDetail?listingId=a0N3000000E7xufEAB).

## 4.54

2024-10-30

#### Improvements:

- Set a new getting started page url when deploying package

## 4.53

2024-10-16

#### Bug Fixes:

- Remote site copying in onboarding checklist fix

## 4.52

2024-10-15

#### Bug Fixes:

- Remote site copying in onboarding checklist fix in configuration iframe

## 4.51

2024-10-14

#### Bug Fixes:

- Remote site copying in onboarding checklist
- Linked issues dropdown and search fix

## 4.50

2024-10-10

#### Improvements:

- Added a helpful checklist in the Connections page

## 4.49

2024-10-01

#### Improvements:

- Improved user interface in the Connections page

#### Bug Fixes:

- Bug fix for Parent field being required even when it is optional
- Bug fix for switching connections could cause the connections to show no bindings/mappings in the Jira Issue (NextGen) component

## 4.48

2024-09-04

#### Bug Fixes:

- Bug fix for Salesforce comments with filtering not displayed in Jira Comments LWC

## 4.47

2024-08-23

#### Bug Fixes:

- Bug fix for Jira Comments LWC writing issue data in a loop for comments

## 4.46

2024-07-05

#### Bug Fixes:

- Bug fix for error popup on Jira Comments lightning component

## 4.45

2024-07-04

#### Bug Fixes:

- Bug fix for email composer not loading when the Jira Comments lightning component is present

## 4.44

2024-06-18

#### Improvements:

- Removed beta label from retry mechanism for auto-sync

#### Bug Fixes:

- Bug fix for multi-line text field in Review & Create screen isn't expandable

## 4.43

2024-04-04

#### Improvements:

- Release components to trigger code when an association is unlinked

## 4.42

2024-02-28

#### Bug Fixes:

- Bug fix for Jira Comments keeps spinning when used in a custom object page
- Bug fix for the issue where two checkboxes with the same values doesn't work

## 4.41

2024-02-01

#### Bug Fixes:

- Bug fix for Jira Issues VF component not showing Jira associations

## 4.40

2024-01-31

#### Bug Fixes:

- Bug fix for Jira issue link redirecting incorrectly

#### Improvements:

- General security enhancements.

## 4.39

2024-01-11

#### Bug Fixes:

- Bug fix for a Jira field default value not being saved for issue creation

#### Improvements:

- General cleanup

## 4.38

2023-11-27

#### Bug Fixes:

- Added action to update the access token from connection
- Added ability to revoke default connections

#### Improvements:

- Added REST endpoint to be triggered by connect app which allows for SF code to react on the UNLINK event

## 4.37

2023-11-15

#### Bug Fixes:

- Fixed a bug where error message is not showing if connection name exceeds 38 characters.

## 4.36

2023-11-02

#### New Features:

- Added a setting to allow synchronising inline attachment in Jira comment over to Salesforce

## 4.35

2023-10-16

#### New Features:

- A new modern and intuitive user interface for the Admin Setting Page.
- Introducing the all-new "Jira Comments (NextGen)" component. This new component incorporates Salesforce's latest Lightning Web Component(LWC).

## 4.31

2023-09-28

#### Bug Fixes:

- Fixed a bug where duplicate options ​​are displayed on fields when present on the mapping.

#### Improvements:

- Added customer org information in request header to support switching to Appfire base URL.

## 4.30

2023-08-17

#### Improvements:

- General security enhancements.

## 4.29

2023-07-28

#### Improvements:

- General usability enhancements.

## 4.28

2023-07-06

#### Improvements:

- General usability enhancements.

## 4.27

2023-06-20

#### Bug Fixes:

- Fixed a bug where Jira Comments Aura Component not showing in Visualforce Pages

#### Improvements:

- General performance improvements.

## 4.26

2023-06-14

#### Improvements:

- General performance improvements and security enhancements.

## 4.25

2023-06-12

#### Improvements:

- General usability enhancements.

## 4.24

2023-06-07

#### Bug Fixes:

- Fixed a bug where Jira issues cannot be created and associated using the Lightning Aura component

## 4.23

2023-05-30

#### Bug Fixes:

- Fixed a bug where the Aura components are throwing Javascript promise error.

#### Improvements:

- General security enhancements.

## 4.22

2023-5-17

#### Bug Fixes:

- Fixed a bug where the package cannot be installed in Salesforce Summer '23 pre-release orgs.

#### Improvements:

- General usability enhancements.

## 4.20

2023-05-09

#### Improvements:

- General performance improvements and usability enhancements.

## 4.19

2023-2-21

#### Improvements:

- General performance improvements and usability enhancements.

## 4.18

2023-1-31

#### Bug Fixes:

- Fixed a bug where apex triggers were throwing error regarding 'uncommitted work'.

## 4.17

2023-1-25

#### Bug Fixes:

- Fixed a bug where new connections could not be created.

## 4.16

2023-1-04

#### New Features:

- Added support for connecting to multiple Jira instances.

## 4.15

2022-11-17

#### Bug Fixes:

- Fixed a bug where creating a Jira Issue from Salesforce fails when there is inbound Parent field mapping.

## 4.14

2022-11-15

#### Improvements:

- General performance improvements and usability enhancements.

## 4.13

2022-10-04

#### Improvements:

- General performance improvements and usability enhancements.

#### Bug Fixes:

- Fixed a bug where changing Select List(cascading) field value causes Jira issue creation to fail from Salesforce.

## 4.12

2022-08-10

#### Improvements:

- Improved the latency of loading Jira fields in the Jira Issue (NextGen) component

## 4.11

2022-07-18

#### Improvements:

- General performance improvements and usability enhancements.

## 4.10

2022-06-24

#### Bug Fixes:

- Fixed a bug where creating new Jira issue from Lightning component did not work.

## 4.9

2022-06-23

#### Bug Fixes:

- Added missing Content-Length header for PUT and PATCH requests.

#### Improvements:

- Remove BETA label from Next Gen component.

## 4.8

2022-06-16

#### Bug fixes:

- Fix an issue where creating new Jira issue from Lightning Web Component will throw an error when the Date field is empty.

## 4.7

2022-05-20

#### New Feature Release:

New in this release

- Developers have delivered a popular feature [request](https://apps.appf.re/jcfs/idea/SFJ-I-183) which has enhanced APEX trigger post-action behavior for Jira issue create.

## 4.6

2022-05-12

#### New Features:

- Added support for issue links to the "Create Jira Issue" screen for the Jira Issues (NextGen) component.
- Added "Beta Feature" custom setting to allow toggling beta features (e.g. auto-sync retry).

#### Bug fixes:

- Fixed an issue where auto-sync retry failed to work due to queueable jobs limit and duplicated job names.

## 4.5

2022-04-25

#### Bug fixes:

- Temporarily disable the auto-sync retry beta feature.

#### Improvements:

- General performance improvements and usability enhancements.

## 4.4

2022-04-11

#### New Features:

- Automatically retries failed auto-sync jobs in case of service disruptions. Please take note that this feature is still in Beta.

#### Improvements:

- General performance improvements and usability enhancements.

## 4.3

2022-01-04

#### New Features:

- Added support to automatically push update to specific Jira issue.

## 4.2

2021-12-08

#### New Features:

- Added support for cascading fields in the create & review screen.

## 4.1

2021-11-24

#### Bug fixes:

- Fixed a UI bug where "Create Jira Issue" page doesn't stop loading when there is no project.
- Fixed a UI bug where toast message title doesn't match with toast description.

## 4.0

2021-11-15

Introducing the all-new “Jira Issue” component. This new component incorporates Salesforce’s latest Lightning Web Component (LWC), and it is packed with new features:
- Associate multiple Jira Issues in one go.
- New combined experience prioritizes Association over Creation, which reduces the chances of creating duplicate Jira issues.
- Prioritizing required Jira fields during Creation.
- Ability to view Jira issues as a sortable Table or Cards.
- Improved error handling for remote site (Jira) errors.
- Improved performance in loading the component due to faster LWC technology.

Please take note that this component is still in Beta.

## 3.53

2021-09-27

#### Bug fixes:

- Fixed a UI bug where inline attachments in Jira comments were shown as broken for unauthorised Jira users.

#### Improvements:

- Made some behind-the-scenes enhancements.

## 3.52

2021-08-02

#### Bug fixes:

- Fixed a bug in the "Create Jira Issue" panel related to radio buttons.
- Fixed a UI bug in the "Associate Jira Issue" panel.

## 3.51

2021-07-22

#### Improvements:

- Made some behind-the-scenes enhancements.

## 3.50

2021-05-17

#### New Features:

- Added feature to allow controlling the syncing behaviour of email attachments for Email-to-Case.

## 3.49

2021-04-22

#### Improvements:

- Made some behind-the-scenes enhancements.

## 3.48

2021-04-07

#### Improvements:

- Made some behind-the-scenes enhancements.

## 3.47

2020-12-29

#### New Features

- Add support for Cascading fields in `Review & Create` for Visual Force view.

#### Bug fixes & Improvements:

- Fix a potential clickjacking vulnerability issue.
- Made some behind-the-scenes enhancements.

## 3.46

2020-05-18

#### Improvements:

- Improved error message on the Review & Create screen for when certain fields are not supported.

## 3.45

2020-05-13

#### Bug fixes:

- Fixed a bug where the ContentDocumentLink trigger was not pushing attachments automatically.
- Made some behind-the-scenes enhancements.

## 3.44

2020-03-31

#### Bug fixes:

- Fixed a bug where fields of the `Labels` custom field type were not being rendered on the Lightning Review & Create screen.

## 3.42

2020-01-31

#### Bug fixes:

- Fixed a bug where the Review & Create panel in Lightning Experience would show an error if a Jira Option field was mapped to a Salesforce Picklist Field.

## 3.41

2019-12-16

#### Bug fixes & Improvements:

- Fixed a bug where the Labels field were not being populated in the Lightning Review & Create screen.
- Minor behind-the-scenes improvements.

## 3.40

2019-12-03

#### Bug fixes:

- Fix a bug where the issue panel would not be rendered caused by `LINE SEPARATOR`(+U2028).

## 3.39

2019-11-14

#### Improvements:

- Security improvements.

## 3.38

2019-10-29

#### Improvements:

- Security improvements.

## 3.37

2019-10-17

#### Bug fixes:

- Minor changes for how user fields are displayed in the Jira Issue Panel, now Display Name is displayed.

## 3.36

2019-08-21

#### Bug fixes:

- Fix newline formatting for SalesforceComment.

## 3.35

2019-06-12

#### Improvements:

- Sustainability improvement.

## 3.34

2019-05-16

#### Bug fixes:

- Fix custom field not showing in Review & Create screen when mapped with Salesforce URL field type.

## 3.33

2019-05-09

#### Bug fixes:

- Optimized querying Multiselect field options when creating a Jira Issue in the Review & Create screen.
- Clicking outside of the Associate and Create Jira Issue popups will not close it now.

## 3.32

2019-04-08

#### Bug fixes:

- Default values can now be used for required fields when creating a Jira Issue in the Review & Create screen.

## 3.31

2019-03-14

#### Bug fixes & Improvements:

- Fix a bug where automatic synchonization direction was flipped when creating a Jira issue in Review & Create mode (Lightning).
- Allow selection of Jira Issue to associate by exact Issue key.

## 3.30

2019-01-30

#### Improvements:

- Improve the search for Jira issues feature in Salesforce. Now search results are filtered by mapped Jira issue types only.

## 3.29

2018-12-20

#### Bug fixes:

- Fix unable to create Jira issue in Create & Review form.

## 3.28

2018-12-19

#### Bug fixes:

- Fix unable to create Jira issue in Create & Review form.

## 3.27

2018-12-18

#### Bug fixes:

- Fix an issue where Lightning Issue Components failed to load if there is an empty Sprint field.
- Fix Jira textarea field does not appear in Create & Review screen if inbound-mapped with a Salesforce picklist.

## 3.26

2018-08-30

#### Bug fixes & Improvement:

- Fix broken comments panel in Safari
- Support special characters for *\u2028* and *\u2029* in Lightning.
- Minor UI improvement when Addon in unlicensed.

## 3.25

2018-08-15

#### Improvements:

- UI improvement on Configure Association Dialog in the lightning mode.
- Minor UI improvement in the Association Dialog.

## 3.24

2018-07-05

#### Improvement:

- Support special characters for *\u2028* and *\u2029*.

## 3.23

2018-06-13

#### New feature and improvements:

- **Review & Create** in Lightning in **Create Issue** dialog now supports more field types:
- Label
- Minor changes for how sprint fields are displayed in the Jira Issue Panel, now sprint names are displayed

## 3.22

2018-06-02

#### Improvement:

- UI Improvements

## 3.21

2018-05-16

#### New features:

- Creating Jira Issue post action will now respect the value from the connection configuration.
- Associating post action will now respect the value from the connection configuration.
- Association configuration settings in the Associate Dialog and the Create Issue Dialog will be hidden depending on the settings in connection configuration.

## 3.20

2018-04-19

#### Bug fix:

- Fix an issue which causes Jira Validation failed in Create & Review screen.

## 3.19

2018-04-06

#### Improvement:

- UI Improvements

## 3.18

2018-02-06

#### Improvement:

- Minor UI improvements

## Archived Releases

For older releases, check the **archive**.