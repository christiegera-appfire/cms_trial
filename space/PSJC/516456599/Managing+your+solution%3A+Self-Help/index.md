# Managing your solution: Self-Help

## SIL Engine Lifecycle

Typically, your engine is always on. However, there might be situations where you need to complete an engine operation in **Self Help** > **SIL Engine Operations.** Here, you can query the engine status and restart it.

![Power Scripts for Jira Cloud backup and restore interface](/cms_trial/assets/b7d67854-c26b-4a1e-b1f7-a375926a3af0.png)

There are rare occasions when the UI works but attempts to contact the engine result in HTTP 401 errors. In these instances, reconfiguration may be required. Only press the **Reconfigure** button in these instances or when instructed by support. After pressing **Restart** or **Reconfigure,** allowup to three minutes for the engine to be operational.

## Monitoring and Global Status

The global status handler displays:

- System availability.
- Maintenance operations.
- Operational problems.

![Power Scripts for Jira Cloud backup and restore tutorial video](/cms_trial/assets/a741e411-7a78-4089-869c-0f52ac5e89a9.png)

Use [this page](https://appfire.atlassian.net/wiki/spaces/PSJC/pages/490998922) for instructions on how to remotely monitor your SIL Engine.

## Backup and Restore

Backup and restore is used for for SIL Scripts and the accompanying files, including silprograms and kepler directories.

![Power Scripts for Jira Cloud engine resize settings panel](/cms_trial/assets/c52ed2c2-909a-4893-98ab-09e5b1363d82.png)

The following video explains these operations:

![Power Scripts for Jira Cloud system messages interface](/cms_trial/assets/c89fb382-9aa7-43e4-8e35-42ae979d5882.mp4)

## Engine Resize

When additional resources are required, request an engine resize by completing the form in **Self Help** > **Engine Resize.** You can also[review this page](/cms_trial/space/PSJC/504004659/Cloud+Performance+and+Resources/) for more information.

![Power Scripts for Jira Cloud advanced configuration panel](/cms_trial/assets/195a02df-7751-4127-ae42-1b51c79dac9c.png)

## Messages

When messages are available, they appear in administrative pages, similar to the example below. To read the messages, open **Self Help** > **Messages**

![Power Scripts for Jira Cloud TLS SSL configuration interface](/cms_trial/assets/1dbad688-29bf-46e9-a984-734fe1587df7.png)

## Atlassian API Token

Starting with version 3.0.14, administrative functions that require an Atlassian API token were added to the system. The functions were furthers refined in subsequent versions and in version 3.2.0 we added the ability for the tokens to be auto-removed from the product after a certain period.

To obtain an Atlassian token, visit:

<https://id.atlassian.com/manage-profile/security/api-tokens>

To obtain an Organizational token, see:

<https://support.atlassian.com/organization-administration/docs/manage-an-organization-with-the-admin-apis/>

Notes:

- Atlassian Tokens are specific to individuals and should not be shared.
- Organizational tokens should be treated as any secrets; they should not be shared.
- The token must belong to a user with Jira administrative privileges otherwise the administrative functions will fail.

To use the token, simply enter the email address for the user who generated the token and the token itself.

The token is stored securely and is used for administrative functions. If these functions are not used, the token is not required.

![Power Scripts for Jira Cloud menu bar options display](/cms_trial/assets/93c8c0fd-49bb-45cf-905f-3e270dbc05de.png)

If you specify the dates, the tokens will be removed from our product at that date. Note that the tokens may still be valid, so read the “Expires on“ more like “auto-remove after”.

We do not check the validity of the tokens and we do not communicate with Atlassian products on this matter. It is your responsibility. Specific administrative functions notify you in the documentation if a token is required or not. Therefore they are not mandatory to be filled in unless you use those administrative routines / functions.

## TLS / SSL - Securing your endpoints

Starting with version 3.0.13, a method for configuring private keys and certificates was added to create a more secure Cloud environment.

![Power Scripts for Jira Cloud toolbar interface options](/cms_trial/assets/fe636b48-b3be-4f3f-930d-c4a719a50292.png)

Please [check this page for details](/cms_trial/space/PSJC/601819283/TLS+%2F+SSL+configuration/).