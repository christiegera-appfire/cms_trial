# Create box in the App widget

You can create a new box directly in Jira using BigPicture’s [App widget](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=BigPicture%20widget%20on%20Jira%20project%20screen&linkCreation=true&fromPageId=2533720090).

- If a perfect match box for a selected Jira space already exists, you will not be allowed to create a box for it.
- If no perfect match box was detected, you can create a box for that space.

## Create a box using the App widget

To create a box while in a Jira space, you must have sufficient [permissions](https://appfire.atlassian.net/wiki/spaces/SPM/pages/1918633268) in BigPicture.

1. Go to Jira and open a Jira space.
2. From the **More** dropdown in the Jira top menu, select **BigPicture**.

   ![How to access BigPicture app widget in Jira space.](/cms_trial/assets/0d0db054-0b4c-4fb1-8483-a555243256e2.png)

   You are now in the App widget. **Get extra views for your Jira project**screen displays.

   ![Get extra views for your Jira Space screen in the App widget.](/cms_trial/assets/010d6749-15ed-4615-80ba-9cbb936886eb.png)
3. Select the box type you want to create for your Jira space. Use the navigation arrows to scroll through the available types. The options available depend on your box type setup. Only [own-scope](/cms_trial/space/SPM/1918766536/Scope+types/) boxes can be selected.  
   When you click a box type, you will see a list of automatically active modules ([module availability](/cms_trial/space/SPM/1918503298/Define+available+modules/) can be customized after a box is created).
4. Click **Start working**to create a perfect match box.
5. The box is ready. You can create timeboxes to subdivide the scope further and adjust the [box configuration](/cms_trial/space/SPM/1918666176/Box+configuration/) to best suit your needs.

The new box inherits its name from the Jira space, but you can rename it by [editing it inline](/cms_trial/space/SPM/1918637324/Inline+edit/). You can also move the box to nest it under another box, for example, a [Portfolio box](/cms_trial/space/SPM/1918634872/Create+portfolio+box/).

![A Jira space is in the box as seen inside the App widget in Jira.](/cms_trial/assets/25de853c-3977-4d3e-83c8-3d0af9955ce1.png)

### Conditions

Requirements for box types used to create a matching box in the context of a Jira Project:

- Own scope box: Sub-scope and None-scope boxes cannot be created using this method.
- It can be created under the root (parent box set as root): **Box type settings** > **General** > **Basics** related to parent types have to allow for a main box type to be a parent.
- Sequentiality is set as **overlapping allowed**. See more on the [Period mode and sequentiality](/cms_trial/space/SPM/1918669073/Period+mode+and+sequentiality/) page.

### Troubleshooting

#### A new box cannot be created

If you want to create a box using a particular box type and cannot find it on the list of available options, the box type settings do not meet one or more of the conditions outlined above.

#### Missing permissions

Make sure you are granted sufficient app-level and box-level permissions and roles.