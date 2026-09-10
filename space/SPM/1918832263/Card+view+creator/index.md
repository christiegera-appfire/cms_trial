# Card view creator

The **card view creator** lets you design and preview the card views used by the **Board** and **Risks modules**.

The list of available fields includes native Jira fields and custom fields added by Jira admins and installed apps. When you connect other tools, fields used by these tools will also appear on that list. Such information will be displayed in the **Origin** column of the field list.

## Security and access

The card view creator works exactly the same at the box type and box levels. See the [Manage card views](/cms_trial/space/SPM/1918830445/Manage+card+views/) page.

For box type configuration:

1. Go to the **App Administration** > **Box type** > **choose the box type you want to edit** > **Board / Risks** > **Card views**.

For box configuration:

1. Go to **box configuration** > **Board / Risks** > **Card views**.

## Add and configure new card view

To add a new card view:

1. Click **Add new card view**.
2. Enter **Summary**.
3. Define **Visibility**. Set the visibility to **Public** if you want other users to select that view from the **Card view** drop-down.
4. Optionally, provide a **Description**.
5. When ready, click **Create**.

   ![Screenshot of adding a new card view on the box configuration page.](/cms_trial/assets/d6b38b94-517a-4591-82e4-a303e37b27a9.png)
6. Once created, the new view appears on the list.
7. To modify the layout, select the clickable name link in the **Summary** column.

   ![Screenshot of clicking on the card view name on the box configuration page.](/cms_trial/assets/fb688dfa-7454-44c4-a5df-ac691c5ee02c.png)

### Card and field dimensions

You can change the card dimensions by adding or removing rows. While there is no limit on the number of rows, remember that the more information a task card displays upon loading, the more it affects the BigPicture performance. Also, the larger the size of the card, the fewer cards you will be able to display in a single view. However, you can solve this problem by creating multiple card views with different settings and switching between your custom layouts as required.

To add a new row, click the **+** button at the bottom of the card.

To remove the row, click the **bin** icon on the right side of the card.

![Screenshot of the card view details on the box configuration page. ](/cms_trial/assets/56859f37-3c41-444f-a2bb-56e3aa6eab85.png)

You can also change the dimensions of the field areas on the card.

To change the field area, use the **...** icon, which appears when you click one of the field areas.

![Video of changing a field area for a card view on the box configuration page.](/cms_trial/assets/17adeb37-5740-42b4-8680-acca5ac2c1d3.mp4)

### Add fields to the card

To find the fields you want to include on the card, scroll through the available fields or use the search box.

To add a field, drag it in the green shaded area of the card.

Some fields, such as **Icon**, **Assignee**, or **Priority types**, can be added to the side columns.

![2024-10-22_12-45-45.mp4](/cms_trial/assets/d755541a-5a3c-4fa8-9e6d-d8b417009082.mp4)

### Field configuration

Fields can have different types, which is essential as it determines what additional display settings you can configure.

For example, the **Status** field can be displayed as:

- Description
- Lozenge

The **Assignee** field can be displayed as:

- Icon
- Name
- Icon and name

To change the display options, click the **cog** icon next to the field.

![Screenshot of clicking on the cog icon to display field options on the card views page.](/cms_trial/assets/b86877a1-1091-4a38-85c8-5d93a1819967.png)

Once the card is ready, click the **Save** button.

![Screenshot of saving the card view on the box configuration page.](/cms_trial/assets/782e533d-00e8-4415-8b4b-da0f71477fec.png)

### Active card view

If you apply one of the available views from the **Card view** drop-down, it becomes active, and a green check mark appears next to its name. This means that this view will be applied whenever a user opens the module or returns to it.

## Card preview

To preview the card, click the **Preview** button and use the search box to find a task by starting to type in the **Summary** or **Issue** key.

## Order of card views

Default box types have default views set to their default order. If non-default views are present, they are put in alphabetical order after all the default ones.

Boxes created from default box types have views set to their default order. If non-default views are present, they are put in alphabetical order after all the default ones.

All views in non-default box types are in alphabetical order.

## Edit card views

To edit a card view:

1. Click the **Details** button.
2. Make changes to the **Name**, **Visibility**, or **Description** fields.
3. To apply changes, click **Save**.

![Screenshot of editing a card view in the box configuration.](/cms_trial/assets/1750a2c7-48cd-49c8-a96b-5e3a76deace5.png)

## Duplicate card views

You can duplicate an existing layout and adjust it to your needs. Click the **Duplicate** button, and BigPicture will create a copy of a selected view.

![Screenshot of duplicating a card view in the box configuration.](/cms_trial/assets/ac9d2435-e686-4a52-a81d-b9463f9350fb.png)

## Delete card views

You can’t delete an active view, and at least one view must be defined.

To delete a card view:

1. Click the **Delete** button next to a card view you want to delete.
2. To confirm, click **Delete**.

   ![box-config-risks-delete.png](/cms_trial/assets/a38fa125-5332-431b-acbd-23955b99a29d.png)