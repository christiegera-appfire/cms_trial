# Analyze changes

## Analyze screen

After Configuration Manager for Jira (CMJ) Cloud finishes analyzing the project configurations and all elements associated with them, it presents you with the *Analyze* screen. There, you’ll find a detailed and structured view of all configuration elements included in your deployment.

![image.png](/cms_trial/assets/8c515b2b-df86-4061-a51d-ed333766a1e4.png)

### Bulk transformations

The **Bulk transformations** button in the top-right corner lets you efficiently modify multiple configuration elements within a deployment by applying changes from a JSON file. You can rename, remap, or adjust configuration objects before deploying them to a destination Jira Cloud site.

Refer to the [Bulk transformations](/cms_trial/space/CMJC/1851621940/Bulk+transformations/) page to learn more about them and how to better utilize JSON files.

![image (1).png](/cms_trial/assets/f51c41e1-4285-489b-bc74-74c35e309623.png)

### Configuration type cards

CMJ Cloud displays your configuration elements in the form of “configuration type cards”. All of these configuration type cards, along with the filter cards above them, allow for efficient navigation and review of deployment changes.

![IssueTypeObjectCard.png](/cms_trial/assets/91c0c16d-16e6-47c9-8bbc-55c900b23640.png)

Each card has four icons that serve as shortcut filters:

- ▢ – New objects to add
- ▢ – Existing objects to modify
- ▢/▢ – Configuration problems
- ▢ – Objects with no changes

The [Filter cards and icons](#Filter-cards-and-icons) section provides information about each icon you may encounter on the *Analyze* screen.

Clicking on any card automatically applies a filter to the overall analysis and navigates you to [*the detailed analysis info screen*](#Detailed-analysis-info-screen) for that configuration object. Alternatively, you can view the full list of configuration objects by clicking **View all X elements sorted by type** button at the bottom and manually navigating the detailed analysis info screen.

![image (7).png](/cms_trial/assets/66d83426-e851-4b00-8f79-433bd8319fd1.png)

### Filter cards and icons

![FilterCards.png](/cms_trial/assets/a33d4f89-f0db-48bb-97e5-70d06f7a2b1f.png)

At the top of the Analyze page, you will find the filter cards. They contain headings and icons to indicate the type of filter they’ll each apply. Also, they’re broken up into three sections - *Change*, *Problem*, and *Transformation*. You can use these filter cards to quickly apply the corresponding filter and move to the detailed analysis info screen to inspect the results.

Below, you can find out more about what each filter represents.

#### Change

These filters each indicate how objects will be handled when deployed on the destination Jira Cloud site.

- addition - The object will be added as a new one to the destination Jira site.
- modification - There is a matching destination object that will be updated with changes from the source.
- no modification - An identical object exists at the destination, so no changes will be made.
- unknown - The object is missing essential information, such as required fields or references, preventing proper deployment.
- deletion - The object will be removed from the destination Jira site as part of the deployment.

#### Problem

- warning - Non-critical issues that do not block deployment but may impact functionality; addressing them is recommended.
- error - Critical issues that must be resolved before proceeding with the deployment; addressing them is required.

#### Transformation

- draft - The object contains draft changes that have yet to be finalized. Drafts are saved as long as you remain in the deployment wizard. You can click the **Apply changes** button to finalize them for this deployment.
- transformed - The object has undergone transformations, such as remapping, renaming, or modifying attributes.

## Detailed analysis info screen

The detailed analysis info screen provides an in-depth look at each configuration element included in the deployment. It is divided into two main sections: the **Left Panel**, which lists and organizes configuration elements, and the **Right Panel**, which provides specific details and options for modifications.

### Filters

Before explaining the main two panels, let’s first cover the filter system and search bar. They can be found at the top of the detailed analysis info screen and are there to help you efficiently locate and review specific configuration elements. The filters themselves match the Analyze screen filter cards, so you’ll see them grouped into four buttons - **Type**, **Change**, **Problem**, and **Transformation**.

![FiltersEventsExample.png](/cms_trial/assets/baa36773-ebd3-4cf2-8d4a-efbf81a41b49.png)

The [Filter cards and icons](#Filter-cards-and-icons) section provides information about each filter group and what it consists of.

The search bar allows users to quickly find configuration elements by name or ID, making it easier to locate and inspect specific objects within the deployment snapshot.

### Left Panel

The left panel presents all configuration elements categorized by type. Expanding a section reveals the names of objects within that category. Each object could be accompanied by an icon indicating its current status, ensuring users can quickly identify additions, modifications, deletions, and other key changes.

Some objects can have other object types nested within them. For example, the **custom field** object type contains **custom field contexts** as a sub-type. If an object has a nested sub-type, the change icons next to it may indicate changes to either the main object, its sub-type, or both.

### Right Panel

The right panel offers a deeper analysis of a selected object. It contains three primary tabs, each serving a specific purpose:

**Overview Tab**: This read-only section displays current details about the selected object. This is also where you can find any warnings or errors related to the selected object. No modifications can be made within this tab — it serves purely for reference.

![image (4).png](/cms_trial/assets/aa2552d9-3d5f-4a12-94f7-c03f88b931b0.png)

**Edit Tab**: This section allows you to remap the selected object or modify its primary attributes. Changing a primary attribute can cause the object to be treated as new or match with an already existing object on the destination Jira site. After making any modifications, you must click the **Analyze changes** button to save the updates and ensure they’re reflected in the deployment analysis.

Refer to the [Inline transformations](/cms_trial/space/CMJC/759529597/Inline+transformations/) page to learn more about remapping and inline modifying.

![image (6).png](/cms_trial/assets/b100d2ca-45db-489d-81ea-74c065b9d173.png)

**Changes Tab**: This tab outlines all modifications that will be applied to the destination Jira site. This section simply displays the current state of all planned deployment changes for the selected object.

![image (5).png](/cms_trial/assets/7b590eda-52b9-4f05-ba27-0af72be1cb96.png)

You can exit out of the detailed analysis info screen by clicking the **X** button in the top-right corner.