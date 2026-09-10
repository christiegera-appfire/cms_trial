# Status mapping

## What is a status mapping?

In Jira, you can’t delete a status from an active workflow before you remap it to another valid status. To accommodate this, **Configuration Manager for Jira (CMJ) Cloud** provides a mapping process that allows you to select an alternative status during deployment. CMJ Cloud then applies the status mapping while updating the active workflow.

## When is status mapping required

CMJ Cloud halts the deployment during the *Analyze* phase if it identifies a status scheduled for deletion from an active workflow. In such instances, you will encounter the following error:

**Status needs to be remapped**

*The [statusname] status won’t be deployed in the current deployment configuration. It needs to be remapped to an active status to maintain workflow stability.*

It requires you to map the status scheduled for deletion to another status. You can choose a status already in the destination or one that the deployment will create. For instructions on how to map statuses using a JSON file, please refer to [this section](#Guidelines-for-mapping-statuses-with-a-JSON-file).

## How to remap statuses with Inline transformations

The easiest way can do status remaps is directly within the **Detailed Analysis Info Screen** by using inline transformations. This method allows users to manually adjust mappings without downloading or modifying a JSON file.

**Steps to remap a status with Inline transformations:**

1. Open the **Issue Migrations** card by selecting it on the *Analyze* page.
2. This opens up the **Status Mapping** section.

![NEWStatusMapping.png](/cms_trial/assets/ef77e258-7134-408e-ad1f-d327fe13b77e.png)

1. Click the dropdown under **New Status** and select a new status to replace the one that’s going to be deleted.
2. The change will be marked as a **Draft**, indicating that the modification has been made but not yet finalized.
3. Click **Analyze Changes** to confirm and save the transformation.
4. Review the **Changes Tab** to verify the updated mapping before proceeding with deployment.

## How to remap statuses with Bulk transformations

Bulk transformations provide a structured approach to map statuses using a JSON file. This method is useful for larger-scale deployments where multiple statuses need to be reassigned efficiently.

**Steps to remap a status with Bulk transformations:**

1. Create a deployment.
2. During the Analyze Changes phase, click the **Bulk Transformations** button.

   - This will allow you to download a JSON file containing the default mapping for all projects, configuration elements, and users in the deployment scope. The file will also include entries for statuses scheduled for deletion and a list of alternative statuses for mapping.

![DownloadMapButton.png](/cms_trial/assets/76f86735-2fce-4241-abb9-a0d269ef881b.png)

1. Modify the JSON file.

   - Enter alternative statuses for those scheduled for deletion. Follow the syntax guidelines outlined in the section [Guidelines for Mapping Statuses with a JSON File](/cms_trial/space/CMJC/759988316/Guidelines+to+customize+the+configuration+mapping/).
2. Upload the updated JSON file via the **Bulk Transformations** button.

![UploadMapButton.png](/cms_trial/assets/dc4bc2f8-7aae-422c-b863-478cefb6717b.png)

1. Confirm the mapping.

   - If no problems are detected, click **Confirm** to apply the status mapping. CMJ Cloud will reanalyze the configuration and finalize the mapping.
2. Resolve any errors.

   - If issues are reported, correct the JSON file and re-upload it. The deployment will not be able to proceed until all problems are resolved.
3. Click **Deploy** to finalize the deployment.

   - CMJ Cloud will apply the status mapping and update affected issues accordingly.

## Guidelines for mapping statuses with a JSON file

As mentioned above, you can download a JSON mapping file that describes how the source configuration elements will be transferred to the destination. If the deployment process involves deleting a status from an active workflow, the file will include a section for status mapping. In this section, you need to specify an alternative status from the list of mappable statuses to replace the one being deleted. After deployment, any issues associated with the deleted status will be reassigned to the new status.

To configure the status mapping, modify the downloaded mapping file or create your own. Make sure any file you generate is in JSON format. Refer to the [Guidelines to customize the configuration mapping](/cms_trial/space/CMJC/759988316/Guidelines+to+customize+the+configuration+mapping/) document for additional instructions on using a JSON file.

### Map statuses in a downloaded JSON file

You can manage the mapping between statuses by downloading the current mapping file, modifying it, and then uploading it back. When the deployment includes deleting a status, the mapping file you download will include entries similar to the example below:

*Status mapping records in a downloaded JSON file*

```json
"statusMapping" : {
    "mappableStatuses" : [ "Build Broken", "To Do", "Done", "Review" ],
    "statusMigrations" : [ {
      "oldStatus" : "Completed"
    } ]
  }
```

The `mappableStatuses` property enumerates all the statuses you can choose as alternatives to the status planned for deletion. You must select a status from this list to map any status scheduled to be deleted.

*Records to map a status being deleted to another one*

```json
"statusMapping" : {
    "mappableStatuses" : [ "Build Broken", "To Do", "Done", "Review" ],
    "statusMigrations" : [ {
      "oldStatus" : "Completed",
      "newStatus" : "Done"
    } ]
  }
```

### Construct a JSON file with status mapping.

You can construct your own JSON file with status mapping entries and apply it to the deployed configuration. The example below shows the records needed in the file to map one status to an alternative one.

```json
"statusMapping" : {
    "statusMigrations" : [ {
      "oldStatus" : "In Progress",
      "newStatus" : "Developing"
    } ]
  }
```

### Set a mapping for more than one status

You might need to set mappings for multiple statuses scheduled for deletion. The example below shows how to structure your JSON entries to accommodate mappings for several statuses.

```json
{
    "statusMapping": {
        "statusMigrations":
                "oldStatus": "TODO",
                "newStatus": "<NEW STATUS NAME>"
            },
            {
                "oldStatus": "PENDING",
                "newStatus": "<NEW STATUS NAME>"
            },
            {
                "oldStatus": "COMPLETED",
                "newStatus": "<NEW STATUS NAME>"
            }
        ]
    }
}
```

### How CMJ Cloud determines the mappable statuses

Cloud Migration Tool determines the mappable statuses by analyzing all source workflows included in the deployment and their statuses. It selects only the statuses common to all these workflows. This approach ensures that any status chosen for mapping is valid across all workflows in the deployment scope.

For example, consider two workflows in a deployment, WF1, and WF2, which require status mapping. Their statuses are *Status1*, *Status2* for WF1 and *Status2*, *Status3* for WF2. In this case, the `mappableStatuses` in the JSON file will only include *Status2*, the common status between the workflows.

### No mappable statuses

You may encounter a scenario with no common statuses between the workflows in the deployment.

When a universal status mapping applicable to all workflows isn't feasible, we suggest the following strategies:

- **Split the projects into smaller deployments:** This is particularly useful if workflows from different projects have no common statuses.
- **Apply transformations:** Specifically, consider renaming a workflow to add it as a new workflow to the destination. Post-deployment, you will have to assign the renamed workflow to the same scheme the original was assigned to. Then, the workflow must become active.
- **Optimize workflows in the source Jira:** Before the deployment, modify your projects and workflows in the source Jira for a smoother process.