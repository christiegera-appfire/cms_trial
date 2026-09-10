# August 4, 2025

## Engineering Release - JMWE for Jira Cloud 2.3.0

**Release date**: August 4, 2025

This release of **JMWE for Jira Cloud** introduces JMWE compatibility for the Atlassian Government Cloud platform. Additionally, this release includes minor updates and bug fixes. See [Atlassian Government Cloud and JMWE](/cms_trial/space/JMWEC/2249131073/Atlassian+Government+Cloud+and+JMWE/) for more information.

---

## Enhancements

## Extensions

### Renamed the ‘Build-your-own (scripted)’ post function

The [‘Build-your-own (scripted)’](/cms_trial/space/JMWEC/466289991/Build-your-own+(Nunjucks+scripted)+Post+function/) post function has been renamed to ‘Build-your-own (nunjucks script)’ for clarity and consistency.

## UI

### Removed the sorting option for User columns

Due to an issue with sorting and generic user names, sorting has been removed for the ‘By’ column (the user column) in all JMWE administration pages for Actions. This includes [Shared actions](/cms_trial/space/JMWEC/466288975/Shared+actions/), [Scheduled actions](/cms_trial/space/JMWEC/466321868/Scheduled+actions/), and [Event-based actions](/cms_trial/space/JMWEC/465473524/Event-based+actions/).

## Bug fixes

The following bugs are fixed in this release:

- **Wrong options in Event-based action pulldown menu** - When configuring an Event-based action to respond to Sprint-related events, the pulldown menu to select which Board should be monitored does not display the correct options. This has been resolved.
- **‘Create issue(s)’ post function encounters error when copying "Parent Link" field despite "Ignore inapplicable fields" enabled** - In some configurations, the Create issue(s) post function encounters an issue when trying to copy the Parent Link field when it is not applicable to the issues being created. This occurs even when the option “Ignore inapplicable fields” is checked. This has been resolved.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the Marketplace.
- Stuck with something? Raise a ticket with our support team.
- Do you love using our app? Let us know what you think here.

**Credits**

A heartfelt thank you to our valued customers! Your incredible support and feedback inspire us to improve our apps and products continually. You are the driving force behind why we create software. We appreciate your trust in JMWE!