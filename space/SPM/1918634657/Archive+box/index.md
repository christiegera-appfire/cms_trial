# Archive box

## Archive a box (old navigation)

Click to expand the guide

## Archive a box

You can archive a box manually or have it automated. However, you cannot archive a box that you are currently viewing.

### Manually

Box admins can manually archive a box in the Overview module.

Image — asset pipeline pending  
Archive option in a box configuration

A success message will appear after a [box is archived](/cms_trial/space/SPM/1918405770/Archived+boxes/):

Image — asset pipeline pending  
Archivization confirmation message

Only the [**Own**](/cms_trial/space/SPM/1918766536/Scope+types/) [and](/cms_trial/space/SPM/1918766536/Scope+types/) [**None**](/cms_trial/space/SPM/1918766536/Scope+types/) [scope boxes](/cms_trial/space/SPM/1918766536/Scope+types/) can be manually archived/restored. Relevant sub-boxes are automatically archived with the parent—archiving the parent automatically archives all its children.

#### Limitations

- Boxes have to be archived in functional clusters. You can't archive a parent box with **Own** scope if it has sub-scope child boxes that are still active.
- You can't archive a context box (a box you are currently in)
- Root Box (Home box of the app) cannot be archived

### Automatically

When enabled, the app will check if any user has used a given box or any of its sub-boxes within a specified number of days. If the whole cluster of Boxes has not been used, they will all be automatically archived.

**Box auto-archiving** is enabled by default. Rules regarding the automatic archiving of boxes can be defined and changed in **App Configuration**> **Modules** >[**Overview**](/cms_trial/space/SPM/1918407114/Overview+(App+configuration)/).

Image — asset pipeline pending  
App Configuration

#### Limitations

1. Closed boxes are not automatically archived. If one box in a cluster is "closed," none of the boxes can be archived since they need to be archived simultaneously.
2. The auto-archiving feature is not applied to sequential boxes with their own scope type.

## How to check which boxes will be archived

Go to the **Overview module** of the Home (root) box and check the **Inactive for** column to see when each box was last used.

### Limitations

Closed boxes are not automatically archived. If any box in a cluster is **Closed**, none of the boxes in that cluster can be archived, as they all need to be archived together.

### Restore archived boxes

Archived boxes can only be restored manually.

## Archive a box (new navigation)

Click to expand the guide

## Archive a box

You can archive a box manually or have it automated. However, you cannot archive a box that you are currently viewing.

### Manually

Box Admins can manually archive a box in the Overview module on the Main box level or while in the box they want to archive.

Image — asset pipeline pending  
Archive option on the box options dropdown.

A success message will appear after a [box is archived](/cms_trial/space/SPM/1918405770/Archived+boxes/).

Image — asset pipeline pending  
Archivization confirmation message

Only the [**Own**](/cms_trial/space/SPM/1918766536/Scope+types/) [and](/cms_trial/space/SPM/1918766536/Scope+types/) [**None**](/cms_trial/space/SPM/1918766536/Scope+types/) [scope boxes](/cms_trial/space/SPM/1918766536/Scope+types/) can be manually archived/restored. Relevant sub-boxes are automatically archived with the parent—archiving the parent automatically archives all its children.

#### Limitations

- Boxes have to be archived in functional clusters. You can't archive a parent box with **Own** scope if it has sub-scope child boxes that are still active.
- You can't archive a context box (a box you are currently in)
- Root Box (Home box of the app) cannot be archived

### Automatically

When enabled, the app checks whether any user has used a given box or any of its sub-boxes within a specified number of days. If the whole cluster of Boxes has not been used, they will all be automatically archived.

**Box auto-archiving** is enabled by default. Rules for automatic archiving of boxes can be defined and changed in **App Configuration** > **Modules** > [**Overview**](/cms_trial/space/SPM/1918407114/Overview+(App+configuration)/).

Image — asset pipeline pending  
Box auto-archiving options.

#### Limitations

1. Closed boxes are not automatically archived. If one box in a cluster is "closed," none of the boxes can be archived since they need to be archived simultaneously.
2. The auto-archiving feature is not applied to sequential boxes with their own scope type.

## Check which boxes will be archived

Go to the **Overview module** of the Home (root) box and check the **Inactive for** column to see when each box was last used.

### Limitations

Closed boxes are not automatically archived. If any box in a cluster is **Closed**, none of the boxes in that cluster can be archived, as they all need to be archived together.

### Restore archived boxes

Archived boxes can only be restored manually.