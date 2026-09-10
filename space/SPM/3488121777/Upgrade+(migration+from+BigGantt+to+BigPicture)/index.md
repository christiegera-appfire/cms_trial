# Upgrade (migration from BigGantt to BigPicture)

The instructions below are for a switch from BigGantt to BigPicture only (within the same Jira instance).

If you want to generate a BigGantt dump for one Jira instance and import it to BigPicture on a different Jira instance, take a look at the [Staging (migration between instances of the same type)](/cms_trial/space/SPM/1918862176/Staging+(migration+between+instances+of+the+same+type)/) instructions.

## Steps overview

Before you proceed, please read the following instructions carefully and copy all the steps to a clipboard to keep them at hand. Make sure to complete each step:

1. Create a backup of the BigGantt data.
2. Download the BigGantt backup to your machine.
3. Turn off BigGantt.
4. Install BigPicture.
5. Restore the BigGantt backup in BigPicture.

---

### Steps 1 & 2 - create a BigGantt backup and download it

1. Go to BigGantt App Configuration > Advanced > **Database dumps.**

   ![image2021-12-31_9-51-15.png](/cms_trial/assets/0865ed99-ec8e-44be-a361-abb06cb85731.png)
2. Press the **New dump**button, add a description and confirm (**Create dump**button).

   ![contentId-3488121777](/cms_trial/assets/34ae134e-19af-4b92-b948-e95761655790.png)

   Wait for the process to finish:

   ![contentId-3488121777](/cms_trial/assets/b027ffbb-8533-4ab0-ab51-548cd325a3e4.png)
3. The newly created database dump should appear at the top of the list (page refresh may be needed).
4. **Download**the file and save it on your machine.

   ![contentId-3488121777](/cms_trial/assets/41d95bb4-2d36-4d47-ba99-6005f0cd243d.png)

### Steps 3 & 4 - turn off BigGantt and install BigPicture

1. Go to Jira Administration > Manage Apps.

   ![contentId-3488121777](/cms_trial/assets/e3225a28-c0ed-4a13-8b7e-0a2a6e75228a.png)
2. Disable BigGantt

   ![contentId-3488121777](/cms_trial/assets/caf03f77-85b4-4668-aac8-620980a932dc.png)
3. Install the BigPicture plugin.
4. Enter a valid license.
5. Run the BigPicture plugin to start the database configuration process.

   ![contentId-3488121777](/cms_trial/assets/43ad3350-3866-4682-aed4-7ae46f75dee7.png)![contentId-3488121777](/cms_trial/assets/e38f23f9-897a-4ec7-bda3-211ff956ca8d.png)

### Step 5 - Restore BigGantt database in BigPicture plugin

1. Go to BigPicture Configuration> Advanced > **Database dumps.**
2. Upload the BigGantt dump you created earlier to BigPicture (**Import**button).

   ![contentId-3488121777](/cms_trial/assets/bcab8360-25ae-4b86-95bc-fa92a0b13214.png)![contentId-3488121777](/cms_trial/assets/242864cd-6942-47c3-b8b1-d5b64112af7f.png)