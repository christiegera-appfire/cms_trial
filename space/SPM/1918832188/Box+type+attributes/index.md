# Box type attributes

## About box type attributes

In this section, you can set up a default basic configuration of a given box type. Specify the box type name, prefix, icon, description, and available parent types. The box attributes are displayed in different modes of the Overview module and the box switcher.

Once a box is created, you can override the default configuration in the box configuration section.

Keep in mind:

- A box type contains the default settings applicable to multiple boxes (all boxes of a given type). Those settings are adjusted in **Administration** > **Box types**.
- Box configuration refers to the settings of a single, individual box. They are dependent on the box type settings.

## Security and access

Only a user with the App admin security role can access and manage the box type configuration.

To access this page:

1. Go to the **App Administration** > **Box type** > **choose the box type you want to edit** > **General** > **Basics**.

![Screenshot of the Basics page in the box type configuration.](/cms_trial/assets/790d1108-5bf5-42f8-82f6-30bef3bd708d.png)

## Basic box type attributes

Under the **Basics** tab in box type configuration, you can define the following attributes.

- Box type name
- Icon and color
- Prefix
- Description
- Parent types

### Box type name

Default box names describe the purpose of a template, such as a hybrid project. You can create your own types with different names.

A box type name appears in the drop-down used for selecting a box type (during the creation of a new box) and is:

- Available as a box type of filter.
- Displayed in a column in the Overview module.
- Listed in a column in **Administration** > **Box types**. A box type name works as a clickable link to the **Box type** editing page.

Changing a box type name updates all existing boxes of that type.

In the example below, you can see the drop-down used for selecting a box type (during creation of a new box):

![Screenshot of creating a new box in the Overview module.](/cms_trial/assets/8a9ad923-f499-4559-9439-7a8c2d64b25f.png)

### Icon and color

Color-code your box type icons - this feature makes it easy to categorize your boxes and identify their content at first glance. A colored icon is displayed in both the Overview module and the box switcher, making finding a particular box easy and quick. The default setup can be changed (either during the creation of a box or later in its configuration).

Changing the color and icon of a box type doesn't impact existing boxes. Only boxes created after a box type configuration has been updated will be affected.

The **Type** column will always display the color selected for a box type.

The **Icon** and its color can always be changed for an individual box. They don't have to follow the box type convention.

![Screenshot of the Box Type column in the Overview module.](/cms_trial/assets/bf675b07-d28b-4ff8-a777-bd1dd1ccc152.png)

When you create a new Program box, color, and icon are automatically recommended, but you can change them.

See the video to learn how to change a box icon and its color when creating a new box.

### Prefix

Whenever you create a new box, BigPicture uses a prefix + a generated number to create a unique box ID. The prefix length cannot exceed five characters. The box ID is displayed in the Overview module and as a column in **Administration** > **Box types**. With enhanced JQL, you can use the box ID to search for issues within the scope of a box.

For example, if the Waterfall type has a "WSTA" prefix, adding the first Waterfall stage sub-box to your Waterfall Project box results in a "WSTA-1" prefix. The next stage will be created with a "WSTA-2" prefix.

Changing the prefix of a box type doesn't impact existing boxes. Only boxes created after a box type configuration has been updated will be affected.

### Description

An additional description field lets you summarise the configuration of a box type or add instructions on when it should be used.

### Parent types

Parent box types determine how you can build the box hierarchy (nest boxes) and, thus, prevent users from making mistakes and mixing methodologies. During box type configuration, you decide under what parent types a particular box type can be nested. Then, after you have specified parent types for a given box type, the App knows possible parent/child relationships. When creating a sub-box, the list of available box type options is limited. Also, the validation mechanism will prevent you from freely using the drag-and-drop mechanism to rearrange the box hierarchy.

If you don't add any parent types, the box type can't be used, as validation rules will not allow it to be placed anywhere in the hierarchy. Make sure to add at least one parent type.

To use a box type in the Home (root) box, add **Main** as a parent type.

Changes made to parent types assigned to a box type apply to all boxes of that type (both existing and newly created). However, the existing hierarchy won't be altered (a box will remain under a parent *A* even if you can't nest it anymore under a different *A* type box).

![Screenshot of the validation error in the Home box.](/cms_trial/assets/16e15005-5b15-416e-973a-fb56ff9c6964.png)