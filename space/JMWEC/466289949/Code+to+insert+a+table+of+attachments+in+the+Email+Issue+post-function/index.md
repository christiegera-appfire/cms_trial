# Code to insert a table of attachments in the Email Issue post-function

### Abstract

This code snippet creates a table with two columns, then access each attachment of the issue and print each in a row of the table. You need two snippets one for the text version and another for the HTML version of the [Email issue](/cms_trial/space/JMWEC/466322658/Email+issue/) post-function.

### Snippet for text version

```text
||File name||URL||
<% issue.attachments.each {
  print "|${it.filename}|${it.url}|"
}%>
```

### Snippet for Html version

```text
<ul>
<% issue.attachments.each {
  print "<li><a href='${it.url}'>${it.filename}</a></li>"
}%>
</ul>
```

### Placeholders

NA

### Examples

The output of the code snippet is a