# Troubleshooting: I opened BigPicture and didn't see any boxes

## Problem

- A BigPicture user opens the app but doesn’t see any boxes.
- Or, a BigPicture user opens a box and only sees a subset of the boxes that are available.

## Solution

- In both scenarios, box Roles are assigned to users, granting the appropriate permissions to access the appropriate boxes in BigPicture.
- Who can solve the problem? app admin jira admin box admin
- Where to solve it? **Configuration** > **Security**

## Detailed steps

### Scenario 1: No boxes display

In the first example, an admin opens BigPicture through the Jira **Apps** menu and, instead of seeing boxes, the following page displays:

![A user opens BigPicture from the Apps menu.](/cms_trial/assets/ade9e83a-ec59-4b81-86bd-b309e18abd23.png)

![After opening the app, no Boxes display in BigPicture.](/cms_trial/assets/86d02b60-ea5c-41e0-943c-f6c23627f8e7.png)

Use the following steps to grant the **box Admin** role to the admin.

1. From the **Overview** module, make sure the Home box is displayed.

   ![Display the Home box in the Overview module.](/cms_trial/assets/3e8c6e8b-26df-4388-9c94-d4bebcc86f66.png)
2. Select **Configuration** from the Module Switcher dropdown.

   ![Open the Module Switcher and select Configuration.](/cms_trial/assets/c4f917e7-0e1e-4701-8e8d-84ce518e0794.png)
3. In the left-hand pane, select **Security** > **Security**.
4. In this example, assume the user is an admin and should have full access to all BigPicture boxes. Expand **box Admin** > **Users**.
5. In the **Users** dropdown, enter the first few letters of the admin’s name.
6. After locating the admin, enter a checkmark next to their name.

   ![Locate the admin in the Users dropdown and enter a checkmark next to their name.](/cms_trial/assets/df58d49c-6e0a-40db-933d-80afb9fd455f.png)
7. When the admin reloads the *Overview* module, all boxes display.

   ![The admin now sees all Boxes in the Overview module.](/cms_trial/assets/6350b2b5-d81d-42eb-894b-ffa55e24cebf.png)

The assigned user displays as a box Admin under the Home box. However, the user will not be displayed if you open the box Admin role for any sub-box. This is because box Roles are inherited.

### Scenario 2: Only one box displays

In the second example, a software company's product manager opens BigPicture from the Jira **Apps** menu and sees one box, but it’s not the one from their project. In the screenshot below, the Alpha box displays. However, Inventory Management is the box the Product Manager wants to work with.

![The only box that displays is Alpha.](/cms_trial/assets/279a908c-930c-488e-a1e4-d9c76aa13157.png)

Use the following steps to grant the box Editor role to the Product Manager for the Inventory Management box:

1. From the **Overview** module, make sure the Home box is displayed.

   ![Display the Inventory management box in the Overview module.](/cms_trial/assets/c2e28d73-5e9f-4d2e-981c-921b4705e774.png)
2. Select **Configuration** from the Module Switcher dropdown.
3. In the left-hand pane, select **Security** > **Security**.
4. In this example, expand **box Admin** > **Users**.
5. In the **Users** dropdown, enter the first few letters of the product manager’s name.
6. After locating the product manager, enter a checkmark next to their name.

   ![Locate the admin in the Users dropdown and enter a checkmark next to their name.](/cms_trial/assets/df58d49c-6e0a-40db-933d-80afb9fd455f.png)
7. When the product manager reloads the *Overview* module, the Inventory Management box displays.

   ![image-20250417-192555.png](/cms_trial/assets/7af307ea-4b22-4079-a1b1-38a725b8cd98.png)

If the product manager should *not* have access to the Alpha box, open that box in the *Overview* module, go to **Configuration**, and remove their box Role for the Alpha box.

### Learn more

- [BigPicture security and permissions in Jira](/cms_trial/space/SPM/1918667044/BigPicture+security+and+permissions+in+Jira/)
- [Box security roles](/cms_trial/space/SPM/1918668158/Box+security+roles/)
- [Concept of a box](/cms_trial/space/SPM/1918404963/Concept+of+a+box/)
- [Box hierarchy](/cms_trial/space/SPM/1918535907/Box+hierarchy/)
- [Navigate between boxes (box switcher)](/cms_trial/space/SPM/1918667414/Navigate+between+boxes+(box+switcher)/)
- [Inheritance mode](/cms_trial/space/SPM/1918700886/Inheritance+mode/)