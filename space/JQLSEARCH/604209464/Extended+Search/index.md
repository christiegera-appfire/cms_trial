# Extended Search

**Extended Search** lets you search your Jira instance using JQL with the [additional functions and keywords](/cms_trial/space/JQLSEARCH/604209395/JQL+functions+and+keywords+reference/) included with JQL Search Extensions for Jira. You can then save your query as a filter and use it anywhere you would use a Jira filter, for example, in advanced search, Jira dashboards, or to set the scope for features in third-party apps, including [JSU](https://marketplace.atlassian.com/apps/5048/jsu-automation-suite-for-jira-workflows?hosting=cloud&tab=overview), [JMWE](https://marketplace.atlassian.com/apps/292/jira-misc-workflow-extensions-jmwe?hosting=cloud&tab=overview), [Power Scripts](https://marketplace.atlassian.com/apps/43318/power-scripts-jira-workflow-automation?hosting=cloud&tab=overview), and [BigPicture](https://marketplace.atlassian.com/apps/1212259/bigpicture-project-management-ppm?hosting=cloud&tab=overview) from Appfire. See [App integrations](/cms_trial/space/JQLSEARCH/1120043993/App+integrations/) to learn more.

new Not sure how to write a JQL query? We now have an AI Search option to help you find issues using natural language prompts. Try telling our AI tool what you are looking for. See [Natural language search - Beta](/cms_trial/space/JQLSEARCH/2225438776/Natural+language+search+-+Beta/) to learn more.

## How to use Extended Search

Watch the Get Started video to learn how to use Extended Search, or follow the step-by-step instructions below to use an example function in a query.

### Step-by-step instructions

1. In the top bar in Jira, select **Apps**>**JQL Search Extensions**. The *Extended Search* page displays.
2. In the query input field, type a JQL query and click **Search**or press `Enter`on your keypad.  
   You can use additional functions provided by JQL Search Extensions. For example, to find all issues with a summary starting with “Hello”, type `issue in wildcardMatch("summary", "Hello*")`.

Want some help with queries or looking for inspiration? Try the in-app cheat sheet. Open the cheat sheet on the right side of the *Extended Search* page to see the full list of keywords and functions with examples.

![Extended Search page showing the location of the cheat sheet.](/cms_trial/assets/778e3003-abe3-4b22-9b32-bcbf67823f32.png)

### Save the query as a filter

You can save your Extended Search query as a Jira filter. After you perform your search, click**Save as filter***.* See [Extended Search filters](/cms_trial/space/JQLSEARCH/604209567/Extended+Search+filters/) to learn more about using and managing your saved filters.

## Extended Search JQL functions and keywords

For our full list of functions and keywords, including examples, see [JQL functions and keywords reference](/cms_trial/space/JQLSEARCH/604209395/JQL+functions+and+keywords+reference/).

See our [use cases](/cms_trial/space/JQLSEARCH/604209757/Use+cases/) to discover how other customers use JQL Search Extensions for precise searching and project insights.

**Not sure which one to try?**

Our recommendations:

- Try the **linksCount** keyword by creating the `linksCount>0` query. It returns all issues that have links.
- Try the **childrenOfEpicsInQuery** function by creating the `issue in childrenOfEpicsInQuery("resolution is not empty")` query. It returns all stories of epics that are done. You can enhance this query to `issue in childrenOfEpicsInQuery("resolution is not empty") AND resolution is empty` and it will return all unfinished stories of epics that are done.

## Permissions and feature availability

The *Extended Search* page is available through the Jira global permission that controls the visibility of the Extended Search feature. By default, this permission is granted to all Jira users.