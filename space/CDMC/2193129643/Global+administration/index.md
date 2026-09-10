# Global administration

## Global configuration

Global administration is available to Confluence site administrators.

Navigate to **Apps** > **Comala Document Management** to access the global settings.

Global settings are organized into three tabs:

- **Global Workflows**: Create, manage, and version-control workflows that can be linked or copied across multiple spaces. See [Global workflows](/cms_trial/space/CDMC/2276786309/Global+workflows/) for details.
- **E-Signatures**: Manage signing tokens for all reviewers in the instance. See [E-signatures](/cms_trial/space/CDMC/2192903044/E-signatures+(credentials)/) for details.
- **Settings**: Configure content restriction controls and other global preferences.

![Comala Document Management page showing the Global Workflows, E-Signatures, and Settings tabs.](/cms_trial/assets/10105b3a-e619-48f8-af3d-942efeff95ea.png)

## Approval signing code admin

If [E-signature](/cms_trial/space/CDMC/2192903044/E-signatures+(credentials)/) is enabled for an approval, reviewers must set up a signing token using an authenticator app. Administrators can manage all signing tokens from the *E-Signatures* tab.

In global administration, to access the **Users with signing tokens** screen:

- Navigate to **Apps** > **Comala Document Management** to access the global settings.
- Go to the *E-signatures* tab. You’ll find the list of users with approval signing tokens.

The screen displays the following:

- User name
- Token expiry date
- Date created
- Last token usage attempt by each user
- Number of failed token authentication attempts by each user

![E-Signatures tab listing users with signing tokens and their token status information.](/cms_trial/assets/6b234296-726a-4714-924a-bf15053a7838.png)

As a global administrator, you can also set an expiry date for a user token or remove the token.

- **Set expiry date**: To amend a token's expiration date. Click the **X** icon to clear the existing expiration value. However, *the token expiration date* *can't be blank*.

  ![Edit token expiration date dialog for a user's signing token.](/cms_trial/assets/bf3be9e0-e770-4e25-a22a-0d9f871049d2.png)
- **Remove token:** To remove the user’s approval signing token from the site. When a user’s signing token is removed, they must set up a new token using a third-party authentication app.

![Actions menu for a signing token showing options to set an expiry date or remove the token.](/cms_trial/assets/18ccf275-4a0b-45b5-9b52-4574802c4196.png)

### Content restriction settings

**Configure how CDM handles restricted pages** from the *Content Restrictions* section under *Settings*. Two toggles are available:

- **Grant Automatic Add-on User Access**: Automatically grants the add-on edit access when users restrict a document. Turn this off to prevent the add-on from accessing restricted pages (workflows stop functioning on those pages).
- **Enforce & Lock Space-Level Override**: Enforces the above setting globally and locks it for space admins, preventing them from overriding it at the space level.

![Comala 2026 release notes dialog update](/cms_trial/assets/99d296ee-d249-464a-be9f-35939ee53143.png)

Settings visibility is based on user permissions. Each tab in *Space Settings* and *Global Settings* is shown or hidden depending on the user’s role:

- **Non-admin users** see only the *Document Report* tab in *Space Settings*.
- **Space admins** can access the *Space Workflows* and *Settings* tabs.
- **Site admins** can access *Global Settings*.

## Global permissions configuration

Installing the app will also automatically add the Comala Approvals for the Confluence Cloud app system user and [configure the global and space permissions for the app system user](/cms_trial/space/CDMC/2192870224/App+scope+and+permissions/).

## App access for a Confluence site accessed behind a company firewall

Some users access Confluence behind a corporate firewall that limits the URLs they can access.

Recent updates to the app use asynchronous notifications of state changes that require one or more URLs.

If the app is used behind a firewall, it may not behave as expected, as the app functions require access to these URLs.

The following URLs need to be on the **URL Allow List** or equivalent for your company firewall for the app to function correctly

- `https://doc-m.comalatech.app`
- `api.sparkpost.com`
- `https://publishing.comalatech.app`
- `api2.amplitude.com`

### Related topics

- [Global workflows](/cms_trial/space/CDMC/2276786309/Global+workflows/)
- [E-signatures](/cms_trial/space/CDMC/2192903044/E-signatures+(credentials)/)
- [Space administration](/cms_trial/space/CDMC/2192776249/Space+administration/)
- [Workflow state dialog](/cms_trial/space/CDMC/2193129918/Workflow+state+dialog/)