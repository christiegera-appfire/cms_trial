# Conditions

Conditions control the availability of a transition to be triggered by the user. Using Conditions, it is possible to hide or show any transition based on specified criteria. It is possible to enable or disable a transition based on:

- The status of the current issue or linked issues
- The existence of specific linked issues
- The user triggering the transition, or a user value in a specified field
- The results of a [Nunjucks](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/) or [Jira expression](/cms_trial/space/JMWEC/465241623/Using+Jira+Expressions/)

**Note**: Conditions are used to check the status of the issue, linked issues, or the user triggering the transition. To check or verify issue data before enabling a transition, use a [**Validator**](/cms_trial/space/JMWEC/465474068/Validators/).