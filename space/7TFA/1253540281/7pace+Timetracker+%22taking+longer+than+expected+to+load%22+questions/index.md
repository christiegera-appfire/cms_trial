# 7pace Timetracker "taking longer than expected to load" questions

## Question - Loading issues using DevOps Server over HTTPS

I'm using DevOps Server over HTTPS  and am experiencing loading issues.

Timetracker pages show red notifications with text "TimetrackerOnPremises by 7pace failed to load":

![FAQ_Loading_Issues.png](/cms_trial/assets/1639dbd2-20fd-48ea-a717-72c7342c23a5.png)

In the browser console (F12), I receive the following error when I try to try to open the Timetracker address directly in my browser: "7pace.TimetrackerOnPremises.TimeMonthly:1 Mixed Content: The page at <\_\_\_\_\_> was loaded over HTTPS, but requested an insecure resource 'http://timetracker\_url\_'. This request has been blocked; the content must be served over HTTPS."

### Answer - Use the Timetracker Configuration Tool to update your DevOps URL

You are using DevOps Server over HTTPS, therefore, 7pace Timetracker needs to be configured over HTTPS as well. This is because Timetracker (and any other extension for DevOps Server) is located in the iframe, and browsers prevent HTTPS iframes from loading on pages with HTTPS.  
  
Please go to the Timetracker Configuration Tool and change it so that the DevOps URL is the same for your end-users (it looks like this: **https**://TFS\_URL/tfs/). After that, you should be asked to configure HTTPS binding for Timetracker and to select the SSL certificate.

![FAQ_Loading_Issues_Change_URL.png](/cms_trial/assets/ef3aaa16-336e-443d-b966-6132745a3b56.png)

## Question (on-premise only) - Timetracker by 7pace failed to load

After installing Timetracker, I received the message "Timetracker by 7pace failed to load" when I tried to navigate to the TIME tab in the DevOps Server web portal. We tried waiting, restarting the server, and using different browser - can you help?

### Answer (on-premise only) - Open 7pace Timetracker directly from the web address

This kind of error usually means that you cannot reach the Timetracker web application. To diagnose Timetracker availability, just open it directly by the address you provided during installation. You can find your address in the 7pace Timetracker Configuration Tool:

![FAQ_Loading_Issues_Config_Tool.png](/cms_trial/assets/b0e302e9-c877-42f5-ac58-2e4dd0a393ef.png)

If Timetracker runs properly, it should display an empty page with the following text: "Welcome to 7pace Timetracker".

**Common issues:**

- Port is blocked by firewall
- The Certificate is not trusted and the browser revokes connection
- The address is not reachable from your PC

## Question - Why are there multiple errors about DOM elements in the Dev console?

I'm seeing "Timetracker is taking longer than expected to load" messages. I looked in our browser's Dev console and see multiple errors about DOM elements. Can you help?

### Answer - Check your browser extensions or security settings

This can occur if your browser has some extensions or security settings that prevents the [Referer](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer) header from being passed to iFrames. 7paceTimetracker relies on this header and expects that it is present when you open a page. Please check your browser settings and see if something is blocking this header (it can be settings in browser, ad-blocking extension or any script blocking extensions).

## Question (on-premise only) - The first time I load Timetracker, I see an error message

When loading any page of Timetracker for the first time I am receiving the following message: "Timetracker is taking longer than expected to load." If I don't use the page for awhile, it also takes some time to add "New Time", however, if I try to add a second time entry immediately, I can do so. Can you help?

### Answer (on-premise only) - Troubleshooting IIS-based applications

This kind of delay is usual for IIS-based applications and can depend on many factors in the system. Try one of the solutions, below, to see if it fixes your issue.

#### **Step 1 - Set the Application Pool “Start Mode” to “Always Running”**

Ensure the Application Pools "Start Mode" is set to "Always Running".  
  
1. Open IIS.  
2. Open Application Pools list.  
3. Select 7pace Timetracker App Pool.  
4. Click the "Advanced Settings" button on the right panel (see screenshot, below).  
5. In the resulting dialog box, ensure that the "Start Mode" setting is set to "Always Running".

![FAQ_Loading_Issues_App_Pools.png](/cms_trial/assets/807dc20a-5978-49f9-baa8-dbdeb58b0657.png)

#### **Step 2 - Check the “Regular Time Interval”:**

Check the Application Pools' "Regular Time Interval" to ensure that it is recycling regularly.

1. Referencing the screenshot, above, click "Advanced Settings".  
2. Scroll down and check the "Regular Time Interval".

![FAQ_Loading_Issues_Advanced_Settings.png](/cms_trial/assets/3b2c9165-91c4-46ad-b354-6a9a680b0ae0.png)

#### **Step 3 - Change the “Idle Time-Out” setting**

Change the "Idle Time-out" Setting to "0".

Sometimes, IIS can send the application to the background when it's not getting requests (even if "Always Running" is true).

1. Referencing the first screenshot, above, click "Advanced Settings".  
2. Scroll down and check the "Idle Time-out".  
3. "Idle Time-out" is usually set to 20. Set it to "0".

![FAQ_Loading_Issues_Idle_Timeout.png](/cms_trial/assets/171dd50c-f5a8-49e5-bcaf-79c99bbd93b6.png)