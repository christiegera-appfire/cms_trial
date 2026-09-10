# Making Code More Eloquent

Code can be just as expressive and eloquent as any professional writer. Learn how to write code that is short, to the point and easy to understand.

## Names

- Use easily pronounceable names for variables and functions.
- Don’t use letters.
- Use searchable names.
- Use consistent naming conventions. For example, use "get" sometimes and "fetch" other times.
- Don't use numbers
- Don't use prefixes
- Create variables with camel case

## User-defined Functions

User-defined functions make code readable and give the reader a better sense of what the code does.

- make functions as short as possible
- functions should do only one thing
- no side-effects
- User-defined functions should be verbs

## Comments

When referencing a 3rd-party library or REST API, post the page of documentation which explains what the REST endpoint does.

- Reference documentation to REST API used.
- If you arrived at a solution using documentation found online (such as an Atlassian Community post or Stack Overflow page), paste a link to that page.
- While comments is a good thing, express yourself through the code, not the comments.
- Don't use comments to make up for bad code.

  - If you feel as if you must explain what the code is, consider refactoring it or create a new function so that it reads better.

## General Suggestions for Writing

- As suggested in YAGNI, do not write extra code to anticipate future needs.
- Avoid feature creep. While it is tempting to add features to existing code, finish the current project, then add features later.
- Avoid "fancy" coding that no one else would understand. If you can refactor one line of code into three that reads better, use three lines of code.
- Avoid using multiple variables when only one will do. For example, “issueKey = key” is unnecessary and makes the code more complicated.
- Declare variables close to their usage.
- If there are variables lines that do not change, consider putting those at the top of the script. While SIL does not, strictly speaking, support constants, it helps to learn about constants and use those variables as if they were constants. For more information, see this wikipedia page on [constants](https://en.wikipedia.org/wiki/Constant_(computer_programming)).
- Keep lines short. Lines should be no longer than 60 to 80 characters long.
- Use spaces to keep related functionality close together.
- Use indentation.
- Avoid files that are too long. Consider splitting longer files into shorter ones based on functionality. Better yet, refactor long pieces of code into separate files and use the [include statement](/cms_trial/space/PSJC/433000499/Inclusions/) for import of that code.
- Use git and bitbucket for version control.