# Jira Expressions Editor

**JMWE for Jira Cloud** provides an editor for Jira expressions in the conditions and validators configuration screens, and anywhere that a condition can be entered. The Jira editor includes syntax checking, automatic keyword highlighting, variables, and comments, among others. Additionally, the editor includes an inline help system detailing standard fields, blocks, tags, and global variables.

The Jira expression editor in JMWE Cloud is available for all input fields that support such expressions. This editor includes a number of features for creating Jira expressions, including:

- Automatic code indenting
- Syntax checking
- Keyword colors
- Comments and variables
- Find and Replace
- Keyboard shortcuts

![JMWE for Jira Cloud Jira expressions editor with basic configuration interface](/cms_trial/assets/fdca15dc-e73f-4eb2-9b5d-08596f0c53a3.png)

The Jira expression editor includes the following functions across the top of the editor window:

- **Find** - Search the current expression code. Includes searching by regular expression. Hit **Enter** to perform the search.
- **Find next** - Locate the next occurrence of the search.
- **Replace** - Find and replace text within the current expression code. Enter a search term and hit **Enter**, then enter the replacement term. Hit **Enter** again to perform the search and confirm each replacement.
- **Lookup user…** - Search for a user ID to insert into the expression code.
- **Lookup group…** - Search for a group ID to insert into the expression code.
- **Test Jira expression…** - Run a test of the Jira expression. Results will be displayed below the editor.

## Inline Help

The editor also includes a Help section below the expression field. The Help tabs include basic instructions for creating Jira expressions, as well as links to more detailed information. Additionally, some of the tabs include shortcuts for inserting common expression elements and issue fields. The Help section has the following tabs:

**Expected Value** - *Not available in the Jira expression tester.* This tab lists the possible expected value for the expression.

**Jira expressions -** This tab has a brief introduction to Jira expressions and links to the official documentation.

**Global Variables -** This tab lists the Global variables that are available for Jira expressions. Hover over any button to get more information and click on it to insert it into the editor. For more information, see [Variables used in Jira expressions](/cms_trial/space/JMWEC/465241693/Variables+used+in+Jira+expressions/).

**Issue Fields -** This tab lists the value of almost any field of an issue in a Jira expression. To find out how to access a field, select the field and the help editor displays a few Nunjucks expressions for accessing the field values and sub-fields using the field id.

**Data types -** This tab lists the properties of a data type returned by the tested script or the data type selected.

**More help -** This menu gives you access to additional help pages.

## Jira Expression Tester

JMWE includes a tool for testing Jira expressions; with this tool, an expression can be built and tested before adding it to a condition or validator configuration. The tool is available through the *JIRA MISC WORKFLOW EXTENSION* section of Jira App Administration. For more information, see Template Tester.