# Filter by project and issue type

## Problem

When using listeners, it is often required that the listener responds to specific events only. The most common ways to filter these events are by the project the issue belongs to and the issue type for the issue.

## Solution

To solve this problem, the listener configuration within Power Scripts has settings which can be used to specify when the filter should fire based on project and issue type.

### Step 1: Create a new listener

1. Navigate to the listeners configuration page by going to **Power Apps Config > Power Scripts > Listeners**
2. Click the **Add listener** button

   ![Power Scripts for Jira Cloud project filter configuration](/cms_trial/assets/640a4423-7a1e-4824-b4d6-559fd2fc967c.png)

### Step 2: Configure the listener

1. After selecting a script for the listener, choose the event the listener should respond to. Only issue specific events like Issue Created, Issue Updated, etc. can then be filtered by project and issue type.

   ![Power Scripts for Jira Cloud issue type filter settings](/cms_trial/assets/75a330f3-184d-402d-8e01-80ba3fc4392f.png)
2. After selecting an issue specific event the input form will update with the new controls for filtering:

   ![Power Scripts for Jira Cloud filtered configuration panel](/cms_trial/assets/7c65ee84-0d34-4252-9a0d-0d5ab11f0017.png)
3. The project and/or issue type filters can then be applied:

   ![Power Scripts for Jira Cloud project and issue type selection](/cms_trial/assets/ebef27d9-36fd-4672-be6a-03c2310c9bb5.png)
4. Click the **Add** button to complete the setup of the listener

Note:

- Both the project and issue type filters can be set independently, they are not needed together
- Multiple projects can be added to the project filter
- Multiple issue types can be added to the issue type filter