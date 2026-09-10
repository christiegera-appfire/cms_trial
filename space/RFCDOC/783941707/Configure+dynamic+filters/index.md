# Configure dynamic filters

## **About dynamic filters**

Dynamic filters allow you to filter the collection of issues displayed by rich filter gadgets. Dynamic filters are based on Jira fields and allow filtering issues by field values. Once configured, the dynamic filters can be displayed in *Rich Filter Controller* gadgets:

- as buttons with drop-down menus in the case of option fields;
- as date input fields with a date picker for date and date time fields.

When a dynamic filter is activated in a Rich Filter Controller gadget, all the other gadgets in the same dashboard, which are based on the same rich filter, apply the selected criteria.

![dynamic_filter dashboard.png](/cms_trial/assets/f81dd455-9367-45d8-a44a-b59dfd8a9ea2.png)

## **Dynamic filter types**

![Dynamic filters.png](/cms_trial/assets/11acd996-bf38-4af4-833e-75994d2aa546.png)

There are four types of dynamic filters, depending on the kind of fields they are based on:

## Option-based dynamic filters

Option-based dynamic filters are used for fields that can take predefined values: checkboxes, select lists (single or multi-select), status, priority, labels, user pickers, etc. Controller gadgets display each dynamic filter as a button with a drop-down menu, providing a list of options from which users can select the ones they want to filter.  
When activated, dynamic filters limit the results to only the issues that match the selected options. If more than one option is selected, the filters will keep the issues that match *any* of the selected values (in JQL syntax, the conditions on the selected options are `OR`ed together, then the resulting clause is `AND`ed with the other JQL clauses).

![apply filtr.png](/cms_trial/assets/0ceebfd1-15ae-4d4d-8dfa-e4b4dddccb4f.png)

The list of options in the drop-down menu is populated only with the values in the issues returned by the base Jira filter. This means that the list doesn’t show options defined by the field configurations, but they do not occur among your issues. Not showing irrelevant options improves the user experience. For example, this is very useful if you add a dynamic filter for the *Assignee* field – the drop-down menu displays only the users who have at least one issue assigned.

When you click a dynamic filter option, the button turns into a search box, making it easier to find the options you are looking for. The options can be checked / unchecked one by one with a click or as a range using Shift + click. These mechanisms are particularly useful for fields with a large number of options.

## Date dynamic filters

Date dynamic filters are used for date and date time fields, both system fields (created, updated, resolution date) and custom fields. Date filters allow users to limit the results to only the issues with the date field value on, before, or after a date or between two dates.  
Each dynamic filter has two date inputs: *From* and *To*:

1. If only **From** is filled, then only the issues having values on or after the **From** date are kept;
2. If only **To** is filled, then only the issues having values on or before the **To** date are kept;
3. If both ***From*** and **To** are filled, only the issues with values between the *From* and *To* dates (both inclusive) are kept. If **From** and **To** are filled with the same date, then only the issues having values on that date are kept.

The inputs *From* / *To* can be selected from a date picker or entered manually as a calendar date (`yyyy/MM/dd` or `yyyy-MM-dd`) or as a time relative to the present (for example, `5d` or -`4w 2d`).

![date filter.png](/cms_trial/assets/78e0ee43-562e-480f-8f8c-c6c916d04dfc.png)![due date.png](/cms_trial/assets/c8dbdf44-3f25-4d83-9d90-3cdd28a52100.png)

If you want to use *now* as an input in *From* or *To*, you can enter the value `0d`.

## Text dynamic filters

Text dynamic filters are used for string and text fields, system fields (such as summary and description), and custom fields. Text filters don’t use a menu—instead, they display a text box for the search query input. When activated, text dynamic filters limit the results to only the issues that match the search query, that is, that contain the entered text.

Jira has two text searchers, one for exact string search and one for full-text search. Each dynamic filter will use the searcher associated with the underlying field. Advanced full-text search features such as wildcard searches and Boolean operators are supported – see Jira’s [documentation page](https://support.atlassian.com/jira-work-management/docs/search-syntax-for-text-fields/) for the syntax.

![COntain text.png](/cms_trial/assets/c005fc43-416b-4a0d-b930-82e8896550c0.png)

Besides issue fields, there are two extra text dynamic filters that you can add to your rich filters:

- *Contains text* – full-text search in all text fields: summary, environment, description, the comments of the issue, as well as all the custom text fields
- *Comment* – full-text search in all the comments on the issue.

When configuring dynamic filters on fields of type Short text, you can also choose the **Filter behavior:**

- **Text search** - Searches issues by keywords
- **Select values** - Displays a dropdown with a list of values to choose from

## **Number dynamic filters**

Number dynamic filters are used for custom number fields, such as **Story Points** or **Business Value**, and the number of votes or watchers. Number filters display a text box for the search query input. The search query can contain one or multiple space-separated terms (numeric values or ranges) as described below:

1. Search by *value*: enter one or several space-separated values to search for – for example, `1 2 3` for the issues having the values 1, 2, or 3;
2. Search by *comparison*: the operators `<`, `>`, `<=`, and `>=` are accepted – for example, `>=1` for the issues having values greater than or equal to 1;
3. Search by *range*: use the form `a:b` to search by values between a and b included – e.g., `1:10` for issues having values between 1 and 10;
4. Search by *empty* or *not empty*: type `empty` for issues with the field empty or “!empty“ for issues with the field empty.

At execution, the terms are joined using OR operators. For example, the query `1 2 <0 4:8` returns the issues having the values 1 or 2, or values less than 0, or in the range 4–8.

![Story points.png](/cms_trial/assets/be56429d-1d8a-478f-ad83-09b8a9481748.png)

## Other dynamic filters

### **Key**

The Key dynamic filter lets you search for work items based on their key. In the controller, the filter displays a box for entering a work item key or words from its summary. When activated, it limits results to the selected work items.

### **Parent**

The Parent dynamic filter lets you search for work items based their parent.

### **Linked Issues**

The Linked Issues dynamic filter returns all work items that are linked to the work items you select.

## **Adding and editing** **dynamic filters**

You can add new and existing dynamic filters in the *Dynamic filters* section of your rich filter.

![dynamic_filters_.png](/cms_trial/assets/653037cb-1b80-428f-8e51-bc4a1a29df69.png)

When using Rich Filters across multiple projects with different types (for example, Jira Software, Jira Product Discovery, JWM), you can encounter duplicate field names, such as multiple "Customer" fields, in dropdown menus.

To help you distinguish between fields with the same name, the app shows additional information in tooltips when you hold the pointer over any field in dropdown menus:

- Field type appears in brackets (for example, "Customer [text]")
- Custom field ID is added when duplicates still exist (for example, "Customer [text] cf[12345]")

The *Dynamic filters* section of your rich filter lets you perform the following operations:

### **1. Add a dynamic filter**

1. Click **Pick a field...** at the bottom of the page. A drop-down menu is displayed, showing all the supported fields.

![contentId-783941707](/cms_trial/assets/c79dab03-72bf-4e66-b120-7f7a47f9c36d.png)

1. You can either scroll down or use the search to find the field you want to add as a new dynamic filter.

![contentId-783941707](/cms_trial/assets/4205e4a9-cbfa-4559-bca4-489692f6943a.png)

You can add up to 100 dynamic filters in each rich filter

### **2. Edit a dynamic filter**

This configuration is available only for option-based dynamic filters.

1. To open the edit dialog, click the **Edit** (▢ ) icon next to the dynamic filter.

![contentId-783941707](/cms_trial/assets/7166c744-2c31-4712-985e-e2dc638bb149.png)

1. The *Edit* dialog lets you:

- Edit the **Filter name** displayed in the dynamic filter. You can keep the **Field name**, display only **Field initials**, or set a **Custom** name.
- **Reverse options order** displayed in the dynamic filter drop-down.

  ![edit_dynamic filter.png](/cms_trial/assets/752d8e48-8643-4c7e-a0e3-91288ff34f87.png)

### 3. **Delete a dynamic filter**

Click the **Delete** (▢) icon next the dynamic filter.

![contentId-783941707](/cms_trial/assets/cb609e6b-0e7c-4d42-aea4-b0841453ece4.png)

### **4. Reorder the dynamic filter**

Hold the pointer over the vertical **Grid** (▢)  icon, then drag the dynamic filter up or down to its new position.

![contentId-783941707](/cms_trial/assets/1cc4c34f-dc15-4b76-99fa-64ea114387d2.png)

When the dynamic filters of this rich filter are displayed by *Controller* gadgets, they are shown in the order configured in this section by default.