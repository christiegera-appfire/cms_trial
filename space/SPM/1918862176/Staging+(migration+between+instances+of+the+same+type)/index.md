# Staging (migration between instances of the same type)

Follow the steps below only if the staging environment is the same as the production environment.

- Cloud → Cloud

## Steps overview

Before proceeding, read the instructions carefully and copy all steps to the clipboard to keep it on hand.

1. Create application backup (production environment).
2. Create Jira backup (production environment).
3. Restore Jira backup on a staging environment.
4. Install the application on a staging environment.
5. Restore application backup on a staging environment.

### Step 1 - Create a BigPicture backup and download it

In this part, you need to create a BigPicture backup and download it:

1. Go to **BigPicture App configuration** > **Advanced** > **Database dumps.**

   ![Screenshot of the App configuration page.](/cms_trial/assets/cb2d9cdd-fe53-483b-8114-1a43125f3412.png)
2. Click the **New dump** button.
3. Add a description.
4. To confirm, click the **Create dump** button.

   ![Screenshot of the new database dump creation.](/cms_trial/assets/92428b38-273c-4c5f-9fca-82b3c393329e.png)
5. You can track the progress:

   ![Screenshot of the database dump creation process.](/cms_trial/assets/b6117c6a-9274-4282-8312-be1ae30e100d.png)
6. The new database dump should appear at the top of the list of backups.
7. Press the **Download**button to save the backup file to the disk (if you don't see the item on the list, refresh the page).

### Step 2 - Create a Jira backup and download it

Go to **System** > **Backup Manager** >**Create backup for cloud.**

![Screenshot of the Backup Manager section in the Jira System settings.](/cms_trial/assets/b6717ad4-267f-406d-845e-cbed97d02878.png)

### Step 3 - Restore Jira backup on a staging environment

Go to **System** > **Restore System** >**Import data**(import the Jira backup file).

![Screenshot of the Restore System section in the Jira System settings.](/cms_trial/assets/3b27c945-b1a2-4ca2-906b-85be3f9bfb40.png)

### Step 4 - Install BigPicture on a staging environment

1. Go to **Jira Apps** > **Find new apps**.
2. Search for the **BigPicture** plugin.

### Step 5 - Restore BigPicture backup on a staging environment

1. Go to **BigPicture App configuration** > **Advanced** > **Database dumps.**
2. Click **Import**.
3. Upload the app database dump.

   ![Screenshot of the App configuration page.](/cms_trial/assets/ae062ad2-7074-492a-9bfe-9916071a9104.png)
4. Press the **Restore**button in the line with the backup name.

   ![Screenshot of the restoring the App database on the App configuration page.](/cms_trial/assets/a63768ac-8a2b-4db4-ade2-0933007ac63f.png)
5. Confirm the next step by selecting **Migrating between instances,** **e.g., production to staging,** and press the **Next**button.

   ![Screenshot of Database dump restore info panel.](/cms_trial/assets/47a1cec0-4276-4269-83bb-64b62b9b8f19.png)
6. Check the confirmation box and press the **Next**button.

   ![Screenshot of Dump restore info panel.](/cms_trial/assets/0c33188a-49f8-455b-846f-5835ee804414.png)
7. Confirm the operation by entering the word **RESTORE** and clicking the **Restore**button.

   If the app instance is not new and some work has already been done, this work will be overwritten! The app will automatically dump its current state before restoring it (so the process can be reversed).

   ![Screenshot of confirming the database dump restore.](/cms_trial/assets/5507a3b2-2fbb-438b-b41c-f6d5cad46939.png)
8. The database recovery process will start.  
   After the recovery process, the migration from one instance to another is over. You can then go to the BigPicture application and verify the data's correctness.

   ![Screenshot of the database recovery process.](/cms_trial/assets/0583eb36-92c2-42a9-8c9b-d920de0e4e6f.png)

## Additional information

### Instance status after restore

Any integration instances after the restore operation will be in a ‘not operational’ state.  
This mechanism prevents a situation where two applications make changes in the same integration instance simultaneously.

To activate selected integrations:

1. Go to **App Configuration** > **Integrations** > **Connections**.
2. Move the switch in the **Active** column.

   ![Screenshot of Connections panel in the BigPicture Advanced configuration.](/cms_trial/assets/746a7837-7570-4da7-830c-009815e24075.png)