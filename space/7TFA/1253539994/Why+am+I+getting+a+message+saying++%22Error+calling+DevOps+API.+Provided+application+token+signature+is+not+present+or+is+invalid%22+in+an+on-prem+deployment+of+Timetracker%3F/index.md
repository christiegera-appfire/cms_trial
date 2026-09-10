# Why am I getting a message saying  "Error calling DevOps API. Provided application token signature is not present or is invalid" in an on-prem deployment of Timetracker?

## Question

I am receiving a message saying "Error calling DevOps API. Provided application token signature is not present or is invalid". What does this mean?

![Error_Call_DevOps.png](/cms_trial/assets/92f8d0a4-c520-4ca5-8e6b-e0facbe84f04.png)

### Answer

The *"Error calling DevOps API. Provided application token signature is not present or is invalid"*message can occur when something with the 7pace Timetracker extension inside DevOps has changed - something on your side may have been changed inside configuration or the collection itself.   
  
If you are seeing this message, open the 7pace Timetracker configuration tool, then open any setting within it, don't change anything, but click "Save". This will trigger changes / reinstall the 7pace Timetracker extension inside the collections.