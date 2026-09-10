# Restore (on the same instance)

Restore of BigPicture is not the same as a restore of Jira.

This feature does not guarantee that all Gantt, Scope, etc. data will remain the same as at the time that the dump was done due to the difference in issue states present in the environment where the dump is restored and the synchronization process. After dump restore, the state shift and synchronization may result in irreversible changes to the Jira instance.

If you want to perform a full restore, you will need to create **a backup of both**:

- Jira
- the App

To successfully perform a restore of the state of both the App and Jira, you will need to:

1. At the same time, generate backup files for:

   1. Jira
   2. the app
2. To restore:

   1. First, you need to stop the synchronization between the App and Jira
   2. Restore Jira
   3. Restore the App
   4. Activate the synchronization between the App and Jira

## Backup and restore of the App

### Create a backup of the App

1. Go to BigPicture App configuration > Advanced > **Database dumps.**

   ![image2021-12-31_14-44-10.png](/cms_trial/assets/12a1aaf8-88f4-40d9-9d54-a07d2e8bb7c0.png)
2. Press the New dump button, add a description, and confirm the process by pressing the Create dump button.

   ![contentId-3487925169](/cms_trial/assets/f3986e3e-e1a8-47e0-8398-b011fea1b361.png)
3. The new database dump should appear at the top of the list of backups (a page refresh might be needed)

### Restore the App backup on the same instance

1. Go to BigPicture App Configuration > Advanced > **Database dumps**
2. Press the **Restore**button in the line with the backup name.

   ![contentId-3487925169](/cms_trial/assets/b1a752e5-e457-4495-a8e0-1811e285a533.png)
3. Confirm the next step by selecting **Restoring saved data**and press the **Next**button.

   ![contentId-3487925169](/cms_trial/assets/fe8a57c5-f7b1-4ff7-8968-bb4bcd3fcc77.png)
4. Confirm the operation by entering the word **RESTORE**and press the **Restore**button.  
   ℹ️ **Info**: If the BigPicture instance is not new and some work has already been done on it, this work will be overwritten! BigPicture will automatically dump its current state before restoring it (so that the process can be reversed).

   ![contentId-3487925169](/cms_trial/assets/c8a7ce9b-54af-470f-bdb6-e86c6cc8850a.png)
5. The database recovery process will start.

   ![image2021-12-31_14-50-35.png](/cms_trial/assets/8fc53d30-ca8a-4465-8d84-4da96e02058a.png)
6. After the recovery process is complete, the restore is over. You can go to the BigPicture application and verify the correctness of the data.

### Additional information - application version mismatch

If the dump was done on a newer version of the application than the one on which the restore is performed, such an operation will not be allowed to be performed. In this case, an application update to a newer version (on which the restore process is made) is required.

If the dump was done on an older version of the application and is incompatible with the newer version of the application, such operation will not be allowed to be performed. In this case, an application update to a more recent version (on which the database dump is made) is required.

## Backup and restore of Jira

### Create a Jira backup and download it

#### Cloud

Go to System > Backup Manager > **Create backup for cloud**

![image2021-12-31_13-43-40.png](/cms_trial/assets/15d4a443-12be-4486-812f-f8a9bacdc980.png)

#### Server

Go to System > Backup system > **Backup**

![image2021-12-31_13-44-26.png](/cms_trial/assets/52467134-9fb3-453f-9926-72788ae595f3.png)

### Restore Jira backup on a staging environment

#### Cloud

Go to System > Restore System > **Import data**(import the Jira backup file)

![image2021-12-31_13-46-7.png](/cms_trial/assets/2a3475a6-b31d-4559-b5cb-ee7ef74cf1a9.png)

#### Server

Go to System > Restore system > restore using the Jira backup file (**Restore**)

![image2021-12-31_13-47-13.png](/cms_trial/assets/9651f048-51d9-44f1-9d8b-b649663a6d72.png)

## Stop/start the synchronization

The source of your tasks (Jira, Trello) and BigPicture App are synchronizing data. Depending on the setup, multiple scheduling BigPicture mechanisms may affect issue information (e.g., a strong dependency can reschedule a task and change its start/end dates). If you simply restore your Jira data, there is a chance that BigPicture scheduling mechanisms will immediately start updating your tasks.

Stopping the synchronization (temporarily setting the field mapping to **Not synchronized**) will give you time to perform a BigPicture restore without Jira data being affected.

### Stop

Go to **App Configuration > General > Fields**.

Ensure **all fields** (for all projects) are set to **Not synchronized.**That includes the General mapping and Custom mapping settings (per project).

Make sure to adjust both the **General synchronization settings** and **Custom synchronization settings** (per project).

Do not forget to save the changes.

![image-2023-3-22_8-12-47.png](/cms_trial/assets/dbc6cb3c-5a15-4619-ac41-d075141db245.png)