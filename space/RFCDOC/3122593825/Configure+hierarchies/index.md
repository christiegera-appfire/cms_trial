# Configure hierarchies

## About hierarchies

In Jira, the issue type hierarchy defines the levels used to create the parent-child relationships between issues (for example, Initiative → Epic → Story → Subtask). For details, see [Configure the work type hierarchy](https://support.atlassian.com/jira-cloud-administration/docs/configure-the-issue-type-hierarchy/). In Rich Filters, *hierarchies* allow you to visualize issues in the [Rich Filter Results](/cms_trial/space/RFCDOC/783941759/The+Rich+Filter+Results+Gadget/) gadget by organizing them according to Jira’s issue type hierarchy. Instead of a flat list, issues appear in a collapsible tree structure that preserves parent-child relationships across multiple levels.

Like queues, hierarchies are specialized issue lists defined in the rich filter configuration. Each hierarchy defines which issues it includes and which views it uses to display them.

Here are some of the main features of the hierarchies:

- Like queues, hierarchies appear as tabs in the *Rich Filter Results* gadget. Users can switch between them with one click.
- The hierarchy displays issues in a collapsible tree structure, with each issue placed under its parent. Issues without a parent are placed under a node named after the level: for example, a story without a parent is placed under the node *Story*.
- Hierarchies respond to the quick filters applied in the controller, but don't show only the matching issues; they also show all issues related to matching issues (ancestors, siblings, etc.), to preserve the hierarchy structure and context. Matching issues are highlighted with a blue vertical line on the left of the row and appear before non-matching issues.

- The hierarchy feature is designed for company-managed projects. Team-managed projects are not supported yet.
- The levels available in a hierarchy are determined by Jira issue type hierarchy. Jira Standard plan only allows three predefined hierarchy levels (Epic, Story, and Subtask), while Jira Premium and Enterprise plans allow additional/custom hierarchy levels. For details, see [Understanding Jira Hierarchy](https://community.atlassian.com/forums/App-Central-articles/Understanding-Jira-Hierarchy-Complete-Guide-in-2025/ba-p/2947722).

![image-20261023-112645.png](/cms_trial/assets/fb3050e0-34fd-476c-a60f-950817179ab3.png)

## Hierarchies key attributes

You can add new hierarchies and view existing hierarchies under **Lists** *>* **Hierarchies**in your rich filter configuration.

![image-20260925-084914.png](/cms_trial/assets/3a219e70-342f-4b99-80ba-3782d0a13378.png)

The **key attributes** of hierarchies are:

| **Attribute** | **Description** |
| --- | --- |
| **Name** | Each hierarchy must have a unique name within the rich filter. |
| **Color** | The selected color will be used to display the hierarchy in the Rich Filter Result gadgets. |
| **Hierarchy structure** | The hierarchy structure lets you customize the level names for the current hierarchy.  Rich Filters supports up to 7 hierarchy levels: from -1 to 5. |
| **Include levels** **From / To** | Select the range of levels you want to include in the hierarchy. Only the issues belonging to the selected level range are part of the hierarchy. |
| **JQL** | You can define a JQL query to further filter the issues that are included in the hierarchy. Optionally, an ORDER BY clause can be used to set the default order of the issues in the hierarchy. |
| **Views** | The views used to display the issues in *Rich Filter Results* gadgets. By default, the hierarchy uses all the views defined in the rich filter (the option *Show all views* is selected).  The list of views can be customized (by selecting the option *Customize shown views*). You can add, remove, or reorder (by drag) the views you want to display. |

## Manage hierarchies

The **Lists > Hierarchies** section of your rich filter lets you perform the following operations:

### **Add a hierarchy**

You can add up to 100 hierarchies in each rich filter.

1. Click the **Create hierarchy** button at the top-right of the page.   
   The **Create a hierarchy** dialog opens.

   ![contentId-3122593825](/cms_trial/assets/482726b4-1a7c-4f5a-a6cc-c0ac1d1eb55d.png)
2. Type a **Name** and select a color.
3. Under **Hierarchy structure**, customize any level names as needed.
4. Under **Include levels**, select the level range for the hierarchy, and under **JQL**, type any additional filtering or sorting query, as needed.
5. Select whether you want to **Show all views** or **Customize shown views**.

You can reorder your customized view list by drag and drop.

1. Click **Create**.

![Create hierarchy](/cms_trial/assets/78a3368f-59e6-4a4d-9850-1bf4b5c90885.png)

### **View or edit a hierarchy**

- Click the **Edit** (▢) icon on the hierarchy row to view or edit its configuration.

  ![edit.png](/cms_trial/assets/e7bef54a-ba18-4fdd-a6a6-16224edc5e79.png)

### **Reorder the hierarchies**

- Hold the pointer over the hierarchy **Grid** (▢) icon, then drag up or down to the new position.  
  The order you set here determines the default order in which hierarchies appear in the *Rich Filter Results* gadget.

  ![2026-07-06_14-22-15.png](/cms_trial/assets/1896bb4b-7db6-4367-98db-0b9ef3eaae3d.png)

### **Delete a hierarchy**

- Click the **Delete** (▢) icon on the hierarchy row.

  ![Delete.png](/cms_trial/assets/7d4583c1-8e35-46e5-b16a-ae302820f668.png)

## See also

- [Organize issues with hierarchies in Jira dashboards](/cms_trial/space/RFCDOC/3122856080/Organize+issues+with+hierarchies+in+Jira+dashboards/)
- [The Rich Filter Results Gadget](/cms_trial/space/RFCDOC/783941759/The+Rich+Filter+Results+Gadget/)
- [Configure views](/cms_trial/space/RFCDOC/783941729/Configure+views/)
- [Configure the work type hierarchy | Atlassian Support](https://support.atlassian.com/jira-cloud-administration/docs/configure-the-issue-type-hierarchy/)
- [Understanding Jira Hierarchy](https://community.atlassian.com/forums/App-Central-articles/Understanding-Jira-Hierarchy-Complete-Guide-in-2025/ba-p/2947722)

---