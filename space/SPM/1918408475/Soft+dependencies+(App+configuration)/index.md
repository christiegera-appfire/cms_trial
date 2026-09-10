# Soft dependencies (App configuration)

## Security and access

Only Jira administrators can access this page.

1. Click the **wrench** icon at the top right and select**General** from the drop-down list.
2. Next, go to **Dependencies** > **Soft dependencies**.

   ![image-20250211-131858.png](/cms_trial/assets/fe66efb0-e55a-428b-9644-1ceebbb4d1d2.png)

## About soft dependencies

**Soft links field**→ you can add multiple Jira link types into the box. All added link types will be visualized in BigPicture as soft dependencies. This field works unidirectionally (all added link types are visualized in BigPicture as soft links).

![image2022-2-14_10-3-49.png](/cms_trial/assets/c0b159ba-e71c-4435-88c3-c6c51ae1b371.png)

**Default soft link**→ when you create a new soft link in BigPicture (for example, in the Board module), a corresponding link is created in Jira. For example, if the "Blocks" link type is selected, each time you make a soft dependency in BigPicture, a "Blocks" Jira link is added for the relevant issues.

![contentId-1918408475](/cms_trial/assets/028d2cd7-d521-42d8-b11e-21e1a9ae8846.png)

The two auto period modes (Auto Top-Down/ Auto Bottom-Up) available in the app work best with default custom links added by the App. If you decide to change the default links, switch to the manual period mode to avoid unintended rescheduling of the tasks.