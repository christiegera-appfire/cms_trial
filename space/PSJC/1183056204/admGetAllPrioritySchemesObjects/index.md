# admGetAllPrioritySchemesObjects

## Description

Returns the list of priority scheme (as JPriorityScheme structures) that exist in the Jira environment

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetAllPrioritySchemesObjects() | **Package** | adm |
| **Alias** |  | **Pkg Usage** | getAllPrioritySchemesObjects() |

## Return Type

[**JPriorityScheme []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns the list of the priority schemes.

## Examples

### Example 1

Returns all the priorities schemes

```javascript
return admGetAllPrioritySchemesObjects();
```

10141|Default priority scheme|This is the default scheme used by all new and unassigned projects|Highest|High|Medium|Low|Lowest|10141|New priority scheme|This is a new scheme|High|Medium|Low

### Example 2

Print the priorities property from all the priorities schemes

```javascript
JPriorityScheme[] schObjects = admGetAllPrioritySchemesObjects();
for (JPriorityScheme scheme in schObjects) {
    string[] schemeName = scheme.name;
    string[] prios = scheme.priorities;
    runnerLog("schemeName \"" + schemeName + "\" has the next priorities: " + prios);
}
```

schemeName "Default priority scheme" has the next priorities: Highest|High|Medium|Low|Lowest|not high at all|towelie
schemeName "New priority scheme" has the next priorities: High|Medium|Low

## See also