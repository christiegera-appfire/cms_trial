# Using HTML with sendEmail()

sendEmail() supports HTML. Great, but how does one construct the HTML so that it works? Find out by reading below!

## Background

There are many guides and tutorials much better than we could cover here. To get started, visit any popular tutorial website dealing with HTML.

[GeeksforGeeks - HTML Tutorials](https://www.geeksforgeeks.org/html-tutorials/)

The basic HTML accepted is in the following format:

|  |
| --- |
| ```text <html><body> <p>Hello Tim,</p> <p></p> <p>Nice conversation we had the other day!</p> </html></body> ``` |

Basically the idea is that the HTML starts with "<html><body>" and ends with "</html></body>". You can pretty much add any elements you wish in between.

## String Concatenation

A basic feature of the SIL Language is that you can concatenate (that is, combine) two strings together like this:

|  |
| --- |
| ```text string stringCombo = "Nice conversation " + "we had the other day!" ``` |

If we were to print this out, it would read, "Nice conversation we had the other day!" Let's say we wanted to switch up what we would like to say, so we can configure "stringCombo" to say, "Nice *discussion* we had the other day!"

|  |
| --- |
| ```text string typeofMeeting = "discussion"; string stringCombo = "Nice " + typeofMeeting + " we had the other day!" ``` |

Now that we have the basics of string concatenation out of the way, let's see how we can use this with HTML.

## Code Example 1 - Passing Data Via a Variable

Joining strings together is no different when using HTML. However, it may be a bit more complicated because we now much be careful with HTML syntax. I find it useful to print out what the string will actually look like once the string variables have been processed. For that, use the runnerLog() function when testing scripts in the SIL Manager. If it turns out there is too much text to read in the console, consider using printInFile() or logPrint().

|  |
| --- |
| ```text string body;   string formattedCurrentDate = formatDate(currentDate(), "yyyy.MM.dd HH:mm"); string formattedCreatedDate = formatDate(created, "yyyy.MM.dd HH:mm");   body = "<html><body>"; body += "<p>" + formattedCurrentDate + "</p>"; body += "<p>" + formattedCreatedDate + "</p>"; body += "</html></body>";   runnerLog(body); ``` |

## Code Example 2 - Creating a Link

A common use case when sending email is to send issue links. To make this work, modify the link so that it reflects the url path as found on your Jira instance. For example, on my test instance, links to an issue look like this: <http://localhost:8080/browse/EX-1>

|  |
| --- |
| ```text string body;   body = "<html><body>"; body += "<p>test</p>"; body += "<a href=\"https://<BASE URL>/browse/" + key + "\">" + key + "</a>"; body += "</html></body>";   sendEmail("first.last@example.com", "subject", body); ``` |

## Code Example 3 - Add Styling to the HTML for Visual Affects

You can make any modification to the HTML using css. For example, let's say we wanted the dates (as defined below) to read in a blue color

|  |
| --- |
| ```text string body;   string formattedCurrentDate = formatDate(currentDate(), "yyyy.MM.dd HH:mm"); string formattedCreatedDate = formatDate(created, "yyyy.MM.dd HH:mm");   body += "<html>"; body += "<head>"; body +=   "<style>"; body +=     "p {"; body +=       "color: blue;"; body +=     "}"; body +=   "</style>"; body += "</head>"; body += "<body>"; body += "<p>" + formattedCurrentDate + "</p>"; body += "<p>" + formattedCreatedDate + "</p>"; body += "</html></body>";   sendEmail("first.last@example.com", "subject", body); ``` |

## Additional Help

Need help implementing this script? Talk to me directly to me by clicking on the bot on this page.