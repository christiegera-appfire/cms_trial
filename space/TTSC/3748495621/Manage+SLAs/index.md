# Manage SLAs

The *SLAs* page displays your configured SLAs and provides options to search, review, edit, clone, enable, disable, and delete them. You can also customize which SLA details appear on the page.

![The SLAs screen, with different actions you can take on the screen highlighted.](/cms_trial/assets/f25e6571-9e5a-47bf-aee2-525bf0246968.png)

1. **SLAs:** Access the list of configured SLAs.
2. **Search:** Find SLAs by selecting a search category and entering a search term. Available categories include *SLA name*, *Project*, *Issue type*, *Priority*, *Request type*, *JQL*, and *Filter*.

   ![A screenshot showing how to use the search bar on SLAs screen.](/cms_trial/assets/d2957b86-9aea-4fce-95d4-8238ae09f740.png)

   For example, select **Priority** and enter `Blocker` to find SLAs that include this priority in their SLA context. Search results depend on the values configured for each SLA.
3. **Hide disabled SLAs:** Select this checkbox to exclude disabled SLAs from the list. Clear it to display both enabled and disabled SLAs. The checkbox is selected by default unless you've saved a different preference.
4. **SLA list:** View your configured SLAs. Click an SLA name to open its details, or select the expand control next to an SLA to view its configuration summary. The displayed information includes the columns you've selected, such as SLA context, conditions, and goals.
5. **Columns:** Customize the information displayed in the expanded SLA details. Select **Columns**, choose the columns you want to display, and click **Done** to apply your changes.
6. **SLA options menu:** Expand an SLA and click the **More** (three-dot) menu to access the following actions:

   ![A screenshot showing the SLA options menu.](/cms_trial/assets/9a9b4ef2-1619-428e-9d2b-c6416e9eea77.png)
   - **Edit:** Open the SLA configuration for editing. After making changes that affect existing SLA calculations, [recalculate SLA data](/cms_trial/space/TTSC/35456416/Recalculation/) to update affected work items.
   - **Manage notifiers:** Configure and manage notifications for the selected SLA.
   - **Clone:** Create a copy of an existing SLA. SLAs created using the old interface (created before June 20, 2024) cannot be cloned. You must create new ones using the new system.
   - **Enable/Disable:** Click to enable or disable the SLA. When an SLA is disabled, all SLA actions are stopped. The SLA won’t appear in fields, reports, and other configurations.   
     You can use this feature to hide SLAs that are irrelevant to your workflow but might be needed in the future. Disabling such SLAs preserves configurations for potential future use.
   - **Delete:** Permanently delete the SLA. This action can't be undone.