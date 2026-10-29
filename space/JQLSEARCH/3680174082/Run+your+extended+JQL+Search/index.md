# Run your extended JQL Search

Jira's standard JQL lets you search many work item fields, but sometimes the information you need isn't available as a standard JQL field.

JQL Search Extensions adds keywords that let you search additional work item information.

In this example, you'll find work items that have PNG files attached to them.

## Search for issues with PNG attachments

1. In Jira, go to **Apps** > **JQL Search Extensions**.
2. Open **Extended Search**.
3. Enter the following query: `attachmentExtension = png`
4. Run the search.

JSE returns issues that have a PNG file attached.

![2026-09-23_16-51-04.jpeg](/cms_trial/assets/6411b4c6-97f9-4d48-af45-a3486eed2f21.jpeg)

If the query doesn’t return any results, try an attachment extension that you know exists in your Jira instance, such as pdf, jpg, or another type used by your team.

JQL Search Extensions (JSE) provides additional keywords for searching issue information beyond standard Jira JQL.

You don't need to memorize these keywords; you can refer to the [JQL functions and keywords reference](https://support.appfire.com/space/JQLSEARCH/604209395/JQL+functions+and+keywords+reference) or the in-app **Cheat Sheet**, available in the right-side panel, to find the appropriate keyword for your search.

## Search for issues with PDF attachments

Once your first query works, try changing the file extension:

`attachmentExtension = pdf`

![2026-09-23_17-06-40.jpeg](/cms_trial/assets/b0b94658-4257-4727-a76d-ab6c4dc3fbea.jpeg)

You've now used an extended JSE keyword to search Jira work item information that isn't available through standard JQL.

## Next step

Keywords are useful when you want to search additional work item information. JSE functions let you go further by performing more complex searches, including searches based on relationships between work items.

Continue to [Search related issues with a JSE function.](/cms_trial/space/JQLSEARCH/3680174342/Search+related+issues+with+a+JSE+function/)