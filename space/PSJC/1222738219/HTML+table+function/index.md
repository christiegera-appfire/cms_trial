# HTML table function

A group of functions designed to take an array of text and convert it to an HTML table.

The main function (htmlTable) takes 2 parameters, a text array of table headings, and a text array or table data. The function creates columns in the table based on the number of heading in the array.

```text
function wrapTag(string text, string tag) {
    return "<" + tag + ">" + text + "</" + tag + ">";
}

function tableHead(string [] headings){
    string body;
    for(string hd in headings)
    {
        body += wrapTag(hd, "th");
    }
    return wrapTag(body, "tr");   
}

function htmlTable(string [] headings, string [] data){
    
    string body = tableHead(headings);
    string temp;
    int colCount = size(headings);
    
    for(int x = 0; x < size(data); x ++) {
        temp += wrapTag(data[x], "td");
        
        if(x > 0) {
            if((x+1) % (colCount) == 0) {
                body += wrapTag(temp, "tr");
                temp = "";
            }
        }
    }
    return wrapTag(body, "table");
}

string [] headings = "Column A|Column B|Column C";
string [] data = "1A|1B|1C|2A|2B|2C|3A|3B|3C";

runnerLog(htmlTable(headings, data), true); //see formatted output
return htmlTable(headings, data); //see raw output
```

**Output:**

![Power Scripts for Jira Cloud HTML table function icon](/cms_trial/assets/4d9171e5-220b-469a-993f-ae9c5de10e8e.png)