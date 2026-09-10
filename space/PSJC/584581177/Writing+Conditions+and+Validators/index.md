# Writing Conditions and Validators

This page describes how to customize your workflow for conditions and validators.

## Writing Conditions and Validators

Conditions and validators are important components in workflow customization. They have no side effects and are written in the [Jira Expressions](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/) language, a subset of Javascript created by Atlassian.

## Runtime User & Issue

Conditions and validators execute when the user activates a transition, and the issue is in scope.

## Return Codes

Expressions must return a boolean statement, signaling the condition or validator passed the system check.

## Validator Message

The validator message is static. It can be defined but not dynamically formatted.