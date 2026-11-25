# Data residency and retention (Cloud)

## What data residency means for Planning Poker

Planning Poker for Jira ("App" or "Planning Poker") offers data residency options. Data residency gives you control over where the in-scope end-user data processed by the App is hosted. In other words, it lets you choose a defined geographic location for that data.

The data residency option available for the App serves, in particular, to:

- help you ensure compliance with local data protection laws,
- enhance security by storing data within specific jurisdictions, and
- give users greater control over their personal information, fostering trust and reducing legal risks.

## Where data is stored

You can store Planning Poker in-scope end-user data in one of these regions, available from [Google Cloud Platform](https://cloud.google.com/about/locations) data centers:

- **europe-west1 (Belgium)**
- **us-central1 (Iowa, United States)**
- **asia-southeast1 (Singapore)**

Planning Poker works with four realms: **US**, **EU**, **SG**, and **global (default)**. The global default is hosted in us-central1.

The region is chosen by your Jira site's data residency realm, which is managed by Atlassian or your organization:

- **If your Jira site is pinned to a supported realm (US, EU or SG):** Planning Poker stores and processes your app data in the same region.
- **If your Jira site is not pinned, or is pinned to a realm Planning Poker does not support:** your data is stored in the global default, in the U.S. (**us-central1, Iowa, United States**).
- **If you installed Planning Poker before data residency was available,** your data stays in the global default (**us-central1, Iowa, United States**).

### Move data between regions

When your Jira site moves to another realm, Planning Poker moves its app data to the same realm through an automated migration. The migration includes error handling and rollback, so no data is lost. If you need help, contact our [Support team](https://appfire.atlassian.net/servicedesk/customer/portal/11/group/36/create/161).

## In-scope end-user data

The following data is stored in the Planning Poker database in your region:

- Game state, including the game name and Jira issue keys
- Votes
- Participants (Jira account IDs and display names)
- Timer
- Game configuration
- Installation metadata: Jira client key (`clientKey`), installation ID (`installationId`), cloud ID (`cloudId`), Forge settings, and keep-alive timestamps

## Inherited from Jira

The following data is stored in your Jira site, in Jira's data residency region. It moves with your Jira site, is owned by Jira, and stays in Jira after you uninstall the App:

- **Issue data and worklogs** that the App reads from or writes to Jira (for example, summaries, assignees, estimates, and worklog authors).
- **App and project properties** `pp-conf` **and** `disablePokerLink`**.** These are on/off settings (booleans). They contain no personal data.
- **Legacy issue property** `async-game`**.** This is historical estimate data stored on the Jira issue by an earlier version of the App. It can include the account IDs and names of players. It is not a configuration flag.

## Out-of-scope product data

The following data may be processed outside the region Planning Poker is pinned to:

- **Amplitude (analytics, from the browser, the Forge backend and cloud functions):** Jira account ID, cloud ID, installation ID, license details, game, issue and project IDs, estimation values and the names of estimation fields. It does not include issue summaries, game names, names, or emails.
- **LogRocket (session monitoring):** Jira account ID, license type and ID, and your Jira site URL. LogRocket also records a replay of the screen, which can show issue summaries, game names, and user names. Input fields are masked. The `clientKey` is not sent.
- **Bugsnag (error reporting):** Jira account ID, stack traces, error messages, page URLs, and breadcrumbs, which can contain issue keys. The `clientKey` is not sent.
- **SendGrid (game-invite emails):** the recipient's name and email address, the game name, the creator's name, and the game link, which contains your Jira site URL and the game ID.
- **Operational logs (Google Cloud Logging):** technical identifiers such as the `clientKey`, cloud ID, installation ID and migration ID, plus error messages. We found no end-user names or email addresses in the logged fields.

## Retention

One retention policy applies in every region. Planning Poker treats an installation as uninstalled when it has not sent its daily heartbeat for 25 hours. Its data is deleted 90 days after that detection.

- **Removed:** the game data and installation metadata stored in the Planning Poker database, including client key mappings, Forge settings, and keep-alive records.
- **Not removed:** data inherited from Jira (see above), analytics data held by third parties, and data residency migration records.
- **Reinstall before the purge:** if you reinstall the same installation within the 90 days, the scheduled deletion is cancelled, your data is kept, and the 90-day clock restarts after any later uninstall.

## Backups

Production backups are kept in the same geography as your data: global and US data in the United States, EU data in the European Union, and SG data in Asia. Each regional database also has an in-region backup copy, kept for 30 days.

## Sub-processors

- Google Cloud / Firebase
- Amazon Web Services (backup storage)
- SendGrid
- Amplitude
- LogRocket
- Bugsnag

## Support

Questions about data residency or data retention: [contact Appfire Support](https://appfire.atlassian.net/servicedesk/customer/portal/11/group/36/create/161).