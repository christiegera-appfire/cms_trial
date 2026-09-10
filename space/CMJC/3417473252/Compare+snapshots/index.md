# Compare snapshots

## Overview

Snapshot comparison lets you analyze the differences between two versions of the same snapshot scope. Only different versions of the same snapshot can be compared.

Comparisons help you review configuration changes over time, identify added or removed configuration objects, and verify updates before deploying a snapshot.

## Prerequisites

Before comparing snapshots:

- Install and license CMJ Cloud on your Jira Cloud site.
- Ensure you have Site Admin or Organization Admin permissions.
- Create at least two versions of the same snapshot.

## Compare snapshots

1. In your Jira Cloud site, go to **Apps > Configuration Manager > Snapshots**.
2. Start a comparison by opening the snapshot summary screen and selecting the **Comparison** tab.

   ![Comparison Empty View.png](/cms_trial/assets/31f1239f-e50d-433a-97bf-40d0fbaeb7b7.png)
3. Select the source snapshot version and the destination snapshot version.
4. Click **Compare** to start the comparison.

   💡 **Note:** You can only compare different versions of the same snapshot. If you only have one version, the comparison feature will be unavailable.
5. Review the comparison results. CMJ groups the analyzed configuration objects into the following filters:

   - **Unique to source snapshot** – Configuration objects that exist only in the source version.
   - **Unique to destination snapshot** – Configuration objects that exist only in the destination version.
   - **Different** – Configuration objects that exist in both versions but contain differences.
   - **Identical** – Configuration objects that are unchanged between versions.

![Comparison Analysis View.png](/cms_trial/assets/cfa55f47-a8ce-4f97-8fdd-b21ccd5e4cb6.png)

1. Select a category or configuration object to view detailed information.

### Review comparison details

When you open a configuration object from the comparison results, the following tabs are available:

#### Overview

Displays information about the selected configuration object:

- If the element exists in both snapshot versions, CMJ shows information from both the source and destination versions.
- If the element exists in only one version, CMJ shows information only for the available version.

![Comparison-Overview.png](/cms_trial/assets/e0294868-fbae-4009-847a-94c744ccaac3.png)

#### Differences

Displays the differences detected between the source and destination versions of the selected configuration object and its sub-elements.

![Comparison Differences.png](/cms_trial/assets/6d4e4535-31eb-456a-808d-ea606b005338.png)

### Manage a comparison

While viewing a comparison, you can:

1. Click **X** in the upper-right corner to exit the comparison.
2. Click **Delete** to remove the comparison.
3. Use the **Compared to** drop-down menu to select a different destination snapshot version.
4. Click **New Comparison** to run a comparison against the newly selected version.

![Comparison-Options.png](/cms_trial/assets/69b022d0-9246-409d-bad3-64ebeac52b66.png)