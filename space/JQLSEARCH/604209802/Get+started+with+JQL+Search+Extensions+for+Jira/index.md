# Get started with JQL Search Extensions for Jira

JQL Search Extensions (JSE) for Jira Cloud helps you build advanced Jira Query Language (JQL) searches using extended keywords and functions. Use this page to learn how JSE keywords and functions work, where to use them in Jira, and how to create more precise issue searches for reporting, troubleshooting, automation, and project management workflows.

Before using the app for the first time, check the status on the in-app *Get Started* page. If the Jira issues are still processing, wait until the process is complete. Using the app before the initial indexing is complete will result in inconsistent or inaccurate results.

## What are keywords and functions?

JQL Search Extensions (JSE) provides over 50 keywords and functions to deliver flexibility and precision to your issue searches in Jira Cloud.

### JSE keywords

[JSE keywords](/cms_trial/space/JQLSEARCH/604209395/JQL+functions+and+keywords+reference/) reference issue properties and act as terms for indexed search results. They make it faster and easier to build your searches in Jira Query Language (JQL). Auto-complete and suggestions also mean you don’t have to memorize all the keywords or operators.

Examples of keywords are `CommentedBy` or `AttachmentExtension. A simple JQL clause could be AttachmentExtension = png. This returns all issues with` an attached PNG file.

### JSE functions

[JSE functions](/cms_trial/space/JQLSEARCH/604209395/JQL+functions+and+keywords+reference/) add precision to your searches using the parameters that you define for the query or calculations within the parentheses. Examples of functions are `childrenOfIssuesInQuery()` or `linkedIssuesOfQuery()`

When using a function, your query begins with `issue in`, for example,   
`issue in linkedIssuesOfQuery("project=ACME", "is blocked by")` finds issues that block project ACME.

To use JQL Search Extensions for Jira, you should know how to write and structure a JQL query. You should understand how to use functions and keywords to build relevant and precise search results. If you need help with JQL, refer to Atlassian’s support documentation <https://support.atlassian.com/jira-software-cloud/docs/use-advanced-search-with-jira-query-language-jql/>

## Where can I use JSE?

### JSE keywords

- In Jira advanced search
- In JSE’s *Extended Search* page

In either case, type the JQL keyword or combine it with other JQL clauses in the issue search field.

![Extended Search page showing a JQL keyword query used to find issues with specific attachment types.](/cms_trial/assets/5705862f-20ed-47aa-a71d-6fddc9e9fd07.png)

### JSE functions

- In the *Extended Search* page  
  You can create queries with functions and save them as filters to use in Jira. All functions are preceded by `issue in`, for example, `issue in dateCompare("duedate < resolved")`.

  ![Extended Search page showing a JSE function query for linked Jira issues.](/cms_trial/assets/ff69b916-5524-4c2f-b973-6bbd5c1d933d.png)
- In Jira advanced search  
  Use JQL Search Extensions (JSE) custom functions directly in Jira's native advanced search. This lets you leverage powerful, non-native JQL functions without leaving your standard search workflow.  
  Refer to [Custom functions in native Jira search](/cms_trial/space/JQLSEARCH/3217883178/Custom+functions+in+native+Jira+search/) for more information on background processing and synchronization.

When you are starting out, keep the list of our [JQL functions and keywords](/cms_trial/space/JQLSEARCH/604209395/JQL+functions+and+keywords+reference/) handy to find the ones you need. The *Extended Search* page also has a cheat sheet so you can find what you need, copy the syntax, or discover other functions and keywords.