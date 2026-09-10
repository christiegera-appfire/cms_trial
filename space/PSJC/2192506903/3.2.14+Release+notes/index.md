# 3.2.14 Release notes

**Release date**: July 14, 2025

Our team is thrilled to announce the latest release of Power Scripts for Jira Cloud.

This release includes expanded Product Discovery field support, improved system performance, and some bug fixes.

---

## Enhancements

This release introduces expanded Product Discovery field support and improved system performance to enhance your automation capabilities.

## Enhanced Product Discovery field support

### **Expanded custom field compatibility**

Power Scripts now supports additional Product Discovery custom fields that were previously inaccessible. The following fields can now be used in SIL scripts and automation:

- Confidence
- Designs ready
- Effort
- Impact
- Product Area
- Spec ready
- Value
- Project start
- Project target

**New JPDInterval date type**

Added support for Product Discovery date fields, such as Project start and Project target, through the new JPDInterval SIL type.

## Performance enhancement

### **Increased default resource allocation for automation processing**

We have revised the default resource allocation to provide more memory to customer containers. This enhancement addresses the increased demand for more robust automation processing.

---

## Bug fixes

The following bugs are fixed in this release:

- **Fixed cloneIssue routine failing with field configuration error:** The `cloneIssue()` routine was failing when attempting to clone issues between projects, with users encountering a "Cannot create issue as ordered" error related to creator and priority fields. This issue has been resolved and the `cloneIssue()` routine now works as expected across all project configurations.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/43318/power-scripts-jira-script-automation?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/43318/power-scripts-jira-script-automation?hosting=cloud&tab=reviews).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Power Scripts for Jira Cloud!

---