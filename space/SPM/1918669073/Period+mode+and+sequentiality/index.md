# Period mode and sequentiality

Under the **General > Advanced** tab, you can configure the following settings for a given box type.

- Period mode
- Sequentiality
- “Read more” URL

![image-20250313-092710.png](/cms_trial/assets/972d52c4-8703-4492-94a6-c795f02429fe.png)

## Possible settings combinations

The table presents possible combinations of settings for period mode and sequentiality.

| **period mode** | **sequential** | **overlapping allowed** |
| --- | --- | --- |
| auto bottom-up | NO | YES |
| auto scope-base | NO | YES |
| auto top-down | YES | YES |
| manual | YES | YES |

## Period mode

Changes apply to both existing boxes and newly created Boxes of a given type.

When you change period mode of a box type to "auto bottom-up" or "auto scope-based", you automatically trigger a recalculation of box period. Duration of existing boxes is adjusted accordingly.

![contentId-1918669073](/cms_trial/assets/6b874320-9229-4cb9-adc0-ec08181df59a.png)

### Manual

Select this mode to manually determine the start and end date of Boxes of a given type. Box duration has to be manually adjusted. The box period is independent of its scope and sub-Box duration.

Auto scheduling rules don't apply to Boxes in manual period mode.

There is no automatic calculation of the Box period. Even if the "manual" period Box is nested under an "auto top-down" Box, the "manual" period will be independent of the auto-scheduling rules.

### Auto Top-Down

Box duration has to be manually adjusted. Select this mode if you want Boxes of this type to limit the duration of their sub-boxes.

- Box period has to be manually adjusted.
- Box period limits periods of its sub-Boxes.

**Exception**: Boxes in a "manual" period mode are unaffected by a parent Box's "auto top-down" period mode.

#### Scheduling conflict

In case of a scheduling conflict, the "auto top-down" rule has lower priority than the "auto bottom-up" and "auto scope-base" rules.

An "auto top-down" Box won't limit the periods of "auto bottom-up" and "auto scope-based" Boxes.

![contentId-1918669073](/cms_trial/assets/7ca8fd4c-3b6b-4e4b-8af8-f1b17b2a22ee.png)

### Auto Bottom-Up

A Box in this period mode adjusts its period to match its sub-boxes.

- The start date of a Box  = the earliest start date of its sub-boxes.
- The end date of a Box  = the latest end date of its sub-boxes.

#### Auto scheduling mechanism

- Only direct children are taken into account during the period calculation (grandchildren and other lower-level sub-boxes won't affect the Box period).
- The Box period will be affected by actions such as: adding a new sub-Box, change of a parent Box (nesting a Box under an "auto bottom-up" Box), changes in Box periods of existing sub-Boxes, and removing an "edge" sub-Box that the start/end date was based on.
- In the case of a conflict of "auto bottom-up" and "auto top-down" Boxes, the "auto bottom-up" rules have priority.

#### Overlapping

Box sequentiality is automatically set to "Overlapping allowed" and can't be changed. Otherwise, a scheduling conflict could potentially occur:

- the app could try to on one hand make sure that Boxes of this type don't overlap
- while at the same time trying to change the Box period based on the duration of sub-Boxes.

Sometimes it would not be possible to enforce both scheduling rules simultaneously. This is why "Overlapping allowed" is automatically selected and can't be changed.

![image-20240110-095223.png](/cms_trial/assets/8e394b85-8b10-4fe4-9299-65920df5e1c3.png)

### Auto Scope-Based

A Box in this period mode adjusts its period to encompass all tasks within its scope. The Box period reflects the duration of tasks in its scope. With those settings, you can be sure there is no discrepancy between the box period and its contents.

- start date = earliest start date of a task in a Box scope.
- end date = latest end date of a task in a Box scope.

 "Auto scope-based" rules have a priority. A parent Box in an "auto top-down" period mode won't limit a Box in the "auto scope-based" period mode.

All elements (tasks) listed in WBS are taken into account when calculating the box period (including tasks based on projects, versions, sprints, and components)

![image-20240110-095320.png](/cms_trial/assets/8e715899-301d-4f27-868b-19d9dc6d7365.png)

#### **Recalculation frequency**

The frequency of Box period recalculation depends on App settings.

Settings can be changed in the App configuration (Overview configuration) by a Jira admin. Click on the wrench at the top right > App configuration > Modules > Overview to manage the recalculation interval.

#### Empty scope

When the Box scope is empty, a user can manually set the Box period (no validation is applied).

A Box with an empty scope (no tasks in a Box) can still be used for roadmapping purposes.

#### Overlapping

Box sequentiality is automatically set to "Overlapping allowed" and can't be changed. Otherwise, a scheduling conflict could potentially occur:

- the app could try to on one hand make sure that Boxes of this type don't overlap
- while simultaneously trying to change the Box duration to encompass all its tasks.

Sometimes it would not be possible to enforce both scheduling rules simultaneously. This is why "Overlapping allowed" is automatically selected and can't be changed.

Auto scope-based Boxes can contain other sub-boxes (such as Program Increments and Iterations). This way, the main Program-type Box will automatically adjust its period to encompass all its tasks, while at the same time, sub-boxes inside can be sequential.

### Period mode edge cases

| **Parent Box** | **sub-box** |
| --- | --- |
|  | **auto bottom-up** | **auto scope-based** | **auto top-down** | **manual** |
| **auto bottom-up** | No conflict | No conflict | No conflict | No conflict |
| **auto scope-based** | **"auto scope-based" has priority** | No conflict | No conflict | No conflict |
| **auto top-down** | **"auto bottom-up" has priority** | **"auto scope-based" has priority** | No conflict | No conflict |
| **manual** | **manual box unaffected** | No conflict | No conflict | No conflict |

## Sequentiality

Changes made to Sequentiality settings apply to all boxes of a given type (both existing and newly created).

The scheduling mechanism does not validate existing Boxes. Validation is triggered when:

- creating a new Box
- editing an existing Box period
- changing a parent Box

### Overlapping allowed

Select this option if you want same-level Boxes to overlap. When you create a new Box, the App will not suggest an end date for a Sub-Box (regardless of the duration of a previously created same-level Box).

### Sequential

Only "manual" and "auto top-down" boxes can be sequential.

When you select this option, overlapping of same-type Box periods is blocked. This rule applies to same-level Boxes only. When you create a new Box, the App suggests an end date based on the duration of a previously created same-level Box.

## "Read More" URL

The link will be displayed when creating new Boxes of a given type. For example, the link can lead to internal documentation or other related information.

![image-20250313-092710.png](/cms_trial/assets/972d52c4-8703-4492-94a6-c795f02429fe.png)