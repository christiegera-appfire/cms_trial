# Clean Code

An important aspect of scripting and programming in general is code maintenance, and to this end keeping code clean, readable and maintainable is an important aspect of scripting over the life of your code. Can others read and understand what is going on in your code?

## Simplicity

Find ways to solve problems without unneeded complexity. If you have ever heard the acronym KISS, “keep it simple”, this will help you and your team immensely in creating readable, maintainable code.

## Don’t Repeat Yourself

Scripting naturally lends itself to endless lines of code that do the same thing. A reader can lose themselves in an ocean of repeated statements.

- If you find that your code has a long list of the same line (but different parameters), consider creating an array (with those same parameters) and loop through those parameters.
- If your code is more complex (and still repeats), consider refactoring your code into a user-defined function, the call that function as necessary. If you give the function a descriptive name of what it does, this gives the user the ability to understand what your code does.

## YAGNI - You Aren’t Gonna Need It

A temptation for many programmers is to prepare code for future need. The needs of future code cannot be predicted as business needs change constantly. If there is code that is currently not being used, remove it.

## Readability

When you write code, you are writing for other humans to read. While your code may perform as expected (as interpreted by the computer), your code is read and maintained by other humans.

## Consistency

Follow the rules as established by your team on accepted convention and coding style.

Use names in a consistent manner. For example, when creating functions that run something (for example runTodo()), do not use “run” sometimes, then “execute” other times.