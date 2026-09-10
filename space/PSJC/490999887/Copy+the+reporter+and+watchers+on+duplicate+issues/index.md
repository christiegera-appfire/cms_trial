# Copy the reporter and watchers on duplicate issues

## Problem

You want to copy the watchers and the reporter from the original issue when developers close an issue with a resolution duplicate.

## Solution

## Write the code

Enter the following SIL™ code.

```text
string u;
number n=0;
n=size(fieldHistory(key, "Link"));
if (n>0 and resolution=="Duplicate")
{
 string dKey=getElement(fieldHistory(key, "Link"),n - 1); // history
 %dKey%.watchers=addElementIfNotExist(%dKey%.watchers, reporter);
 for (u in watchers)
 {
 %dKey%.watchers=addElementIfNotExist(%dKey%.watchers, u);
 }
}
```

Next, add this code to the action on the **Resolve issue** transition.