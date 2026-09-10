# Rich text formatting guide for Jira Cloud

This page explains how to format text in Jira Cloud using Power Scripts syntax. It covers basic formatting, content structure elements, tables, media embeds, detailing field compatibility, and known limitations.

Atlassian Document Format (ADF) is the underlying system that powers rich text in Jira Cloud.

Formatting behavior varies between Jira Data Center and Jira Cloud. Jira DC typically uses Wiki Markup format. Line breaks (`\n`) are consistently preserved across both Jira DC and Jira Cloud.

ADF requires detailed technical knowledge, but Power Scripts provides a simplified syntax to efficiently format text in various Jira fields.

This simplified syntax:

- Reduces the learning curve.
- Minimizes formatting errors.
- Maintains consistency across documentation.
- Converts automatically to valid ADF format.

## Fields compatibility

Some fields do not support rich text formatting due to their specific design purposes and technical limitations. Understanding field compatibility helps you manage content effectively.

Compatible fields:

- Can store ADF content in the Jira database.
- Include the necessary frontend components to display rich text.
- Can process and validate ADF content.

The following table provides detailed information about Jira field compatibility:

| **Field type** | **Compatibility** | **Description** |
| --- | --- | --- |
| Description | ✅ | Core Jira fields that are built to process and display formatted content |
| Environment | ✅ | Built-in Jira field designed to store detailed environment information with rich text support |
| Comments | ✅ | Native Jira elements that support rich text for better communication |
| Worklog entries | ✅ | Built with ADF support to allow formatted documentation of work |
| Built-in text fields (multi-line) \* | ✅ | Native Jira field designed to handle rich text content and store it as ADF |
| Custom fields: text field (multi-line) \*\* | ✅ | Custom fields of this type are configured to support ADF content |
| Text field (single line) | ❌ | Designed for brief, plain text input only (like titles or short references) |
| Text field (read-only) | ❌ | Created solely for displaying plain text without editing capabilities |

\*A standard multi-line text field that comes with Jira  
\*\* A custom field that you create and configure in Jira

---

## Basic text formatting

Jira supports text formatting options for creating well-structured content. The tables below show the available formatting syntax, how it appears when rendered, and common use cases for each style. All formatting can be combined to create rich text content that effectively communicates your information.

### Basic text styles

| **Style** | **Syntax** | **Result** | **Suggested use** |
| --- | --- | --- | --- |
| Bold | `**text**` | **text** | Use for emphasis |
| Italic | `//text//` | *text* | Use for subtle emphasis |
| Strikethrough | `~~text~~` | ~~text~~ | Use for outdated content |
| Underline | `__text__` | text | Alternative emphasis; use sparingly |

### Text position

| **Format** | **Syntax** | **Result** | **Suggested use** |
| --- | --- | --- | --- |
| Superscript | `^^text^^` as in `3x^^2^^` | 3x2 | Mathematical expressions |
| Subscript | `--text--` as in `H--2--O` | H₂O | Chemical formulas |

### Text enhancement

| **Format** | **Syntax** | **Result** | **Notes** |
| --- | --- | --- | --- |
| Color text | `{{color:#FF0000}} red text{{/color}}` | red text | - Use hex colors only - There should be no spaces before `:` |
| Links | `[[https://example.com||Visit example]]` | [Visit example](https://example.com/) | Double pipe separates URL and text |

### Other elements

| **Formatting** | **Syntax** | **Notes** | **Example** |
| --- | --- | --- | --- |
| Break in paragraph | {{break}} | No ending tag. Inserts a paragraph break. | [line break] |
| Unicode emoji | `{{emoji}}char||text||emoji_id{{/emoji}}` | Includes three parts separated by double pipe:   - Unicode emoji; - Emoji shortcode; - Emoji ID. | `{{emoji}}🙂||:slight_smile:||1f642{{/emoji}}` |
| Mention | `{{mention}}@Username||userID{{/mention}}` | Must contain `@` right after `{{mention}}`. | @John Smith |
| Inline code | ``` ``code here`` ``` | - Use two backticks with no space after opening or before closing. - Inline code is for short snippets within a line of text, commands, or technical terms; do not confuse with code blocks (used for multiple lines of code). | Command example:  ```text Run ``npm install`` to install dependencies Use the ``--force`` flag if needed ```  Technical reference example:  ```text The ``userId`` parameter must be an integer Access the API at ``api/v1/users`` ``` |

#### Example

This code demonstrates how to build a multi-line description string that showcases various text formatting options in Jira.

```text
description += "Examples: **bold** , //italics// or ~~strike through~~ and __underline__.\n";
description += "Links are given like this: [[https://google.com||Google text that appear]].\n";
description += "This is some {{color:#2266AA}} colored text{{/color}} followed by normal text.\n";
description += "Emojis: {{emoji}}🙂||:slight_smile:||1f642{{/emoji}} {{emoji}}😄||:smile:||1f604{{/emoji}} or a custom one {{emoji}}🎺||:trumpet:||1f3ba{{/emoji}}\n";
description += "A mention: {{mention}}@John Smith||6093b81a539c14006ad3c137{{/mention}}\n";
description += "A--Subscript-- and A^^Superscript^^\n";
```

Let’s analyze each line:

|  |  |
| --- | --- |
| **Line #1** | - Shows four basic text styles in one line - `\n` adds a new line |
| **Line #2** | - Demonstrates link syntax with URL and display text - URL and display text are separated by `||` |
| **Line #3** | - Shows how to add colored text (blue shade) - Demonstrates mixing colored and normal text |
| **Line #4** | - Shows three different emoji examples - Each emoji has three components:    - Unicode emoji (🙂, 😄, 🎺)   - Shortcode (:slight\_smile:, :smile:, :trumpet:)   - Emoji ID (1f642, 1f604, 1f3ba) |
| **Line #5** | - Demonstrates how to mention a user - Includes username and user ID |
| **Line #6** | - Shows both subscript and superscript formatting |

---

### Escaping special characters in Jira text

When you need to display formatting characters as plain text (like showing `--` or `**` literally) rather than using them for formatting, you'll need to use escape characters. The method differs depending on whether you're typing directly in Jira or writing code:

#### Direct text input (in Jira UI)

- Single backslash (`\`) is used to escape special characters
- When typed directly in Jira, `\-\-` will display as `-`
- Instead of creating subscript text, it will show literal hyphens
- Result: `--` appears as plain text instead of creating subscript formatting

#### Example

```text
\-\- will not be treated as subscript text \-\-       //will display as -
```

#### Programming context (in code)

- Double backslash (`\\`) is required in code strings. This is because:

  - The first `\` escapes the second `\`.
  - The resulting single `\` then escapes the special character.
- Same end result as above, but requires double backslashes in code.

#### Example

```text
addComment(key, currentUser(), "\\-\\- will not be treated as subscript text \\-\\-");
```

#### Examples comparison

| **Context** | **Syntax** | **Result** |
| --- | --- | --- |
| Direct in Jira | `\-\-text\-\-` | `-text-` |
| In code | `"\\-\\-text\\-\\-"` | `-text-` |

---

## Content structure elements

These core formatting elements are used to organize and structure your Jira content hierarchically.

| **Element** | **Syntax** | **Notes and examples** |
| --- | --- | --- |
| Headers | ```text // Header levels syntax ## Header level 1 ## ### Header level 2 ### #### Header level 3 #### ##### Header level 4 ##### ###### Header level 5 ###### ####### Header level 6 ####### //Use horizontal lines to create visual separation between sections ---- ``` | Headers help organize content into hierarchical sections. Jira supports six levels of headers. Each header must be placed on a separate line.  End headers and separators with `\n`  This example creates a level 2 heading and adds a dividing line under it:  ```text description += "### This is a level 2 header ###\n"; description += "----\n"; ``` |
| Lists | ```text // Unordered lists syntax * item 1  //Start each line with an asterisk (*) followed by a space. * item 2 * item 3 //Ordered lists syntax - item 1   //Start each line with a hyphen (-) followed by a space - item 2 - item 3 ``` | Jira supports two types of lists to help organize and structure your content: bullet lists for unordered collections and ordered lists for sequential items.  End each line with `\n`  This example creates a paragraph text followed by numbered steps 1 and 2:  ```text description += "Steps to reproduce:\n"; description += "- Step 1\n"; description += "- Step 2\n"; ``` |
| Panels | ```text //Panel types <note> Note content </note>          // Neutral information <info> Information content </info>    // General information <success> Success content </success>  // Positive outcomes <warning> Warning content </warning>  // Cautionary messages <error> Error content </error>        // Error messages or failures //Example of using rich text formatting in a panel <info> <! This is **important** information !> </info> ``` | Panels are HTML-style containers that highlight content with distinct visual styles.  You can include rich text in panels by marking the text with  `<!` and `!>`delimiters on separate lines.  - Each panel needs both opening and closing tags - Use proper line breaks (`\n`) when building programmatically  This example creates an info panel and uses bold text formatting:  ```text <info> <! This is **important** !> </info> ``` |
| Tables | ```text <table> <tr> <th>header text</th> </tr> <tr> <td>data</td> </tr> </table> ``` | HTML-style tables are useful for organizing data in rows and columns.  To learn more about working with tables in Jira, see the [Building tables](/cms_trial/space/PSJC/491002144/Rich+text+formatting+guide+for+Jira+Cloud/) section on this page. |

#### Examples

This example creates a level 1 heading, adds a dividing line, and adds text under the dividing line.

```text
// Basic task description with header and details
description += "= Bug Report: Login Form Validation =\n";
description += "----\n";
description += "Login validation fails when using special characters\n";
```

---

## Content emphasis elements

These formatting elements are used to highlight, quote, or distinguish specific content.

| **Element** | **Syntax** | **Notes** |
| --- | --- | --- |
| Quotes | ```text // You can use multiple lines // Start each line with a greater-than symbol (>) followed by a space > Quote line 1 > Quote line 2 > Quote line 3 ``` | Quotes in Jira are used to visually distinguish referenced or cited content from regular text.  End each quote line with `\n`  The example creates a paragraph followed by a two-line quote:  ```text description += "As described on this page:\n"; description += "> Quotes in Jira are used to visually distinguish referenced or cited content from regular text\n"; description += "> See also: Content emphasis elements section\n"; ``` |
| Code | ```text //Inline code `sample code here` //Code block ``` sample code here //code block with language reference ```java sample code here ``` | Code is typically used in technical content and code snippets. Jira supports two types of code formatting:   - Inline code - Code blocks; can have language reference   - Code blocks must start and end on separate lines. - Use `\n` to mark the beginning and the end of a code block  This example creates level 4 heading and adds a Java code block under it:  ```text description += "#### Code block with language ####\n"; description += "```java\n"; description += "auto i = 0;\n"; ``` |

---

## Media and attachments

These are elements for including and managing non-text content in your Jira items. This includes attached documents, images, videos, and other media content.

| **Element** | **Syntax** | **Notes** |
| --- | --- | --- |
| Single media | ```text //Single media elements can specify layout alignment  <media: layout align-start> uuid#type#collection#width#height#occurrence#alt# </media> ``` | You can embed media files in two ways: single media element or multiple media elements.  Each media element requires these parameters, separated by #:   - `uuid`: Unique identifier of the attachment - `type`: File type (for example, 'file', 'image') - `width`, `height`: Display dimensions - `collection`, `occurrence`: Internal Atlassian identifiers - `alt`: the name.extension of the media |
| Multiple media | ```text <mediagroup> uuid#type#collection#width#height#occurrence# # uuid#type#collection#width#height#occurrence# # </mediagroup> ``` |

---

## Building tables

Jira offers three types of tables to help you organize and present information effectively: basic tables for simple data presentation, styled tables for customized formatting, and dynamic tables for automated content generation.

Every table has these main elements:

All table elements require both opening and closing tags.

- `<table></table>`: Container for the entire table
- `<tr></tr>`: Table row container
- `<th></th>`: Table header cell
- `<td></td>`: Table data cell

### Basic Tables

Basic tables use the following syntax:

```text
<table>
<tr>
<th>header text</th>
</tr>
<tr>
<td>data</td>
</tr>
</table>
```

#### Example

This example demonstrates code for a simple table with a header row, 3 data rows and 3 columns. The last row demonstrates column spanning.

- Each table element starts on a new line.
- Line breaks (`\n`) are required after each element.

```text
// Start the table
description += "<table>\n";
// Create header row with three columns
description += "<tr>\n<th>\nColumn 1\n</th>\n<th>\nColumn 2\n</th>\n<th>\nColumn 3\n</th>\n</tr>\n";
// Add first data row
description += "<tr>\n<td>\nrow 1, col 1\n</td>\n<td>\nrow 1, col 2\n</td>\n<td>\nrow 1, col 3\n</td>\n</tr>\n";
// Add second data row
description += "<tr>\n<td>\nrow 2, col 1\n</td>\n<td>\nrow 2, col 2\n</td>\n<td>\nrow 2, col 3\n</td>\n</tr>\n";
// Add third row with colspan
description += "<tr>\n<td>\nrow 3, col 1\n</td>\n<td: colspan 2>\nrow 3, col 2 and 3\n</td>\n</tr>\n";
// Close the table
description += "</table>\n";
```

This example code renders the following table:

![Jira table showing three columns, multiple data rows, and a merged final row.](/cms_trial/assets/fc47c4fe-db6a-4537-b0d4-adb14724da6d.png)

### Decorated (styled) tables

You can use table layout and table cell properties to add styling to a table.

| **Style element** | **Property** | **Description** | **Examples** |
| --- | --- | --- | --- |
| Table layout | `default` | Suited for most cases; fits content within normal margins | In this example, you define a table with numbered rows which uses the default layout:  ```text <table: numbered layout default> ``` |
| `full-width` | Uses the entire page width; good for large datasets |
| `wide` | Extends beyond normal margins; useful for complex tables |
| Table cell | `colspan` | - Merges cells horizontally across columns - Takes a numeric value | ```text <td: colspan 3>This cell spans three columns</td> ``` |
| `rowspan` | - Merges cells vertically across rows - Takes a numeric value | ```text <td: rowspan 3>This cell spans three rows</td> ``` |
| `background` | - Sets the cell's background color - Uses hex color codes | ```text <td: background #FF0000>Red background cell</td> ``` |

You can use multiple properties in the same cell. In your code, space-separate the properties as shown in this example:

```text
<td: colspan 2 rowspan 3 background #CCCCCC>
    This cell spans 2 columns, 3 rows, and has a gray background
</td>
```

To prevent parsing errors, do NOT include spaces before the colon in `<table` and `<td` elements: `<td:` is correct, `<td :` is not.

### Rich content in cells

To add complex formatting with a table cell, follow these guidelines:

- Use `<!` and `!>` markers on separate lines.
- You can include any supported Jira formatting.
- Suitable for embedding media, panels, or code blocks.

#### Examples

This example demonstrates the syntax for embedding a note panel in a cell:

```text
<td>
<!
<media: layout align-start>
[media-id]#file##974#262## #
</media>
<note>Panel content here</note>
!>
</td>
```

This more complex example demonstrates the following rich text formatting:

- Basic table structure
- Column spanning
- Rich text formatting
- Embedded note panels
- Proper escape marker usage

```text
description += "<table>\n";
// Standard header row
description += "<tr>\n<th>\nColumn 1\n</th>\n<th>\nColumn 2\n</th>\n<th>\nColumn 3\n</th>\n</tr>\n";
// Regular data rows
description += "<tr>\n<td>\nrow 1, col 1\n</td>\n<td>\nrow 1, col 2\n</td>\n<td>\nrow 1, col 3\n</td>\n</tr>\n";
// Row with merged cells
description += "<tr>\n<td>\nrow 3, col 1\n</td>\n<td: colspan 2>\nrow 3, col 2 and 3\n</td>\n</tr>\n";
// Row with rich content
description += "<tr>\n<td>\n<!\n ** Decorated row 4 ** \n!>\n</td>\n<td>\nrow 4, col 2\n</td>\n<td>\n<!\n<note>\nrow 4 col 3\n</note>\n!>\n</td>\n</tr>\n";
description += "</table>\n";
```

### Dynamic tables

Tables can be generated dynamically from data sources, such as CSV files or databases. Use dynamic tables when data needs to be automatically populated or updated.

This example demonstrates how to create a table automatically in response to user comments:

```text
JComment c = getLastComment(key);
string comment = c.text;
string countryName;
if(startsWith(comment, "Country:") || startsWith(comment, "country:")) {
    string s = trim(substring(comment, 8, -1));
    int ndx = indexOf(comment, " ");
    if(ndx > 0) {
        countryName = substring(s, 0, ndx);
    } else {
        countryName = s;
    }
}
//countryName will actually contain the input from the comment
if(countryName == null) {
    description += "\n<error>\n Bad query\n</error>\n";
    return;
}
//define a structure that matches the CSV data
struct Country {
    string code;
    number latitude;
    number longitude;
    string name;
}
int added = 0;
string tableString = "\n<table>\n<tr><th>Name & Code</th><th>Geo</th></tr>\n"; 
//note that we read structures directly from the CSV:
Country [] allCountries = readFromCSVFile("countries.csv", true);
for(Country c in allCountries) {
    if(startsWith(c.name, countryName)) {
        //add the row
        tableString += "<tr><td>" + c.name + "[" + c.code + "]</td><td>\n<!\n```\n";
        //this is a code block in a cell, so we must escape it 
        tableString += "Lat:" + c.latitude + "\n";
        tableString += "Long:" + c.longitude + "\n";
        tableString += "```\n!>\n</td>\n</tr>\n"; //notice the line breaks.
        added++;
    }
}
tableString += "</table>\n";
string content = added > 0 
        ? "\n### Found " + added + (added > 1 ? " countries" : " country") +" ###\nWe have **" + added + "** countries available. The details follow:\n" + tableString
        : "\n<warn>\n There is no country matching your query\n</warn>\n";
description += content;
JComment c = getLastComment(key);
string comment = c.text;
string countryName;
if(startsWith(comment, "Country:") || startsWith(comment, "country:")) {
    string s = trim(substring(comment, 8, -1));
    int ndx = indexOf(comment, " ");
    if(ndx > 0) {
        countryName = substring(s, 0, ndx);
    } else {
        countryName = s;
    }
}
//countryName will actually contain the input from the comment
if(countryName == null) {
    description += "\n<error>\n Bad query\n</error>\n";
    return;
}
//define a structure that matches the CSV data
struct Country {
    string code;
    number latitude;
    number longitude;
    string name;
}
int added = 0;
string tableString = "\n<table>\n<tr><th>Name & Code</th><th>Geo</th></tr>\n"; 
//note that we read structures directly from the CSV:
Country [] allCountries = readFromCSVFile("countries.csv", true);
for(Country c in allCountries) {
    if(startsWith(c.name, countryName)) {
        //add the row
        tableString += "<tr><td>" + c.name + "[" + c.code + "]</td><td>\n<!\n```\n";
        //this is a code block in a cell, so we must escape it 
        tableString += "Lat:" + c.latitude + "\n";
        tableString += "Long:" + c.longitude + "\n";
        tableString += "```\n!>\n</td>\n</tr>\n"; //notice the line breaks.
        added++;
    }
}
tableString += "</table>\n";
string content = added > 0 
        ? "\n### Found " + added + (added > 1 ? " countries" : " country") +" ###\nWe have **" + added + "** countries available. The details follow:\n" + tableString
        : "\n<warn>\n There is no country matching your query\n</warn>\n";
description += content;
```

 Here's what it does:

- Monitors for new comments on a Jira issue
- When a comment starts with `Country:`, the automation:

  - Extracts the country name from the comment.
  - Searches for matching countries in a CSV file.
  - Creates a formatted table with the results.
  - Updates the issue description with the new table.

While this example uses a CSV file (`countries.csv`) as the data source, you can adapt the code to fetch data from any source, such as a database or API.

---

## Format limitations

Power Scripts for Jira Cloud provides partial support for ADF. Known formatting limitations:

- InlineCards are not yet supported.
- Nested tables (tables within tables) are not allowed.
- Some formatting features that work in our system may be rejected by Atlassian.

Always verify your formatting against the Atlassian Document Format guidelines. If you receive a 400 (Bad Request) error:

1. Verify your formatting follows Atlassian Document Format guidelines.
2. Remove any nested tables.
3. Check for unsupported Atlassian constructs.

### Malformed documents

When formatting errors are detected, the system returns an error document listing the issues. You can fix the errors and reapply formatting using this SIL script:

```text
// Replace KEY with your issue key
// description.txt should contain your corrected text
KEY.description = readFromTextFile("description.txt")
```