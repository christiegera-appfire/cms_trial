# Release notes 25th August 2026

**Release date**: August 25, 2026

This page outlines the updates included in the latest release of Comala Document Management Cloud.

**App version:** 50.17.0

**Release version:** 5.0.24

---

## New features

### Filter the Space Document Report by workflow

The Space Document Report now includes a **Workflow** filter. Narrow the report to pages with no workflow, a single workflow, or multiple workflows.

---

## Enhancements

### Clearer Document Activity for manual state overrides

Document Activity clearly describes manual state changes. Override entries now read *Changed state from [X] to [Y] (state override)*, so it’s easy to tell when a state was set manually.

### Approvals are now protected during page edits

Workflow actions are now paused while a page edit is still being processed. This prevents approvals and transitions from being lost when a delayed content update arrives.

![approvals-error.png](/cms_trial/assets/ab06a52c-f2f6-4d5f-8ffc-86d9c71d669d.png)

---

## Bug fixes

- Fixed an issue where delayed page-update events could trigger unexpected workflow transitions and undo completed approvals. Updates are now validated against their timestamp and the current workflow state before they are processed.
- The `assignable` and `rememberAsignees` parameters now appear in the Code Editor even when they are set to `false`.
- Fixed an error that occurred when editing a *Set restriction* or *Add restriction* that contained only a group and no individual users.
- Restored the workflow state filters in the Document Report for spaces that use page-level workflows only.
- Assignment activities now record the correct document version from the transition instead of a previously stored value.

---

## Security and privacy

- Patched high-severity dependency vulnerabilities and upgraded `@forge/api` to 8.0.4.
- Added automated logging guardrails, including lint rules, CI checks, and a pull request checklist, to prevent personally identifiable information (PII) from being written to logs.
- A one-time migration removes legacy records that stored user display names in the `startedBy` field, improving data privacy.

---

## Maintenance and platform updates

- Migration SQL error records now expire automatically after 90 days.
- Workflow outcomes records now automatically expire after 7 days unless cleaned up sooner.
- Migrated from the deprecated `confluence:fullPage` Forge module to `global:fullPage` to stay aligned with the latest Atlassian platform modules.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/142/comala-document-management?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/142/comala-document-management?hosting=cloud&tab=reviews).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Appfire's Comala Document Management Cloud!