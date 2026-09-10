# Sizing guide

## Large number of Jira issues in a single BigPicture box (comfortable use ensured)

BigPicture carried out performance and load tests, confirming that a single BigPicture box can support 20,000 to 30,000 issues for comfortable use, with the actual capacity depending on the number of users accessing it simultaneously.

The BigPicture app is designed to manage a significant volume of data, allowing for an unlimited number of tasks within a single box. While an increased task count may extend the box synchronization time and potentially impact user interface responsiveness, it's important to note that this should not influence the loading times of the respective modules.

## Improve app performance

If the app speed and responsiveness do not meet you expectations, we recommend the following adjustments - [How to improve performance](/cms_trial/space/SPM/1918635504/How+to+improve+performance/).

We are constantly working on performance improvements, so don't hesitate to contact us and [let us know](https://appfire.atlassian.net/servicedesk/customer/portal/11) if you experience any problems with using BigPicture on a larger scale.

## BigPicture users

When it comes to responsiveness, the end-user hardware has an impact. Having **an updated Chrome, Safari or Firefox browser on a modern PC (quad-core CPU, preferably at least an Ice Lake series for Intel and at least 8 GB RAM, preferably 16**) is advised when you use BigPicture with small amount of data.

## BigPicture Gantt automatic WBS

Configuring synchronizers in any box synchronization configuration directly affects the performance of BigPicture when opening the Gantt module.

Each synchronizer adds additional work performed for every Jira issue in the scope of a box. If you configure your Jira based on best practices as described in [Jira Sizing Guide](https://confluence.atlassian.com/enterprise/jira-sizing-guide-461504623.html) and BigPicture described in this document, it will ensure successful implementation into your environment.