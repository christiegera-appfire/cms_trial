# Variable Substitution and Jira Context

This article describes the use of variable substitution and how it functions.

## Variable Substitution

The following script demonstrates the substitution principle in practice. Note how we can print the value for “original value” by using the percent signs when printing out “substitutedVariable”.

|  |
| --- |
| ```text string originalVariable = "test"; string substitutedVariable = "originalVariable"; runnerLog(%substitutedVariable%); ``` |

## Referencing an Issue via Variable Substitution

Here we do the same thing, except the “original variable” referenced is the Jira Issue scope (while we cannot interact with the issue object itself, SIL sets the value behind the scenes).

|  |
| --- |
| ```text string key = "DEMO-1"; %key%.summary = "Summary Goes Here"; ``` |

The above script is the same as:

|  |
| --- |
| ```text DEMO-1.summary = "Summary Goes Here";  ``` |

## Additional Help

Need help implementing this script? Talk to me directly to me by clicking on the bot on this page.