# JSONifying a String with Unusual Dimensions

We have all had instances when we need to aggregate data together, but because of an extra comma or quote character, there is no way to make the data uniform. Do you need to have data fit and cannot figure out how to make your JSON take shape? If so, read on!

## Background

Let's say I want to update a custom field that stores its information using JSON. While SIL does not support updating complex data structures out of the box, you can still set those values using Atlassian's REST API. Consuming REST API will be dealt with elsewhere, but how do we take a list of variables like this:

|  |
| --- |
| ```text string [] elementsValues = {"10001", "10002", "10003"}; ``` |

And turn it into JSON like this?

|  |
| --- |
| ```text {      "fields": {          "customfield_10000": ["10001", "10002", "10003"]      }  } ``` |

## Code Example

|  |
| --- |
| ```text string fullCustomfieldId = "customfield_10000"; string [] elementsValues = {"10001", "10002", "10003"}; string [] keyBody;   for (string elementsValue in elementsValues) {     keyBody += "\""+ elementsValue +"\""; }   keyBody = replace(keyBody, "|", ",");   string updateInfo = "{" +     "\"fields\" : { " +         "\"" + fullCustomfieldId + "\" : [" + keyBody + "]" +     "}" + "}";   runnerLog(updateInfo); ``` |

## Code Breakdown

We have a list of values as set by this line of code:

|  |
| --- |
| ```text string [] elementsValues = {"10001", "10002", "10003"}; ``` |

We also know that SIL stores arrays like this with pipes in between each element of data:

|  |
| --- |
| ```text "10001"|"10002"|"10003" ``` |

We can use this to our advantage by using the replace function:

|  |
| --- |
| ```text keyBody = replace(keyBody, "|", ","); ``` |

Next, create the JSON data using escaped characters with any quotes you wish to be interpreted as literally a quote. Append the "fullCustomfieldId" and "keyBody" variables to the JSON string.

|  |
| --- |
| ```text string updateInfo = "{" +     "\"fields\" : { " +         "\"" + fullCustomfieldId + "\" : [" + keyBody + "]" +     "}" + "}"; ``` |

Congratulations, you have successfully created JSON!

|  |
| --- |
| ```text {      "fields": {          "customfield_10000": ["10001", "10002", "10003"]      }  } ``` |

## Additional Help

Need help implementing this script? Talk to me directly to me by clicking on the bot on this page.