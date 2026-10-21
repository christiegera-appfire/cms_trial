# Release notes 14th October 2026

**Release date**: October 14, 2026

This page outlines the updates included in the latest release of Comala Document Management Cloud.

**App Version:** 52.3.0

**Release version:** 5.0.35

---

## Enhancements

## Global Document Report

You can now export data from the **Global Document Report** to a CSV file.

- The CSV file includes content title, space name, workflow name, scope, state, reviewers, creator, owner, updated by, and updated date.
- If you apply column filters, the CSV includes only the matching rows.

  ![CDM_Global Document Report_Export to CSV](/cms_trial/assets/f9ad2edc-b81d-49cc-8fc5-b380ba0ca865.png)

## Workflow builder

**Visual Builder Editor** and **JSON** **Code Editor** now include:

- **On label** **added** trigger event with **Added Label** condition.
- **Has Label** condition for all events.

### Event: On label added

- Use the **On label added** event in a workflow trigger to run the workflow when specific labels are added to a page.
- To limit the trigger to specific labels, add a condition:

  - Under **Condition**, choose the event-specific condition **Added label**.
  - Choose an operator and specify the labels:

    - **Equals:** The trigger runs when the page is updated with any of the specified labels.
    - **Not equals:** The trigger runs when the page does not include any of the specified labels.

      ![CDM_Add trigger_On label added.png](/cms_trial/assets/d4c67417-b096-421a-ac6b-06c7957cf344.png)

### Condition: Has label

The workflow trigger conditions now include a new **Has Label** condition. You can use it with any event.

**Has Label**:

- Choose the operator *Equals* and *Not equals* and specify one or more labels.

  - **Equals**: The trigger runs only when the page has at least one of the specified labels.
  - **Not equals**: The trigger runs only when the page has none of the specified labels.

    ![CDM_Triggers_Has label condition](/cms_trial/assets/c21700fb-c400-4621-b66b-a3abc4b5e2ab.png)

---

## Bug fixes

The following bugs are fixed in this release:

- The **Updated** column in the **Document Report** now displays absolute dates by default, as expected, instead of relative dates.
- When you export a page containing the **Document Activity** macro to **PDF**, the **Action** column now shows the correct *Approved* and *Rejected* actions and matches the live **Document Activity** view for approval rows. Previously, these rows displayed incorrectly in PDF.
- When you export a page containing the **Document Approvals** macro to **Word**, the export now includes all column details, such as status and version, and matches the live **Document Activity** view and the PDF export. Previously, the Word export was missing a few column details.
- Group names in **pre-assigned groups** for approval now resolve to the Confluence group, and the group members are assigned as reviewers. Previously, the group name didn't resolve, and reviewers were not assigned as expected.
- The **Document Activity** macro now displays correctly. Previously, it was replaced with **Page Activity**.
- Opening a Confluence page with an applied workflow no longer changes its state. Previously, opening a page moved it back to **Draft** state without making any edits.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/142/comala-document-management?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/142/comala-document-management?hosting=cloud&tab=reviews).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Appfire's Comala Document Management Cloud!