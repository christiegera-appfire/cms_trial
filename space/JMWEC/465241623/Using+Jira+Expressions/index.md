# Using Jira Expressions

## Introduction to Jira Expressions

This section details the use of Jira expressions within **Jira Miscellaneous Workflow Extension (JMWE)** post functions, conditions, and validators; Jira expressions can be used to execute custom code in the context of Jira entities. It’s a domain-specific language designed for Jira and evaluated on Jira Cloud. Jira expressions follow JavaScript syntax, and can be thought of as a dialect of JavaScript. Jira expressions use a data model loosely inspired by Jira’s REST API JSON model. You can learn more about the various data types supported by Jira expressions [here](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference/), and explore them interactively on the Data Types help tab of the Jira expression editor included in JMWE.

## Jira expressions in JMWE for JIRA Cloud

Jira expressions in JMWE for Jira Cloud are used to insert information in various functions of JMWE, including:

- [Linked Issues Condition](/cms_trial/space/JMWEC/466226242/Linked+Issues+Condition/) and [Linked Issues Validator](/cms_trial/space/JMWEC/466323119/Linked+Issues+Validator/) to check on each linked issue
- [Build-your-own (scripted) Condition](/cms_trial/space/JMWEC/465474365/Build-your-own+(scripted)+Condition/) and [Build-your-own (scripted) Validator](/cms_trial/space/JMWEC/466226183/Build-your-own+(scripted)+Validator/) to input a Jira expression to be evaluated
- Validator scope to control the execution of the validator in [Linked Issues Validator](/cms_trial/space/JMWEC/466323119/Linked+Issues+Validator/) and [Linked Issues Status Validator](/cms_trial/space/JMWEC/465504708/Linked+Issues+Status+Validator/)

You can insert issue, transition and current user information into the conditions using Jira expressions.

## Scripting features in Jira expressions

To learn more about Jira expressions:

- [Syntax and semantics](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/#syntax-and-semantics)
- [Examples](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/#examples)
- [Entity properties](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/#entity-properties)
- [Date and time manipulation](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/#date-and-time)
- [Restrictions](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/#restrictions)

## Limitations of Jira expressions

Jira Cloud enforces the following stringent limitations while using Jira expressions. This section explains them in context to JMWE. For more information, see the [official Jira expressions documentation](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/#restrictions).

1. The expression's length is limited to 1,000 characters or 100 syntactic elements.
2. Limitations inside the Jira expressions written by users: The expression can execute at most 10 expensive operations (expensive operations are those that load additional data, such as entity properties, comments, or custom fields). For example, A condition that checks for a version `1.0` on every issue linked to the current issue.

   ```text
   issue.links.every(link => link.outwardIssue.versions.every(ver => (ver.name == "1.0")))
   ```

   Evaluation will fail if there are more than 10 linked issues.