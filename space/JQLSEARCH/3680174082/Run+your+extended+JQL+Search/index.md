# Run your extended JQL Search

## Run your extended JQL search

Jira's standard JQL lets you search many issue fields, but sometimes the information you need isn't available as a standard JQL field.

JQL Search Extensions adds keywords that let you search additional issue information.

In this example, you'll find issues that have PNG files attached to them.

## Search for issues with PNG attachments

1. In Jira, go to **Apps** > **JQL Search Extensions**.
2. Open **Extended Search**.
3. Enter the following query:

   `AttachmentExtension = png`
4. Run the search.

JSE returns issues that have a PNG file attached.

![2026-09-23_16-51-04.jpeg](/cms_trial/assets/6411b4c6-97f9-4d48-af45-a3486eed2f21.jpeg)

If the query doesn’t return any results, try an attachment extension that you know exists in your Jira instance, such as pdf, jpg, or another type used by your team.

JSE provides additional keywords for searching issue information beyond what's available through standard Jira JQL.

You don't need to memorize them. Refer to the [JQL functions and keywords reference](/cms_trial/space/JQLSEARCH/604209395/JQL+functions+and+keywords+reference/) when you need to find the appropriate keyword for a particular search.

## Try another search

Once your first query works, try changing the file extension:

`AttachmentExtension = pdf`

Compare the results with your first search.

![2026-09-23_17-06-40.jpeg](/cms_trial/assets/b0b94658-4257-4727-a76d-ab6c4dc3fbea.jpeg)

You've now used an extended JSE keyword to search Jira issue information that isn't available through standard JQL.

## Next step

Keywords are useful when you want to search additional issue information. JSE functions let you go further by performing more complex searches, including searches based on relationships between issues.

Continue to [Search related issues with a JSE function.](/cms_trial/space/JQLSEARCH/3680174342/Search+related+issues+with+a+JSE+function/)