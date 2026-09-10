# Administration

Time to SLA offers default settings for optimal use and performance. On the **Administration** page, you can modify and adjust some of the default values to suit your needs and system.

![image-20260827-150847.png](/cms_trial/assets/4c66e528-449a-4533-9e1d-566ce277b29a.png)

1. **SLA fields:** Here you can create and manage SLA custom fields. For more information, refer to the related [documentation](/cms_trial/space/TTSC/2875654192/Custom+fields/).
2. **General:** Configure general Time to SLA settings, including:

   - **24/7 calendar time zone:** Select the time zone used for calculations based on the 24/7 calendar.
   - **Require extension reason:** Choose whether users must provide a reason when extending an SLA. This setting is disabled by default. When enabled, users must enter an extension reason before they can extend an SLA.
   - **Require reset reason:** Require users to enter a reason when manually resetting an SLA. This setting is disabled by default and does not apply to resets triggered by workflow post functions.

### About time values

After the move to Forge, time values in several areas of the app now follow your device’s system time zone rather than your Jira profile settings.

This affects SLA start, target, and end dates shown on the SLA panel, SLA history tab, and Detail report. It also applies to the request creation dates shown on the recalculation, background reports, and periodic reports pages.

These changes only affect how times are displayed, not how SLAs are calculated.

1. **Permissions:** Manage access permissions to control who can interact with Time to SLA. [Refer to this page](/cms_trial/space/TTSC/36110655/Manage+permissions/) for details**.**
2. **SLA Panel:** Here you can customize your SLA panel settings, such as where the panel appears and what’s shown on the screen. [Refer to this page](/cms_trial/space/TTSC/35815658/SLA+panel/) for details.
3. **SLA Calculation Scope:** On this page, you can define which work items are eligible for SLA calculations and which users’ webhook events are processed by Time to SLA using the allowlist and blocklist feature. [Refer to this page](/cms_trial/space/TTSC/48529969/SLA+calculation+scope/) to learn more.
4. **Import/Export:** This page provides options for efficiently transferring data in and out of the Time to SLA for Jira Cloud app. For more details, [refer to this page](/cms_trial/space/TTSC/36110672/Import%2FExport/).
5. **API Token:** This is where you generate and manage Rest API tokens, which can help you edit and view your SLA data. For more information, [refer to the documentation](/cms_trial/space/TTSC/36209134/REST+APIs/).
6. **Audit Logs:** Stay informed about the actions taken within your Time to SLA environment by accessing detailed audit logs. [Refer to this page](/cms_trial/space/TTSC/36110718/Audit+logs/) for more details.
7. **Advanced:** In this section, you can specify how frequently you’d like the [SLA Target Date custom field to update](/cms_trial/space/TTSC/35684678/SLA+custom+field/) the Target Date on an SLA and [how often reports](/cms_trial/space/TTSC/36208985/FAQ%3A+Reports/) and [audit logs](https://appfire.atlassian.net/wiki/spaces/TTSC/pages/36012475) should be deleted.