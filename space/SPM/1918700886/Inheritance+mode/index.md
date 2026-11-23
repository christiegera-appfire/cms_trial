# Inheritance mode

## About the inheritance mode

The Inheritance mode allows some [Box configuration](/cms_trial/space/SPM/1918666176/Box+configuration/) elements to be created in an upper-level box and inherited (applied to) its sub-boxes.

When a box inherits elements, it takes them from all its upper-level boxes.

## Inherited elements

You can set inheritance mode for:

- [Card views](/cms_trial/space/SPM/1918830445/Manage+card+views/)
- [Quick filters](/cms_trial/space/SPM/1918830532/Manage+quick+filters/)
- [Column views](/cms_trial/space/SPM/1918503715/Manage+column+views/)
- [Task templates](/cms_trial/space/SPM/1918503892/Manage+task+templates/)
- [Security settings](/cms_trial/space/SPM/1918829579/Permissions/) (Security settings as they are always inherited)

These settings can be inherited when a new box is created or moved to an upper-level box of a different type.

## Security and access

Inheritance mode is set up for a [box type](/cms_trial/space/SPM/1918830000/Box+types/), meaning all Boxes of a given type have the same setup.

Inheritance mode is set up for each element separately. This means you can, for example, ensure Column views are inherited, but Quick filters aren't.

Inheritance settings can be found in **App Administration** > **Box types section** > **Box details (select one of the Box types)** > **go to a particular element, for example, Column views** > **Inheritance mode**.

To access it, you need the App Administrator security role.

![image-20250327-114935.png](/cms_trial/assets/090edd99-d028-4328-834f-62b623d5d8a4.png)

## Inheritance modes

In general, selecting "Inherited mode" means that the upper-level boxes impose the configuration, and you can change the settings of all sub-boxes by editing the upper-level Box. As a result, users will be unable to change some of the settings of the Box configuration since it is already preconfigured. Fewer settings to choose from will make the app more straightforward to understand. The "Own mode" provides much more flexibility.

There are three Inheritance modes that determine whether users can customize the box settings.

| **Inheritance mode** | **Description** | **Active and favorite settings** | **Mode change** | **Editing inherited items** |
| --- | --- | --- | --- | --- |
| Own | In this mode, you can personalize the settings on the Box type configuration and Box configuration pages.  The personalized settings of the upper-level boxes are not shown when viewing the sub-Box configuration. | The currently used (Active) setting is selected for the sub-Boxes if the sub-Box mode is set to:   - Inherited - Own with Inherited | To "Own with Inherited:"   - reveals "Inherited" items   To "Inherited:"   - hides "Own" items - shows "Inherited" items | Not applicable |
| Own with inherited | All the configured items for the upper-level Box are available to users in this mode.  The box admin cannot add your configuration to the Box configuration. | Apply to both upper-level and sub-Boxes in the following modes:   - Inherited - Own with Inherited | To "Inherited:"   - hides "Own" items | Not allowed |
| Inherited only | In this mode, you can not personalize the settings predefined in the upper-level Box.  The configuration tabs in the Box configuration are not displayed. | Apply to both upper-level and sub-Boxes in the following modes:   - Inherited - Own with Inherited | To "Own with Inherited:"   - reveals "Own" items - allows creating "Own" items | Not allowed |

## Recommended use

If you want specific settings to apply to all boxes, you can change them for the Home (root) Box. As long as other boxes are set to inherit an element, changing it on the root level will apply to all inheriting Boxes.

## Impact of the inheritance mode on the box type settings

### [Column views](/cms_trial/space/SPM/1918503715/Manage+column+views/)

The table presents how inheritance mode settings impact column views.

Changes made to the inheritance mode apply to **ALL** boxes of a given type (existing and newly created).

| **Inheritance mode** | **Description** |
| --- | --- |
| **Own** | Each box uses its column views (editable). |
| **Own with Inherited** | Each box uses:   - Its column views (editable). - Column views created in boxes on the upper level (non-editable). |
| **Inherited only** | Each box uses only column views created in boxes on the upper level (non-editable).  You can use them, but to edit them, you must go to the box in which they were created.  **Note**: The **Column views** tab is hidden in the box configuration. (The column views are inherited from the upper-level box and can only be edited in that box.) |

| **Results in a box** | **Gantt/Scope module → Column views configuration** |
| --- | --- |
| Own | Screenshot of the column views and inheritance mode set to Own in the box type configuration. |
| Inherited | Screenshot of the column views and inheritance mode set to Inherited in the box type configuration. |

### [Card views](/cms_trial/space/SPM/1918830445/Manage+card+views/)

The table presents how inheritance mode settings impact card views.

| **Inheritance mode** | **Description** |
| --- | --- |
| Own | The **own** mode provides much more flexibility. When enabled:   - You can define the default card views for all boxes of a given type. - You can bulk update all existing boxes. The card views added in upper-level boxes are not inherited. - The default views are set up when a new box is created but can later be adjusted for each box by a box admin (the default configuration can be manually overridden). |
| Inherited only | The **inherited only** mode doesn't allow for making any changes directly in the sub-box configuration.   - The card views are inherited from an upper-level box. - The task card views page is not shown in the box configuration. - Box admins can impact the sub-box by editing the card views directly in the configuration of an upper-level box (if they are also box admins for the upper-level box). As a result, users cannot save the modified card views, and sub-box admins cannot change the views in the box configuration since it is already preconfigured. |
| Own with inherited | The **own with inherited** mode mixes the two.   - A box admin can create new card views directly in the sub-box configuration. - The card views are inherited from the upper-level box (those views can only be edited in the upper-level box). |

### [Security roles](/cms_trial/space/SPM/1918829579/Permissions/)

User roles inherited from upper-level boxes are not listed in **Box Configuration** > **Security**. They can be viewed only at the upper level.

Roles are always inherited from the upper levels. Security settings are always inherited. There are only two possible security inheritance modes:

- Own with inherited
- Inherited

The table presents how inheritance mode settings impact the security settings.

| **Inheritance mode** | **Description** |
| --- | --- |
| Own with inherited | Box users = manually added + inherited |
| Inherited only | Box users = inherited  In the "Inherited only" mode, the Security tab of an individual Box is hidden (you can't access it in Box configuration). |

| **Change of the inheritance mode affects ALL boxes** |
| --- |
| **from** |  | **to** |  | **result** |
| Own with inherited | → | Inherited only | = | manually added users lose access |
| Inherited only | Own with inherited | restores the previously existing users |

### [Task templates](/cms_trial/space/SPM/1918503892/Manage+task+templates/)

| **Inheritance mode** | **Description** |
| --- | --- |
| Own | - You can define the default task templates for all boxes of a given type. The default templates are set up when a new box is created and can later be adjusted for each box by a Box Admin (the default configuration can be manually overwritten). |
| Inherited only | - You cannot make any changes directly in the sub-box configuration since the task templates are inherited from the upper-level Box. - The *Task Template* page is not shown in the box configuration. - Box Admins can edit the task templates directly in the upper-level box configuration (if they are also Box Admins for the upper-level box). - As a result, you cannot change some of the settings of the box configuration since it is already preconfigured. |
| Own with inherited | - A Box Admin can create new task templates directly in the sub-box configuration. |

### [Quick filters](/cms_trial/space/SPM/1918830532/Manage+quick+filters/)

| **Inheritance mode** | **Description** |
| --- | --- |
| Own | When a Box type has a Quick Filters inheritance mode set to "Own," you can only use filters defined for an individual Box.  For example, "Program" is a Box type. When you create a new Box using this type, it will have the "Default Quick Filters" (specified for the "Program" Box type) + filters you manually add to an individual Box.  Once a new Box has been created, a Box admin can access its Configuration to manage filters (change existing ones, add new ones, delete, etc.) What you see is what you get. Filters listed in the tab are the only ones available for the "Omega" Box. |
| Inherited only | When Quick Filters for a Box type are set to "Own with inherited," a resulting Box has filters that can be edited/deleted/created in Box Configuration + filters inherited from upper-level Boxes (that cannot be changed). A Box admin can review Box settings in Box configuration.  Inherited filters are marked with arrows in the Box Configuration of a Program Increment Box. Those filters cannot be edited or removed (this type of change would have to be done in the upper-level Boxes those filters originate from). New filters can be added to the Box. |
| Own with inherited | When Quick Filters for a Box type are set to "Inherited only," a resulting Box doesn't have its filters - only filters inherited from upper-level Boxes are available. The "Quick Filters" tab is hidden in Box Configuration.  In Box Configuration of all Boxes of this type, the "Quick Filters" tab is hidden. You can't change or review the filters there.  You must try using them to see the filters - all inherited filters are visible on the list. |