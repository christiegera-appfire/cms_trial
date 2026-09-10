# Release notes, Dec 08, 2025

**Release date**: December 8, 2025

Our team is thrilled to announce the latest release of BigPicture Enterprise Cloud.

---

## New

## OKR widget

### OKR widget has been added to the app

The OKR widget on the Jira work item details screen provides a direct view into the OKRs the work item is linked to. The widget displays a snippet of the OKR hierarchy of the associated KRs with the following information:

- KR’s direct parent
- KR status
- OKR Owner (for an Objective and Key Result)
- OKR period
- OKR progress (for an Objective and Key Result)
- OKR key (for an Objective and Key Result); click it to open the OKR details page

![OKR widget on the Jira work item details screen.](/cms_trial/assets/24aff37d-fe05-402c-b41f-98f72fbac034.png)

Make sure to enable the widget [OKR widget](/cms_trial/space/SPM/2576875874/OKR+widget/).

---

## Enhancements

## Scope definition

### You can narrow down a box scope using Jira labels

The items in a box that have been added to a box (spaces, boards, filters) can be limited to include only the ones that have specified labels. The “AND” operator is used. This field retrieves labels from Jira (data type “Labels”).

For example, the SAFe ART (Smart house) box shown below will contain tasks from PI PLANNING and OBJECTIVES FOR PI PLANNING that also have an “AMBER” label added to them. Items from those spaces without that label are automatically excluded from the scope of the box.

Multiple labels can be used at the same time.

![image-20251201-122901.png](/cms_trial/assets/fa4bb7c5-8381-40ac-8220-d6bc862b1f18.png)

## Task structure

### Link-based builders allow for a more flexible multi-level task tree

The combined use of built-in and link-based structure builders allows for setting up a multi-level structure of similar items (for example, nesting stories under tasks, without the need to create sub-tasks).

![image-20251201-123758.png](/cms_trial/assets/532f21cc-aee3-48ea-9c25-13f1d5611ec9.png)

With the task structure set up as shown above, when you manually change the task nesting in the tree, the change is allowed. The items are linked with the “relates” link in Jira, while all items keep the same epic as their parent.

If a built-in builder cannot be used due to its limitations (eg, Epic under Epic, Story under Story), then a Link-based builder is used.

![Task structure based on built-in and link-based.mp4](/cms_trial/assets/15e6ce69-08bd-4980-94c3-d075292bea2d.mp4)

**Note**: In the situation below, the built-in builder takes priority despite its second position on the list.

1. Link-based builder (eg. Blocks, Relates)
2. Built-in builder (eg. Epic, Parent)

## Strategic Areas

### The share button has been added to the Strategic Areas

With the **Share view** functionality, you can generate a link and send it to other users. The link opens the app view you had when generating it (for example, the selected filters remain active).

![image-20251201-131014.png](/cms_trial/assets/c386c1ce-3cfa-4d6f-9bb0-129e2e3903ad.png)

[Unmapped macro: button-handy — no content to fall back on]

## UX/UI changes

### Projects renamed to spaces

To align with Jira changes, we have replaced “projects” with “spaces” in our user interface.

![image-20251201-125954.png](/cms_trial/assets/c51236d2-a92a-4c48-bc70-18a6fb0a1a81.png)

### In the scope definition, the “Narrow down” section has been renamed to “Additional filters for work items”

![image-20251201-130253.png](/cms_trial/assets/510678c3-7674-4331-b09f-d8006855d44d.png)

### In the scope definition, the “Additional filters for work items” section was moved above the “OKR linked work” section

![image-20251201-130147.png](/cms_trial/assets/296aaaef-4263-417e-987a-4420a0e3febb.png)

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the Marketplace. [unmapped inline: placeholder]
- Stuck with something? Raise a ticket with our [support team](https://appfire.atlassian.net/servicedesk/customer/portal/11).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1215158/bigpicture-enterprise?tab=overview&hosting=cloud).

**Credits**

A heartfelt thank you to our valued customers! Your incredible support and feedback inspire us to continually improve our apps and products. You are the driving force behind why we create software. We appreciate your trust in BigPicture Enterprise Cloud!