# Customfield_XYZ cannot be set

When using the cloud version of our app, you may encounter the following error:

*Project Key XXX - customfield\_XXXXX: Field 'customfield\_XXXXX' cannot be set. It is not on the appropriate screen, or unknown.*

**To resolve this problem, you must have Jira administrator permissions.**

![contentId-1918634926](/cms_trial/assets/d693cbf4-5926-4718-9faf-15c2db37bb2e.png)

The app is trying to use an issue field and fails because the field is missing from a Jira project screen scheme.

In the example above, the problem concerns:

- a Jira project with a key: **DP0**
- a field:**customfield\_10015**

## Classic Projects

### Find the Field Name Missing from the Screen Scheme

1. BigGantt and BigPicture may use issue custom fields. Those custom fields are configurable under **Apps > Manage your apps.**
2. From the list on the left, access **BigPicture/ BigGantt Configuration.**
3. A warning will appear. Click **Cancel** to access the App configuration.
4. Go to the **General > Fields** tab.
5. If the project in question uses **custom mapping settings**, check them specifically. As specified in the warning message, the Jira project in question has the following Key: **DP0.**
6. Switch to the **"Custom mapping"** section. Click the project name or the **Edit**button to see the settings. The custom field ID will help you quickly locate the field in question. In this case, because **customfield\_10015** was listed in the warning message, we know the **Start date** isthe field missing from the screen scheme**.**

### **Use the Project Key to Find the Project**

1. Click **Projects**> **View all projects**.
2. Enter **DP0** in the search box.
3. Open the project by clicking on its name.

### Find the Screen Scheme Associated with the Project

1. Go to the **Project settings** page.

   ![contentId-1918634926](/cms_trial/assets/023fdbdb-adaa-48c9-bbe4-e3c8b9404155.png)
2. Select **Screens**from the list on the left.

   ![contentId-1918634926](/cms_trial/assets/dff4b83c-0e17-4474-924c-aa72f0ac5c86.png)

### Find the Fields Associated with the Screen

Update the Issue Type Screen Scheme(s)

1. Click the **edit**button on the right.

   ![contentId-1918634926](/cms_trial/assets/ecb4e377-5cb6-46cc-88b3-a837d7d62669.png)
2. Click the name of the screen.

   ![contentId-1918634926](/cms_trial/assets/b91b32c6-d7b4-43d3-920d-572cb2b42d40.png)
3. You will see the list of fields associated with this screen scheme.

   ![contentId-1918634926](/cms_trial/assets/7f4c9b90-7237-433b-8abe-10548f166813.png)
4. Add the missing field (**Start date**) to the screen scheme.

   ![contentId-1918634926](/cms_trial/assets/026b9ab2-7a9f-4c37-8d6e-aaef0d282ea1.png)

Once all the issues have been addressed, clear the log by clicking the 'Clear log' button within the 'Program warnings' dialog. Even if issues have been fixed, the dialog box won't disappear until the log has been cleared.

---

## Team-managed Jira projects

Activate the toggle switch on the **BigPicture configuration > General > Fields** page. The App will run without problems, even though the fields have not been added to the issue types.

Keep in mind that the use of team-managed Jira projects is not recommended.

![contentId-1918634926](/cms_trial/assets/6f40f2ed-fe2f-4c11-a81e-a93bbf5687f1.png)

Keep in mind more than one field can be causing an issue.

![contentId-1918634926](/cms_trial/assets/f10ebeed-a051-45fb-aae0-718295fdbe2a.png)

### Check the Technical Configuration of the App

1. BigGantt and BigPicture may use issue custom fields. Those custom fields are configurable under **Apps > Manage your apps.**
2. From the list on the left, access **BigPicture/ BigGantt Configuration.**
3. A warning will appear. Click **Cancel** to access the App configuration.
4. Go to the **General > Fields** tab.
5. If the project in question uses **custom mapping settings**, check them specifically. As specified in the warning message, the Jira project in question has the following Key: **NXTGN2022.**
6. Switch to the **"Custom mapping"** section. Click on the project name or the**Edit**button to see the settings. Scroll down to find the **toggle switch**. Make sure to hit **Save.**

   ![image-2023-3-22_8-35-17.png](/cms_trial/assets/6f40f2ed-fe2f-4c11-a81e-a93bbf5687f1.png)

Once all the issues have been addressed, clear the log by clicking the 'Clear log' button within the 'Program warnings' dialog. Even if issues have been fixed, the dialog box won't disappear until the log has been cleared.

![image2021-2-4_21-53-40.png](/cms_trial/assets/d693cbf4-5926-4718-9faf-15c2db37bb2e.png)