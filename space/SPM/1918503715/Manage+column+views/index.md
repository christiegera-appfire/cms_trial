# Manage column views

On this page, you can learn how to:

- Configure default column views (box type configuration).
- Set inheritance mode to determine available default column views (box type configuration).
- Configure column views for a particular box (box configuration).

## Security and access

Keep in mind:

- A box type contains the default settings applicable to multiple boxes (all boxes of a given type). Those settings are adjusted in the BigPicture Administration.
- Box configuration refers to the settings of a single, individual box. They are dependent on the box type settings.

The table presents what you can configure at the box type and box levels.

| **Area** | **Security and access** | **What can be configured** |
| --- | --- | --- |
| Box type configuration | Only a user with the App admin security role can access and manage the box type configuration.  Go to the **App Administration** > **Box type** > **choose the box type you want to edit** > **Gantt / Scope** > **Column views**. Screenshot of the Column views page in the box type configuration. | For a box type (all boxes of a given type), you can configure:   - Inheritance mode - Default column views |
| Box configuration | Only a user with a minimum box admin security role can access and manage the box configuration.  Go to **box configuration** > **Gantt / Scope** > **Column views**. box-config-gantt-column-views.png Alternatively, you can access the box configuration page directly from the Gantt / Scope module. Navigate to the **Current view** and select the **Manage Column views** from the drop-down menu. Gantt module. | For a particular box, you can configure:   - Column views |

## Inheritance mode

Selecting an inheritance mode determines if an upper-level box imposes the configuration. As a result, when the inheritance mode is set to **inherited** or **own with inherited**, the column views from upper-level boxes appear in the column views drop-down of the Gantt and Scope modules.

See more about inheritance mode on the [Inheritance mode](/cms_trial/space/SPM/1918700886/Inheritance+mode/) page.

## Column view creator

To learn more about managing column views, see the [Column view creator](/cms_trial/space/SPM/1918668503/Column+view+creator/) page.

## Default column views

Changing the default column views doesn't impact existing boxes of a given type - only boxes created after changed settings are affected.

![image-20240725-092138.png](/cms_trial/assets/f9e3b7c4-e8cc-45ed-ba08-c253b88ba496.png)

### Portfolio boxes (none scope boxes)

The table presents the default columns views for portfolio boxes.

| **Module name** | **Default column views for portfolio boxes** |
| --- | --- |
| Gantt module | - Essentials Portfolio - Agile Portfolio - Classic Portfolio  Screenshot of default column views in the box type configuration. |
| Scope module | - Essentials Portfolio - Agile Portfolio - Classic Portfolio - Baseline Portfolio - Time tracking Portfolio  image-20240725-092715.png |