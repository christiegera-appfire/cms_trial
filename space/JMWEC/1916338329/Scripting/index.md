# Scripting

**JMWE for Jira Cloud** supports two types of scripting within the various configurations of its Actions - [Shared](/cms_trial/space/JMWEC/466288975/Shared+actions/), [Event-based](/cms_trial/space/JMWEC/465473524/Event-based+actions/), and [Scheduled](/cms_trial/space/JMWEC/466321868/Scheduled+actions/) - and within nearly all Extensions - [Post functions](/cms_trial/space/JMWEC/465242045/Post+functions/), [Conditions](/cms_trial/space/JMWEC/465473735/Conditions/), and [Validators](/cms_trial/space/JMWEC/465474068/Validators/). Those two scripting languages are:

- **Jira Expressions**
- **Nunjucks**

Most often, scripting is used in configuring conditional execution or determining on which issues to operate with an Action or Extension. Scripting is also often used for any configuration that sets a field value where that value can be generated dynamically.

This section contains information relevant to using these scripting languages with JMWE. However, it does not cover full usage of these languages and does not provide full tutorials. It does provide reference to JMWE-specific implementations (in the case of Nunjucks).