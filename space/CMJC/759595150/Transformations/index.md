# Transformations

## What are transformations?

Transformations in Configuration Manager for Jira (CMJ) Cloud allow users to modify configuration elements before deploying them to a destination Jira Cloud site. This page will explain the two main types of transformations in CMJ Cloud: **Inline Transformations** and **Bulk Transformations**.

## **Inline Transformations**

Inline transformations enable users to make quick, manual adjustments within the UI. These modifications can be applied to individual configuration objects, allowing you to:

- Rename any configuration object.
- Remap specific objects to align with destination configurations.
- Adjust project keys to avoid conflicts.
- Modify user mappings for better consistency.

These changes are applied instantly and help you fine-tune your configurations before deploying.

## **Bulk Transformations**

Bulk transformations in CMJ Cloud allow you to efficiently modify multiple configuration elements within a deployment by applying changes from a JSON file. This method goes through the following steps:

1. Download a JSON file containing all deployment configurations.
2. Modify the JSON file to rename, remap, or adjust objects in bulk.
3. Upload the modified JSON file back into the system for validation and application.

Bulk transformations are ideal for handling complex migrations and applying any changes through code for more control.

By utilizing **Inline** and **Bulk Transformations**, you can ensure their Jira Cloud configuration is structured as intended before deployment, minimizing errors and improving system consistency.