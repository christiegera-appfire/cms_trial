# Manage Rich Filters

## **About rich filters**

The Rich Filters *Home*page allows you to create, navigate through, and edit existing rich filters. To access it, open the **Apps** section of Jira’s main menu and click**Rich Filters**.

![Apps_Rich FIlters.png](/cms_trial/assets/1c431eeb-0d7d-4fd0-9e2c-ad469e2dc380.png)

The Rich Filters *Home* page lists all the rich filters you can view. (See [Rights and Permissions](/cms_trial/space/RFCDOC/783941839/Rights+and+Permissions/) for more about access rights.)

![home.png](/cms_trial/assets/b98e1964-40ad-4ae8-9c3e-42cb54bdabab.png)

## Manage Rich Filters

### 1. Create a new rich filter

You need to have [Create Rich Filters permission](/cms_trial/space/RFCDOC/783941839/Rights+and+Permissions/) to perform this operation.

1. Click **Create rich filter** at the top-right of the screen.

   ![create rich filter](/cms_trial/assets/0624a34e-3169-4ca3-ac54-d340333e6579.png)
2. Choose a name, select an existing native Jira saved filter as the base for your rich filter, and click **Create**.

   ![Create rich filter](/cms_trial/assets/204be430-9ec9-4c26-b227-9a774d622d78.png)

By default, the maximum number of rich filters that can be created on one given Jira Cloud instance is 1,000. If you need to create more rich filters, please get in touch with our support service to request an increase in this limit for your Jira Cloud instance.

### 2. **Find an existing rich filter**

1. Use the search box at the top left to find rich filters by name.

   ![Search option](/cms_trial/assets/50266e7e-1b4a-4813-8345-86173a5f2b6b.png)
2. Search filters by their admin using the **Administrator** dropdown.

![Admin search](/cms_trial/assets/a0637a0d-d35c-40a0-ad86-041ebcb7d4eb.png)

You can see only the rich filters based on Jira saved filters shared with you and the rich filters you’re an administrator of. If you are an administrator of a rich filter but the base Jira saved filter is not shared with you, then you'll be able to see the rich filter but not the filter it's based on (you'll be able to change it if you want).

Search results are limited to about 50 filters. Try using `+` before keywords to narrow results (for example, `+abc +xyz`), or put search terms in quotes for exact matches. The search doesn't work reliably with special characters in filter names (like (), /, or - ). For detailed search tips and limitations, see [Rich filter search](/cms_trial/space/RFCDOC/3374972942/Rich+filter+search/).

### 3. **View and edit the configuration of a rich filter**

If you can see a rich filter on the *Rich Filters list* page, you can also view its configuration. However, only the [rich filter’s administrators](/cms_trial/space/RFCDOC/783941695/Details+configuration/) and Jira Administrators can change (edit) its configuration. See the [Rights and Permissions](/cms_trial/space/RFCDOC/783941839/Rights+and+Permissions/) section for more about access rights.

- Click the rich filter’s name.

  ![Filter name.png](/cms_trial/assets/8cdc6721-772c-450e-a534-ffb15631f391.png)
- You can also click the **View** option in the **Menu** of any rich filter.

  ![view.png](/cms_trial/assets/c9896c14-22f7-4d20-a7de-2e768964bb45.png)

### 4. **Duplicate a rich filter**

1. Select the **Duplicate** option in the **Menu** of any rich filter.

   ![duplicate.png](/cms_trial/assets/2b31b7a9-5137-4a29-b8b9-fc7e986bc601.png)
2. Type the name of the new rich filter and click **Duplicate**.   
   A new rich filter is created, identical to the first one but with your entered name.

   ![duplicate filter.png](/cms_trial/assets/035cf054-37b5-499f-8307-9b45ff74d831.png)

### **5. Move to trash a rich filter**

Only the [rich filter's administrators](/cms_trial/space/RFCDOC/783941695/Details+configuration/) and [Jira Administrators](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/) can perform this operation.

- Click the **Move to Trash**option in the **Menu** of any rich filter.

  ![move_to trash.png](/cms_trial/assets/27e072e1-9113-40a5-b672-8c0d145cbf44.png)
- You can also click **Trash** in the left pane menu on the configuration page of each rich filter.

  ![trash.png](/cms_trial/assets/6db3d2f4-11a1-4f44-9974-a5101e4cc888.png)

After 60 days, discarded rich filters are permanently deleted. During this period, their admins can view, manually restore, or manage them forever.

## **Archived rich filters**

Rich filters that are not used for **180 days** are automatically archived. A rich filter is considered *used* or *active* when a gadget based on it is loaded in a dashboard or when the rich filter’s configuration is changed. Once archived, rich filters can no longer be edited or selected in the configuration of rich filter gadgets. However, if an existing dashboard based on an archived rich filter is loaded, the rich filter is automatically unarchived.

To access the list of archived rich filters, click **Archive** on the left pane.

![archive.png](/cms_trial/assets/d2f90d1b-478b-4940-9b1e-25b7d38b0ed1.png)

Once archived, a rich filter can be accessed only by its administrators. The available actions for the archived rich filters are to view the configuration in read-only mode, delete the rich filter, or unarchive it.

Archived rich filters are never deleted automatically. They remain archived until one of their administrators deletes or unarchives them. Also, an archived rich filter is automatically unarchived if any user loads an existing dashboard based on it.

## **Trashed rich filters**

*Trashed rich filters* are rich filters that have been moved to trash, as explained in the [About rich filters](/wiki/pages/resumedraft.action?draftId=783941683#ManagingRichFilters-section1) section. Once trashed, they cannot be edited or used in gadgets anymore, and they will be automatically deleted forever after **60 days**.

To access the list of trashed rich filters, click **Trash** on the left pane.

![trash.png](/cms_trial/assets/6db3d2f4-11a1-4f44-9974-a5101e4cc888.png)

After being moved to the trash, a rich filter remains accessible exclusively to its administrators until it is permanently deleted 60 days later. During this period, administrators can perform the following actions:

- **View:** view the rich filter configuration in read-only mode
- **Download usage data**: get an Excel file with the usage information
- **Delete forever**: permanently delete the rich filter
- **Restore from trash**: restore the rich filter to use it again

![filters trash.png](/cms_trial/assets/781834b2-d3a3-464f-bcea-2758562dc5b7.png)

Trashed rich filters do not count toward the 5,000 rich filters limit per instance, while archived rich filters do count. We recommend to regularly move archived rich filters to the trash using the **Move to trash** bulk operation, to free up space for new rich filters.