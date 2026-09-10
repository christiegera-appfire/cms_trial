# Xray

This article describes possible use cases of JQL Search Extensions and Xray.

Xray is a popular test management app for Jira. You can leverage its power with additional JQL keywords and functions that **JQL Search Extensions** provides.

## External use

Xray integrates well with the Jira UI. What’s missing in Xray Cloud is good support for JQL and issue sourcing.

You can save JQL as a filter and use it in:

- dashboard gadgets
- boards
- Jira search - simply use this syntax `filter="Your filter name"`
- 3rd party apps that accept filters and JQL

## Use cases

### Source requirements associated with tests

Standard JQL makes it possible to get requirements for one Test issue:

`issue in linkedIssues(TST-123,"tests")`

To get a list of requirements that match a JQL:

`issue in linkedIssuesOfQuery("project='ACME tests' and labels=Q3", "tests")`

### Source tests associated with requirements

Standard JQL makes it possible to get tests for one Requirement issue:

`issue in linkedIssues(REQ-123,"is tested by")`

To get a list of tests that match a JQL:

`issue in linkedIssuesOfQuery("project='ACME requirements' and labels=Q3", "is tested by")`

### Source tests associated with the requirements of the input fix versions of the specified project

This can be achieved with the following nested query:

`issue in linkedIssuesOfQuery("project='ACME requirements and fixVersion in ('v1.0', 'v1.1')", "is tested by")`

### Source defects created during the execution of the specified test

With standard JQL you can get defects created by a single test:

`issue in linkedIssues(TST-123,"created")`

To get a list of defects that match a JQL:

`issue in linkedIssuesOfQuery("project='ACME tests' and labels=Q3", "created")`

### Source list of defects created during the execution of test execution

To get all the defects:

`issue in linkedIssuesOfQuery("project='ACME tests' and type='Test Execution'", "created")`

You can filter the defects by assignee:

`issue in linkedIssuesOfQuery("project='ACME tests' and type='Test Execution'", "created") and assignee="John Doe"`

### Source defects created during the execution of tests covering the specified requirement

First create a filter, *Tests for requirements,* that matches all the tests of your requirements:

`issue in linkedIssuesOfQuery("project='ACME tests' and labels=Q3", "tests")`

Create another filter that matches the defects created during the tests:

`issue in linkedIssuesOfQuery("filter='Tests for requirements'", "created")`