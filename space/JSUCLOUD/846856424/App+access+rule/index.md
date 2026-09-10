# App access rule

### What is the app access rule?

The app access rule is a new Atlassian data security policy rule that allows organizations to limit access to content by third-party apps in Confluence spaces and Jira spaces. The app access rule is currently available in the Early Access Programme. See, <https://support.atlassian.com/security-and-access-policies/docs/app-access-rule-coverage-summary/> for more details.

### What happens if the app access rule blocks JSU?

If JSU is on your list of blocked apps, it won’t be able to access work items in any of the restricted spaces. You will still be able to configure and manage a rule with JSU; however, if the rule applies to a restricted space, the rule will not run following the transition.

### How do I know if the app access rule blocks JSU?

JSU identifies which spaces are restricted by the app access rule. If any of these spaces use a workflow with active JSU rules, they are identified by a warning icon on the *My Workflows* page.

### Manage the app access rule for JSU

If you want to allow JSU to access spaces in Jira you can use an allow list or a block list, depending on how you have defined the default permission for the rule. You can either remove JSU from a block list or add JSU to an allow list. See, <https://support.atlassian.com/security-and-access-policies/docs/block-app-access/> for detailed instructions.