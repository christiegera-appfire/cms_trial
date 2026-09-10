# Inline Documentation

Making code readable and accessible helps your team communicate and reduces wasted time when making changes to scripts. The ideas outlined here are guidelines based on experience and will give your team the ability to understand how your system is set up and track changes to the system.

## Create a README file

For administrators that are looking at your system for the first time, knowing where to begin is often a difficult task. If you create a README file at the base of the silprograms folder, this will provide a guide of where to get started.

## Commenting Code

Each script should have a small description describing what the script does and how it is run. If your code has user-defined functions, create a description for each parameter for each argument that would be passed into the function. Copy the description to your Ops Confluence site.

## Block Comments

Block Comments are useful when making multiple line comments. When making a block comment, it begins with "/\*" and ends with "\*/". Everything in between these symbols is considered a comment. This is useful when you are testing and need to comment out a large block of code.

|  |
| --- |
| ```text /* this is a comment this is also a comment string value = "even this line will be considered a comment"; */ ``` |

## Line Comments

An Line Comment is great when commenting one line of code. A line comment is created with two forward slashes, "//". Everything after the double forward slashes is considered a comment for the rest of the line. For example:

|  |
| --- |
| ```text // this is a comment string value = "string goes here"; // this is also a comment ``` |

## Conclusion

For a complete explanation of commenting, see this Oracle page on [commenting code](https://www.oracle.com/java/technologies/javase/codeconventions-comments.html).

## Additional Help

Need help implementing unit tests on your script? Talk to me directly to me by clicking on the bot on this page.