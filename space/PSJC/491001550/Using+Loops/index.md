# Using Loops

Loops are an important feature in programming in that it provides replication without having to write code repeatedly. However, loops can also be dangerous in that they can result in delirious affects to your system if not used in a careful manner.

## Using a Development Environment

If at all possible, use a testing environment so as to prevent an administrator's worst nightmare, data loss. Even when carefully creating scripts, you can still cause major damage to your system. For this purpose, you are highly encouraged to use a testing environment while developing scripts.

## Try the Script out Without Any For Loops

For most scripts, a for loop creates a copy, of a copy, of a copy. Make sure that the first copy does what you want it to before making copies of the original. Once you have run the script a few times and know it works as expected, then through in a for loop.

## Avoid While Loops if Possible

The most frequent way coders create infinite loops is with a while loop and should only be used when absolutely necessary. If you do find a situation when you do need to use a while loop, consider adding some kind of maximum limit the loop would be allowed. Consider the following function, getUsersFromLastComment(). Looping through text is the only way that such a loop could work as you would always want to check if there were more users to be found in the comment.

|  |
| --- |
| ```text function getUsersFromLastComment() {     string [] commentUsers;     number maxUsers = 100;     string lastComment = getLastComment(key);     string matchingText;     number count = 0;           while (length(matchText(lastComment, "\\[~.*.*\\]")) > 0 && count < maxUsers) {         matchingText = matchText(lastComment, "\\[~.*.*\\]");         matchingText = substring(matchingText, 2 , length(matchingText)-1);         commentUsers += matchingText;         number end = matchEnd(lastComment, "\\[~.*.*\\]");         lastComment = substring(lastComment, end, -1);         count++;     }           return commentUsers; }     string [] users = getUsersFromLastComment(); ``` |

As you can see, the while loop has a maximum limit of 100 users that can be returned when searching through the last comment by adding the "&& count < maxUsers" clause at the end of the while loop.

## What to Do If You Have Created an Infinite Loop

If you have spent any time at all programming, you will at one time or another create an infinite loop. If this ever happens you, there are two options:

1. End the thread running the script. To do this, click on administration (the cog) → Manage Apps → SIL Diagnostic. You can kill the thread of the offending script user the "SIL Executions" section.
2. Restart Jira

## Additional Help

Need help implementing unit tests on your script? Talk to me directly to me by clicking on the bot on this page.