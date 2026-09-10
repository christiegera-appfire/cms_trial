# Automatically update the custom field ID and/or name in filters

## Problem

When replacing an old custom field with a new custom field (for a variety of reasons) it can be quite cumbersome to perform the change in all the required places. In fact, it can be so cumbersome that it prohbits making the change in the first place since the amount of work si too great. This script is designed to simplify and reduce the work required by automatically updating the custom field id and/or name in saved filters this means the following areas will be updated as well

- Users personal filters
- Subscriptions
- Filters used in dashboards
- Filters used un Agile boards

## Solution

### Creating a SIL script file

1. Log in as a Jira administrator and navigate to **Administration > Add-ons > Power Plugins Configuration** > **SIL Manager**. Right-click the **silprograms** folder in the left panel of SIL Manager, click the **New** button.

   ![Power Scripts for Jira Cloud field update script configuration dialog](/cms_trial/assets/c26e4226-b392-4265-b729-d671fba91a61.png)
2. Select **New > File** option and type your new script file name. Remember to add the **.sil** extension. Save the name by checking the input box,  put this SIL™ code into the right panel.

   ![Power Scripts for Jira Cloud custom field mapping interface](/cms_trial/assets/c2fecd85-868e-4a98-9caa-ad2178c7c862.png)

   **updateFilters.sil**

   ```java
   /*******************************************************************************
   The following script will update ALL filters in Jira to use a new
   custom field id or name. This is useful when a new custom field is created
   to take the place of an old one. This method avoids using database queries
   to perform the change which can lead to data corruption.
   *******************************************************************************/

   //setting up
   struct debug {
       boolean update_id;
       boolean update_name;
       boolean test_mode;
       boolean print_log;
   }

   //flags used to test and control behavior of the script
   debug goldBug;
   goldBug.update_id = true;
   goldBug.update_name = false;
   goldBug.test_mode = true; //<<----- this must be changed in order to persist changes
   goldBug.print_log = true;

   /************************CUSTOM FIELD ID - INPUT REQUIRED**********************/
   string oldCustomFieldId = "12345"; //enter old custom field id
   string newCustomFieldId = "67891"; //enter new custom field id
   /********************CUSTOM FIELD NAME - INPUT REQUIRED************************/
   string oldCustomFieldName = "Old Field Name"; //enter old name
   string newCustomFieldName = "New Field Name"; //enter new name

   //fields used by CSV log output
   string CSV = "Times Stamp, Filter Id, Filter Name, Filter Owner, Old Query, New Query, Update Required, Updated\n";
   string format = "yyyyMMdd_hhmmss";

   //get all filters and loopt through them
   JFilter []filters = admGetAllFilters();
   for(JFilter f in filters) {
       
       //build line for CSV output log
       string temp_row = formatDate(currentDate(), format) + ", " + f.id + ", \"" + f.name + "\", " + f.owner + ", \"" + f.query + "\", ";
       
       //get query from filter
       JFilter updatedFilter = f;
       string newQuery = f.query;
       
       //update custom field id in query
       if(goldBug.update_id) {
           newQuery = replace(newQuery, "cf[" + oldCustomFieldId + "]", "cf[" + newCustomFieldId + "]");
       }
       //update custom field name in query
       if(goldBug.update_name) {
           newQuery = replace(newQuery, oldCustomFieldName, newCustomFieldName);
       }
       
       //update flags used in CSV log
       boolean updateRequired = false;
       boolean success = true;
       
       //did a change occur???
       if(f.query == newQuery) {
           //no change to filter was requires since it did not include the modified custom field
           string HTML = "Filter \"" + f.name + "\" (" + f.id + ") was <strong>not modified</strong> since it did not contain the field that requires updating.";
           runnerLog(HTML, true);
       } else {
           //filter was changed!
           updatedFilter.query = newQuery;
           updateRequired = true;
           string HTML; //container for user output
           
           //push update to filter
           if(goldBug.test_mode != true) {
               success = admUpdateFilter(updatedFilter);
           } else {
               HTML = "<strong> TEST MODE: </strong>"; //mark output with test mode text if running in test mode
           }
           
           //output to display to user
           if(success) {
               //whoopie!
               HTML = "Filter \"" + f.name + "\" (" + f.id + ") has been <strong style='color: green'>successfully</strong> updated."; //:)
           } else {
               //awwww crap!
               HTML = "<strong style='color: red'>ERROR:</strong> Filter \"" + f.name + "\" (" + f.id + ") could not be updated for an unknown reason."; //:(
           }
           runnerLog(HTML, true);
       }
       //add row to CSV log output
       CSV += temp_row + "\"" + newQuery + "\", " + updateRequired + ", " + success + "\n";
   }
   //print CSV output log
   //right click silprograms folder and select 'refresh' to see the new file
   if(goldBug.print_log) {
       printInFile("filterUpdateLog_" + formatDate(currentDate(), format) + ".csv", CSV);
   }
   ```
3. Update the required information on lines 24-28.
4. Click**Check**  to validate the syntax and **Save** your file.

   ![Power Scripts for Jira Cloud filter update automation results](/cms_trial/assets/685d72f8-a767-41c9-85fc-67c73d1411a4.png)
5. Run the script by clicking the green run button
6. Check the output in the console

   ![Power Scripts for Jira Cloud custom field ID replacement configuration](/cms_trial/assets/354f6a62-4c0d-4d71-8ecb-db79ce1b111c.png)