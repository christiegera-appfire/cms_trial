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

   Image — asset pipeline pending  
   image-20250307-090941.png
5. Ensure that Google Chrome is recording. A **red button** indicates that a recording is already in progress. If the button is grey, click **Record network log**.

   Image — asset pipeline pending  
   image-20250307-091255.png
6. Clear any existing logs by clicking **Clear network log**.

   Image — asset pipeline pending  
   image-20250307-091621.png
7. Go to the page where the issue occurred and **reproduce the issue**.
8. Click **Export HAR** to export the file as HAR.

   Image — asset pipeline pending  
   image-20250307-092302.png
9. If any items are marked in red, click on them one by one and take screenshots (enlarge the Dev tool window to make the data visible). Share the files in the support ticket.

   Image — asset pipeline pending  
   image-20250307-092556.png

   Image — asset pipeline pending  
   image-20250307-092724.png
10. When contacting our Support, remember to:

    1. Share the HAR file in the support ticket.
    2. Share the screenshots in the support ticket.

### **Taking Performance profile**

Step-by-step

1. Open the Dev Console tool (F12 on a PC or ⌘+⌥+i  on a Mac).
2. Go to the Performance tab in the Dev Console.
3. Click the record button.

   Image — asset pipeline pending  
   contentId-1918407593
4. Reproduce the issue while the profile is being recorded.
5. Please keep the tab open in the foreground until the recording finishes!
6. Once the page loads (the problem is reproduced) click Stop.

   Image — asset pipeline pending  
   contentId-1918407593
7. Save profile.

   Image — asset pipeline pending  
   contentId-1918407593
8. Send us the file. It is a good idea to compress it before sending it.

### **Problems loading a blank page, a button that is not working, or unexpected behavior while using the plugin**

Step-by-step

1. Open the Dev Console tool (F12 on a PC or ⌘+⌥+i on a Mac).
2. Go to the Console tab in the Dev Console.

   Image — asset pipeline pending  
   contentId-1918407593
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

   Image — asset pipeline pending  
   image-20250310-094646.png
5. Ensure that Microsoft Edge is recording. A **red button** indicates that a recording is already in progress. If the button is grey, click **Record network log**.

   Image — asset pipeline pending  
   image-20250310-094803.png
6. Clear any existing logs by clicking **Clear network log**.

   Image — asset pipeline pending  
   image-20250310-094837.png
7. Go to the page where the issue occurred and **reproduce the issue**.
8. Click **Export HAR** to export the file as HAR.

   Image — asset pipeline pending  
   image-20250310-095101.png
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

   Image — asset pipeline pending  
   contentId-1918407593
4. Reproduce the issue while the profile is being recorded.
5. Please keep the tab open in the foreground until the recording finishes!.
6. Once the page loads(the problem is reproduced) click Stop.

   Image — asset pipeline pending  
   contentId-1918407593
7. Save profile.

   Image — asset pipeline pending  
   contentId-1918407593
8. Send us the file. It is a good idea to compress it before sending it.

### **Problems loading a blank page, a button that is not working, or unexpected behavior while using the plugin**

Step-by-step

1. Open Dev Console tool F12 on a PC or ⌥+⌘+i on a Mac.
2. Go to the Console tab in the Dev Console.

   Image — asset pipeline pending  
   contentId-1918407593
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

   Image — asset pipeline pending  
   image-20250310-100418.png
3. Go to the page where the issue occurred and **reproduce the issue**. The page automatically starts recording as you navigate.
4. When ready, click **Pause/Resume recording network log**.

   Image — asset pipeline pending  
   image-20250310-100513.png
5. Right-click anywhere in the **File** column and select **Save All as HAR** or click **Network settings** > **Save All as HAR**.

   Image — asset pipeline pending  
   image-20250310-100612.png

   Image — asset pipeline pending  
   image-20250310-100651.png
6. If any items are marked in red, click on them one by one and take screenshots (enlarge the Dev tool window to make the data visible). Share the files in the support ticket.
7. When contacting our Support, remember to:

   1. Share the HAR file in the support ticket.
   2. Share the screenshots in the support ticket.

### **Taking Performance profile**

Step-by-step

1. Open the Dev Console tool (Shift + CTRL + J on a PC or ⌥+⌘+K on a Mac).
2. Go to the Performance tab in the Dev Console.
3. Click the record button.

   Image — asset pipeline pending  
   contentId-1918407593
4. Reproduce the issue while the profile is being recorded.
5. Please keep the tab open in the foreground until the recording finishes!
6. Once the page loads(the problem is reproduced) click Stop.

   Image — asset pipeline pending  
   contentId-1918407593
7. Save profile.

   Image — asset pipeline pending  
   contentId-1918407593
8. Send us the file. It is a good idea to compress it before sending it.

### **Problems loading a blank page, a button that is not working, or unexpected behavior while using the plugin**

Step-by-step

1. Open the Dev Console tool (F12 on a PC or ⌥+⌘+K on a Mac).
2. Go to the Console tab in the Dev Console.

   Image — asset pipeline pending  
   contentId-1918407593
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

   Image — asset pipeline pending  
   image-20250310-101608.png
4. Open a new Safari window.
5. From the **Develop** menu, select **Show Web Inspector**.

   Image — asset pipeline pending  
   image-20250310-101729.png
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

   Image — asset pipeline pending  
   image-20250318-141900.png

   Open Dev Console tool ⌥ + ⌘ + C.
2. Go to the Timelines tab in the Dev Console.

   Image — asset pipeline pending  
   image-20250318-141908.png
3. Click the record button.

   Image — asset pipeline pending  
   contentId-1918407593
4. Reproduce the issue while the profile is being recorded.
5. Please keep the tab open in the foreground until the recording finishes!
6. Once the page loads (the problem is reproduced) click Stop and Save profile.

   Image — asset pipeline pending  
   contentId-1918407593
7. Send us the file. It is a good idea to compress it before sending

### **Problems loading a blank page, a button that is not working, or unexpected behavior while using the plugin**

Step-by-step

1. Open Dev Console (⌥ + ⌘ + C).
2. Go to the Console tab in the Dev Console.

   Image — asset pipeline pending  
   contentId-1918407593
3. Attach the screenshot to the support ticket.

In case you are experiencing more complicated issues or having problems following the instructions please contact our helpful support using the customer [portal](https://appfire.atlassian.net/servicedesk/customer/portal/11)[.](mailto:support@bigpicture.on) Our team will be more than happy to assist.