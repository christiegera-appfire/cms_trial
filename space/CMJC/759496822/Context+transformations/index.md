# Context transformations

## What are custom field contexts?

When you create a custom field, Jira automatically generates *context*within the field. Contexts are configuration elements that only live within the custom field’s configuration. Learn more about contexts in Atlassians’ [*Configure custom field context*](https://support.atlassian.com/jira-cloud-administration/docs/configure-custom-field-context/)document.

Contexts allow you to set combinations of projects and issue types where a custom field will be available. Moreover, you can specify default values and options for these combinations. With that, you can have different *default values* and *options* when using the custom field in *different projects* and*issue types*. You can achieve that by creating multiple custom field contexts to set your preferences.

It’s important to note that there are two types of contexts:

- *Global contexts* - a custom field with such context appears in all projects on the Jira Cloud site.
- *Project-specific* *contexts* - the custom field is available only in the projects configured in the context.

## Apply transformations to change how contexts are deployed

Managing contexts mid-deployment is vital to successfully deploying custom fields between Jira Cloud sites. For a seamlessly working destination site, it’s important to be able to fine-tune how the source custom fields’ contexts will be deployed.

CMJ Cloud looks for matches between source and destination contexts during deployment and creates the source context as new on the destination site if no match is found. However, if there is a match, the source and destination contexts will be linked (mapped). We call this event *default mapping*. As a result, the source context, its values, and options will be merged into the destination context it’s mapped to. [Learn more about the rules defining how this happens](#Rules-for-context-transformations).

The default mapping also indicates whether the source context will be created as new on the destination. We know that the default mapping of your contexts offered by CMJ Cloud might only meet some of your configuration needs. We’ve created the **Bulk transformations** feature to give you the flexibility to achieve your deployment goals. It gives you control over how projects, configuration elements, and users, including contexts, will be deployed to a destination Jira Cloud site. [Learn more about the Customize mapping feature.](/cms_trial/space/CMJC/759824434/Download+and+customize+the+configuration+mapping/)

This feature allows you to list and apply transformations to contexts with the help of a JSON file. The transformations you can apply are:

- Creating a source context as a new destination context.
- Mapping a source context to a destination context of your choice.
- Remapping an already mapped context to a different destination context.

[Learn more about the different context transformation use cases](#Use-cases-for-context-transformations).

## Step-by-step guide to transforming custom field contexts

**To transform a custom field context during deployment:**

1. Create a [deployment](https://appfire.atlassian.net/wiki/spaces/CMJC/pages/193921424).
2. On the *Analyze*screen, click the **Bulk transformations**button on the top right.
3. A new window will pop up where you can click the **Download map** button.  
   ℹ️ You will get a JSON file with the default mapping for all projects, configuration elements (including contexts), and users in the deployment scope.

   ![DownloadMapButton.png](/cms_trial/assets/72e6c113-0dab-4c1b-b4ff-69ea5bbb2548.png)
4. Modify the JSON file to contain transformations of contexts. Check the guidelines about customizing contexts in the next section. Also, check the general syntax and rules for [customizing mapping](/cms_trial/space/CMJC/759988316/Guidelines+to+customize+the+configuration+mapping/).
5. Click **Bulk transformations** againto get the option to upload the JSON file with the changes.
6. Either drag and drop the modified JSON file or use the **Click here to browse** button to upload it manually.
7. Review the number of changed elements in the dialog. If there aren’t any problems with the elements, click **Confirm** to apply the transformations from the file.

   ![video showing how to upload JSON file.](/cms_trial/assets/0956eda3-1049-44d8-8dbe-dbf1d285bbbb.mp4)

After **confirmation**, the CMJ Cloud reanalyzes the configuration and applies the transformations from the file.

## Guidelines for creating JSON context transformations

As described in the [Step-by-step guide](#Step-by-step-guide-to-transforming-custom-field-contexts) above, you can download a file that contains all custom field context details for a deployment. Customize this file or create your own, and make sure it's in **JSON format**. [Refer to our guide for transformation listing requirements](/cms_trial/space/CMJC/759988316/Guidelines+to+customize+the+configuration+mapping/).

Using transformations, you can map a source context to a selected destination one or create a mapped source context as a new one on the destination. [Read more about the context transformations you can perform.](#Apply-transformations-to-change-how-contexts-are-deployed) This way, you can change existing context mappings, set a mapping for new contexts, or transform a mapped context to a new destination context. You can find information about the logic of what happens with the source and destination context configurations in the [Use cases for context transformations](#Use-cases-for-context-transformations)section.

**Provide source context’s ID in the JSON file**

Source and destination contexts are matched by their IDs. Make sure you include the source context's ID in the JSON file to create or update a mapping.

The specific thing for contexts is that the transformation is always **defined within a custom field record** in the JSON file.

### Required JSON records to transform contexts

With the **Bulk transformations** option in the deployment wizard, you can apply two types of transformations to contexts:

- Mapping a source context to a selected destination context
- Creating a new destination context

**Map contexts by ID**

With this transformation, you can map a source context to an existing destination context. This includes remapping an already mapped source context or mapping new contexts to destination contexts. Simply provide the ID of an existing destination context in the following format:

```json
"transformation": {
    "id": "100123"
}
```

**Create a new context**

With this transformation, you can transform the mapped source contexts into a new destination context. You need to add the following record for a given context to the JSON file to achieve the transformation:

```json
"transformation": {
    "newObject": true
}
```

After that transformation, any existing mapping will be disregarded.

**Rename a context**

With this transformation, you can change the name of a destination context. You need to add the following record for a given context to the JSON file to achieve the transformation:

```json
"transformation": {
    "name": "new context name"
}
```

After that transformation, any existing mapping will be ignored.

### Edit a context in a downloaded JSON file

You can apply the transformations above by [downloading the current mapping](/cms_trial/space/CMJC/759824434/Download+and+customize+the+configuration+mapping/) file and editing it. This is the case when you only add a `transformation` record without changing the default `source` and `destination` context records in the downloaded file. For more details about editing or constructing a mapping file, check this [guide](/cms_trial/space/CMJC/759988316/Guidelines+to+customize+the+configuration+mapping/). To apply transformations to map or create new contexts using a downloaded JSON file, you need to insert a `transformation` record by following the syntax below:

*Mapping a source context to a chosen destination context by ID*

```json
{
    "source": {
        "id": "customfield_10000",
        "name": "Custom Field",
        "type": "com.demo.text"
    },
    "children": [
        {
            "contexts": [
                {
                    "source": {
                        "id": "10000",
                        "name": "Name",
                        "projectKeys": [
                            "Demo",
                            "Doc"
                        ],
                        "global": true
                    },
                    "destination": {
                        "id": "10100"
                    },
                    "transformation": {
                        "id": "10102"
                    }
                }
            ]
        }
    ]
}
```

*Creating a source context as new in the destination*

```json
{
    "source": {
        "id": "customfield_10000",
        "name": "Custom Field",
        "type": "com.demo.text"
    },
    "children": [
        {
            "contexts": [
                {
                    "source": {
                        "id": "10000",
                        "name": "Name",
                        "projectKeys": [
                            "Demo",
                            "Doc"
                        ],
                        "global": true
                    },
                    "destination": {
                        "id": "10100"
                    },
                    "transformation": {
                        "newObject": true
                    }
                }
            ]
        }
    ]
}
```

### Construct a JSON file with context transformations

You can also apply context transformations by constructing your own JSON file. In this case, you again need to have a `transformation` record, but you don’t need a destination record. The source record for the custom field and its content can contain only the IDs of these elements. That’s the minimum source configuration required for a transformation. For more details about editing or constructing a mapping file, check this [guide](/cms_trial/space/CMJC/759988316/Guidelines+to+customize+the+configuration+mapping/).

To build a JSON file with a context transformation, you need to have a minimum set of data in the file. You still need a `transformation` record, but many of the records in a downloaded JSON file are not mandatory. The examples below list the minimum JSON records needed when mapping or creating new contexts in the destination.

*Mapping a source context to a chosen destination context by ID*

```json
{
    "source": {
        "id": "customfield_10000"
    },
    "children": [
        {
            "contexts": [
                {
                    "source": {
                        "id": "10000"
                    },
                    "transformation": {
                        "id": "10102"
                    }
                }
            ]
        }
    ]
}
```

*Creating a source context as a new destination context*

```json
{
    "source": {
        "id": "customfield_10000"
    },
    "children": [
        {
            "contexts": [
                {
                    "source": {
                        "id": "10000"
                    },
                    "transformation": {
                        "newObject": true
                    }
                }
            ]
        }
    ]
}
```

## Rules for context transformations

CMJ Cloud applies the following rules for context transformations:

1. A *source context* can be mapped to only *one destination context* or created as a *new context* within a given custom field.
2. If a *source context* is mapped to a *chosen destination context*:

   1. The destination context’s options that don’t match any source context options will be deleted.
   2. The source and destination contexts’ options that match (by name/label) won’t be modified.
   3. The source context’s options that don’t match any of the destination context’s options will be added as new to that context.
3. The source context’s projects will be assigned to the destination context. The added projects will, at the same time, be unassigned from any other contexts of the custom field.  
    contexts without projects As a result of this logic, some contexts in the destination might lose all of their projects. CMJ Cloud, in this case, will remove such destination contexts. However, the context won’t be deleted if there are issues with option values. Instead, the deployment stops and an error appears after the configuration analysis finishes. In this case, you’ll be advised to visit [this document](/cms_trial/space/CMJC/193692433/Manage+custom+fields+contexts/) for instructions on how to resolve the problem to be able to continue the deployment.
4. A project can be present in only one of the contexts of a custom field.

## Use cases for context transformations

### **Project-specific context → Project-specific context**

If you map a *source project-specific* context to a *destination project-specific* context of your choice:

- The merge result will have the destination context’s name.
- The projects from the source and destination context will be set in the merge result.
- The source context’s projects will be removed from other destination contexts for the same custom field.  
  Contexts without projects A destination context might end up without any projects set during the deployment. As a result, CMJ Cloud will try to delete it. However, the context won’t be deleted if there are issues with option values. Instead, an error stopping the deployment will appear after the configuration analysis finishes. In this case, you’ll be advised to visit [this document](/cms_trial/space/CMJC/193692433/Manage+custom+fields+contexts/) for instructions on how to resolve the problem to be able to continue the deployment.

### **Project-specific context → Global context**

If you map a *source project-specific* context to a *destination global*context:

- The merge result will have the destination context’s name.
- The merge result will still be a *global context*.
- The source context’s projects will be removed from other destination contexts of the same custom field.

### **Global context → Project-specific context**

If you map a *source global*context to a *destination project-specific* context:

- The merge result will have the destination context’s name.
- The merged result will be a project-specific context (*not global*).
- The global context will first be converted to a project-specific source context. All projects in the **deployment scope**will be set in this transformed context.
- After the merge, the projects in the transformed source and destination context will be set in the merge result.
- The source context’s projects will also be removed from other destination contexts for the given custom field.
- As a result of such mapping, some destination contexts might end up without any projects. This situation will be reported on the **Analyze** page.

### **Global context → Global context**

If you map a source *global* context to a destination *global*context:

- The merge result will have the destination context’s name.
- The merge result will still be a *global context*.

### **Project-specific context → Create a new context**

With *Bulk transformations*, you can convert any mapped source project-specific context to a new destination context. Just keep in mind that the context’s projects will be removed from the other destination contexts of the same custom field.

By default, if no match is detected in the destination and there is no mapping, the source context gets created as a new one in the destination.

Global contexts CMJ Cloud doesn’t allow transforming a source global context to a new one in the destination. If you upload a JSON file with such a transformation, an error will appear, stopping you from applying the transformation.