# Configure smart filters

## **About smart filters**

Smart Filters can be more versatile than static filters and dynamic filters. Smart filters allow the users to:

- Filter the collection of issues displayed by rich filter gadgets. In Rich Filter Controller gadgets, smart filters can be displayed as buttons with drop-down menus (similar to dynamic filters).
- Add computed columns and color-coding in *Rich Filter Results* gadgets.
- Build statistics on configurable criteria.

![Configure smart filter](/cms_trial/assets/57a3e1a4-0ea2-4cbd-b570-40d8df1310b7.png)

## **Smart filters key attributes**

You can add new and see existing smart filters in the *Smart filters*section of your rich filter.

![Smart filters tab](/cms_trial/assets/08b356e2-0aeb-4841-80a1-27ed0b00d282.png)

The key attributes of a smart filter are:

| **Attribute** | **Description** |
| --- | --- |
| **Name** | Each smart filter has a **name** that identifies it. This name is mandatory and must be unique among the smart filters within the rich filter. |
| **Clauses** | A smart filter contains a list of clauses (options). Each clause is identified by a color and a label tag, and a JQL is applied when it is used. |

## **Adding and editing smart filters and smart filter clauses**

The *Smart filters* section of your rich filter allows you to perform the following operations:

### 1. Add a new smart filter

1. Click **Create smart filter** at the top right of the page.

   ![create smart filter option](/cms_trial/assets/7ceb7bda-3a13-43ee-be15-f36f15b683ef.png)
2. Type a name.
3. Tick **Enable AND operator** if you want the smart filter to allow the AND operator when used for filtering in the controller.
4. Click **Create**.

   ![Create a smart filter](/cms_trial/assets/3a83062e-00d4-44ec-88d5-19cd3fcc9e1a.png)

You can add up to 100 smart filters in each rich filter.

### **2. Browse the smart filters list**

The *Smart filters* section of your rich filter lets you browse the smart filters list. Depending on your rights, you can click any smart filter to view or edit its properties (see below).

![smart filter list.png](/cms_trial/assets/a3008184-5776-4f19-a34f-49253cc96438.png)

### 3. **Reorder the smart filters**

Hold the pointer over the vertical **Grid** (▢)  icon, then drag the filter up or down to the new position.

![change position](/cms_trial/assets/d81807fe-9536-461b-8d50-2bb224495eb5.png)

When the smart filters of this rich filter are displayed by Controller Gadgets, they are displayed in the order configured in this section by default.

### 4. **Duplicate a smart filter**

1. Click the **Duplicate** option available in the corresponding smart filter’s menu.

![duplicate smart filter.png](/cms_trial/assets/4dccaf94-a2f4-42c0-a7c4-05370c2e72cc.png)

1. Name of the new smart filter and click **Duplicate**.   
   A new smart filter identical to the first one, but with the name you have entered, is created.

![Duplicate teams.png](/cms_trial/assets/9f317d04-d799-4460-8148-f6fd076f3640.png)

### **5. Delete a smart filter**

In the *Smart filters* list, click the **Delete** option in the corresponding smart filter's menu.

![delete smart filter.png](/cms_trial/assets/3f63fe7a-86b0-4f38-9784-1c45d52973ef.png)

### **6. Create a smart clause**

Click the **Plus** icon next to the smart filter to create a new smart clause.

![plus icon to create smart clause](/cms_trial/assets/2f2b21ce-b434-4bd8-911f-5a30ad96f135.png)

When you create a new smart filter or click an existing smart filter, a new screen focusing on the selected smart filter is displayed. This screen lets you perform the following operations on the selected smart filter:

### **1. Edit a smart filter’s name**

Click the **Edit** (▢) icon next to the static filter.

![Edit filter name](/cms_trial/assets/0842da72-f1db-4159-a035-d0c9d6731308.png)![edit name](/cms_trial/assets/2b5b2fb4-1354-40d4-b19c-f12c914ce7c7.png)

### 2. **Add clauses to the smart filter**

1. Click the **Create smart clause**button.

![Create smart clause](/cms_trial/assets/522f04a0-5535-4edb-bf76-87c76e15fe25.png)

2. Select a color, enter a **Name** and a **JQL** clause, and click **Create**.

![create a mart clause](/cms_trial/assets/e2ed9305-a84b-466f-b03a-e4d05065e95c.png)

You can add up to 10 smart clauses in each smart filter.

### 3. **Edit the clauses of the smart filter**

1. Click any smart clause to edit it (or click the corresponding **Edit** (▢) icon at the right of the clause).
2. Update the clause's color, name, and/or JQL clause.
3. Click **Update** to save the changes.

![Edit the clauses of the smart filter](/cms_trial/assets/d7f182c7-9618-4787-a6df-5f5db319582a.png)

### 4. **Enable AND operator**

Tick **Enable AND operator** if you want the smart filter to allow the AND operator when used for filtering in the controller.

![Enable AND operator](/cms_trial/assets/57816322-115c-438e-967e-3a0f1cd87d1e.png)

### 5. **Reorder the clauses of a smart filter**

Hold the pointer over the vertical **Grid** (▢)  icon, then drag up or down to the new position.

![contentId-783941713](/cms_trial/assets/96698364-0d1a-46e6-9784-eafc804bb91f.png)

When Rich Filter gadgets display the smart filter, the smart filter options are shown in the order configured in this section.

### 6. **Delete clauses from the smart filter**

Click the **Delete** (▢) icon at the right of the clause.

![Delete clauses ](/cms_trial/assets/21b785ce-0d5c-4aaf-b213-243ad9275d56.png)

## **Using smart filters in Rich Filter gadgets**

Once configured, smart filters can be used in several rich filter gadgets:

- The **Rich Filter Controller** gadget – You can use the smart filters to apply additional filtering to the other rich filter gadgets. The smart filters are displayed as drop-down menus (similar to dynamic filters).

  ![controller with smart filter](/cms_trial/assets/540c8668-ebee-4a50-9e09-5d7459b31b6d.png)

Look at [The Rich Filter Controller Gadget](/cms_trial/space/RFCDOC/783941745/The+Rich+Filter+Controller+Gadget/) documentation page to find out how to configure the gadget.

- The **Rich Filter Results** gadget lets you add smart filter views as smart columns for issue highlighting/tagging.

  ![results with warnings](/cms_trial/assets/5479eea8-0067-4f96-8b28-cfdddbb664aa.png)

  Please see the [Configuring Views](/cms_trial/space/RFCDOC/783941729/Configure+views/) documentation page to learn how to add smart filters as smart columns and how to configure [The Rich Filter Results Gadget](/cms_trial/space/RFCDOC/783941759/The+Rich+Filter+Results+Gadget/).
- The **Rich Filter Statistics** gadget – the smart filters can be used as statistics criteria.

  ![STATISTICS WITH SMART FILTERS.png](/cms_trial/assets/bf809fd4-b0ef-4518-8c29-872efed3fd46.png)

Have a look at [The Rich Filter Statistics Gadget](/cms_trial/space/RFCDOC/783941781/The+Rich+Filter+Statistics+Gadget/) documentation page to learn how to configure the gadget to aggregate data using a smart filter.

- The **Rich Filter Two-Dimensional Statistics** gadget—the smart filters can be used as statistics criteria on either of the two axes.

  ![Two dimenttional statistics](/cms_trial/assets/0fec7c8a-b922-4f4c-95e3-469e1874817e.png)

Have a look at [The Rich Filter Two Dimensional Statistics Gadget](/cms_trial/space/RFCDOC/783941803/The+Rich+Filter+Two+Dimensional+Statistics+Gadget/) documentation page to learn how to configure the gadget to aggregate data using smart filters.

- **The Rich Filter Flexi Charts** gadgets – the smart filters can be used as statistics criteria.

  ![flexi charts with smart filter](/cms_trial/assets/ea845b80-759e-4a40-8a79-5e6da84d62db.png)

Look at [The Rich Filter Flexi Charts Gadget](/cms_trial/space/RFCDOC/783941863/The+Rich+Filter+Flexi+Charts+Gadget/) documentation page to learn how to configure the gadget to aggregate data using a smart filter.

When deciding which clause an issue falls into, we use a *match-all criteria:* the same issue can be part of multiple smart clauses if it matches their corresponding JQL clauses. This means that when the smart filter is used as a filter or as a computed column, it behaves as a multi-select option field.

If you want your smart clauses to be mutually exclusive, you must write your JQL so that an issue can match only one clause at any time. For instance, these are mutually exclusive clauses; an issue cannot possibly match more than one clause at a time:

![high level priority](/cms_trial/assets/70613def-bfba-4eec-8c4c-bcd7b346bb64.png)