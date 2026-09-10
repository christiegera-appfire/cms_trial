# Objectives - Business value and associated work

In this section, you can preconfigure the objectives settings of a given box type. These include the following:

- Business value display options
- Objective colors

Changing the configuration might turn off (hide) settings or features in the box configuration and within different modules.

## Business value display options

You can set the default configuration of the **Business value** fields. When enabled, the **Actual Business Value** and **Planned Business Value** fields appear next to the objectives defined in the Objectives module.

The business value should not be confused with other measures, such as the associated effort or total story points associated with an objective. The field values range from 0 to 10 and aren't synchronized with Jira.

Once data is available, the Planned Business Value (PBV) of new objectives scored during the planning meeting can be compared with the Actual Business Value (ABV). This is usually done during the inspection and adapt ceremonies.

The PBV versus ABV ratio can be calculated for each team's objectives and main objectives and rolls up to the team and timebox level.

### Security and access

Only a user with the App admin security role can access and manage the box type configuration.

1. Go to the **App Administration** > **Box type** > **choose the box type you want to edit** > **Objectives** > **Basics**.

![Screenshot of the Basics configuration page for Objectives in App Administration.](/cms_trial/assets/8592cd9a-155b-4cf6-badd-19da010093c1.png)

## Display business value fields

Changes to the default business value configuration apply to all existing boxes of a given type (existing and newly created).

### Main objectives

To enable the Business value fields:

1. Go to the **App Administration** > **Box type** > **choose the box type you want to edit** > **Objectives** > **Basics**.
2. Enable the **Business Value for Main Objectives can be set** option.

![Screenshot of the Basics configuration page for Objectives in App Administration.](/cms_trial/assets/03d87dde-7035-40d1-a646-7fe624293c2e.png)

When enabled, box editors can enter the **Actual Business Value (ABV)** and **Planned Business Value (PBV)** for each timebox.

The field values range from 0 to 10 and aren't synchronized with Jira.

### Team objectives

1. Enable the **Business Value for Team Objectives can be set** option.
2. When enabled, box editors can enter the **Actual Business Value (ABV)** and **Planned Business Value (PBV)** for each team in the timebox.

![objectives-business-values.png](/cms_trial/assets/a854921c-7151-48a5-8450-01488f4595ac.png)

### Associated work

With the **Associated work** option, you can assign tasks to each box objective to easily keep track of work associated with specific goals.

By default, associated work is enabled in all box types.

![Screenshot of the Associated work option in the box-type configuration.](/cms_trial/assets/b3ec7f8d-5be2-48c9-a26d-6f0294c1df02.png)

Settings are adjusted for all boxes of a given type (not for individual boxes).

| **Associated work toggle enabled** | **Associated work toggle disabled** |
| --- | --- |
| When enabled, you can select associated work for an objective in the Objectives module. Screenshot of adding associated work to an objectives in the Objectives module. The associated work is displayed that way. Screenshot of associated work added to an objective in the Objectives module. | When disabled, the associated work data is still stored in the database. Data isn't lost and can be restored once the option is enabled again. |