# Troubleshooting: Field mapping button is grayed out

## Problem

- As a Box Admin, I cannot access the custom field mapping screen because the button is grayed out.

![image-20240209-093351.png](/cms_trial/assets/bae1c5f2-7c3f-4b74-935c-f43bc7c4547b.png)

## Solution

Custom field mapping can be set directly in a box when the scope of that box contains only one Jira project or tasks from one Jira project.

In such a case, a Jira or App Admin can [customize the field mapping](/cms_trial/space/SPM/1918635376/Fields/) for the respective projects in the scope.

## Detailed steps

1. Click the **wrench icon** (**App settings**) and select **General** on the dropdown.
2. You are now on the **Fields > General mapping** page. Switch to the **Custom mapping** tab.
3. Click the **Add project** button.
4. The **Add project** modal displays.

![Add project modal on the App Configuration page.](/cms_trial/assets/fb6ef6e1-6dca-4b2f-9de9-fe6afb8d865e.png)

1. Select a Jira project from the dropdown. Confirm with the **Add and configure** button.
2. A field mapping screen displays for the selected Jira project.
3. Customize the field mapping.
4. Click **Save**.
5. Repeat the same process for other Jira projects.

## More information

- [Fields](/cms_trial/space/SPM/1918635376/Fields/)