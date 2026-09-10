# Can we run JQL search in JMWE Cloud Conditions, Validators?

**Question:**

Can we run JQL search in JMWE Cloud Conditions, Validators?

**Answer:**

No!

**Reason:**

Unfortunately, this is simply impossible to do on Jira Cloud, **whatever app you use**, because workflow Conditions and Validators can only be written using Atlassian's [Jira Expressions](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/), which don't support running a JQL search [until Atlassian plans to revisit the <https://ecosystem.atlassian.net/browse/ACJIRA-1789> in the future again]

**Additional information:**

1. You can run a JQL search using [searchIssues](/wiki/spaces/JMWEC/pages/78482118/Custom+Filters#searchIssues) Nunjucks filter in JMWE Cloud [workflow](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=jmwec&title=Post-functions&linkCreation=true&fromPageId=465474029) [*post-functions*](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=jmwec&title=Post-functions&linkCreation=true&fromPageId=465474029) (and Actions) that use the more powerful [Nunjucks language](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/) specific to JMWE.
2. You can run a JQL search using the [jqlSearch](/wiki/spaces/JMWE/pages/106561567/Variables+and+functions+used+in+a+Groovy+expression#Global-Functions) global function in JMWE Server/DC (Conditions, Validators, Post-functions) that use [Groovy language](https://appfire.atlassian.net/wiki/spaces/JMWE/pages/461537291).