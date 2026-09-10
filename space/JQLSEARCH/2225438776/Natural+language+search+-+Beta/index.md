# Natural language search - Beta

You can now use natural language prompts to search for issues in the *Extended Search* page in JQL Search Extensions (JSE).

beta Our natural language search is currently in Beta. While the feature evolves, you might have unexpected or incorrect results. Jira Admins can control access to the AI natural language search from the **Admin tools** featureon the *Extended Search* page. AI Search is available to users by default. If you don’t see the AI Search option in your instance, contact your Jira Administrator.

Follow the interactive demo below for a quick introduction, or refer to the step-by-step instructions.

**To use the natural language search:**

1. Go to **Apps** > **JQL Search Extensions** > **Extended Search**.
2. Click **AI Search (BETA)**.

   ![Screenshot of the prompt input field in the JSE's natural language search.](/cms_trial/assets/afbc524f-fe2f-4788-8c38-e35842b53854.png)
3. Type a prompt describing what you want to search for. For example, try `find all closed issues that I have commented on`, or `find all open issues that are unassigned`. Try to use targeted prompts to limit searches that return too many issues.
4. Click **Search**.
5. The AI generates an appropriate JQL query and displays any matching results.

A monthly AI search credit limit applies according to your Jira instance tier. If you reach this limit, you can wait until the start of the next month or contact our [support](https://appf.re/support) team to continue using the app.

## How to save an AI search as a filter

Once you perform a search, you can save the query as a filter. If you edit the query or change the prompt, you will need to run the search again before you can save it as a filter.

**To save a query as a filter:**

1. Click **Save as filter**.
2. Provide a name for the filter.
3. Click **Save**.

See [Extended Search filters](/cms_trial/space/JQLSEARCH/604209567/Extended+Search+filters/) to learn more.

**Nested functions**: JSE doesn’t support nested functions. If you want to include a nested function, first save the nested query as a filter, then use the filter name in the sub-query.

## How to edit an AI-generated search

If you want to perform a different search, you have two options:

### **Try a different prompt**

You don’t need to edit the JQL to perform another search. Edit the prompt, or enter a new one, then click **Search**.

### **Edit the JQL query**

1. Click the **Edit** icon.

   ![Screenshot of the AI-generated JQL with the edit button highlighted in yellow.](/cms_trial/assets/fa0749e8-3739-4987-955a-3aa997631d35.png)
2. In the AI JQL editor, make any required changes to the query using JQL syntax. You can use any of our keywords and functions here.   
   Click **Search**.

Open the cheat sheet on the right side of the Extended Search page to discover all of our keywords and functions. You can copy the example JQL query and update the parameters to suit your needs.

## Help improve our AI feature

If you want to help improve this feature, please use the voting icons to indicate whether the results were accurate.

![Screenshot showing the search results voting buttons.](/cms_trial/assets/e842eb44-4ea4-4b41-9620-8f4ba916cdd7.png)