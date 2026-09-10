# Tempo authorization

This page applies only to Jira Cloud users. The additional authorization step is unnecessary when using the Server version of BigPicture.

To synchronize with Tempo on Jira Cloud, you must first authorize BigPicture with Tempo Cloud.

## **1. Register the BigPicture App in Tempo**

Go to Tempo settings > OAuth2.0 Applications.

Click "New Application."

Enter the following information:

- Name of your application: **BigPicture**
- Redirect URL: [**https://cloud.softwareplant.com/cloudmanager/rest/oauth2/authorization/accept-code**](https://cloud.softwareplant.com/cloudmanager/rest/oauth2/authorization/accept-code)
- Client type: **Confidential**
- Authorization grant type: **Authorization code**

Confirm by clicking the "Create Application" button.

The user registering the application should have all necessary permissions to synchronize Tempo items with BigPicture.  
Otherwise, the authorization process will be blocked in BigPicture (to avoid possible problems while synchronizing items with Tempo).

## **2. Get the credentials of the registered App**

After you register the BigPicture App, a window with your credentials is displayed - copy the values of the 'Client ID' and 'Client secret' fields.

If there is no such window, click Actions "..." > Credentials to open it.

## **3. Enter the copied credentials from Tempo to BigPicture**

Go to BigPicture Technical Configuration> Integrations > Tempo and enter the values in the corresponding fields.

Confirm by clicking the "Save" button.

Note:

After steps 1-3, BigPicture is ready to be authorized with Tempo on Jira Cloud. Make sure that these steps are executed correctly.

This is not the authorization yet - you are only ready for the App authorization.

If there are any errors in the above steps, the authorization will not be possible. See the Troubleshooting section below to see common problems and solutions.

During this process, the entire BigPicture application is registered in Tempo but is done in a specific user's name.

Later, when the authorization starts, it is done in the name of the BigPicture App. It then uses the permissions of the user who registered BigPicture in Tempo, no matter who starts the authorization process.

## **4. Start the authorization process**

Go to the BigPicture Administration, enter one of the tab pages where the Tempo synchronization can be done (e.g., Workload plans, Holiday plans, Resource manager, Skills), and click the 'Synchronize' button.

Before the synchronization starts, the authorization with Tempo is activated automatically.

You don't have to authorize BigPicture with Tempo at each synchronization; it has to be done only once for all those pages. However, it might be necessary to proceed to the authorization again for technical reasons.

## **5. Go through the authorization process steps**

The 'Authorization in progress...' window is displayed automatically when the authorization process starts.

Another tab in the browser opens automatically, and you will be redirected there. Click the "Authorize Access" button to confirm the authorization.

When you see the 'Success' message, click the "Onwards" button to finalize the authorization process. After that, the page will be automatically closed.

Go back to the BigPicture tab. The  "Authorization completed" window pops up. This means that the authorization process has finished successfully.

If the window doesn't close, or there is no successful authorization message, there might have been some technical problems.

## **6. Finalize synchronization with Tempo**

Once authorization is completed, click the "Synchronize with Tempo" button to finalize the synchronization with Tempo.