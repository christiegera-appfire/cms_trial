# Troubleshooting front-end performance problems

Please execute these steps using the **incognito tab of your browser** in case you are experiencing problems with loading pages in BigPicture plugins.

## **Data has to be recorded during problem reproduction!**

1. Start recording data.
2. Reproduce the problem (when data is being recorded).
3. Stop recording data and download the file.

### **See a video example of how to extract a Network analysis file**

Image — asset pipeline pending  
Get a HAR file.mp4

## Step-by-step guide for Chrome browser.

Please bear in mind that **improper handling of browser console data** such as HAR files **could potentially cause a security threat** if such data is intercepted by a third-party agent. The data contained in such a report could be used to log in to your Jira/BigPicture system and impersonate you and/or view your sensitive data (not only the data captured in such a file). It is essential to **make sure only authorized parties handle such files.**

### **Network analysis** - HAR file

Step-by-step

1. Open the **Dev Console** tool (F12 on a PC or ⌘+⌥+i  on a Mac).
2. Go to the **Network** tab in the Dev Console.
3. Choose the **Fetch/XHR tab**.
4. Select **Preserve Log**.

   ![image-20250307-090941.png](/cms_trial/assets/8c5d23cf-c21b-438e-8cdb-5b34c87ddc32.png)
5. Ensure that Google Chrome is recording. A **red button** indicates that a recording is already in progress. If the button is grey, click **Record network log**.

   ![image-20250307-091255.png](/cms_trial/assets/de8790e5-d8fd-42e3-bbf9-699c4a328446.png)
6. Clear any existing logs by clicking **Clear network log**.

   ![image-20250307-091621.png](/cms_trial/assets/d1670d92-3d89-4f98-96a6-eab25f668243.png)
7. Go to the page where the issue occurred and **reproduce the issue**.
8. Click **Export HAR** to export the file as HAR.

   ![image-20250307-092302.png](/cms_trial/assets/e50caac9-0d38-4c69-9f46-c30354e77390.png)
9. If any items are marked in red, click on them one by one and take screenshots (enlarge the Dev tool window to make the data visible). Share the files in the support ticket.

   ![image-20250307-092556.png](/cms_trial/assets/9cc5d59b-d5c9-4232-988d-f72014507093.png)![image-20250307-092724.png](/cms_trial/assets/a3bc4951-d7f4-4ca4-bdae-52762824c94a.png)
10. When contacting our Support, remember to:

    1. Share the HAR file in the support ticket.
    2. Share the screenshots in the support ticket.

### **Taking Performance profile**

Step-by-step

1. Open the Dev Console tool (F12 on a PC or ⌘+⌥+i  on a Mac).
2. Go to the Performance tab in the Dev Console.
3. Click the record button.

   ![contentId-1918407593](/cms_trial/assets/0ebf9bf0-0294-4714-a48a-509ff78b3338.png)
4. Reproduce the issue while the profile is being recorded.
5. Please keep the tab open in the foreground until the recording finishes!
6. Once the page loads (the problem is reproduced) click Stop.

   ![contentId-1918407593](/cms_trial/assets/cb42e7ee-5812-4c46-9f21-2a72c356545b.png)
7. Save profile.

   ![contentId-1918407593](/cms_trial/assets/f00c4a2e-4aa9-44e7-9304-23dc3528e3d1.png)
8. Send us the file. It is a good idea to compress it before sending it.

### **Problems loading a blank page, a button that is not working, or unexpected behavior while using the plugin**

Step-by-step

1. Open the Dev Console tool (F12 on a PC or ⌘+⌥+i on a Mac).
2. Go to the Console tab in the Dev Console.

   ![contentId-1918407593](/cms_trial/assets/3ef961a7-bcd4-4a83-9503-656f6c9a47ac.png)
3. Right-click anywhere on the list, "Save as" and attach the screenshot to the support ticket.
4. if there are any items marked in red please expand (by clicking on the item) and take a screenshot (see above).
5. In the support ticket:

   1. Share the file
   2. Share the screenshots

## Step-by-step guide for Microsoft Edge browser.

### **Network analysis** - HAR file

Step-by-step

1. Open the Dev Console tool (F12 on a PC or ⌥+⌘+i on a Mac).
2. Go to the **Network** tab in the Dev Console.
3. Choose the **Fetch/XHR** tab.
4. Select **Preserve Log**.

   ![image-20250310-094646.png](/cms_trial/assets/abbd71af-3a3f-491c-8bee-f5ad16a5520d.png)
5. Ensure that Microsoft Edge is recording. A **red button** indicates that a recording is already in progress. If the button is grey, click **Record network log**.

   ![image-20250310-094803.png](/cms_trial/assets/618ff34a-86ad-40f3-a58f-0b3515d1fdc2.png)
6. Clear any existing logs by clicking **Clear network log**.

   ![image-20250310-094837.png](/cms_trial/assets/73b2c997-9be4-4020-94ff-ad0199f923c7.png)
7. Go to the page where the issue occurred and **reproduce the issue**.
8. Click **Export HAR** to export the file as HAR.

   ![image-20250310-095101.png](/cms_trial/assets/7372fcc3-6d7d-493c-a1c1-d9b37085473b.png)
9. If any items are marked in red, click on them one by one and take screenshots (enlarge the Dev tool window to make the data visible). Share the files in the support ticket.
10. When contacting our Support, remember to:

    1. Share the HAR file in the support ticket.
    2. Share the screenshots in the support ticket.

### **Taking Performance profile**

Step-by-step

1. Open the Dev Console tool (F12 on a PC or ⌥+⌘+i  on a Mac).

   [Unmapped macro: legacy-content — no content to fall back on]
2. Go to the Performance tab in the Dev Console.
3. Click the record button.

   ![contentId-1918407593](/cms_trial/assets/1d0adf3f-8b13-43fc-aed4-59d5413a8ce0.png)
4. Reproduce the issue while the profile is being recorded.
5. Please keep the tab open in the foreground until the recording finishes!.
6. Once the page loads(the problem is reproduced) click Stop.

   ![contentId-1918407593](/cms_trial/assets/a5e4a773-6ee1-4e7f-bb5c-fabb98bcb30d.png)
7. Save profile.

   ![contentId-1918407593](/cms_trial/assets/5b11bdd6-245a-4aae-9d7d-d286546be3a2.png)
8. Send us the file. It is a good idea to compress it before sending it.

### **Problems loading a blank page, a button that is not working, or unexpected behavior while using the plugin**

Step-by-step

1. Open Dev Console tool F12 on a PC or ⌥+⌘+i on a Mac.
2. Go to the Console tab in the Dev Console.

   ![contentId-1918407593](/cms_trial/assets/6cb2434c-ab2d-4783-8331-84ce53169519.png)
3. Right-click anywhere on the list, "Save as" and attach the screenshot to the support ticket.
4. if there are any items marked in red please expand and take a screenshot (see above).
5. In the support ticket

   1. Share the file
   2. Share the screenshots

## Step-by-step guide for Firefox browser

### **Network analysis** - HAR file

Step-by-step

1. Open the Dev Console tool (F12 on a PC or ⌥+⌘+K on a Mac).
2. Go to the **Network** > **XHR** tab.

   ![image-20250310-100418.png](/cms_trial/assets/3001e685-600d-4011-9bad-6cb1542c77f7.png)
3. Go to the page where the issue occurred and **reproduce the issue**. The page automatically starts recording as you navigate.
4. When ready, click **Pause/Resume recording network log**.

   ![image-20250310-100513.png](/cms_trial/assets/269fa52d-07be-4493-a6d5-275446851585.png)
5. Right-click anywhere in the **File** column and select **Save All as HAR** or click **Network settings** > **Save All as HAR**.

   ![image-20250310-100612.png](/cms_trial/assets/e4a248fb-c5cb-4900-b53a-7a65b286edad.png)![image-20250310-100651.png](/cms_trial/assets/21360151-cb08-4cf5-8aec-24debb1269b5.png)
6. If any items are marked in red, click on them one by one and take screenshots (enlarge the Dev tool window to make the data visible). Share the files in the support ticket.
7. When contacting our Support, remember to:

   1. Share the HAR file in the support ticket.
   2. Share the screenshots in the support ticket.

### **Taking Performance profile**

Step-by-step

1. Open the Dev Console tool (Shift + CTRL + J on a PC or ⌥+⌘+K on a Mac).
2. Go to the Performance tab in the Dev Console.
3. Click the record button.

   ![contentId-1918407593](/cms_trial/assets/a479628e-8e78-4598-af56-eb7de006ee51.png)
4. Reproduce the issue while the profile is being recorded.
5. Please keep the tab open in the foreground until the recording finishes!
6. Once the page loads(the problem is reproduced) click Stop.

   ![contentId-1918407593](/cms_trial/assets/ea8b376f-5007-4fcb-b5c6-f55f5aa0e0ba.png)
7. Save profile.

   ![contentId-1918407593](/cms_trial/assets/2ce350a3-d437-4f73-b9d3-447d7e9c98da.png)
8. Send us the file. It is a good idea to compress it before sending it.

### **Problems loading a blank page, a button that is not working, or unexpected behavior while using the plugin**

Step-by-step

1. Open the Dev Console tool (F12 on a PC or ⌥+⌘+K on a Mac).
2. Go to the Console tab in the Dev Console.

   ![contentId-1918407593](/cms_trial/assets/e57922a2-c608-49a3-b8ae-1a4b560af7e8.png)
3. Right-click anywhere on the list, and export all to a file.
4. if there are any items marked in red please expand and take a screenshot.
5. In the support ticket:

   1. Share the file
   2. Share the screenshots

## Step-by-step guide for the Safari browser

### **Network analysis** - HAR file

Step-by-step

1. If the Develop menu doesn't appear in the menu bar, go to **Safari Settings**.
2. Click **Advanced**.
3. Select **Show features for web developers**.

   ![image-20250310-101608.png](/cms_trial/assets/30cca82a-b0bb-4cea-94b0-d8ef4eaff77b.png)
4. Open a new Safari window.
5. From the **Develop** menu, select **Show Web Inspector**.

   ![image-20250310-101729.png](/cms_trial/assets/17c50851-31ae-46f5-98ad-4b986fee79cd.png)
6. Click the **Network** tab.
7. Go to the page where the issue occurred and **reproduce the issue**.
8. When ready, click **Export**.
9. Save the file.
10. If any items are marked in red, click on them one by one and take screenshots (enlarge the Dev tool window to make the data visible). Share the files in the support ticket.
11. When contacting our Support, remember to:

    1. Share the HAR file in the support ticket.
    2. Share the screenshots in the support ticket.

### **Taking Performance profile**

Step-bypstep

1. Enable the Developer Menu - in the Browser (Safari Menu> Preferences) and select Advanced Tab. 

   ![image-20250318-141900.png](/cms_trial/assets/de656a16-cc33-437d-b275-582ccad01c69.png)

   Open Dev Console tool ⌥ + ⌘ + C.
2. Go to the Timelines tab in the Dev Console.

   ![image-20250318-141908.png](/cms_trial/assets/357459b6-b6ea-40a8-a206-66616ebf18e9.png)
3. Click the record button.

   ![contentId-1918407593](/cms_trial/assets/032c7273-7eef-462f-99ac-94853838f9d5.png)
4. Reproduce the issue while the profile is being recorded.
5. Please keep the tab open in the foreground until the recording finishes!
6. Once the page loads (the problem is reproduced) click Stop and Save profile.

   ![contentId-1918407593](/cms_trial/assets/5ce97181-15b1-4cb3-92a5-1490cc6fb832.png)
7. Send us the file. It is a good idea to compress it before sending

### **Problems loading a blank page, a button that is not working, or unexpected behavior while using the plugin**

Step-by-step

1. Open Dev Console (⌥ + ⌘ + C).
2. Go to the Console tab in the Dev Console.

   ![contentId-1918407593](/cms_trial/assets/a75f3499-c5fb-4049-855f-fb27fbfbf090.png)
3. Attach the screenshot to the support ticket.

In case you are experiencing more complicated issues or having problems following the instructions please contact our helpful support using the customer [portal](https://appfire.atlassian.net/servicedesk/customer/portal/11)[.](mailto:support@bigpicture.on) Our team will be more than happy to assist.