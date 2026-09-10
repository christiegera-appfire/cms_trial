# Release notes 30 July 2026

**Release date**: July 30, 2026

This page outlines the updates included in the latest release of Advanced Tables for Confluence.

Version: 7.7.0

---

## Enhancements

## Advanced Table Viewer

### Ask Rovo UI enhancement

The **Ask Rovo** button embedded in the **Advanced Table Viewer** macro now includes contextual tooltips. In the disabled state, it prompts you to take the required action:

- If the **Enable Ask Rovo** toggle is disabled in Global configuration, it prompts you to contact your Confluence Administrator. Refer to [Global configuration](/cms_trial/space/TBL/74812041/Configuration+-+Cloud/).

  ![Global Config_Rovo disabled.png](/cms_trial/assets/987a7f40-250b-4724-ba09-3de856776d80.png)
- If the macro dataset exceeds 1.5 MB, it prompts you to reduce or filter the dataset before sharing.

  ![Ask Rovo_Disabled_tool tip.png](/cms_trial/assets/d40ad9e4-423a-4d2a-993a-1f794e2ff257.png)

For more information, refer to [Analyze Advanced Table Viewer data with Atlassian Rovo](/cms_trial/space/TBL/3429499007/Analyze+Advanced+Table+Viewer+data+with+Atlassian+Rovo/).

### Column calculation UI enhancement

- Renamed **Edit sum up type** to **Edit column calculation**.

  ![Edit column calculation](/cms_trial/assets/6b8ea448-6d5a-42f1-a205-2f0131bcc133.png)

---

## Bug fixes

The following bugs are fixed in this release:

- **JSON Table macro** was rendering empty columns for nested field paths when a wildcard array path matched only one item.

  - This issue is resolved, and the JSON Table macro renders correct data regardless of array size when using wildcard array paths and dot-notation fields.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/197/advanced-tables-for-confluence?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/197/advanced-tables-for-confluence?hosting=cloud&tab=reviews).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Advanced Tables for Confluence!