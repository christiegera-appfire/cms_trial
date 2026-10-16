# 7.3.0 Release notes

**Release date:** October 15, 2026

This page outlines the updates included in the latest release of Power Scripts for Jira Cloud.

---

## Bug fixes

This release includes fixes to improve the reliability of SIL Manager, configuration settings, script security, workflow post functions, and issue linking.

- **Fixed folder downloads in SIL Manager**  
  Resolved an issue where downloading folders or large script libraries (6 MB or larger) from the SIL Manager context menu failed to start. You can now download the complete SIL file tree, including its folder structure.
- **Fixed SMTP+STARTTLS configuration not being retained**  
  Fixed an issue where the SMTP+STARTTLS protocol selection reverted to plain SMTP after saving and reopening the Outgoing Mail configuration. The selected protocol now displays correctly and remains saved.
- **Fixed incorrect Jira project links in Listener configuration**  
  Resolved an issue where the project link on the Listener configuration edit screen directed users to an invalid URL. The link now opens the correct Jira project.
- **Improved validation for script security permissions**  
  Fixed an issue in **Settings** → **Security** where invalid Read or Exec permissions could be assigned to folders instead of script files. Validation errors are now displayed, allowing users to correct invalid permissions before saving.
- **Fixed script template navigation in SIL Manager**  
  Resolved an issue where scripts created from Script Templates displayed a `preselected node can't be found` error. Newly created scripts now open immediately, and the `generated_templates` folder appears without requiring a manual refresh.
- **Fixed workflow post function ID mismatches**  
  Resolved inconsistencies between workflow post function IDs stored in PowerScripts and their corresponding IDs in Jira.
- **Fixed issue link filtering in the** `allLinkedIssues()` **function**  
  Fixed an issue where `allLinkedIssues(issueKey, linkType)` returned sub-task parent issues even when they did not match the specified link type. The function now returns only issues matching the requested link type, consistent with Jira Data Center behavior. Parent and sub-task relationships are included when using an unfiltered call or the relevant Parent/Sub-task link types.

**Questions and feedback**

- Explore features, pricing, and reviews on the [Marketplace](https://marketplace.atlassian.com/apps/43318/power-scripts-jira-workflow-automation?tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/43318/power-scripts-jira-workflow-automation?tab=reviews).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Power Scripts for Jira Cloud!