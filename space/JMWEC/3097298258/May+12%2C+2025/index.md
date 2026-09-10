# May 12, 2025

## Feature Release - JMWE for Jira Cloud 1.2.43

**Release date**: May 12, 2025

This release of **JMWE for Jira Cloud** includes Dark Mode support and a new post function - [Send Slack message](/cms_trial/space/JMWEC/1848017067/Send+Slack+message/)! This new post function allows you to send a Slack message to any channel or user on a connected Slack workspace. Additionally, bugs have been resolved.

---

## Enhancements

## Extensions

### New post function - Send Slack message

This new post function allows you to send a message to any channel and user (or group of users) in a connected Slack workspace. You can send plain text notifications using Nunjucks to dynamically write message content, or use the Slack [Block-kit API](https://api.slack.com/block-kit/building) to compose messages. **Please note**: the Slack app **Notifier by Appfire** is required when using this post function; this is a **free app** available on the [Slack Marketplace](https://slack.com/marketplace/A080NTPSM0E).

![JMWE for Jira Cloud Slack integration icon for messaging and notifications](/cms_trial/assets/f311180d-ee61-479f-b3a3-5e1a6e540fa6.png)

![JMWE for Jira Cloud dark mode interface theme for improved user experience](/cms_trial/assets/e3fc1481-a0c1-4b4a-91a1-d52365f16ea3.png)

## UI Updates

### Dark mode support for JMWE

[Dark mode](https://community.atlassian.com/forums/Jira-articles/How-to-turn-on-dark-mode-in-Jira/ba-p/2371322) is now fully supported in JMWE! All JMWE screens have been updated when switching Jira to Dark mode. **Please note**: there are no configurations required for JMWE Dark mode - the app matches your Jira configuration.

## Bug fixes

The following bugs are fixed in this release:

- **Editing post functions on slow connections causes loss of configuration** - In some instances, editing a post function using a slower connection would lead to lost scripts in configurations even when the UI displayed the configuration correctly. This has been resolved.
- **Issue picker is fetching incorrect issues** - In some circumstances, configuration options that retrieve issues are not fetching the correct issues even when an issue key is input. This has been resolved.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the Marketplace.
- Stuck with something? Raise a ticket with our support team.
- Do you love using our app? Let us know what you think here.

**Credits**

A heartfelt thank you to our valued customers! Your incredible support and feedback inspire us to improve our apps and products continually. You are the driving force behind why we create software. We appreciate your trust in JMWE!