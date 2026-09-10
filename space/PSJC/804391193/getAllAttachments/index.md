# getAllAttachments

Looking for a getAllAttachments() function? You won’t find it because there isn’t any. Instead, all the attachments for an issue can be retrieved using the ‘attachments’ [standard variable](/cms_trial/space/PSJC/434602568/Variable+types+and+reference+methods/). Examples on how to use this variable can be found below.

**Example 1**

```text
return attachments;
```

**Example 2**

```text
string [] allAttachments = attachments;

for(string a in allAttachments) {
    runnerLog(a);
}
```