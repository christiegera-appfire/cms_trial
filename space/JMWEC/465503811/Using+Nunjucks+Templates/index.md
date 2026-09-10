# Using Nunjucks Templates

## Introduction to Nunjucks

One of the powerful features of **JMWE** is the ability to use Nunjucks templates to calculate field values dynamically, including text and date values for Jira fields, setting links between Jira issues using complex logic, and calculating transition values for Jira issues using values from other issues. [**Nunjucks**](http://mozilla.github.io/nunjucks/templating.html)is a sophisticated templating engine for JavaScript. It allows for dynamic content generation in any text field through the use of templates. A template contains variables and/or expressions, which get replaced with values when a template is *rendered*; and tags, which control the logic of the template.

Some basic templating features are described in the pages of this section and more are documented on the [Nunjucks](http://mozilla.github.io/nunjucks/templating.html) website. For more information on Nunjucks templating, including additional features, please see the [**Nunjucks documentation**](http://mozilla.github.io/nunjucks/templating.html).

## Nunjucks in JMWE for Jira Cloud

[**Nunjucks**](http://mozilla.github.io/nunjucks/templating.html)in JMWE for Jira Cloud can be used to insert information in a variety of configuration values for numerous extensions; both issue and transition information can be inserted into new values using the various templating features. These include:

- Setting post function field values

  - [Set issue fields](/cms_trial/space/JMWEC/465504849/Set+issue+fields/)
  - [Set field value of linked issues](/cms_trial/space/JMWEC/465504997/Set+field+value+of+linked+issues+(Deprecated)/)
  - [Comment issue(s)](/cms_trial/space/JMWEC/466322568/Comment+issue(s)/)
  - [Comment linked issues](/cms_trial/space/JMWEC/465373854/Comment+linked+issues+(Deprecated)/)
- The [Create issue(s)](/cms_trial/space/JMWEC/466256916/Create+issue(s)/) post function to

  - Calculate a project by selecting **Calculated** for the **Project** field under **Destination**
  - Calculate a parent issue key by selecting **Another issue** for the **Parent issue** field (only available when **Issue type** is set to **Sub-task**)
  - Set specific fields of new issue by selecting **Set field value to** for any field added under **Set specific fields of new issue(s)**
  - Add dynamic values when using the **Add a comment to the current issue** option
- The [Email issue(s)](/cms_trial/space/JMWEC/466322658/Email+issue/) post function to

  - Write the **Subject**, **HTML body**, and/or **Text body** fields
  - Set recipients from the **Users from template** and **Groups from template** fields
- The [Conditional Execution](/cms_trial/space/JMWEC/466256678/Conditional+Execution/) section to conditionally execute a post function
- Calculating the transition to be triggered in Transition post functions

  - [Transition issue(s)](/cms_trial/space/JMWEC/465242612/Transition+issue(s)/)
  - [Transition linked issues](/cms_trial/space/JMWEC/466257658/Transition+linked+issues+(Deprecated)/)
  - Transition parent issue
- [Unlink issues from the current issue](/cms_trial/space/JMWEC/465504784/Unlink+issues+from+the+current+issue/) post function to unlink issues based on the result of a Nunjucks template
- [Link issues to the current issue](/cms_trial/space/JMWEC/465242225/Link+issues+to+the+current+issue/) post function to generate an expression for the **JQL search expression** field

## Additional Information

Additional information on accessing the data about an issue or a transition can be found on [Issue and Transition Data](/cms_trial/space/JMWEC/465373107/Issue+and+Transition+Data+in+Nunjucks/).

Use cases that include Nunjucks annotations can be found on [Use cases for post functions](/cms_trial/space/JMWEC/465373017/Use+Cases+for+Post-Functions+(Legacy)/).