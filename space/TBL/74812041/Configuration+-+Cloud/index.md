# Configuration - Cloud

Check out this video for detailed configuration guidance, including how to set up and use custom Profiles.

## Advanced Tables Configuration

After [installing](/cms_trial/space/TBL/74814028/Installation/) or updating the Advanced Tables for Confluence app, configure the app settings in the Advanced Table Configuration screen.

You can navigate to the configuration screen from either **Settings** or the **App connections** section.

To navigate to the configuration screen from **Settings**:

1. Log in as a Confluence administrator and select **Settings**(▢).
2. In the left navigation, under **Apps**, click **Advanced Tables Configuration**.
3. The **Advanced Tables** **Configuration** page opens.

   ![AT_Global configuration page.png](/cms_trial/assets/0b28f44b-90e8-4d26-b47e-db35f8507f02.png)

To navigate to the configuration screen from the **App** **connections** section.

1. Log in to <https://admin.atlassian.com/> as a Confluence administrator and select your **organization**.
2. In the left navigation pane, go to **Apps** and under **Sites**, click the **Site** name.
3. The **Site settings** page opens. Under **Site settings**, click **Connected apps**.
4. On the **Connected apps** page, search for **Advanced Tables for Confluence** and click **View app details**.

   ![Advanced Tables_connected apps.jpg](/cms_trial/assets/76bffa18-0287-4448-b97a-c470a4900844.jpg)
5. The app **Details** page opens. Go to the **Connections** tab.

   ![App details page_connections.png](/cms_trial/assets/35c5b5b2-221b-45ad-877f-fc7ba0896eb4.png)
6. In the **App connections** section, for the Confluence app, under **Actions**, click **Configure**.

   ![Connections_click Configure.png](/cms_trial/assets/22826e09-cfe3-4b83-a9f3-5307cf4f4daa.png)
7. The **Advanced Tables** **Configuration** page opens.

   ![AT_Global Config page.png](/cms_trial/assets/dc6be8cb-f240-4690-beb8-587db73ce574.png)

The following configuration options are available:

- [Global Configuration](/cms_trial/space/TBL/74812041/Configuration+-+Cloud/)
- [Profiles](/cms_trial/space/TBL/74812041/Configuration+-+Cloud/) (available for CSV Table, JSON Table, and Advanced Table Viewer macros)

### Global configuration

Use the toggle to enable or disable the *Global configuration* settings.

![AT_Global configuration.png](/cms_trial/assets/bc076ebd-1296-4815-9d77-2731bede4bbb.png)

Click **Save** to save the modified settings.

As an administrator, you can:

| **Parameter** | **Default** | **Description** |
| --- | --- | --- |
| Allow JavaScript | ON | Enable this option to allow execution of JavaScript within the *Advanced Tables for Confluence* macros.  This parameter is not applicable for the *Attachment Table* macro. |
| Enable Ask Rovo | ON | - This applies to the **Advanced Table Viewer** and **Native Table Enhancer** macros. - Enable this option toactivate the **Ask Rovo** button in the Advanced Table Viewer macro and Native Table Enhancer macros. When a user opens Ask Rovo in the macro, the table data is sent to Rovo for analysis. Before enabling, review [Rovo usage allowance](https://support.atlassian.com/rovo/docs/rovo-usage-limits/). - You can disable the **Enable Ask Rovo** toggle at any time to manage Rovo usage. When disabled, the Ask Rovo button remains visible in the macro but is disabled, with a tooltip prompting users to contact their Confluence Administrator. - For more information, refer to [Analyze Advanced Table Viewer data with Atlassian Rovo](/cms_trial/space/TBL/3429499007/Analyze+Advanced+Table+Viewer+data+with+Atlassian+Rovo/) and [Analyze Native Table Enhancer data with Atlassian Rovo](/cms_trial/space/TBL/3568173411/Analyze+Native+Table+Enhancer+%5BBeta%5D+macro+data+with+Atlassian+Rovo/).   - Rovo is automatically [activated](https://www.atlassian.com/software/rovo/guides/admin-guide/rovo-activation) for Enterprise, Premium, and Standard Cloud plans. To fully use Rovo, AI must be enabled on each site to which Rovo has been added. If Rovo is not enabled, contact your Atlassian Organization Administrator. [Read more](https://support.atlassian.com/organization-administration/docs/manage-rovo-access/). - If Ask Rovo isn't working, contact your Atlassian Organization Administrator to check **Atlassian Administration > Rovo > Rovo access** and confirm Confluence isn't on the blocked list. [Read more](https://support.atlassian.com/organization-administration/docs/manage-rovo-access/). |
| Help us improve the product | ON | Enable this option to report usage data that helps us improve the app continually. The app does not send any private user data or personally identifiable information. To learn more about what is being sent, refer to [Data security and privacy](/cms_trial/space/TBL/74815010/Data+security+and+privacy/). |

### Profiles

Profiles consist of a common set of parameters that allow users to use the configured profile in the macros. Some advantages of using profiles are:

- Profiles allow user authentication required by some URLs to be hidden from page viewers and editors. Only Confluence administrators have access to this information.
- Enables macro editors to quickly configure the macro by reusing a shared definition for URL access.
- Relative addressing can be used, making the page content less likely to require changes when base URLs are relocated.

  - Macro configured URL (that is not a full URL) is appended to the profile provided URL.

As only the CSV Table, JSON Table, and Advanced Table Viewer macros have the ability to access external data through URLs, profiles can be used only in these macros.

![Advanced Tables Profiles list with configured URL profiles for macros](/cms_trial/assets/6b4bda9a-de8f-48ac-a64b-09f19360f4da.jpg)

The page displays a list of profiles available for the macros. Click **Add profile** to open a pop-up window as:

![Advanced Tables Add Profile dialog with name, type, URL, and credentials](/cms_trial/assets/67afd819-5e0b-499d-b21e-6793756b526f.jpg)

| **Parameter** | **Description** |
| --- | --- |
| *Profile name* | Enter a name for the profile.  This name must be unique; else, the details specified overwrite the details of the existing profile. This may cause errors in pages where the profile is used. |
| *Profile type* | Specify whether this is a URL, GitLab, or GitHub profile. |
| *URL* | Enter the URL to be accessed. If the *Profile type* is either *GitLab* or *GitHub*, a default URL is displayed here that is editable. |
| *User; Password* | - Enter the user name and password to access the specified URL. - For **Atlassian Rest APIs**, ensure you enter the following details**:**    - **User**: Enter your email address.   - **Password**: Enter your **Atlassian API token**. Note that using your Confluence password will not retrieve data for profiles configured with Atlassian URLs. |
| *Access token* | *Applicable for GitLab and GitHub URLs*. Administrators must generate the access tokens from either the GitLab or GitHub applications and enter the same here. |
| *URL parameters* | Mention any extra parameters that must be appended to the URL here. |
| *Request headers* | Displays the request header(s) created as per the given information. |

You can perform the following actions on this page:

- To edit the profile details, click **Edit** ([edit pencil icon]).
- To remove the profile, click **bin**.
- To save the profile, click **Save profile**.