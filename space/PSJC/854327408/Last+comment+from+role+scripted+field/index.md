# Last comment from role scripted field

## Problem

You want to show the last comment made by a specific role on an issue as a custom field so that it will display in the issue results list or on an issue sidebar. This role could be for a customer support agent, or a developer for example.

## Solution

```text
string lastDeveloperComment = "There have been no comments left by a developer for this issue";

for(integer comm in getAllCommentIds(key)) {
   JComment c = getCommentById(key, comm);
   if(isUserInRole(c.author, project, "Developers")) {
       lastDeveloperComment = c.text;
   }
}
return lastDeveloperComment;
```