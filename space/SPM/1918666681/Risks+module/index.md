# Risks module

## Risks module (old navigation)

Click to expand the guide

**Looking for more advanced risk management?**  
Try our new **Risk Management** module, which offers enhanced features like customizable templates, multiple risk registers per box, automatic risk score calculation, and advanced risk reporting capabilities. See more on the [Risk management](/cms_trial/space/SPM/1918502862/Risk+management/) page.

## About the Risks module

Use the **Risks module** to assess the risk probability and consequence and show your risks on the [heatmap](/cms_trial/space/SPM/1918767574/Heatmap+mode+(Risks+module)/). The Risks module consists of two main elements:

- Customizable risk heatmap
- Customizable risks table (register)

The dimensions of the heatmap depend on the number of selected options. The default dimension is 5x5, and it is the recommended size because risk levels are colored with the heatmap mode enabled.

Any issue type can be displayed on the heat map, but to do so, you need to add the **Risk probability** and **Risk consequence** fields to your issue screens first. You can synchronize your risks with other fields.

See more on the [Risks (global configuration)](/cms_trial/space/SPM/1918505973/Risks+(App+configuration)/) page.

![Screenshot of the Risks module.](/cms_trial/assets/02f0c4d9-29e1-4401-9922-acf443e73fa6.png)

## Main features

The table presents the main features of the Risks module.

| **Feature** | **Description** |
| --- | --- |
| [Manage risks](/cms_trial/space/SPM/1918701278/Manage+risks/) (add, edit, delete) | Add new issues to be displayed on the heat map. Any Jira issue can be presented on the heat map, but we recommend creating a separate issue type to represent the identified risks.  There are three options available:   - Create new - Add existing issue - Manage scope definition   The Risks module is also available in boxes with no scope. However, you **can’t** create new risks in such boxes (the **Add** button is greyed out). |
| View options | Change the view options to include more information on the risk heat map or show additional features:   - Compact mode-risks - Heatmap mode – risk levels are color-coded. When the heatmap mode is enabled, the cards will also change their colors to reflect the risk level. - Show heatmap – show/hide the heat map. - Show table – show/hide the register. - Invert and transpose the axis |
| [Column view](/cms_trial/space/SPM/1918404907/Column+views/) | A Box Admin can change the column view without affecting the Box Editor’s or Box Viewer’s view.  A Box Admin must click the **Save changes for all users** button to make changes in the column view visible to box editors and viewers.  Box Editors and box viewers can restore previously changed column views to the ones set by a Box Admin.  After adding or removing columns, a Box Admin can click the **Restore columns** button to return to the initial set. Once changes are saved, the **Restore columns** button becomes inactive. Screenshot of the column view in the Risks module. |
| [Export](https://appfire.atlassian.net/wiki/spaces/BTc) | To unlock the export features, install BigTemplate from the Atlassian Marketplace.   - XLSX - PDF image  Screenshot of the Export feature in the Risks module. Export is disabled in case there are no risks to be exported. Screenshot of the Export feature unavailable in the Risks module. |
| [Quick filters](/cms_trial/space/SPM/1918635901/Quick+filters/) | Add your favorite filters to the header and filter the risks from the list and the heat map. |
| [Date range filter](/cms_trial/space/SPM/1918799022/Date+range+filters/) | Narrow the list of displayed risks to a particular time period using the mapped **Start** and **End date** fields. |
| [Axis description](/cms_trial/space/SPM/1918505973/Risks+(App+configuration)/) | You can change the axis description in the App configuration. Jira Admin access is required. |
| Risk field's values | The module uses the **Select-list** (single-choice) field type, which means you need to preconfigure the select options (Jira admin access is required). |
| Customizable risk card | The layout of the card can be modified in the box configuration section. |
| [Search box](/cms_trial/space/SPM/1918407393/Search+box/) | The search box functionality helps you quickly find your interests and filter out unwanted tasks or work. The search box operates in two modes:   - Text search mode, which filters information based on the Jira Summary field. - JQL mode, which filters information using JQL queries.   To clear the search box, delete your search query, press the enter key, or click the magnifying glass button. Screenshot of the search box in the Risks module. |
| [Card views](/cms_trial/space/SPM/1918536034/Card+views/) | Change the layout of your risk cards and mark your favorite ones using a star. |
| [Risks table](/cms_trial/space/SPM/1918407329/Risks+table+(Risks)/) | Customizable risk table that can display any issue type with the **Risk probability** and **Risk consequence** values set.  Modify the columns of the risk table by adding available Jira fields.  Available actions:   - Edit risks (use inline editing to update field values). - Delete risks – when a risk is deleted, it's only removed from the Risks module, that is, the values of Risk probability and Risk consequence values are cleared, and the risk will not appear on the list. - Sort your risks in ascending or descending order based on the fields added to the risk card. |
| [Inline edit](/cms_trial/space/SPM/1918637324/Inline+edit/) | Inline edit fields Text fields and number fields are displayed on the Risk cards and in the Risk table. |

### Risks in none-scope boxes

The Risks module in the [boxes with no scope](/cms_trial/space/SPM/1918766536/Scope+types/) has access to risks collected from its child boxes from:

- All own-scope boxes one level down (direct children).
- All sub-scope boxes (all levels down) of the own scope boxes mentioned above.

## Risks module (new navigation)

Click to expand the guide

**Looking for more advanced risk management?**  
Try our new **Risk Management** module, which offers enhanced features like customizable templates, multiple risk registers per box, automatic risk score calculation, and advanced risk reporting capabilities. See more on the [Risk management](/cms_trial/space/SPM/1918502862/Risk+management/) page.

## About the Risks module

Use the **Risks module** to assess the risk probability and consequence, and show your risks on the [heatmap](/cms_trial/space/SPM/1918767574/Heatmap+mode+(Risks+module)/). The Risks module consists of two main elements:

- Customizable risk heatmap
- Customizable risks table (register)

The dimensions of the heatmap depend on the number of selected options. The default dimension is 5x5, and it is the recommended size because risk levels are colored with the heatmap mode enabled.

Any work item type can be displayed on the heat map, but to do so, you need to add the **Risk probability** and **Risk consequence** fields to your work item screens first. You can synchronize your risks with other fields.

See more on the [Risks (global configuration)](/cms_trial/space/SPM/1918505973/Risks+(App+configuration)/) page.

![Screenshot of the Risks module.](/cms_trial/assets/43b98474-1777-4d1b-82fc-3f9a744c4a99.png)

## Main features

The table presents the main features of the Risks module.

| **Feature** | **Description** |
| --- | --- |
| [Manage risks](/cms_trial/space/SPM/1918701278/Manage+risks/) (add, edit, delete) | Add new work items to be displayed on the heat map. Any Jira work item can be presented on the heat map, but we recommend creating a separate work item type to represent the identified risks.  There are three options available:   - Create new risk - Add existing risk - Add work items from Jira   The Risks module is also available in boxes with no scope. However, you **can’t** create new risks in such boxes (the **Add** button is greyed out). Screenshot of the Risks tab in the Risks module. |
| View | Change the view options to include more information on the risk heat map or show additional features:   - Sort tasks - Compact mode - Heatmap mode – risk levels are color-coded. When the heatmap mode is enabled, the cards will also change their colors to reflect the risk level. - Transpose the matrix - Invert consequence axis - Invert probability axis |
| [Column view](/cms_trial/space/SPM/1918404907/Column+views/) | A box admin can change the column view without affecting the box editor’s or Box Viewer’s view.  A box admin must click the **Save changes for all users** button to make changes in the column view visible to box editors and viewers.  Box editors and box viewers can restore previously changed column views to the ones set by a box admin.  After adding or removing columns, a box admin can click the **Restore columns** button to return to the initial set. Once changes are saved, the **Restore columns** button becomes inactive. Screenshot of the Column view in the Risks module. |
| [Export](https://appfire.atlassian.net/wiki/spaces/BTc) | To unlock the export features, install BigTemplate from the Atlassian Marketplace.   - XLSX - PDF image  Screenshot of the Export feature in the Risks module. Export is disabled if there are no risks to export. |
| [Quick filters](/cms_trial/space/SPM/1918635901/Quick+filters/) | Add your favorite filters to the header and filter the risks from the list and the heat map. |
| [Date range filter](/cms_trial/space/SPM/1918799022/Date+range+filters/) | Narrow the list of displayed risks to a particular time period using the mapped **Start** and **End date** fields. |
| [Axis description](/cms_trial/space/SPM/1918505973/Risks+(App+configuration)/) | You can change the axis description in the App configuration. Jira Admin access is required. |
| Risk field's values | The module uses the **Select-list** (single-choice) field type, which means you need to preconfigure the select options (Jira admin access is required). |
| Customizable risk card | The layout of the card can be modified in the box configuration section. |
| [Search box](/cms_trial/space/SPM/1918407393/Search+box/) | The search box functionality helps you quickly find your interests and filter out unwanted tasks or work. The search box operates in two modes:   - Text search mode, which filters information based on the Jira Summary field. - JQL mode, which filters information using JQL queries.   To clear the search box, delete your search query, press the enter key, or click the magnifying glass button. Screenshot of the search box in the Risks module. |
| [Card views](/cms_trial/space/SPM/1918536034/Card+views/) | Change the layout of your risk cards and mark your favorite ones using a star. |
| [Risks table](/cms_trial/space/SPM/1918407329/Risks+table+(Risks)/) | Customizable risk table that can display any work item type with the **Risk probability** and **Risk consequence** values set.  Modify the columns of the risk table by adding available Jira fields.  Available actions:   - Edit risks (use inline editing to update field values). - Delete risks – when a risk is deleted, it's only removed from the Risks module, that is, the values of Risk probability and Risk consequence values are cleared, and the risk will not appear on the list. - Sort your risks in ascending or descending order based on the fields added to the risk card. |
| [Inline edit](/cms_trial/space/SPM/1918637324/Inline+edit/) | Inline edit fields, text fields, and number fields are displayed on the Risk cards and in the Risk table. |

### Risks in none-scope boxes

The Risks module in the [boxes with no scope](/cms_trial/space/SPM/1918766536/Scope+types/) has access to risks collected from its child boxes from:

- All own-scope boxes one level down (direct children).
- All sub-scope boxes (all levels down) of the own scope boxes mentioned above.