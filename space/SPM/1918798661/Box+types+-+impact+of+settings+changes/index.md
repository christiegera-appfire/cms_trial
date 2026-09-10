# Box types - impact of settings changes

## Box types - impact of settings changes (old navigation)

## The impact of changes in the box type settings

Changing a [box type's](/cms_trial/space/SPM/1918830000/Box+types/) settings affects the boxes created with it. Depending on the settings, the change can affect the existing boxes, new boxes created after the change in settings, or both.

### Change of the scope type

When you change the **default** [**scope type**](/cms_trial/space/SPM/1918766536/Scope+types/) of the box type on the [*Scope definition*](/cms_trial/space/SPM/2400714956/Populate+a+box+with+Jira+work+items/) page (**box type configuration** > **Tasks** > **Scope definition**), this change applies only to boxes you create afterward. Existing boxes are not affected.

The scope of the current boxes will remain as it was set up during the [box creation process](/cms_trial/space/SPM/1918406376/Create+box/).

![Scope definition page of the Program box type.](/cms_trial/assets/bd6b0157-0a9d-44f5-a82c-9eb622203034.png)

### Change of the inheritance mode of the quick filters

Changes made to the [inheritance mode](/cms_trial/space/SPM/1918700886/Inheritance+mode/) of the [quick filters](/cms_trial/space/SPM/1918503449/Filters+and+search/) (**box type configuration** > **Tasks** > **Quick Filters**) in the box type affect the existing and future boxes.

Let's consider the case of the *theta* Iteration box. It has two parents:

- Home box (or Main; Portfolio type)
- *Program of Programs* (Iteration box)

![Theta box is highlighted and the arrows point the Program and Portfolio boxes as the parent of theta box.](/cms_trial/assets/1ac2fcbc-f69b-427a-88e7-a1d8654189ba.png)

The inheritance mode of the quick filters in the Iteration box type settings is set to **Own with inherited**.

![Quick filters settings of the iteration box type.](/cms_trial/assets/9f5f82ef-0586-473e-bcc7-cee01ee5ebb3.png)

It means that all the current and future Iteration boxes will **inherit** the quick filters from all the parent boxes (marked with an arrow).

![All the quick filters of the theta box.](/cms_trial/assets/9da2c4b4-4441-4ca2-83a4-1677e57cf983.png)

In addition, users can create custom quick filters in their Iteration boxes. The High priority tasks to do at the bottom of the list is theta’s **own** filter that you will not find in its parent boxes.

In such a case, these custom filters will be present only in the boxes where they were created, but not in the parent boxes.

When you change the inheritance mode of the Iteration box type to **Inherited only**, the custom filter will disappear from theta and all other Iteration boxes, and you will no longer be able to add any new quick filters.

| Iteration box type quick filters settings. | arrow.jpg | Quick Filters page no longer shown on the box configuration page. |
| --- | --- | --- |

The same changes will affect all existing and future boxes when you change the inheritance mode to **Own**. In such a case, the Iteration boxes will only keep their custom filters and lose the inherited ones.

### Change in the box parent type

To create more advanced [box hierarchies](/cms_trial/space/SPM/1918535907/Box+hierarchy/), you can set which box types can be parents to which boxes (**box type configuration page** > **General** > **Basics** > **Parent types** section). This change affects all the existing and future boxes. However, the change will not disrupt the current box hierarchy.

For example, let’s say you add the Program box type as a parent to the Classic project box type. As a result, you can nest the existing and create new Classic boxes under Home, Portfolio, and Program boxes.

![Parent types of the classic project box type.](/cms_trial/assets/10d17c3b-3c3f-4835-8448-16fe21436ff2.png)

When you nest a Classic box under a Program box, and then remove Program from the Parent type list, the existing nesting will remain unaffected. But once you move a Classic box out of the Program box, you will not be able to nest it back.

See the [table at the bottom of this page](https://appfire.atlassian.net/wiki/spaces/SPMDRAFT/pages/1726710859/Box+types+-+impact+of+settings+changes#How-box-type-settings-impact-existing-and-future-boxes) to learn more about individual box type settings that affect boxes of a given type.

## Update rules

The table below presents the rules that govern the changes made to [box type attributes](/cms_trial/space/SPM/1918832188/Box+type+attributes/).

| **Update rule** | **Description** | **Example** |
| --- | --- | --- |
| Existing boxes updated | New values for a box type attribute will automatically affect all existing boxes of a given type. | If you change the box type name attribute of an existing box type, a new box type name will be updated in every box of that type. |
| Existing boxes affected (no invalidation) | New values for a box type attribute will not recalculate/change boxes according to the existing rules.  All existing and new boxes of a given type will follow the new rules from the moment of the change. | You remove a type A and add a new type B in box type C’s Parent types attribute. Once you save changes, you can create sub-boxes C for boxes B.” for example, PROJ-12.  Existing boxes of a given type will retain their current IDs. For example, PROG-23 will not be changed to PROJ-23. |

## How box type settings impact existing and future boxes

The table below shows how a given change in the Box type settings impacts existing and new Boxes.

| **Settings** | **New boxes** | **All boxes** | **All boxes**  **(validation of future changes;** **the present setup is retained)** | **Box type settings can be overridden for an individual box of that type** |
| --- | --- | --- | --- | --- |
| General > Basics > **Box type name** |  | X |  | Yes |
| General > Basics > **Prefix** | X |  |  | No |
| General > Basics > **Parent types** |  |  | X | No |
| General > Basics > **Icon** | X |  |  | Yes |
| General > Basics > **Icon color** | X |  |  | Yes |
| General > Basics > **Color** |  | X |  |  |
| General > Advanced > **Sequentiality** |  |  | X | No |
| General > Advanced > **Period mode** |  |  | X | No |
| General > **Modules** | X |  |  | Yes |
| Tasks > Scope definition > **Scope type** | X |  |  | No |
| Tasks > **Task Structure** | X |  |  | Yes |
| Tasks > Scheduling > **Default period mode** | X |  |  | Yes |
| Tasks > Workload contouring > **Default contouring mode** | X |  |  | Yes |
| Tasks > Quick Filters > **Inheritance mode** |  | X |  | No |
| Tasks > Quick Filters > **Default Quick Filters** | X |  |  | Yes |
| Resources > Basics > **Manually allocated teams** |  | X |  | No |
| Resources > Basics > **Auto-inherited upper-level teams** |  |  |  | No |
| Resources > Basics > **Configurable Story Point conversion ratio** |  | X |  | No |
| Security > Basics > **Inheritance mode** |  | X |  | No |
| Security > Basics > **Default security role assignment** | X |  |  | Yes |
| Gantt > Column Views > **Inheritance mode** |  | X |  | No |
| Gantt > Task Templates > **Inheritance mode** |  | X |  | No |
| Gantt > Task Templates > **Default Task templates** | X |  |  | Yes |
| Scope > Column Views > **Inheritance mode** |  | X |  | No |
| Scope > Column Views > **Default Column Views** | X |  |  | Yes |
| Board > Card Views > **Inheritance mode** |  | X |  | No |
| Board > Card Views > **Default Card Views** | X |  |  | Yes |
| Roadmap > Business value > |  | X |  |  |
| Roadmap > **Colors** |  | X |  | No |
| Risks > Card Views > **Inheritance mode** |  | X |  | No |
| Risks > Card Views > **Default Card Views** |  | X |  | Yes |

## Box types - impact of settings changes (new navigation)

## The impact of changes in the box type settings

Changing a [box type's](/cms_trial/space/SPM/1918830000/Box+types/) settings affects the boxes created with it. Depending on the settings, the change can affect the existing boxes, new boxes created after the change in settings, or both.

### Change of the scope type

When you change the **default** [**scope type**](/cms_trial/space/SPM/1918766536/Scope+types/) of the box type on the [*Work items from Jira*](/cms_trial/space/SPM/2400714956/Populate+a+box+with+Jira+work+items/) page (**box type configuration** > **Tasks** > **Work items from Jira**), this change applies only to boxes you create afterward. Existing boxes are not affected.

The scope of the current boxes will remain as it was set up during the [box creation process](/cms_trial/space/SPM/1918406376/Create+box/).

![box-types-work-items-from-jira.png](/cms_trial/assets/8a0bba33-6284-44b2-a410-3955376c2094.png)

### Change of the inheritance mode of the quick filters

Changes made to the [inheritance mode](/cms_trial/space/SPM/1918700886/Inheritance+mode/) of the [quick filters](/cms_trial/space/SPM/1918503449/Filters+and+search/) (**box type configuration** > **Tasks** > **Quick Filters**) in the box type affect the existing and future boxes.

Let's consider the case of the *theta* Iteration box. It has two parents:

- Home box (or Main; Portfolio type)
- *Program of Programs* (Iteration box)

![Theta box is highlighted and the arrows point the Program and Portfolio boxes as the parent of theta box.](/cms_trial/assets/1ac2fcbc-f69b-427a-88e7-a1d8654189ba.png)

The inheritance mode of the quick filters in the Iteration box type settings is set to **Own with inherited**.

![quick-filters.png](/cms_trial/assets/3a760786-1772-4d83-91bb-a0a4daaaeca2.png)

It means that all the current and future Iteration boxes will **inherit** the quick filters from all the parent boxes (marked with an arrow).

![All the quick filters of the theta box.](/cms_trial/assets/9da2c4b4-4441-4ca2-83a4-1677e57cf983.png)

In addition, users can create custom quick filters in their Iteration boxes. The High priority tasks to do at the bottom of the list is theta’s **own** filter that you will not find in its parent boxes.

In such a case, these custom filters will be present only in the boxes where they were created, but not in the parent boxes.

When you change the inheritance mode of the Iteration box type to **Inherited only**, the custom filter will disappear from theta and all other Iteration boxes, and you will no longer be able to add any new quick filters.

| Iteration box type quick filters settings. | arrow.jpg | Quick Filters page no longer shown on the box configuration page. |
| --- | --- | --- |

The same changes will affect all existing and future boxes when you change the inheritance mode to **Own**. In such a case, the Iteration boxes will only keep their custom filters and lose the inherited ones.

### Change in the box parent type

To create more advanced [box hierarchies](/cms_trial/space/SPM/1918535907/Box+hierarchy/), you can set which box types can be parents to which boxes (**box type configuration page** > **General** > **Basics** > **Parent types** section). This change affects all the existing and future boxes. However, the change will not disrupt the current box hierarchy.

For example, let’s say you add the Program box type as a parent to the Classic project box type. As a result, you can nest the existing and create new Classic boxes under Home, Portfolio, and Program boxes.

![Parent types of the classic project box type.](/cms_trial/assets/10d17c3b-3c3f-4835-8448-16fe21436ff2.png)

When you nest a Classic box under a Program box, and then remove Program from the Parent type list, the existing nesting will remain unaffected. But once you move a Classic box out of the Program box, you will not be able to nest it back.

See the [table at the bottom of this page](https://appfire.atlassian.net/wiki/spaces/SPMDRAFT/pages/1726710859/Box+types+-+impact+of+settings+changes#How-box-type-settings-impact-existing-and-future-boxes) to learn more about individual box type settings that affect boxes of a given type.

## Update rules

The table below presents the rules that govern the changes made to [box type attributes](/cms_trial/space/SPM/1918832188/Box+type+attributes/).

| **Update rule** | **Description** | **Example** |
| --- | --- | --- |
| Existing boxes updated | New values for a box type attribute will automatically affect all existing boxes of a given type. | If you change the box type name attribute of an existing box type, a new box type name will be updated in every box of that type. |
| Existing boxes affected (no invalidation) | New values for a box type attribute will not recalculate/change boxes according to the existing rules.  All existing and new boxes of a given type will follow the new rules from the moment of the change. | You remove a type A and add a new type B in box type C’s Parent types attribute. Once you save changes, you can create sub-boxes C for boxes B.” for example, PROJ-12.  Existing boxes of a given type will retain their current IDs. For example, PROG-23 will not be changed to PROJ-23. |

## How box type settings impact existing and future boxes

The table below shows how a given change in the Box type settings impacts existing and new Boxes.

| **Settings** | **New boxes** | **All boxes** | **All boxes**  **(validation of future changes;** **the present setup is retained)** | **Box type settings can be overridden for an individual box of that type** |
| --- | --- | --- | --- | --- |
| General > Basics > **Box type name** |  | X |  | Yes |
| General > Basics > **Prefix** | X |  |  | No |
| General > Basics > **Parent types** |  |  | X | No |
| General > Basics > **Icon** | X |  |  | Yes |
| General > Basics > **Icon color** | X |  |  | Yes |
| General > Basics > **Color** |  | X |  |  |
| General > Advanced > **Sequentiality** |  |  | X | No |
| General > Advanced > **Period mode** |  |  | X | No |
| General > **Modules** | X |  |  | Yes |
| Tasks > Work items from Jira > **Scope type** | X |  |  | No |
| Tasks > **Task Structure** | X |  |  | Yes |
| Tasks > Scheduling > **Default period mode** | X |  |  | Yes |
| Tasks > Workload contouring > **Default contouring mode** | X |  |  | Yes |
| Tasks > Quick Filters > **Inheritance mode** |  | X |  | No |
| Tasks > Quick Filters > **Default Quick Filters** | X |  |  | Yes |
| Resources > Basics > **Manually allocated teams** |  | X |  | No |
| Resources > Basics > **Auto-inherited upper-level teams** |  |  |  | No |
| Resources > Basics > **Configurable Story Point conversion ratio** |  | X |  | No |
| Security > Basics > **Inheritance mode** |  | X |  | No |
| Security > Basics > **Default security role assignment** | X |  |  | Yes |
| Gantt > Column Views > **Inheritance mode** |  | X |  | No |
| Gantt > Task Templates > **Inheritance mode** |  | X |  | No |
| Gantt > Task Templates > **Default Task templates** | X |  |  | Yes |
| Scope > Column Views > **Inheritance mode** |  | X |  | No |
| Scope > Column Views > **Default Column Views** | X |  |  | Yes |
| Board > Card Views > **Inheritance mode** |  | X |  | No |
| Board > Card Views > **Default Card Views** | X |  |  | Yes |
| Roadmap > Business value > |  | X |  |  |
| Roadmap > **Colors** |  | X |  | No |
| Risks > Card Views > **Inheritance mode** |  | X |  | No |
| Risks > Card Views > **Default Card Views** |  | X |  | Yes |