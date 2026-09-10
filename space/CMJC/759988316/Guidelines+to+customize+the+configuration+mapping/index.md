# Guidelines to customize the configuration mapping

## Basics of customizing the configuration mapping

To customize the mapping of a project, configuration element, or user, you need to have a JSON file with a `transformation` record for it. The transformations are customizations you can apply to an element from the configuration being deployed.

The available JSON transformations to source configurations being deployed are:

- Mapping a configuration element to a chosen destination element.
- Renaming any configuration element such as project, workflow, custom field, or user.
- Changing a project key.
- Changing a user email.

**Contexts** can be transformed as well from a JSON file. To learn all the context transformation rules, guidelines and use cases, refer to the [Context transformations](/cms_trial/space/CMJC/759496822/Context+transformations/) page.

In the JSON file, you always need to provide the source ID of the configuration element you want to transform. Later, we’ll show you end-to-end what you need to do in order to apply a JSON transformation.

Now, let’s take a closer look at each transformation type and its JSON record.

## Transformations you can apply with custom mapping

When the deployment analysis process detects a match between a source and a destination Jira Cloud configuration element, it creates a mapping between them.

### Projects and configuration elements: Map the configuration element to a chosen destination element

With the **Bulk transformations** option, you can change the destination element the source element is mapped to. Provide a different ID in the following way, and the deployment analysis will create a new mapping:

**Map by ID**

Provide the ID of an existing destination configuration element of the same type.

```json
"transformation": {
    "id": "100123"
}
```

### Projects and configuration elements: Rename

With this transformation, you can:

- Create source elements as new ones on the destination instead of mapping to existing elements.
- Deploy new elements with a different name to the destination.
- Map a source element to a destination element with the new name.

For this purpose, you need to provide a new destination name like this:

```json
"transformation": {
    "name": "New configuration element name"
}
```

After the renaming, any existing mapping will be disregarded afterward.

**Use configuration elements' ID to ensure accurate mapping**

Mapping by name works correctly when a configuration element's uniqueness is determined by its name. But when elements, like filters, have the same name, renaming them won't guarantee a correct match with a destination element of the same name.

In these cases, where the name isn’t a unique attribute of the configuration element, use the unique IDs to map source and destination elements.

### Projects: Change project key

You can add a transformation record to a project to change its key. Remember that you can change the project key using the inline edit [transformation](/cms_trial/space/CMJC/759529597/Inline+transformations/) in the UI.

```json
"transformation": {
     "key": "PROJDOC"
}
```

### Users: Change user email

For users, you can add a transformation record to change the user’s email address or to match it to another destination user by providing an ID. These transformations let you create, merge, and remap users. The source and destination users are matched either by their names or by their IDs.

[Learn more about transforming users](/cms_trial/space/CMJC/760315914/User+transformations/).

```json
"transformation": {
    "name": "Karlie Davis",
    "email": "karlie@demo.com"
}
```

### Users: Map to a destination user by ID

You can also add a transformation record to map a source user to a chosen destination user by providing the destination user’s ID.

[Learn more about transforming users](/cms_trial/space/CMJC/760315914/User+transformations/).

```json
"transformation": {
    "id": "5da444878f33800c416f30ed",
}
```

## Ways of customizing the configuration mapping

To make transformations to projects, configuration elements, and users, you can:

- Download a JSON [mapping file](/cms_trial/space/CMJC/759824434/Download+and+customize+the+configuration+mapping/), add transformations to it, and upload it back to the deployment wizard.
- Construct a JSON file containing the transformations you want to apply and upload it back to the deployment wizard.
- Reuse a mapping file from a previous deployment and upload it back to the deployment wizard.

### Download mapping and customize it

With the **Download map** button, you’ll get a JSON file listing the configuration elements in the deployment scope. This mapping file contains a description of how all these configuration elements will be deployed to Jira Cloud. The following JSON snippet illustrates how configuration elements are listed in the file:

```json
{
    "issueTypeSchemes": [
        {
            "source": {
                "id": "10208",
                "name": "DOM: Scrum Issue Type Scheme",
                "default": false
            },
            "destination": {
                "newObject": true
            }
        }
    ]
}
```

As you can see, each configuration element has a `source` and `destination` record. The `source` record contains all the details of the source element, and the `destination` record holds information about how this element will be deployed. The configuration element can either be created as a new one or mapped to an existing destination element.

To customize the default mapping of a configuration element, add a `transformation` record for it like this:

```json
{
    "issueTypeSchemes": [
        {
            "source": {
                "id": "10208",
                "name": "DOM: Scrum Issue Type Scheme",
                "default": false
            },
            "destination": {
                "newObject": true
            },
            "transformation": {
                "id": "10206"
            }
        }
    ]
}
```

Then, in the `transformation` record, you can map the element to a destination element or create it as a new element.

### Construct your own mapping file

You can create your own mapping file without downloading such from the UI. Just follow the guidelines in this section. After creating it, you upload it through the **Bulk transformations** option in the UI, the same way you would do with a downloaded mapping file. The following snippets show how to construct the JSON records of a transformation to a single configuration element:

```json
{
    "issueTypeSchemes": [
        {
            "source": {
                "id": "10208"
            },
            "transformation": {
                "id": "100119"
            }
        }
    ]
}
```

or

```json
{
    "issueTypeSchemes": [
        {
            "source": {
                "id": "10208"
            },
            "transformation": {
                "name": "Destination issue type scheme"
            }
        }
    ]
}
```

The `source` record must contain the ID of the source configuration element. Similarly to the example above, you can add more details to the `source` record. However, for a successful transformation, the only required component for the `source` record is the source element’s ID. Then, you need to have a `transformation` with the new ID or name, as shown in the example above. You can also change projects' keys this way and users' email addresses and keys.

#### Users

In the source `record`, we always refer to source users by their IDs. So, when building your mapping file with a user transformation, you need to provide the source user’s ID like so:

```json
{
    "users": [
        {
            "source": {
                "id": "5ed730807d0c0f0ab20920b8"
            },
            "transformation": {
                "email": "karlie@test.com"
            }
        }
    ]
}
```

This transformation will change the user’s email address. You can also build a transformation that will map a source user to a destination user by ID. You just need to provide the destination user’s ID in the `transformation` record :

```json
{
    "users": [
        {
            "source": {
                "id": "5ed730807d0c0f0ab20920b8"
            },
            "transformation": {
                "ID": "5da444878f33800c416f30ed"
            }
        }
    ]
}
```

You can learn more about what you can do with users in the [User Transformations](/cms_trial/space/CMJC/760315914/User+transformations/) document.

### Reuse a mapping file from a previous deployment

The third option to customize the mapping through JSON is to reuse a mapping file created for a previous deployment. It will work only if it’s applicable to the currently deployed configuration.

For example, you may want to apply a custom mapping file from a larger deployment to a deployment with a subset of the previously deployed projects. This way, you can break a large deployment down into smaller, more manageable chunks of data.

**Key points:**

- The `source` JSON record must always contain the ID of the deployed source project, configuration element, or user. For users, the ID is their email address.
- If you add configuration elements that aren't part of the deployment to a downloaded or created mapping file, they will be skipped. This means that these elements won't be included in the deployment at all.
- Configuration elements are mapped to destination elements by ID. Exceptions are users, as their ID is the user’s email address. You can learn more about them in the [User Tranformations](/cms_trial/space/CMJC/760315914/User+transformations/) document.
- Remember that renaming a default scheme or workflow will create a new non-default scheme or workflow in the destination.
- Don’t use the name of a default scheme from the destination to create a new scheme. Instead, map the default schemes only by ID.

## Validations and conflict detection

During the mapping file upload, we perform JSON validation checks for:

- Non-JSON file formats
- Syntax errors like missing source records or IDs.

After validation and confirmation of the new mapping, a configuration analysis process kicks off. It performs scans and applies the transformations to the configuration. All elements in the deployment scope referring to the transformed elements are fixed accordingly.

We’ve also built a fail-safe mechanism into the analysis process to avoid data loss or deployment failures. It’s able to detect and report conflicts that can be introduced with customized mapping, such as:

- Multiple source configuration elements being mapped to the same destination element after transformations.
- A configuration element being mapped to a non-existent destination element.

All these errors appear on the *Analyze* page for the particular project or configuration element.