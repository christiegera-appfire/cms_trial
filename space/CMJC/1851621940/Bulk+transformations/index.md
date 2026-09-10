# Bulk transformations

## Get started with bulk transformations

Bulk transformations in Configuration Manager for Jira (CMJ) Cloud allow you to efficiently modify multiple configuration elements within a deployment by applying changes from a JSON file. You can rename, remap, or adjust configuration objects before deploying them to a destination Jira Cloud site. This allows you to change how projects and configuration elements are deployed without leaving the deployment wizard.

The bulk transformations' feature set includes:

- **Downloading configuration mapping** involves downloading a file holding JSON records for all configuration elements in the deployment scope, their details, and how they’ll be deployed. The file specifies whether configuration elements, including projects and users, will be newly created or mapped to existing destination elements. [Learn more about downloading the configuration mapping](/cms_trial/space/CMJC/759824434/Download+and+customize+the+configuration+mapping/).
- **Customizing configuration mapping**involves applying transformations from a JSON file to the deployed configurations. These transformations can include renaming and remapping configuration elements or changing project keys. You can also apply transformations to multiple configuration elements simultaneously.[Learn more about configuration mapping](/cms_trial/space/CMJC/759824434/Download+and+customize+the+configuration+mapping/).
- **User transformations** involve applying transformations from a JSON file to the users being deployed. This allows you to merge users, correct emails and names, and choose different mappings between source and destination users. [Learn more about user transformations](/cms_trial/space/CMJC/760315914/User+transformations/).
- **Context transformations** involve applying transformations from a JSON file to the custom field contexts being deployed. This capability allows you to correct custom field problems and optimize their contexts on the destination. [Learn more about context transformations](/cms_trial/space/CMJC/759496822/Context+transformations/).
- **Status mapping** involves defining how source statuses that will be deleted should be mapped to valid destination statuses. [Learn more about status mapping](/cms_trial/space/CMJC/1129480719/Status+mapping/).

We’ve developed a group of documents to allow you to easily learn these features and utilize them in your daily deployment routines:

[Unmapped macro: aura-cards — no content to fall back on]