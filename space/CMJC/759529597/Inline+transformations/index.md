# Inline transformations

## **Transform configuration elements inline during a deployment**

Configuration Manager for Jira (CMJ) Cloud allows you to modify how configuration elements from one Jira Cloud site will be deployed to another. These modifications, called transformations, can be applied in two ways - through **inline transformations** or **bulk transformations**.

Inline transformations are quick actions that allow users to edit configuration elements directly within the *detailed analysis info screen* during the **Analyze** phase of a deployment. This feature provides flexibility to modify or remap elements efficiently without exiting the deployment wizard.

### **Use cases**

Inline transformations can be used to:

- Resolve conflicts detected in configuration elements during deployment analysis.
- Fix problems with duplicate configuration elements added to the deployment scope.
- Rename and modify objects to ensure correct alignment with the destination Jira Cloud instance.
- Update user mappings to ensure accurate user associations.
- Optimize and organize configurations according to your organization's needs before deployment.

**Source Jira Cloud's configuration isn't modified in any way**

The projects and configuration elements **remain unchanged** in the source Jira Cloud site. You're only changing how the source configuration elements are deployed to the destination Jira Cloud.

### **Example use case**

Let’s say you have a workflow scheme with the same name on source and destination. If you don’t want to modify or interfere with the current configuration of that workflow scheme on destination, then you can rename it to inform CMJ Cloud that you want to deploy it as a new scheme. Once renamed, if there isn’t another workflow scheme with the same name on your destination Jira site, then it will be set to be deployed as new.

![image (8).png](/cms_trial/assets/582451c0-c7ce-451a-a7ed-1734f683c279.png)

Similarly, changing a project's key allows CMJ Cloud to upload it as a new project instead of merging it with an existing one in the destination Jira Cloud site.

## **How are inline transformations applied?**

After the configuration analysis is complete, you’ll be shown the *Analyze* screen, which lists all planned configuration changes along with detected conflicts or issues. By selecting any object type card, you’ll open up the **Detailed Analysis Info Screen**. Once there, you can make inline transformations through the **Edit Tab**.

The transformations applied are not final until confirmed with the **Apply Changes** button. Before confirmation, any inline modification is marked as a **Draft** change in the UI.

Once all necessary changes have been made and applied, the deployment process can continue.

**Draft changes**  
You'll lose all draft changes if you close the browser tab before applying them.

After making all the necessary changes and applying them, you can continue the deployment.

**New analysis runs when applying changes**

Once you confirm the draft changes, a new analysis will start automatically and run until the configuration is fully updated. The purpose of the new analysis is to detect conflicts between the updated and the destination configurations. This new analysis will be quicker than the original analysis you experienced at the start of the deployment.

## **When to use attribute changing vs. remapping?**

While both attribute changing and remapping allow users to modify configuration objects, they serve different purposes and should be used in different scenarios.

**Use attribute changing when:**

- You need to make adjustments to your object attributes, such as name or key, **without affecting your source counterparts.**
- You want to **modify secondary attributes,** such as the name of a custom field context.

**Use remapping when:**

- You want to **change the association** between a source object and its destination counterpart.

## **Perform inline transformations**

Inline transformations allow users to modify the key and secondary attributes of any configuration object directly within the **Detailed Analysis Info Screen**. While the specific attributes available for editing may vary depending on the object type, the inline editing process remains the same.

**Steps to perform an inline transformation:**

1. Open the **Detailed Analysis Info Screen** by selecting a configuration object type from the *Analyze* page.
2. Navigate to the **Edit Tab**, where the editable attributes of the selected object will be displayed.
3. Click the field you want to modify and enter the new value.
4. The object will be marked with a **Draft** label, indicating that modifications have been made but not yet finalized.
5. Click **Analyze Changes** to confirm and save the transformation.
6. Review the **Changes Tab** to see the updated deployment impact before proceeding.

**Matching destination objects**

If the object is matched to an object on the destination Jira site, then changing a primary attribute can result in:

- *Created as new* - this will happen if the new primary attributes don’t match the primary attributes of another object on destination.
- *Matched to a different object* - this will happen if the new primary attributes are changed in such a way that they now result in a match with a different object on destination.

If an object is created as new, changing primary attributes is still possible, and depending on the same criteria, it may have the same outcomes as above.

## **Re-map configuration objects**

In addition to inline modifications, users can also remap configuration objects to align source elements with their correct counterparts in the destination Jira Cloud site. This is useful for resolving conflicts and ensuring that objects are mapped correctly before deployment.

**Steps to re-map a configuration object:**

1. Open the **Detailed Analysis Info Screen** by selecting the configuration object from the **Analyze** page.
2. Navigate to the *Edit*tab and locate the remapping options in the purple panel at the top of the tab.
3. Select a valid destination object from the dropdown list or input the name or ID of the destination object manually.
4. The object will be marked with a **Draft** label, indicating that the remapping has been applied but not yet finalized.
5. Click **Analyze Changes** to confirm and save the remapping.
6. Review the *Changes*tab to verify that the updated mapping is correctly applied before proceeding with deployment.

## **Undo an inline transformation or remap**

If you need to undo an inline transformation or remap, the process depends on whether the changes have already been saved.

**Undoing before saving**

- *For inline transformations* - click the **Undo** button next to the modified attribute’s field.
- *For remaps* - exit the **Detailed Analysis Info Screen**, and the modifications will be discarded.

Draft changes are automatically removed if the deployment wizard is exited before applying them.

**Undoing after saving**

Once an inline transformation or remap has been confirmed by clicking **Analyze Changes**, it cannot be undone directly within the UI. The only way to revert these changes is by using the [Bulk transformations](/cms_trial/space/CMJC/1851621940/Bulk+transformations/) functionality.