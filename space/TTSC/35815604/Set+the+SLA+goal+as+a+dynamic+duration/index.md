# Set the SLA goal as a dynamic duration

Dynamic duration is a Jira custom field. When you enter a time string here, Time to SLA will set the SLA duration as the input entered in this field.

This lets users enter different SLA goals for each work item. If you have changing SLA durations per work item, you can use this function to set SLA duration dynamically. The SLA clock will count according to this field.

### Step 1: Create the field

To set an SLA goal as a Dynamic duration, you need to create a field that will store the SLA duration beforehand. This field will appear only in the screens you select while creating the field, regardless of whether you designate the SLA goal as Dynamic duration or not.

1. Open **Jira** **Settings** > **Work items**.
2. Click **Fields** in the side menu.
3. Click **Create new field**.
4. For **Field type**, select **Short text** **(plain text only)**.

   ![Time to SLA dynamic duration goal configuration page](/cms_trial/assets/a88695b0-2b2e-4a16-adb0-4f45852c2efe.png)
5. Give the field a **Name**.
6. Click **Create.**
7. Go to the field you created, click the actions button, then select **Add field to screen**.
8. Tick the screens on which you want the duration field to appear. The field will **only** be in the screens that you selected.
9. Click **Update**.

Now, you can see the field you’ve createdin the Dynamic duration dropdown menu while defining or updating an SLA.

### Step 2: Set the SLA goal as a Dynamic duration

1. While defining the SLA, go to the **SLA Goals** section**.**
2. Click **+ Add goal**.
3. Fill out the goal requirements.
4. For *Goal Target Type*, select **Dynamic Duration**. The *Field* dropdown appears.
5. Click the dropdown menu to see all of the possible date fields, and select the field you created in the first step.

   ![Time to SLA dynamic duration field selection dialog](/cms_trial/assets/b4da74c7-e935-47c6-8baa-cf540ed750e4.png)

Your Dynamic duration has been set.

### (Optional) Set a default value in the duration custom field

1. Open **Jira Settings** > **Work items** > **Fields**.
2. Click the actions button in the row of theduration field you created.
3. Select **Contexts and default values**. The *Configure custom field*page displays.
4. Click **Edit Default Value.** The *Jira Set Custom Field Defaults*screen displays.

   ![Time to SLA dynamic duration goal settings with selected field](/cms_trial/assets/a0513571-7e6b-44e0-ae16-510564b3906a.png)
5. Enter a value for the duration field.

   ![Time to SLA dynamic duration validation message](/cms_trial/assets/b0756a97-ea67-44e0-87d4-f01293a88105.png)
6. Click **Set Default**.