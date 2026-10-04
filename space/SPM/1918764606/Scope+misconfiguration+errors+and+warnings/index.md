# Scope misconfiguration errors and warnings

## X tasks in the scope. Synchronization may take a bit longer...

While trying to save the scope, you might encounter the following warnings:

- "X tasks in the scope. Synchronization may take a bit longer..."

The warning will appear if the task limit in Technical info is not defined or exceeds 25,000 tasks.

- "Scope misconfiguration! A value with ID '10375' does not exist for the field 'id.' user: (...)."  
  In case of **Scope Misconfiguration / Scope corruption**, visit the Scope Misconfiguration - Corrupted Scope page for troubleshooting instructions.

The scope is corrupted:

- A scope element (Jira project, filter, board) ceased to exist - JQL used to define box scope leads to a deleted item
- A scope owner no longer has permission to access at least one of the scope elements.
- A scope owner is no longer active (the user account in the connected tool has been disabled)

## There is a problem with at least one scope element

![contentId-1918764606](/cms_trial/assets/fbda33f0-f04e-4c17-9cae-40818ba46a48.png)

Scope Owner doesn't have access to one of the elements (Board/ Filter/ Project) you have tried to use to define the Box scope.

### Example

The app 'reads' all tasks through the lens of a Scope Owner. A Box can only include tasks to which the Scope owner has at least viewing access.

In the example below, "Tofu" is the Jira user chosen to be a scope owner. User "Tofu" doesn't have permission to access the project added to the scope definition. As a logged-in user, you can have full access to a given item, but if the Scope Owner can't access it, the error will pop up.

![contentId-1918764606](/cms_trial/assets/1837b828-51cb-42c0-874d-8eb48bf63191.png)

### Solutions

#### Change the scope owner

You can use a different user as a scope owner. The new Scope Owner user must have permission to access a given project/filter/board.

#### Change permissions of the item

In the example above, the Project permissions were the problem. Go to project settings:

![image2021-5-26_15-53-36.png](/cms_trial/assets/958199ca-8134-4684-9d11-1434e4778d1f.png)

You have two options.

1. Associate a different scheme with the project.

   ![contentId-1918764606](/cms_trial/assets/4984f9d4-53b0-46ee-8399-10131d990b18.png)
2. Modify the existing permissions scheme.

   ![contentId-1918764606](/cms_trial/assets/baf404f3-f3b5-4008-8182-fbc6beed4cb2.png)