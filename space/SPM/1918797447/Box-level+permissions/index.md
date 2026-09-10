# Box-level permissions

Access to a box is based on:

- [Global roles](/cms_trial/space/SPM/1918535770/App-level+permissions/) defined in the app *Administration* (Jira users need to be assigned some global role to access BigPicture)
- Default roles specified for each box type
- Box roles configured in individual boxes
- Box roles inherited from upper-level boxes (parent boxes)

## Inheritance mode

The [inheritance of the box security roles](/cms_trial/space/SPM/1918700886/Inheritance+mode/) depends on the box types settings and determine the access to individual boxes that were created based on the specific box type. Secruity roles are inherited by the child boxes from their parent boxes.

| **Inheritance mode** | **Description** |
| --- | --- |
| Own with inherited | Box users are inherited from the parent boxes but additional users can also be manually added. |
| Inherited only | Box users can only be inherited from the parent boxes. If you want more users to have access to the box but without changing the inheritance mode, add them on the **box type configuration** > **Secruity** > **Basics** page.  In the **Inherited only** mode, the **box configuration** > **Security** tab of an individual box is unavailble (since you cannot add or edit security roles in such a box). |

When you create a new box of a specific type, that box is set to **Own with inherited** or **Inherited only** depending on the box type settings.

However, you can change the box type settings at any point (before or after creating a new box). Depending on the change in the inheritance mode, the access to the box will be updated as explained in the table below:

| **Change of the inheritance mode affects** **all** **boxes** |
| --- |
| **from** |  | **to** |  | **result** |
| **Own with inherited** | → | **Inherited only** | = | The “own” (manually added) users lose access to the box. |
| **Inherited only** | **Own with inherited** | Restores the previous “own” (manually added) users. |

Learn more about the impact of setting changes in the box type on the existing and new boxes: [Box types - impact of settings changes](/cms_trial/space/SPM/1918798661/Box+types+-+impact+of+settings+changes/).

### Inherited security roles

- Users and their security roles are always inherited (regardless of the inheritance mode).
- The inherited users are not displayed on the **box configuration** > **Security** page.

To find out what users and in what roles were inherited, check all the box’s parent boxes, including the Home/root box.

#### **Example 1**

Cassandra is a Box Editor in "SAFe ART (Smart house App)" box. She is also automatically a Box Editor for "PI 1" and "Iteration 1" boxes. In the example below, "Iteration 1" inherits security roles from "PI 1", "SAFe ART (Smart house App)" and "Home" boxes.

![Home box. The Iteration 1 box is highlighted.](/cms_trial/assets/647bbddf-f99a-4781-9472-3f8923b7fd51.png)

#### Example 2

Angela Hambleton is a Box Editor in the "Project Portfolio" box.

![Security page in box configuration.](/cms_trial/assets/a442a940-e1d6-4447-8b67-4af232908239.png)

The "Hybrid project (Sport App)" box is nested under the "Project Portfolio" box.

![Box switcher. The Hybrid project sport app is highlighted.](/cms_trial/assets/df31050e-5215-4a05-8671-ae22797090a9.png)

In the "Hybrid project (Sport App)" box, Angela is not visible on the user list on the **box configuration** > **Security** page. That’s because she inherited the Box Editor role in that box.

![Box security page of the hybrid project sport app box.](/cms_trial/assets/df407d78-ceae-425d-87a3-f1e394d44e67.png)

## Default security roles assignment

When you create a box of a specific type, default users and groups are automatically added (per the box type settings).

Existing boxes remain unaffected.