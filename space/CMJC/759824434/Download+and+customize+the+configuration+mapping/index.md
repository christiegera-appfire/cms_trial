# Download and customize the configuration mapping

## Change how projects, configuration elements, and users get deployed

What makes Configuration Manager for Jira (CMJ) Cloud a powerful admin tool is its ability to control how configurations are deployed from one Jira Cloud site to another. You have full control over how your projects, configuration elements, and users are migrated to the destination Jira Cloud site.

This is possible with the **Bulk transformations** option, a code-centered alternative to the [inline transformations](/cms_trial/space/CMJC/759529597/Inline+transformations/) available in CMJ Cloud’s UI. With it you can modify just about any configuration element and even change the destination element it is mapped to.

We're also giving you the option to download the current configuration mapping built by the analysis process with the **Download map** button within the **Bulk transformations** option. Keep in mind that the current mapping is always the latest mapping, and it will include any previous transformations you applied to the configuration.

![BulkTransformationsButton.png](/cms_trial/assets/51213824-4d95-4c8e-b7ad-5380adec8df5.png)

**What is mapping or configuration mapping?**

*Mapping* or *configuration mapping* is an extensive map built by CMJ Cloud’s analysis process. It holds information on how the configuration elements in the deployment scope will be moved to the destination Jira Cloud site.

After reading this map, CMJ Cloud decides if it needs to:

- create new elements,
- merge matching source and destination elements, and
- map destination elements to source elements without the need for updates to the destination.

## Download and customize the default configuration mapping

Once you add projects to your deployment and reach the analysis phase, you'll have access to the **Bulk transformations** button. You'll spot it at the top right of the *Analyze phase* page in the deployment wizard.

With the **Download map** button, you'll get a JSON file listing the details of the deployed configuration elements and how they'll be deployed. Review the following example file ▢ for a better idea of what to expect. The file contains all elements in the deployment scope, no matter their type - projects, users, custom fields, workflows, schemes, etc.

You can take this file and make changes to it or construct your own mapping file and apply it to the configuration. For this purpose, you need to upload a mapping file with transformations to the **Bulk transformations** option. [Check out the guidelines for customizing the configuration mapping](/cms_trial/space/CMJC/759988316/Guidelines+to+customize+the+configuration+mapping/).

## Step-by-step guide for downloading and customizing configuration mapping

**To customize the default configuration mapping:**

1. Start a [deployment](https://appfire.atlassian.net/wiki/spaces/CMJC/pages/193921424).
2. On the *Analyze*page, click the **Bulk transformations**button on the top right.
3. A new window will pop up where you can click the **Download map** button.  
   ℹ️ You will get a JSON file with the default mapping for all projects, configuration elements, and users in the deployment scope.

   ![DownloadMapButton.png](/cms_trial/assets/a2e1d823-7704-4f55-b05f-8ce89a3d190c.png)
4. Modify the JSON file to correct problems or change the deployment option of an element. [Check the guidelines about customizing the configuration mapping](/cms_trial/space/CMJC/759988316/Guidelines+to+customize+the+configuration+mapping/).
5. Click **Bulk transformations** againto get the option to upload the JSON file with the changes.
6. Either drag and drop the modified JSON file or use the **Click here to browse** button to upload it manually.
7. Review the number of changed elements in the dialog. If there are no elements with problems reported, click **Confirm** to apply the transformations from the file.  
   The video below shows how to upload and apply custom configuration mapping.

   ![UploadingJSON.mp4](/cms_trial/assets/a3d1291a-d201-4e28-bc11-124425064c6f.mp4)
8. Once you're done with the transformations, click **Deploy** to move on with the deployment.

After you click **Confirm** on the *Bulk transformations* window, CMJ Cloud performs a new analysis of the deployed configuration and applies the transformations from the file.