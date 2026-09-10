# Retrieving Data From a Separate File

It is a good idea to keep data (such as JSON) and queries (such as SQL) in a separate file. The reason for this is because the data tends to read better. This article discusses techniques for keeping data in a separate file and how to import the data into a SIL script.

## Using readFromTextFile() to Import Data

You can keep almost any kind of data in a separate file--CSV, JSON, SQL queries, JQL queries and even other scripts such as Groovy or SIL.

1. Using readFromTextFile() is fairly straightforward. Simply pass the path and file name of the file you wish to read from. For example, the following will read from a file called “nameOfFile.txt” directly from the “silprograms” directory.   
   `string fileContents = readFromTextFile("nameOfFile.txt");`  
     
   The silprograms directory contains all SIL scripts. The silprograms folder is found in the <JIRA\_HOME>/silprograms directory.

2. To reference a file inside a folder of the silprograms folder, use the relative path beginning after the silprograms folder. Do not use any preceding forward slashes. For example:

`string fileContents = readFromTextFile("FirstFolder/SecondFolder/nameOfFile.txt");`

3. To reference a file using the full path, begin with a forward slash from the root directory. For example:

`string fileContents = readFromTextFile("/path/to/JIRA_HOME/nameOfFile.txt");`

Note that there are no forward slashes at the beginning of a relative path. Dot slash notation “./” is not supported.

## Using the replace() Function

Using the replace() function is absolutely essential if we want to treat data values as a variable. In our example below, let’s say we want to create a custom template. To create a variable in the target file, wrap the variable name in curly braces using the following format: `${<name of variable goes here>}`.

In our target file, `template.txt`, we have something like:

`Three ducks in a ${nameOfVariable}.`

We want our phrase to say, “Three ducks in a row”. Our code would look like:

```text
string phrase = readFromTextFile("template.txt");
phrase = replace(phrase, "${nameOfVariable}", "row");
runnerLog(phrase);
```

In the script, "${nameOfVariable}" is replaced by “template”. The output would be:

`Three ducks in a row.`

## Additional Help

Need help implementing unit tests on your script? Talk to me directly to me by clicking on the bot on this page.