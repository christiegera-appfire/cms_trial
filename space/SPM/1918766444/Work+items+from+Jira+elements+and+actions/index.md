# Work items from Jira elements and actions

## Work items from Jira elements

### Scope of the context box

The scope of the box you're configuring can be managed at the top part of the page.

If the box you're configuring has scope set to **Own**, you can modify the scope definition details at the top of the page.

![Screenshot of the Work items from Jira tab in the box configuration.](/cms_trial/assets/b4786378-60b2-4c5d-9f0d-9a062387ca59.png)

If the box you're configuring has scope set to **Sub-scope**, you can modify the synchronization rules.

![Scope definition page of the Sub-scope type of the box scope.](/cms_trial/assets/6c18a44f-b26e-4e6b-8c36-b86a6110550a.png)

### Scope of the sub-boxes

Scope information of boxes nested under the box you are currently configuring can be found at the bottom part of the page:

![work-items.png](/cms_trial/assets/e2d0e4d5-0dc2-4ad2-9f3c-e8e8ebac6323.png)

Depending on the scope type of a child box, you will see:

When a child box is set to be a **Sub-scope,** you will see synchronization rules:

![sub-scope.png](/cms_trial/assets/bf078d89-b6ca-41ae-afb7-138c6529be46.png)

You will be informed when a child box has its **Own** scope. The link in the message will take you directly to the configuration page for the relevant box scope.

![work-items-own.png](/cms_trial/assets/8d3a4710-10c5-458a-8645-5101c85ecc73.png)

When a child box functions as a portfolio and has a scope set to **None**, you will see the following message:

![work-items-none-3.png](/cms_trial/assets/b57f2d43-712a-4e09-a952-82f4c8715555.png)

### Switch between levels of child boxes

Use the arrows to switch between viewing the level of children and grandchildren of a given box.

![navigation-arrows.png](/cms_trial/assets/e22792fb-0132-4bed-b699-c4fc6d4bef61.png)![navigation-arrows-2.png](/cms_trial/assets/c1218765-82d2-4f62-8ae6-1c86df646615.png)

### Basic info and status of child boxes

You can check basic information about a sub-box and change its status directly from the scope configuration page of a box.

![basic-info-on-tasks.png](/cms_trial/assets/e674ee1e-00ae-415f-b53f-d447725c67f9.png)

[unmapped inline: placeholder]

### Manually added tasks

This option displays tasks that exist in the box but were not included by the automatic rules outlined in the previous section. This task might have been added manually, or they are present here unintentionally. If you would rather keep in the box only tasks chosen by automatic rules, you can:

- Move the tasks from this section to the right project (chosen in the previous section)
- Modify the automatic rules in the previous section to also include the tasks from the manually added task
- Click the X next to a specific task to exclude it from the scope.

## Save the scope

The App validates the scope. Saving the scope fails if errors occur.

If you define the scope correctly (all tasks exist, and the filters are not corrupted), the total number of tasks will be displayed.

You will not be able to save the scope if one of the following occurs:

- At least one item in the scope definition is incorrect or doesn't exist (for example, JQL Query is incorrect, Scope Owner doesn't exist, added Project doesn't exist, etc)
- Private filters are used - the App doesn’t detect private filters.
- The total number of tasks exceeds the task limit set for boxes.

## Update the scope

When you update the scope definition, the synchronization will be performed in the background. You can track the progress once you click the box icon in the top left corner.

![Scope synchronization animation.](/cms_trial/assets/62d8d2f4-420f-4d86-94e5-6d4a8d1e1d8e.png)

The synchronization status is displayed in detail in a new window, where you can see the synchronization status in detail. To implement changes, click **Manage scope definition**.

Once you save changes, the synchronization stops and starts again from the beginning for the new scope.

![Scope synchronization details and progress.](/cms_trial/assets/a9eea6d5-54b5-4fb6-b33f-7fb9f8aedabe.png)

## Duplicated tasks

When a task is added manually and updated to fit the filter described in the Automatic rules section, it will be classified as a duplicate (alternatively, when the automatic rules are updated and the manually added task now fits the filtering criteria).

## Refresh search list

The **Refresh search list** option on the scope definition page is available only on Jira Cloud.

The **Refresh search list** option is useful when you cannot find the project, board, or quick filters on the scope definition page. After pressing the **Refresh search list** button, the screen is disabled for 5 seconds. The option refreshes only projects, boards, and quick filters.

![refresh.png](/cms_trial/assets/a432b7d5-204f-408e-824b-347de04f8d6d.png)

## Scope misconfiguration errors and warnings

See the <https://appfire.atlassian.net/wiki/spaces/SPMDRAFT/pages/1858699732/Scope+misconfiguration+errors+and+warnings?force_transition=2abc0438-43c2-4bf7-a66e-6a7b04713703> page for more information.