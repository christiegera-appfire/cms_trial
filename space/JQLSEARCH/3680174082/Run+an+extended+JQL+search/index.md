# Run an extended JQL search

Jira's standard JQL lets you search many work item fields, but sometimes the information you need isn't available as a standard JQL field.

JQL Search Extensions adds keywords that let you search additional work item information.

## Search for issues with PNG attachments

In this example, you'll find work items with .PNG files attached to them.

1. In Jira, go to **Apps** > **JQL Search Extensions**.
2. Open **Extended Search**.
3. Enter the following query: `attachmentExtension = png`
4. Run the search.

JSE returns issues that have a PNG file attached.

![2026-09-23_16-51-04.jpeg](/cms_trial/assets/6411b4c6-97f9-4d48-af45-a3486eed2f21.jpeg)

If the query doesn’t return any results, try an attachment extension you know exists in your Jira instance, such as pdf, jpg, or another type your team uses.

You don't need to memorize JQL Search Extensions keywords. Instead, refer to the [JQL functions and keywords reference](https://support.appfire.com/space/JQLSEARCH/604209395/JQL+functions+and+keywords+reference) or the in-app **Cheat Sheet** in the right-side panel to find the right keyword for your search.

## Search for issues with PDF attachments

Once your first query works, try changing the file extension and run a second search:

`attachmentExtension = pdf`

![2026-09-23_17-06-40.jpeg](/cms_trial/assets/b0b94658-4257-4727-a76d-ab6c4dc3fbea.jpeg)

You've now used an extended JQL Search Extensions keyword to search Jira work item information that isn't available through standard JQL.

## Next step

Keywords are useful when you want to search work items. JQL Search Extensions functions let you go further by performing more complex searches, including searches based on relationships between work items.

Continue to [Search related issues with a JSE function.](/cms_trial/space/JQLSEARCH/3680174342/Find+work+items+linked+to+epics/)