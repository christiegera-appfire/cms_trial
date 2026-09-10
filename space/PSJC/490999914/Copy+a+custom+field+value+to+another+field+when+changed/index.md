# Copy a custom field value to another field when changed

This script runs as a listener to the **Issue Updated** event. If the value of the **Colors** field (**customfield\_10712**) changes, the script updates the **Colors 2** custom field (**customfield\_10717**).

## Updated script

```text
struct _history {
  date changeDate;
  string value;
}

_history h = fieldHistory(key, "customfield_10712");
int hCount = arraySize(h);

if(hCount >= 3 ) {   
     if((h[hCount - 1] != h[hCount - 3]) || hCount == 3) {
        %key%.customfield_10717 = %key%.customfield_10712;
    }
}
```

## Initial script

```text
//gets the history of the Color custom field
string [] h = fieldHistory(key, "customfield_10712");
int hCount = arraySize(h); //get the size of the history array

//If the value of the field is null the array size (hCount) will be 0
//If the value has been set only 1 time the array size (hCount) will equal 3
//If the value has been set more than once the array size (hCount) will be greater than 3
if(hCount >= 3 ) {
    
    //If the value in history has changed OR the value was only set once
    if((h[hCount - 1] != h[hCount - 3]) || hCount == 3) {
        %key%.customfield_10717 = %key%.customfield_10712;
    }
}
```