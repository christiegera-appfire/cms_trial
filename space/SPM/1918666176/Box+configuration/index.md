# Box configuration

## Box type vs box configuration

**Box type** settings contain the default settings applicable to multiple boxes (all boxes of a given type). Those settings are adjusted in **App Administration**. To check the settings that are only box type specific, go to [Box types](/cms_trial/space/SPM/1918830000/Box+types/).

See an interactive demo on how to access the box type settings.

**Box settings** refer to the settings of a single, individual box. They are dependent on the box type settings.

See an interactive demo on how to access the box settings.

## Access and security

Box type settings can be accessed and modified by:

- App admins

Box settings can be accessed and modified by:

- Box admins
- Jira admins (every Jira admin has full access to the App and can edit the configuration of boxes)
- BigPicture admins

## Configuration overview

Some setting pages are nearly identical for both box types and individual boxes. The table below highlights settings that are mostly the same for both.

Since box type settings apply to all boxes of a given type, App admins can configure additional options like inheritance mode, default quick filters, default column, or default card views.

Click the selected feature to be redirected to a full page.

| **Feature** | **Box type configuration** | **Box configuration** |
| --- | --- | --- |
| [Available modules](/cms_trial/space/SPM/1918503298/Define+available+modules/) | For a box type (all boxes of a given type), you can configure:   - Available modules   Go to the **App Administration** > **Box type** > **choose the box type you want to edit** > **General** > **Modules**. image-20250327-083059.png | For a particular box, you can configure:   - Available modules   Go to **box configuration** > **General** > **Modules**. contentId-1918666176 |
| [Task structure](/cms_trial/space/SPM/1918667217/Manage+task+structure/) | For a box type (all boxes of a given type), you can configure:   - Default task structure - Advanced configuration   Go to the **App Administration** > **Box type** > **choose the box type you want to edit** > **Tasks** > **Task structure**. image-20250327-084049.png | For a particular box, you can configure:   - Box task structure - Advanced configuration   Go to **box configuration** > **Tasks** > **Task structure**. image-20250327-084155.png |
| [Scheduling](/cms_trial/space/SPM/1918667098/Configure+task+scheduling/) | For a box type (all boxes of a given type), you can configure:   - Default box scheduling mode   Go to the **App Administration** > **Box type** > **choose the box type you want to edit** > **Tasks** > **Scheduling**. contentId-1918666176 | For a particular box, you can configure:   - Box scheduling mode - [Task period alignment](/cms_trial/space/SPM/1918830096/Define+task+period+alignment/)   Go to **box configuration** > **Tasks** > **Scheduling**. image-20250327-083713.png |
| [Workload contouring](/cms_trial/space/SPM/1918831697/Set+workload+contouring+mode/) | For a box type (all boxes of a given type), you can configure:   - Default workload contouring mode   Go to the **App Administration** > **Box type** > **choose the box type you want to edit** > **Tasks** > **Workload contouring**. Box type configuration page. | For a particular box, you can configure:   - Box workload contouring mode   Go to **box configuration** > **Tasks** > **Workload contouring**. image-20250327-084640.png |
| [Quick filters](/cms_trial/space/SPM/1918830532/Manage+quick+filters/) | For a box type (all boxes of a given type), you can configure:   - [Inheritance mode](/cms_trial/space/SPM/1918700886/Inheritance+mode/) - Default quick filters   Go to the **App Administration** > **Box type** > **choose the box type you want to edit** > **Tasks** > **Quick filters**. contentId-1918666176 | For a particular box, you can configure:   - Quick filters   Go to **box configuration** > **Tasks** > **Quick filters**. contentId-1918666176 |
| [Task templates](/cms_trial/space/SPM/1918503892/Manage+task+templates/) | For a box type (all boxes of a given type), you can configure:   - [Inheritance mode](/cms_trial/space/SPM/1918700886/Inheritance+mode/) - Add default task templates   Go to the **App Administration** > **Box type** > **choose the box type you want to edit** > **Tasks** > **Task templates**. contentId-1918666176 | For a particular box, you can add:   - Task templates   Go to **box configuration** > **Tasks > Task templates**. Task templates settings in the box configuration. Alternatively, go to **+Add task** > **Manage templates** in the Gantt, Scope, or Calendar module. Screenshot of adding a new task from a template in the Gantt module. The box configuration page will not be visible if the module was deactivated or the inheritance mode is set to **inherited only**. |
| [Column views](/cms_trial/space/SPM/1918503715/Manage+column+views/) | For a box type (all boxes of a given type), you can configure:   - [Inheritance mode](/cms_trial/space/SPM/1918700886/Inheritance+mode/) - Default column views   Go to the **App Administration** > **Box type** > **choose the box type you want to edit** > **Gantt / Scope** > **Column views**. contentId-1918666176 | For a particular box, you can configure:   - Column views   Go to **box configuration** > **Gantt / Scope** > **Column views**. box-config-gantt-column-views.png Alternatively, you can access the box configuration page directly from the Gantt / Scope module. Navigate to the **Current view** and select the **Manage Column views** from the drop-down menu. Gantt module. |
| [Card views](/cms_trial/space/SPM/1918830445/Manage+card+views/) | For a box type (all boxes of a given type), you can configure:   - [Inheritance mode](/cms_trial/space/SPM/1918700886/Inheritance+mode/) - Default card views   Go to the **App Administration** > **Box type** > **choose the box type you want to edit** > **Board / Risks** > **Card views**. Screenshot of the Card views page in the App Administration. | For a particular box, you can configure:   - Card views   Go to **box configuration** > **Board / Risks** > **Card views**. Screenshot of the Card views page in the box configuration. Alternatively, to access this page, you can click the **Manage card views** button in the **Card view** drop-down of the Board/Risks module. See the video below. |