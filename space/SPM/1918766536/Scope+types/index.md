# Scope types

## Scope types (old navigation)

## About scope types

A scope type is set in **Administration** > **Box types** settings. A box type contains the default settings applicable to multiple boxes (all boxes of a given type). Boxes can be created with different types of scope. Those settings determine how a box can be configured and what can be done when defining a scope.

There are three different scope types:

- Own-scope
- Sub-scope
- None (aggregations only)

![image-20250313-121926.png](/cms_trial/assets/5548f97c-bd97-4f0e-bf74-4e80cd98be90.png)

## Security and access

Keep in mind:

- A box type contains the default settings applicable to multiple boxes (all boxes of a given type). Those settings are adjusted in the BigPicture Administration.
- Box configuration refers to the settings of a single, individual box. They are dependent on the box type settings. Go to the [Populate a box with tasks (work items from Jira)](/cms_trial/space/SPM/1918634319/Populate+a+box+with+tasks+(work+items+from+Jira)/) page to learn more about scope definition settings at the box level.

The table presents what you can configure at the box type level.

| **Area** | **Security and access** | **What can be configured** |
| --- | --- | --- |
| Box type configuration | Only a user with the App admin security role can access and manage the box type configuration.  Go to the **App Administration** > **Box type** > **choose the box type you want to edit** > **Tasks** > **Scope definition**. image-20250313-121926.png | For a box type (all boxes of a given type), you can configure:   - Scope type |

## Own-scope

The box scope has a separate task structure and is a scope base for sub-scopes. Automatic rules can sync it. Use it when you want to define and extend the scope of a box by selecting tasks from Jira and connected tools. See the [Own-scope](/cms_trial/space/SPM/1918765868/Own-scope/) page to learn more about box configuration.

## Sub-scope

The box scope is always a subset of the scope already defined at an upper level of the box hierarchy (the upper-level box must have own-scope). It can be automatically synced with a value of a selected field.

[Unmapped block: nestedExpand]

See the [Sub-scope](/cms_trial/space/SPM/1918799715/Sub-scope/) page to learn more about box configuration.

### Sub-scope definition template

When you select the sub-scope in the box type settings, a new section **Sub-scope definition template** appears, and you can choose the field to synchronize with it.

![Screenshot of the Scope definition page in BigPicture Administration for a sub-scope box.](/cms_trial/assets/b7074ade-ddda-45dc-b798-188dbf3909c7.png)

[Unmapped block: nestedExpand]

## None (aggregations only)

The box scope cannot be defined. Currently, you can only use such a box to calculate respective aggregates in the box hierarchy (visible in the Overview module). Use this setting to organize boxes into portfolios, programs, etc. The scope is always a sum of the scopes of the sub-boxes in the box hierarchy. For none-scope boxes, the **Scope definition** page in the box configuration is unavailable.

See the [None (aggregations only)](/cms_trial/space/SPM/1918537743/None+(aggregations+only)/) page to learn more about box configuration.

## Scope types (new navigation)

## About scope types

A scope type is set in **Administration** > **Box types** settings. A box type contains the default settings applicable to multiple boxes (all boxes of a given type). Boxes can be created with different types of scope. Those settings determine how a box can be configured and what can be done when defining a scope.

There are three different scope types:

- Own-scope
- Sub-scope
- None (aggregations only)

![work-items-scope-type.png](/cms_trial/assets/7af81751-43df-4cee-98dc-97b0e6267bf7.png)

## Security and access

Keep in mind:

- A box type contains the default settings applicable to multiple boxes (all boxes of a given type). Those settings are adjusted in the BigPicture Administration.
- Box configuration refers to the settings of a single, individual box. They are dependent on the box type settings. Go to the [Populate a box with tasks (work items from Jira)](/cms_trial/space/SPM/1918634319/Populate+a+box+with+tasks+(work+items+from+Jira)/) page to learn more about scope settings at the box level.

The table presents what you can configure at the box type level.

| **Area** | **Security and access** | **What can be configured** |
| --- | --- | --- |
| Box type configuration | Only a user with the App admin security role can access and manage the box type configuration.  Go to the **App Administration** > **Box type** > **choose the box type you want to edit** > **Tasks** > **Add work items from Jira**. work-items-scope-type.png | For a box type (all boxes of a given type), you can configure:   - Scope type |

## Own-scope

The box scope has a separate task structure and is a scope base for sub-scopes. Automatic rules can sync it. Use it when you want to define and extend the scope of a box by selecting tasks from Jira and connected tools. See the [Own-scope](/cms_trial/space/SPM/1918765868/Own-scope/) page to learn more about box configuration.

## Sub-scope

The box scope is always a subset of the scope already defined at an upper level of the box hierarchy (the upper-level box must have own-scope). It can be automatically synced with a value of a selected field.

[Unmapped block: nestedExpand]

See the [Sub-scope](/cms_trial/space/SPM/1918799715/Sub-scope/) page to learn more about box configuration.

### Sub-scope definition template

When you select the sub-scope in the box type settings, a new section **Sub-scope definition template** appears, and you can choose the field to synchronize with it.

![sub-scope-definition-template.png](/cms_trial/assets/92a73e98-cf2c-451a-9a38-0642118e4d7d.png)

[Unmapped block: nestedExpand]

## None (aggregations only)

The box scope cannot be defined. Currently, you can only use such a box to calculate respective aggregates in the box hierarchy (visible in the Overview module). Use this setting to organize boxes into portfolios, programs, etc. The scope is always a sum of the scopes of the sub-boxes in the box hierarchy. For none-scope boxes, the **Work items from Jira** page in the box configuration is unavailable.

See the [None (aggregations only)](/cms_trial/space/SPM/1918537743/None+(aggregations+only)/) page to learn more about box configuration.