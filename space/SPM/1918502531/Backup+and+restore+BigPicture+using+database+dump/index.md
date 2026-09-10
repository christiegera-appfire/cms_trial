# Backup and restore BigPicture using database dump

Restoring BigPicture is not the same as restoring Jira.

This feature does not guarantee that all Gantt, Scope, etc. data will remain the same as when the dump was done due to the difference in work item states present in the environment where the dump is restored and the synchronization process. After the dump is restored, the state shift and synchronization may result in irreversible changes to the Jira instance.

If you want to perform a full restore, you will need to create **a backup of both**:

- Jira
- the App

To successfully perform a restore of the state of both the app and Jira, you will need to:

1. At the same time, generate backup files for:

   1. Jira
   2. the app
2. To restore:

   1. First, you need to stop the synchronization between the app and Jira
   2. Restore Jira
   3. Restore the app
   4. Activate the synchronization between the app and Jira

## Backup and restore of the App

### Create a backup of the app

1. Go to App Configuration > Advanced > **Database dumps.**

   ![image2021-12-31_14-44-10.png](/cms_trial/assets/b749ae1e-8734-4cde-ae41-ed687e7e9bfc.png)
2. Press the **New dump** button, add a description, and confirm the process by pressing the **Create dump** button.

   ![contentId-1918502531](/cms_trial/assets/4c415e33-f47d-4335-8d22-504df3b1ab28.png)
3. The new database dump should appear at the top of the list of backups (a page refresh might be needed)

### Restore the app backup on the same instance

1. Go to the App Configuration > Advanced > **Database dumps**
2. Press the **Restore**button in the line with the backup name.

   ![contentId-1918502531](/cms_trial/assets/46430c25-a9ba-430b-b55f-214b7b1b57e8.png)
3. Confirm the next step by selecting **Restoring saved data**and pressing the **Next**button.

   ![contentId-1918502531](/cms_trial/assets/4d9b366d-5176-496d-8809-2c03af0f6a92.png)
4. Confirm the operation by entering the word **RESTORE**and pressing the **Restore**button.  
     
   If the app instance is not new and some work has already been done on it, this work will be overwritten! The app will automatically dump its current state before restoring it (so that the process can be reversed).

   ![contentId-1918502531](/cms_trial/assets/a09522df-32e7-4ea6-a27d-95409893322f.png)
5. The database recovery process will start.

   ![image2021-12-31_14-50-35.png](/cms_trial/assets/28d31dd3-8bf2-42b4-ba8d-510b6c8c74ef.png)
6. After the recovery process is complete, the restore is over. You can then go to the app and verify the data's correctness.

### Additional information - app version mismatch

If the dump was done on a newer version of the app than the one on which the restore is performed, such an operation will not be allowed to be performed. In this case, an app update to a newer version (on which the restore process is made) is required.

If the dump was done on an older version of the app and is incompatible with the newer version of the app, such an operation will not be allowed to be performed. In this case, an app update to a more recent version (on which the database dump is made) is required.

## Backup and restore of Jira

### Create a Jira backup and download it

Go to System > Backup Manager > **Create backup for cloud**

![image2021-12-31_13-43-40.png](/cms_trial/assets/33a8b0ee-5b6b-44f0-ba0a-e0412ce80c4b.png)

### Restore Jira backup on a staging environment

Go to System > Restore System > **Import data**(import the Jira backup file)

![image2021-12-31_13-46-7.png](/cms_trial/assets/7e593d7d-9d28-409b-9660-9c2de93d486e.png)

## Stop/start the synchronization

The source of your tasks (Jira, Trello) and BigPicture App are synchronizing data. Depending on the setup, multiple scheduling BigPicture mechanisms may affect work item information (e.g., a strong dependency can reschedule a task and change its start/end dates). If you simply restore your Jira data, there is a chance that BigPicture scheduling mechanisms will immediately start updating your tasks.

Stopping the synchronization (temporarily setting the field mapping to **Not synchronized**) will give you time to perform a BigPicture restore without affecting Jira data.

### Stop

Go to **App Configuration > General > Fields**.

Ensure all fields (for all projects) are set to **Not synchronized.**That includes the General mapping and Custom mapping settings (per project).

Make sure to adjust both the **General synchronization settings** and **Custom synchronization settings** (per project).

Do not forget to save the changes.

![image-2023-3-22_8-12-47.png](/cms_trial/assets/d3da9f44-e3d2-4708-adbe-b72059f77b07.png)