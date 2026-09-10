# Getting started with SIL

Simple Issue Language (SIL) is an easy-to-learn scripting language used by Power Scripts for Jira Cloud and other apps. SIL offers a powerful yet accessible way to enhance your Jira workflows and automate processes without deep technical expertise.

In this section, you'll learn the fundamentals of SIL scripting - from basic syntax to best practices. We've organized the content to take you from your first script to building sophisticated solutions.

For example, with SIL and Power Scripts for Jira Cloud, you can create a workflow action that automatically creates a sub-task.

```text
string projectKey= "TSTP";

string issueType = "Sub-task";
string issueSummary = "Issue created using SIL";
//create function
issue = createIssue(projectKey, key, issueType, issueSummary);
```

This guide focuses on practical applications, step-by-step procedures, and scripting best practices.

For comprehensive details about SIL language syntax, data types, operators, and other language-specific elements, see the [SIL reference guide](/cms_trial/space/PSJC/1934458884/SIL+reference+guide/). The reference guide provides complete technical documentation for the language itself, while this section will help you apply SIL effectively in real-world scenarios.

| **In this section:**   - [How SIL works](/cms_trial/space/PSJC/15732008/How+SIL+works/)   - [Background and design philosophy of SIL](/cms_trial/space/PSJC/15731838/Background+and+design+philosophy+of+SIL/) - [Scripting basics](/cms_trial/space/PSJC/491001660/Scripting+basics/)   - [Get started with SIL Manager](/cms_trial/space/PSJC/491001674/Get+started+with+SIL+Manager/)   - [Getting and Setting Custom Fields](/cms_trial/space/PSJC/491001743/Getting+and+Setting+Custom+Fields/)   - [Variable Substitution and Jira Context](/cms_trial/space/PSJC/491001773/Variable+Substitution+and+Jira+Context/)   - [Printing Output](/cms_trial/space/PSJC/491001788/Printing+Output/) - [Basic examples and code snippets](/cms_trial/space/PSJC/490996499/Basic+examples+and+code+snippets/)   - [Code snippets](/cms_trial/space/PSJC/491001871/Code+snippets/) - [Scripting best practices](/cms_trial/space/PSJC/491001471/Scripting+best+practices/)   - [General Best Practices](/cms_trial/space/PSJC/491001485/General+Best+Practices/)   - [Inline Documentation](/cms_trial/space/PSJC/491001514/Inline+Documentation/)   - [Version Control](/cms_trial/space/PSJC/491001533/Version+Control/)   - [Using Loops](/cms_trial/space/PSJC/491001550/Using+Loops/)   - [Clean Code](/cms_trial/space/PSJC/491001626/Clean+Code/) - [Testing framework for SIL scripts](/cms_trial/space/PSJC/491001565/Testing+framework+for+SIL+scripts/)   - [Introduction to Test-Driven Design (TDD)](/cms_trial/space/PSJC/491001579/Introduction+to+Test-Driven+Design+(TDD)/)   - [silUnit Annotations](/cms_trial/space/PSJC/491001596/silUnit+Annotations/)   - [silUnit Source Code](/cms_trial/space/PSJC/491001611/silUnit+Source+Code/) |
| --- |