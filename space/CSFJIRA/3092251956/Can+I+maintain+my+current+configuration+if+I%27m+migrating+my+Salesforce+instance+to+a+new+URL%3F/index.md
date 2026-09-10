# Can I maintain my current configuration if I'm migrating my Salesforce instance to a new URL?

1. Revoke your current Connection to Salesforce.

   ![image-20241213-091452.png](/cms_trial/assets/5a73901f-9f5d-47ff-a906-c01f2d42b8d8.png)
2. Reauthorize the Connection.

   ![image-20241213-090227.png](/cms_trial/assets/186545c3-d490-4ae9-967f-bb92c33039ab.png)

Your configuration and bindings will be maintained. Please ensure that the Instance URL is pointing to your new Salesforce URL.

You will also need to reauthorize the connection in Salesforce by regenerating an API access token and applying it in Salesforce. For more information, consult the following documentation:

- [Setting up a connection to Jira](/cms_trial/space/CSFJIRA/1873346949/Set+up+a+connection+to+Jira/)