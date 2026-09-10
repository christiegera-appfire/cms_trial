# Create box

## Create a new box (old navigation)

Click to expand the guide

You can create a new box in multiple ways. You can find detailed instructions on the following pages:

- [Create box in the Overview module](/cms_trial/space/SPM/1918538558/Create+box+in+the+Overview+module/)
- [Create box from Jira space](/cms_trial/space/SPM/1918800104/Create+box+from+Jira+space/)
- [Play with sample data](/cms_trial/space/SPM/2530541787/Play+with+sample+data/)
- [Create box in the App widget](/cms_trial/space/SPM/2533720090/Create+box+in+the+App+widget/)

## Box creation: Rules

Before you start creating a new box, keep these key rules in mind.

### Box creation validation

Boxes can create hierarchies. Before you create a new box, make sure the parent-child relationships you're trying to create are valid.

The following things determine how you can nest boxes:

- In the [box type configuration](https://appfire.atlassian.net/wiki/spaces/SPM/pages/1918829342), you decide the possible parents of each Box type. [Parent box types](/cms_trial/space/SPM/1918830000/Box+types/) determine how to build the box hierarchy (nest boxes) and prevent users from making mistakes and mixing methodologies
- Each Box type has [scope type](/cms_trial/space/SPM/1918766536/Scope+types/) settings (None, Own scope, Sub-scope)
- [Sequentiality](/cms_trial/space/SPM/1918669073/Period+mode+and+sequentiality/) (box type settings)
- [Box period mode](/cms_trial/space/SPM/1918669073/Period+mode+and+sequentiality/)

### Possible parent box types

Parent Box types determine how you can build the Box hierarchy.

![View of settings, Iteration, Parent Types](/cms_trial/assets/d3f4ff63-717f-4d1c-86cf-0333736b59d6.png)

### Scope type

How the scope types affect box nesting:

![A table presenting scope settings](/cms_trial/assets/2a894e1e-d617-4381-940b-fd43dcb9260d.png)

### Sequentiality

Sequentiality settings affect same-level Boxes (can potentially prevent box periods from overlapping).

**Auto bottom-up** and **auto scope-based** boxes are never sequential - they can always overlap.

Only "**manual**" and "**auto top-down**" Boxes can be sequential—if set to 'sequential,' same-level sequential Boxes can't overlap.

![Validation error when adding a new box](/cms_trial/assets/0d945678-00fe-4a3b-a25d-88c99bb7f05f.png)

### Period mode

Box type period mode can affect if a new child Box can be created with a specified start/date.

#### Period of a new box vs. child box period mode

Newly created boxes don't have any children, so they can't be affected by them.

#### Period of a new box vs. parent box period mode

- **An "auto top-down" parent** →

  - **limits the period of an "auto top-down" child box**
  - child boxes in "manual"/ "auto scope-based" period mode are not affected
  - "auto bottom-up" child overrides an "auto top-down" parent

Effects of the parent box period mode on a child Box period are outlined in the table below.

| **Parent Box →** | **New Box (child)** |
| --- | --- |
| auto bottom-up | unaffected (regardless of child period mode) |
| auto scope-based | unaffected (regardless of child period mode) |
| auto top-down | **An "auto top-down" parent limits the period of an "auto top-down" child** Period of an "auto bottom-up" child is unaffected ("auto bottom-up" child has priority over an auto "top-down parent") Periods of "manual" and "auto scope-based" Boxes unaffected |
| manual | unaffected (regardless of child period mode) |

## Create a new box (new navigation)

Click to expand the guide

You can create a new box in multiple ways. Detailed instructions can be found on the following pages:

- [Create box in the Overview module](/cms_trial/space/SPM/1918538558/Create+box+in+the+Overview+module/)
- [Create box from Jira space](/cms_trial/space/SPM/1918800104/Create+box+from+Jira+space/)
- [Play with sample data](/cms_trial/space/SPM/2530541787/Play+with+sample+data/)
- [Create box in the App widget](/cms_trial/space/SPM/2533720090/Create+box+in+the+App+widget/)

## Box creation: Rules

With boxes, you can build complex box hierarchies.

Before you create a new box, make sure the parent-child relationships you are trying to form are valid.

The following aspects determine whether you can or cannot nest boxes of one type under another:

- [Parent box types](/cms_trial/space/SPM/1918830000/Box+types/) - you can nest a child box only under a parent box. Hierarchies cannot be formed without parents. This guards from making mistakes and mixing methodologies.
- [Scope type](/cms_trial/space/SPM/1918766536/Scope+types/) - each box has one specific scope type (None, Own scope, Sub-scope) that allows or prevents nesting under specific scope types.
- [Sequentiality](/cms_trial/space/SPM/1918669073/Period+mode+and+sequentiality/) controls the logical order in which boxes are organized.
- [Box period mode](/cms_trial/space/SPM/1918669073/Period+mode+and+sequentiality/) affects box start/end dates, which in turn can affect child boxes.

### Possible parent box types

Parent box types determine which box type can be a parent box, so that you can build the box hierarchy.

![Parent type settings for an Iteration box.](/cms_trial/assets/f276a07b-d30f-401d-8ab6-ac76e45e89e8.png)

### Scope type

Box scope types also affect box nesting.

![A table presenting scope settings](/cms_trial/assets/2a894e1e-d617-4381-940b-fd43dcb9260d.png)

### Sequentiality

Sequentiality settings affect same-level boxes (which can potentially prevent box periods from overlapping).

**Auto bottom-up** and **auto scope-based** boxes are never sequential; they can always overlap.

Only the boxes in the **manual** and **auto top-down** period modes can be sequential. If the boxes are set to **sequential**, then the same-level boxes cannot overlap.

![Validation error when adding a new box](/cms_trial/assets/0d945678-00fe-4a3b-a25d-88c99bb7f05f.png)

### Period mode

A box type period mode can affect whether a new child box can be created with a specified start/date.

#### Period of a new box vs. child box period mode

Newly created boxes have no children, so they cannot be affected by them.

#### Period of a new box vs. parent box period mode

- An **auto top-down** parent →

  - limits the period of an **auto top-down** child box**.**
  - child boxes in the **manual**/ **auto scope-based** period mode are not affected.
  - **auto bottom-up** child overrides an **auto top-down** parent.

The effects of the parent box period mode on the child box period are outlined in the table below.

| **Parent Box →** | **New Box (child)** |
| --- | --- |
| Auto bottom-up | Unaffected (regardless of the child's period mode) |
| Auto scope-based | Unaffected (regardless of the child’s period mode) |
| Auto top-down | - An **auto top-down** parent limits the period of an **auto top-down** child. - The period of an **auto bottom-up** child is unaffected (an **auto bottom-up** child has priority over an **auto top-down parent**). - Periods of the **manual** and **auto scope-based** boxes are unaffected. |
| Manual | Unaffected (regardless of child period mode) |