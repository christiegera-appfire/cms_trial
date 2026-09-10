# "Timetracker is taking longer than expected to load" troubleshooting guide (on-prem only)

| **On this page:**   - [Start by opening the 7pace Timetracker website direct link](/cms_trial/space/7TFA/1253540333/%22Timetracker+is+taking+longer+than+expected+to+load%22+troubleshooting+guide+(on-prem+only)/) - [Getting 500.19 error after opening the direct link](/cms_trial/space/7TFA/1253540333/%22Timetracker+is+taking+longer+than+expected+to+load%22+troubleshooting+guide+(on-prem+only)/) - [HTTP Error 500.30 - ASP.NET Core app failed to start](/cms_trial/space/7TFA/1253540333/%22Timetracker+is+taking+longer+than+expected+to+load%22+troubleshooting+guide+(on-prem+only)/) - [Checking the certificate being used for the 7pace Timetracker website](/cms_trial/space/7TFA/1253540333/%22Timetracker+is+taking+longer+than+expected+to+load%22+troubleshooting+guide+(on-prem+only)/) - [Checking the port on which the 7pace Timetracker website is hosted](/cms_trial/space/7TFA/1253540333/%22Timetracker+is+taking+longer+than+expected+to+load%22+troubleshooting+guide+(on-prem+only)/) - [Checking the Application Pool Start Mode](/cms_trial/space/7TFA/1253540333/%22Timetracker+is+taking+longer+than+expected+to+load%22+troubleshooting+guide+(on-prem+only)/) - [Checking the Application Pool recycling interval](/cms_trial/space/7TFA/1253540333/%22Timetracker+is+taking+longer+than+expected+to+load%22+troubleshooting+guide+(on-prem+only)/) - [Modifying the Application Pool Idle Time-out Setting](/cms_trial/space/7TFA/1253540333/%22Timetracker+is+taking+longer+than+expected+to+load%22+troubleshooting+guide+(on-prem+only)/) |
| --- |

If you are receiving the message "Timetracker is taking longer than expected to load" when you try to navigate to the Time tab in the DevOps Server web portal **after a fresh install** or after you have **made changes to your DevOps/TFS instance** and reinstalled Timetracker, below you will find the steps to troubleshoot this issue.

![FAQ_Time_Tracker_Troubleshoot.png](/cms_trial/assets/3d3b8227-e002-4348-b95e-5e3b63b4ab18.png)

### Starting troubleshooting

Check that you are able to open the direct link for the 7pace Timetracker website URL. To find it, run the 7pace Timetracker Configuration Tool and copy the link that is listed under the Bindings field:

![FAQ_Time_Tracker_Start_Troubleshoot.png](/cms_trial/assets/56605bcd-b438-44f6-be27-de6ff6e32a97.png)

If Timetracker is running properly, it should display an empty page with the following text: "Welcome to 7pace Timetracker".

![FAQ_Time_Tracker_Welcome_Message.png](/cms_trial/assets/2d55168e-4ca7-4a85-a486-2d64df33ff1b.png)

### Possible scenario 1

If you are seeing a **500.19 error** after opening the direct link, this indicates that the **ASP.NET Core Runtime Hosting Bundle** is not installed, or an incorrect version is installed. To resolve the issue, please see the [Prerequisites for 7pace Timetracker](/cms_trial/space/7TFA/1253539922/Installation+guide/) and install the correct version of the [ASP.NET Core Runtime Hosting Bundle](/cms_trial/space/7TFA/1253539922/Installation+guide/).

![FAQ_Time_Tracker_Possible_Scenario_1.png](/cms_trial/assets/e099022e-fdcf-4085-92ee-064f0b2c4d6f.png)

After installing ASP.NET Core, try to open the direct link again. If ASP.NET Core missing was the cause of your issue, Timetracker should work now without problems.

### Possible scenario 2

If you are seeing the following message:

"HTTP Error 500.30 - ASP.NET Core app failed to start"

Then check the Application event viewer logs on the server where Timetracker is installed and they should give you an indication for the reason for this issue. If you need assistance to resolve it, please contact [technical support](https://appfire.atlassian.net/servicedesk/customer/portal/35).

### Possible scenario 3

Check the certificate that you are using for the 7pace Timetracker website. Whatever URL you have configured for Timetracker under the Bindings in the 7pace Timetracker Configuration Tool, this URL must be contained in the certificate, or should be covered by a wildcard certificate used with the website.  
If you are seeing the below certificate error (depending on your browser) when navigating to any Timetracker page, then there is an issue with the certificate:

![FAQ_Time_Tracker_Possible_Scenario_3.png](/cms_trial/assets/fd073cc4-ba88-4c89-8d37-d6113c815fc0.png)

To check the certificate that is used with the Timetracker website, open IIS and select the 7pace Timetracker website under Sites (1). Then, in the Edit Site section, click on Bindings (2). Here you will be able to see a list of the bindings for the website. Select the binding you are using and click on the Edit button (3). In the SSL certificate section, click on the View button (4) and ensure that the Timetracker website URL is contained in the Subject field on the Details tab of the certificate (5):

![FAQ_Time_Tracker_Possible_Scenario_Edit_3.png](/cms_trial/assets/b346031a-487a-4ba2-8c87-e087a14bedf9.png)

Once the certificate is updated correctly, check the direct link once more, and if you are able to open any Timetracker pages from DevOps.

### Possible scenario 4

Ensure that only 7pace Timetracker is hosted on port 8080 in IIS, which is the default port for Timetracker.

To check if you have any other websites hosted on the same port as you are hosting 7pace Timetracker, open the 7pace Timetracker Configuration Tool and check which port is configured for the Timetracker website. Then, open your IIS (Internet Information Services) and check the hosted websites by selecting each website in the navigation panel under Sites, and ensuring that port 8080 is not occupied by any of them, or whatever port you are using for the 7pace Timetracker website in the Browse Website section. In the screenshot below, you can see a misconfiguration where the Azure DevOps Server website is using port 8080, which prevents Timetracker from using it since this port is configured by default under the Timetracker Bindings:

![FAQ_Time_Tracker_Possible_Scenario_4.png](/cms_trial/assets/587a54e0-cc2c-4d0a-b7db-e3fbcc136b1c.png)

Check the direct link once more and if you are able to open any Timetracker pages from DevOps.

### Possible scenario 5

If none of the previously described scenarios are valid for you, then ensure that the Application Pools "Start Mode" is set to "Always Running".  
  
1. Open IIS.  
2. Open Application Pools list.  
3. Select 7pace Timetracker App Pool.  
4. Click the "Advanced Settings" button on the right panel (see screenshot below).  
5. In the resulting dialog box, ensure that the "Start Mode" setting is set to "Always Running".

![FAQ_Time_Tracker_Possible_Scenario_5.png](/cms_trial/assets/e91f0f79-7ded-476c-bd64-4da4e79d390d.png)

### Possible scenario 6

If none of the previously described scenarios are valid for you, then check the Application Pools' "Regular Time Interval" to ensure that it is recycling regularly.

1. On the "Edit Application Pool" panel, click "Advanced Settings" (screenshot in Step x)  
2. Scroll down and check the "Regular Time Interval".

![FAQ_Time_Tracker_Possible_Scenario_6.png](/cms_trial/assets/17a8736d-07bb-4137-882c-f756f345ae78.png)

 Possible Scenario 7

Change the "Idle Time-out" Setting to "0".

Sometimes, IIS can send the application to the background when it is not getting requests (even if "Always Running" is true).

1. On the Edit Application Pool panel, click "Advanced Settings". (screenshot in Step x)  
2. Scroll down and check the "Idle Time-out".  
3. "Idle Time-out" is usually set to 20. Set it to "0".

![FAQ_Time_Tracker_Possible_Scenario_7.png](/cms_trial/assets/2c3ea081-813b-4210-a2c5-f24177569143.png)

*If you were unable to resolve your issue after following all the steps described, please reach out to* [*7pace Support*](mailto:supportazure@appfire.com) *for assistance.*