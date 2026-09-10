# Use case: Filter Jira work items added to project

## Use case: Filter Jira work items added to project (Old navigation)

## Track initiative progress within a large Jira project

|  |  |
| --- | --- |
| **Goal** | Use JQL query and labels features under **Additional filters for work items** to choose specific work items from a Jira space or spaces. |
| **Scenario** | In organizations that use a single large Jira space, a common requirement is to track the progress and constituent parts of specific high-level initiatives.  These initiatives are typically represented as standard Jira work items within the overarching space. Stakeholders often need a consolidated view that includes the initiative itself, the significant pieces of work that consist of it (usually represented as epics), and the detailed tasks (stories) associated with those epics. |
| **Key benefits** | This JQL query provides a focused view on a specific initiative within a large Jira project by displaying:   - The initiative issue itself. - All the direct child epics of that initiative. - The stories (and other linked issues) belong to a pre-selected list of epics, likely representing the epics currently being actively worked on.   This approach allows for a structured and manageable way to monitor the progress of key initiatives within a complex Jira environment. |

### Preconditions

- app user You were granted the [App User role](/cms_trial/space/SPM/1918535770/App-level+permissions/) (to open BigPicture)
- box admin You were granted a [Box Admin](/cms_trial/space/SPM/1918797447/Box-level+permissions/) role of the Home box / the required box (to access box configuration)

### Track initiative progress within a large Jira space step-by-step

1. Choose your box (or create a new one).
2. Go to **Box configuration** > **Tasks** > **Scope definition**.
3. Create a JQL query in the **JQL query** field under **Additional filters for work items**.

![Additional filters for work items section.](/cms_trial/assets/4dfc5a2b-c47f-4da8-a4f1-1885365c4c5e.png)

Example query:  
To address this need, the following JQL query can be employed to narrow down the tasks:  
`key in (TEST-87503) or parent in (TEST-87503) or "Epic Link" in (TEST-99748, TEST-91798, TEST-96542, TEST-91799, TEST-29059, TEST-22245, TEST-54368, TEST-96389, TEST-96543)`

1. Click the **Save** button.

#### **Query elements and functions**

This query leverages three primary clauses connected by the logical operator `OR`, meaning an issue will be included in the results if it satisfies any of the specified conditions:

1. `key in (TEST-87503)`:

   - Function: This clause directly retrieves the Jira issue with the key "TEST-87503". This issue represents the central initiative to track in this business case.
2. `parent in (TEST-87503)`:

   - Function: This clause retrieves all direct child issues of the issue with the key "TEST-87503". In the context of tracking an initiative, these child issues are the epics that constitute the major deliverables or phases of the initiative. It's important to note that this clause only retrieves the immediate children and does not recursively include further nested issues like stories or sub-tasks of these epics.
3. `"Epic Link" in (TEST-99748, TEST-91798, TEST-96542, TEST-91799, TEST-29059, TEST-22245, TEST-54368, TEST-96389, TEST-96543)`:

   - Function: This clause retrieves all Jira issues linked to the specific epics identified by the provided keys through the **Epic Link** field. In this business scenario, this part of the query is used to specifically pull in the stories (and potentially other issue types linked to an epic) for a select group of epics. This targeted approach allows stakeholders to focus on the detailed work being done within the epics currently in progress or of particular interest, without being overwhelmed by the stories of all epics related to the initiative.

## Track selected epics and their related work

|  |  |
| --- | --- |
| **Goal** | Use the **JQL query** option to filter epics along with their stories and subtasks. |
| **Scenario** | In large Jira projects, teams often need to focus on a select set of key epics and their associated tasks, rather than the entire project scope. This targeted approach is beneficial for focusing on specific features, addressing customer requirements, or achieving strategic objectives. |
| **Key benefits** | - Focus only on relevant epics and their context. - Avoid clutter from unrelated issues. - Ideal for tracking cross-functional work or custom workflows that don’t rely on the standard Jira hierarchy. |

### Preconditions

- app user You were granted the [App User role](/cms_trial/space/SPM/1918535770/App-level+permissions/) (to open BigPicture).
- box admin You were granted a [Box Admin](/cms_trial/space/SPM/1918797447/Box-level+permissions/) role of the Home box / the required box (to access box configuration).

### Track selected epics and their related work step-by-step

1. Choose your box (or create a new one).
2. Go to **Box configuration** > **Tasks** > **Scope definition**.
3. Create a JQL query in the **JQL query** field under **Additional filters for work items**. Example query:  
   `linkedIssue in (TEST-01, TEST-02, TEST-03)`

### Query elements and functions

- Fetches all issues linked to the specified epics (TEST-01, TEST-02, TEST-03).
- Includes related stories, sub-tasks, or any other issues connected using issue links (like `relates to` or `blocks`).
- Useful when work is associated by issue links, not just the **Epic Link** field.

## **Create a task structure for Jira Standard**

|  |  |
| --- | --- |
| **Goal** | To create a task structure based on the **JQL query** option and the Custom Structure Builder. |
| **Scenario** | In Jira Standard, users are limited to a fixed hierarchy in which epics are the highest level (unlike Jira Cloud Premium, which allows additional custom hierarchy levels).  However, BigPicture enables users to create a flexible hierarchy by leveraging issue links. By narrowing the scope to a specific project and filtering issues connected by `is child of` or `is parent of` links, teams can define a custom structure that reflects their actual work relationships. |
| **Key benefits** | This approach allows users of Jira Standard to:   - Build a hierarchy that extends beyond the built-in epic level - Organize work items based on custom parent-child relationships - Visualize and manage this structure using BigPicture’s Custom Structure Builder.   It’s an effective solution for teams needing structured planning without access to advanced Jira hierarchy features. |

### Preconditions

- app user You were granted the [App User role](/cms_trial/space/SPM/1918535770/App-level+permissions/) (to open BigPicture)
- box admin You were granted a [Box Admin](/cms_trial/space/SPM/1918797447/Box-level+permissions/) role of the Home box / the required box (to access box configuration)

### **Create a task structure for Jira Standard** step-by-step

1. Choose your box (or create a new one).
2. Go to **Box configuration** > **Tasks** > **Work items from Jira**.
3. Create a JQL query in the **JQL query** field under **Additional filters for work items**. Example query:  
   `project = <project_name> AND issueLinkType in (“is child of”, "is parent of")`
4. Once the scope is defined, [apply a Custom Structure Builder in the Box configuration](/cms_trial/space/SPM/2400551350/Use+case%3A+Build+a+task+structure+with+custom+links+(%27is+child+of%27+%2F+%27is+parent+of%27)/) to visualize and manage the hierarchy based on these link types.

### **Query elements and functions**

- `project = <project_name>`  
   Filters work items to a specific Jira spacet.
- `issueLinkType in (“is child of”, "is parent of")`  
   Retrieves work items connected by parent-child relationships via issue links.

## Define the box scope by filtering with labels

| **Goal** | To configure a BigPicture Box to automatically include all tasks from potentially different Jira spaces that are tagged with a specific label. |
| --- | --- |
| **Scenario** | Imagine your organization is working on a cross-product initiative called *Customer Onboarding Improvement*. Tasks related to this initiative are spread across multiple Jira projects (for example, *Product A Development*, *Product B Development*, *Marketing Initiatives*). All tasks related to this initiative are consistently tagged with the label `onboarding-improvement`.  You want to create a BigPicture Box to track and manage all tasks associated with the `onboarding-improvement` initiative in a single central place, regardless of which project they belong to. |
| **Key benefits** | - Cross-Project Visibility: Easily aggregate and manage tasks related to a specific theme or initiative that span across different Jira projects. - Flexible Categorization: Labels provide a simple and flexible way to categorize tasks in Jira, which can then be directly used to define Box scopes in BigPicture. - Dynamic Scope: As tasks are labeled or unlabeled in Jira, the Box scope automatically updates during synchronization. - Focused Management: The Box provides a centralized view for managing all work related to the labeled initiative, improving focus and coordination.   By utilizing label filtering in your Box scope definition, you can create dynamic and focused Boxes in BigPicture that align with your organization's initiatives and how you categorize work in Jira. |

### Preconditions

- app user You were granted the [App User role](/cms_trial/space/SPM/1918535770/App-level+permissions/) (to open BigPicture)
- box admin You were granted a [Box Admin](/cms_trial/space/SPM/1918797447/Box-level+permissions/) role of the Home box / the required box (to access box configuration)

### Define the box scope by filtering with labels step-by-step

1. **Choose your box** (or create a new one).
2. Go to **Box configuration** > **Tasks** > **Scope definition**.
3. Create a JQL query in the **JQL query** field under **Additional filters for work items**:  
   `labels = onboarding-improvement`

Alternatively, add the label to the **Label** field.

## Use case: Filter Jira work items added to project (New navigation)

## Track initiative progress within a large Jira project

|  |  |
| --- | --- |
| **Goal** | Use JQL query and labels features under **Additional filters for work items** to choose specific work items from a Jira space or spaces. |
| **Scenario** | In organizations that use a single large Jira space, a common requirement is to track the progress and constituent parts of specific high-level initiatives.  These initiatives are typically represented as standard Jira work items within the overarching space. Stakeholders often need a consolidated view that includes the initiative itself, the significant pieces of work that consist of it (usually represented as epics), and the detailed tasks (stories) associated with those epics. |
| **Key benefits** | This JQL query provides a focused view on a specific initiative within a large Jira project by displaying:   - The initiative issue itself. - All the direct child epics of that initiative. - The stories (and other linked issues) belong to a pre-selected list of epics, likely representing the epics currently being actively worked on.   This approach allows for a structured and manageable way to monitor the progress of key initiatives within a complex Jira environment. |

### Preconditions

- app user You were granted the [App User role](/cms_trial/space/SPM/1918535770/App-level+permissions/) (to open BigPicture)
- box admin You were granted a [Box Admin](/cms_trial/space/SPM/1918797447/Box-level+permissions/) role of the Home box / the required box (to access box configuration)

### Track initiative progress within a large Jira space step-by-step

1. Choose your box (or create a new one).
2. Go to **Box configuration** > **Tasks** > **Work items from Jira**.
3. Create a JQL query in the **JQL query** field under **Additional filters for work items**.

![Additional filters for work items section.](/cms_trial/assets/4dfc5a2b-c47f-4da8-a4f1-1885365c4c5e.png)

Example query:  
To address this need, the following JQL query can be employed to narrow down the tasks:  
`key in (TEST-87503) or parent in (TEST-87503) or "Epic Link" in (TEST-99748, TEST-91798, TEST-96542, TEST-91799, TEST-29059, TEST-22245, TEST-54368, TEST-96389, TEST-96543)`

1. Click the **Save** button.

#### **Query elements and functions**

This query leverages three primary clauses connected by the logical operator `OR`, meaning an issue will be included in the results if it satisfies any of the specified conditions:

1. `key in (TEST-87503)`:

   - Function: This clause directly retrieves the Jira issue with the key "TEST-87503". This issue represents the central initiative to track in this business case.
2. `parent in (TEST-87503)`:

   - Function: This clause retrieves all direct child issues of the issue with the key "TEST-87503". In the context of tracking an initiative, these child issues are the epics that constitute the major deliverables or phases of the initiative. It's important to note that this clause only retrieves the immediate children and does not recursively include further nested issues like stories or sub-tasks of these epics.
3. `"Epic Link" in (TEST-99748, TEST-91798, TEST-96542, TEST-91799, TEST-29059, TEST-22245, TEST-54368, TEST-96389, TEST-96543)`:

   - Function: This clause retrieves all Jira issues linked to the specific epics identified by the provided keys through the **Epic Link** field. In this business scenario, this part of the query is used to specifically pull in the stories (and potentially other issue types linked to an epic) for a select group of epics. This targeted approach allows stakeholders to focus on the detailed work being done within the epics currently in progress or of particular interest, without being overwhelmed by the stories of all epics related to the initiative.

## Track selected epics and their related work

|  |  |
| --- | --- |
| **Goal** | Use the **JQL query** option to filter epics along with their stories and subtasks. |
| **Scenario** | In large Jira projects, teams often need to focus on a select set of key epics and their associated tasks, rather than the entire project scope. This targeted approach is beneficial for focusing on specific features, addressing customer requirements, or achieving strategic objectives. |
| **Key benefits** | - Focus only on relevant epics and their context. - Avoid clutter from unrelated issues. - Ideal for tracking cross-functional work or custom workflows that don’t rely on the standard Jira hierarchy. |

### Preconditions

- app user You were granted the [App User role](/cms_trial/space/SPM/1918535770/App-level+permissions/) (to open BigPicture).
- box admin You were granted a [Box Admin](/cms_trial/space/SPM/1918797447/Box-level+permissions/) role of the Home box / the required box (to access box configuration).

### Track selected epics and their related work step-by-step

1. Choose your box (or create a new one).
2. Go to **Box configuration** > **Tasks** > **Work items from Jira**.
3. Create a JQL query in the **JQL query** field under **Additional filters for work items**. Example query:  
   `linkedIssue in (TEST-01, TEST-02, TEST-03)`

### Query elements and functions

- Fetches all issues linked to the specified epics (TEST-01, TEST-02, TEST-03).
- Includes related stories, sub-tasks, or any other issues connected using issue links (like `relates to` or `blocks`).
- Useful when work is associated by issue links, not just the **Epic Link** field.

## **Create a task structure for Jira Standard**

|  |  |
| --- | --- |
| **Goal** | To create a task structure based on the **JQL query** option and the Custom Structure Builder. |
| **Scenario** | In Jira Standard, users are limited to a fixed hierarchy in which epics are the highest level (unlike Jira Cloud Premium, which allows additional custom hierarchy levels).  However, BigPicture enables users to create a flexible hierarchy by leveraging issue links. By narrowing the scope to a specific project and filtering issues connected by `is child of` or `is parent of` links, teams can define a custom structure that reflects their actual work relationships. |
| **Key benefits** | This approach allows users of Jira Standard to:   - Build a hierarchy that extends beyond the built-in epic level - Organize work items based on custom parent-child relationships - Visualize and manage this structure using BigPicture’s Custom Structure Builder.   It’s an effective solution for teams needing structured planning without access to advanced Jira hierarchy features. |

### Preconditions

- app user You were granted the [App User role](/cms_trial/space/SPM/1918535770/App-level+permissions/) (to open BigPicture)
- box admin You were granted a [Box Admin](/cms_trial/space/SPM/1918797447/Box-level+permissions/) role of the Home box / the required box (to access box configuration)

### **Create a task structure for Jira Standard** step-by-step

1. Choose your box (or create a new one).
2. Go to **Box configuration** > **Tasks** > **Work items from Jira**.
3. Create a JQL query in the **JQL query** field under **Additional filters for work items**. Example query:  
   `project = <project_name> AND issueLinkType in (“is child of”, "is parent of")`
4. Once the scope is defined, [apply a Custom Structure Builder in the Box configuration](/cms_trial/space/SPM/2400551350/Use+case%3A+Build+a+task+structure+with+custom+links+(%27is+child+of%27+%2F+%27is+parent+of%27)/) to visualize and manage the hierarchy based on these link types.

### **Query elements and functions**

- `project = <project_name>`  
   Filters work items to a specific Jira spacet.
- `issueLinkType in (“is child of”, "is parent of")`  
   Retrieves work items connected by parent-child relationships via issue links.

## Define the box scope by filtering with labels

| **Goal** | To configure a BigPicture Box to automatically include all tasks from potentially different Jira spaces that are tagged with a specific label. |
| --- | --- |
| **Scenario** | Imagine your organization is working on a cross-product initiative called *Customer Onboarding Improvement*. Tasks related to this initiative are spread across multiple Jira projects (for example, *Product A Development*, *Product B Development*, *Marketing Initiatives*). All tasks related to this initiative are consistently tagged with the label `onboarding-improvement`.  You want to create a BigPicture Box to track and manage all tasks associated with the `onboarding-improvement` initiative in a single central place, regardless of which project they belong to. |
| **Key benefits** | - Cross-Project Visibility: Easily aggregate and manage tasks related to a specific theme or initiative that span across different Jira projects. - Flexible Categorization: Labels provide a simple and flexible way to categorize tasks in Jira, which can then be directly used to define Box scopes in BigPicture. - Dynamic Scope: As tasks are labeled or unlabeled in Jira, the Box scope automatically updates during synchronization. - Focused Management: The Box provides a centralized view for managing all work related to the labeled initiative, improving focus and coordination.   By utilizing label filtering in your Box scope definition, you can create dynamic and focused Boxes in BigPicture that align with your organization's initiatives and how you categorize work in Jira. |

### Preconditions

- app user You were granted the [App User role](/cms_trial/space/SPM/1918535770/App-level+permissions/) (to open BigPicture)
- box admin You were granted a [Box Admin](/cms_trial/space/SPM/1918797447/Box-level+permissions/) role of the Home box / the required box (to access box configuration)

### Define the box scope by filtering with labels step-by-step

1. **Choose your box** (or create a new one).
2. Go to **Box configuration** > **Tasks** > **Scope definition**.
3. Create a JQL query in the **JQL query** field under **Additional filters for work items**:  
   `labels = onboarding-improvement`

Alternatively, add the label to the **Label** field.