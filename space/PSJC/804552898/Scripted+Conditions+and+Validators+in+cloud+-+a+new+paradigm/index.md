# Scripted Conditions and Validators in cloud - a new paradigm

When Jira Cloud was launched custom conditions and validators didn’t even exist. This is because they completely break the design of the cloud architecture. Performing an action in the cloud sets off a chain reaction of micro-services and events all at once, like knocking over multiple rows of dominos. Conditions and validators require a pause in those events while they determine if the domino *should* fall over or if it is *allowed* to fall over. It really doesn't work like that so instead of being able to use scripted conditions and validators Atlassian release the [expressions language](https://developer.atlassian.com/cloud/jira/service-desk/jira-expressions/) which is the only available way to create custom conditions and validators.

Jira expressions is like any problem “solved” by the government or some service provided by the government. Yes, it technically does the job but the experience usually leaves a lot to be desired. While you can use Jira expressions if you really want to, another solution may be to approach the problem from another direction. Instead executing the script that decides if the transition can/should be performed right at that moment in time like conditions and validators do, you could use scripts to pre-calculate the answer. Using listeners you could store the answer to that question in invisible issue fields called issue entity properties. Then, with expressions you could simply check the value of that property thus created a truly scripted solution and minimizing the need to use expressions.

## Example

**Goal**: I've got an issue type of "Dev ask" that uses a workflow that is standard for all subtasks. When this groundwork status is updated to "Complete", I want to check that all sibling subtasks are assigned (because this is just part of the responsibilities for the person who completes the groundwork task). If any are Unassigned this transition should fail.

## Jira Expressions

```text
issue.issueType.name.match('^(Dev Task)$') == null || 
(issue.issueType.name.match('^(Dev Task)$') != null && 
issue.parent.subtasks.filter(subtask => subtask.assignee != null).length == 
issue.parent.subtasks.length)? true : false
```

## Power Scripts alternative solution

The alternative solution is to prepopulate the result of the condition or validator much the same way the Jira Cloud prepopulates JQL functions. A SIL Listener updates hidden field values for the issue (issue entity properties) with the result. Then, in the workflow a condition/validator is added that simply checks the value of that hidden property.

### Benefits

- SIL is easier to **write** compared to Jira expressions
- SIL is easier to **read** compared to Jira expressions
- SIL is easier to **test** compare to Jira expressions

### SIL Listener or Action script

In this example this script should be placed on the “Complete” transition for the subtask workflow. However, this script can also be used as a listener script that is trigger when the issue is updated.

```text
boolean passConditionValue = true;
if(issueType == "Dev Task") {
    for(string s in subtasks(parent)) {
        
        if(s.issueType == "Dev Task && isNull(s.assignee)) {
            passConditionValue = false;
        }
    }
}
setIssueEntityPropertyValue(key, "passCondition", passConditionValue);
```

### Jira Expression that uses SIL script value

The benefit of this expressions condition/validator is that is can work any action that uses this method. The expression can be copied from workflow to workflow with only the name of property requiring an update. There is no need to master the difficult expressions syntax.

```text
JSON.stringify(issue.properties['passCondition']).includes('true')
```