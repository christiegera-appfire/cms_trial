# Using the split() Function

Many support requests come from users who want to do some kind of text parsing. One of the most effective (and easiest!) ways of parsing scripts is by using the split() function.

## Splitting a Multiline Text Custom Field

Let's say you want to get the value of the third line a multiline text field. At first, this may seem difficult but not if we use the split() function. For example:

|  |
| --- |
| ```text string [] textLines = split(#{textFieldMultiLine}, "\\u000A"); string thirdLine = textLines[2]; ``` |

As you can see by the above code that we can split up the lines by telling the SIL interpreter to look for the line feed unicode (\u000A). Since our escape character is embedded inline, we use two escape characters.

For a complete list of unicode characters, see this Wikipedia article:

<https://en.wikipedia.org/wiki/List_of_Unicode_characters>

## String Concatenation

Let's say you wanted to join all lines of our hypothetical multiline text field. You can either loop through all the elements and append each element together, or you can cheat and use the replace() function.

|  |
| --- |
| ```text string [] textLines = split(#{textFieldMultiLine}, "\\u000A"); string allTogether = replace(textLines, "|", ""); ``` |

All this does is replace pipe separators found in an array with an empty string. The same thing can be accomplished by using the join() function:

|  |
| --- |
| ```text string [] textLines = split(#{textFieldMultiLine}, "\\u000A"); string allTogether = join(textLines, " "); ``` |

## Splitting a Table in Confluence

A user was kind enough to post an example of how he split values in a table in Confluence.

|  |
| --- |
| ```text number pageId = getPage("DEMO", "table example"); string [] tabletext = split(pageId.content, "table>"); string [] tables;     int i; int j=0; for(i=0; i<size(tabletext); i++){     if(contains(tabletext[i],"<tbody>")){         tables[j] = "<table>" + tabletext[i] + "table>";         j++;     } } ``` |

As you can see, using the split() function can be used to parse text in surprising (yet effective) ways.

## Additional Help

Need help implementing this script? Talk to me directly to me by clicking on the bot on this page.