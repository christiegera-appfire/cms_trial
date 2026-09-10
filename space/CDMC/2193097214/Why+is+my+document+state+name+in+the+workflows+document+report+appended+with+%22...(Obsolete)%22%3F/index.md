# Why is my document state name in the workflows document report appended with "...(Obsolete)"?

## Background

Sometimes, when accessing the Document Report, some documents might appear as shown in the report below.

![Comala document report showing workflow states appended with Obsolete](/cms_trial/assets/0885a392-edeb-4597-8d9f-92d337ad3254.png)

In the above report, two documents are displayed with the current state as **Review (obsolete).**

In addition, the state status indicator circle is grey.

The grey color indicates that the document is in a confused workflow state.

## Questions

- Why does the report display a document **Status** with a workflow state name appended with **...(obsolete)**?
- Why does the document **Status** change once it has been accessed?

## Explanation

Workflow **Status** is displayed as **<*****old state name*****>(obsolete),** and the workflow report appends the state name with **...(obsolete)** due to one of the following:

- A workflow is added to a document, but ’s initial state has the same name as the legacy workflow state - **<*****old state name*****>**

- The workflow configuration is changed and renames the **<*****old state name*****>** state name
- a different workflow is added to the document, and the new workflow does not have a state that is the same name as the document's legacy workflow **<*****old state name*****>** state name
- You access the Document Report before accessing the document

In each of these changes, the state property of the document retains the old value, although there might not be any valid state name in the workflow that is now applied to the document.

- Hence, the state is displayed in the report as **<*****old state name*****> (obsolete)**

The new workflow initial state name is assigned to the document when either

- A user accesses the document
- The workflow transitions the document to a state in the new workflow
- The space workflow is initialized

The Document Report then displays the new state name

- The state name does not include **...(obsolete).**
- The state status indicator circle is updated.

If a document's status is displayed as **Not Initialized,** see [FAQ—Why is my document state shown as "Not initialized" in the Document Report?](/cms_trial/space/CDMC/2192968035/Why+is+my+document+status+shown+as+%E2%80%9CNot+initialized%E2%80%9D+in+the+Document+Report%3F/)