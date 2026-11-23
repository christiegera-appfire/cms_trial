# Extended Search

Jira's standard JQL lets you search many work item fields, but sometimes the information you need isn't available as a standard JQL field.

JQL Search Extensions adds keywords that let you search additional work item information.

## Search for issues with PNG attachments

In this example, you'll find work items with .PNG files attached to them.

1. In Jira, go to **Apps** > **JQL Search Extensions**.
2. Open **Extended Search**.
3. Enter the following query: `attachmentExtension = png`
4. Run the search.

JSE returns issues that have a PNG file attached.

![JQL Search Extensions - Result of an extended search for PNG files.](/cms_trial/assets/39ef7a99-01a8-4ed4-aa9b-0b1c0c7533ba.jpeg)

If the query doesn’t return any results, try an attachment extension you know exists in your Jira instance (PDF, JPG).

You don't need to memorize JQL Search Extensions keywords. Instead, refer to the [JQL functions and keywords reference](https://support.appfire.com/space/JQLSEARCH/604209395/JQL+functions+and+keywords+reference) or the in-app **Cheat Sheet** in the right-side panel.

## Search for issues with PDF attachments

Once your first query works, try changing the file extension and run a second search:

`attachmentExtension = pdf`

![JQL Search Extensions - Results of an extended search for PDF files.](/cms_trial/assets/600f3e02-2df7-46f8-a299-9f0cdd537fc9.jpeg)

You've now used an extended JQL Search Extensions keyword to search Jira work item information that isn't available through standard JQL.

## Next step

Keywords are useful when you want to search work items. JQL Search Extensions functions let you go further by performing more complex searches, including searches based on relationships between work items.

Continue to [Search related issues with a JSE function.](/cms_trial/space/JQLSEARCH/3680174342/Find+work+items+linked+to+epics/)