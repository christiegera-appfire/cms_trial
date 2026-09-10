# July 15, 2025

## Feature Release - JMWE for Jira Cloud 2.2.0

**Release date**: July 15, 2025

This release of **JMWE for Jira Cloud** includes Use Case Templates! JMWE now includes more than 30 pre-built configurations covering many of the most common use cases. Additionally, a few UI updates and tools related to deprecated post functions are introduced. Lastly, several bugs have been resolved.

---

## Enhancements

## Extensions

![JMWE for Jira Cloud use case templates selection interface for workflow setup](/cms_trial/assets/30183f9d-59ea-42e6-89e7-62a2133662c7.png)

### Use Case Templates

JMWE for Jira Cloud now includes Use Case Templates! More than 30 pre-built configurations covering many of the most common use cases have been added in a new administration page, providing quick installation of Event-based actions, Scheduled actions, and other workflow automations (though some may require customization for your specific instance). See [Use Case Templates](/cms_trial/space/JMWEC/2196245303/Use+case+templates/) for more information.

### ‘Run as’ option added to Increase value of field post function

The Increase value of field post function has been updated to include the ‘Run as’ option, matching the functionality of the Data Center version of this post function. See [Increase value of field](/cms_trial/space/JMWEC/466289696/Increase+value+of+field/) for more information.

## UI Updates

## Administration

![JMWE for Jira Cloud obsolete functions filter for managing deprecated features](/cms_trial/assets/8796244d-1081-4e73-bd98-49fbe6464a47.png)

### New options for locating Deprecated Post Functions

Due to updates to Atlassian’s infrastructure, several deprecated JMWE post functions will be **completely removed by the end of September 2025**. This update adds an option to several of the Administration pages to help locate deprecated post functions that will need to be replaced. Each of the following pages now include a **Show obsolete only** checkbox in the upper right corner of the screen

- [JMWE workflow extensions](/cms_trial/space/JMWEC/466321411/JMWE+workflow+extensions/)
- [Shared actions](/cms_trial/space/JMWEC/466288975/Shared+actions/)
- [Scheduled actions](/cms_trial/space/JMWEC/466321868/Scheduled+actions/)
- [Event-based actions](/cms_trial/space/JMWEC/465473524/Event-based+actions/)

This checkbox will filter the list to only display obsolete post functions or actions that include obsolete post functions. See [Deprecated post functions](/cms_trial/space/JMWEC/542803231/Deprecated+post+functions/) for more information on how to replace obsolete post functions.

## Actions

### Expanded error payload for webhooks

The webhook error payload has been expanded to include all parent Shared Action IDs, allowing for quick identification of exactly which Shared Action encountered an error.

## Bug fixes

The following bugs are fixed in this release:

- **Event-based actions do not work for Epics in Team-managed projects** - When configuring an Event-based action to trigger against Epics in Team-managed projects causes the Event-based action to not fire. This has been resolved.
- **‘Linked issue status’ Condition and Validator do not work for linked issues in Team-managed projects** - Utilizing a **Linked issue status** [Condition](/cms_trial/space/JMWEC/466323193/Linked+Issues+Status+Condition/) or [Validator](/cms_trial/space/JMWEC/465504708/Linked+Issues+Status+Validator/) on a Company-managed project where the linked issues exist in a Team-managed project causes the Condition or Validator to not function as designed. This has been resolved.
- **Search in ‘Lookup group…’ does not return all groups** - The Lookup group function in the script editors only returns 20 groups. This function has been updated to return 50 groups.
- **Long descriptions for Actions push UI off the page** - Long descriptions for Actions (Shared, Scheduled, and Event-based actions) are not wrapping correctly and are pushing other UI elements off the page, requiring scrolling right. This has been resolved.
- **‘Linked issue status’ settings do not migrate** - When using Configuration Manager for Jira to migrate from Data Center to Cloud, some settings do not migrate. This has been resolved.
- **‘Invalid field’ displays in Automation Rule Builder** - In some circumstances, lists of fields within post function configurations may display the text ‘Invalid field’ for some fields. This most often occurs when a large number of fields are listed. This issue has been resolved.
- **Dark mode display issues** - The configuration screens for some extensions are incorrectly displaying options with a white background even when Jira is configured to use Dark Mode. This has been resolved.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the Marketplace.
- Stuck with something? Raise a ticket with our support team.
- Do you love using our app? Let us know what you think here.

**Credits**

A heartfelt thank you to our valued customers! Your incredible support and feedback inspire us to improve our apps and products continually. You are the driving force behind why we create software. We appreciate your trust in JMWE!