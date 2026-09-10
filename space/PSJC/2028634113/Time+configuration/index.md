# Time configuration

Thе *Time Configuration* page in Power Scripts for Jira Cloud lets you set fundamental time-related parameters that affect how scripts process date calculations. These time settings ensure that all scripts process dates and times consistently across your Jira instance, especially important in automated workflows involving deadlines or time-based calculations.

To access the page, go to **Power Scripts** > **Settings** > **Time**. Use the respective fields to specify the following:

- **Time Zone**: The base timezone used for all date calculations in your SIL scripts. All dates processed in a SIL script will be affected by the timezone setting. This setting is particularly important for scripts that perform date calculations or time-based operations.
- **Work Hours per Day**: The standard number of working hours in a business day. This value reflects the working hours per day as set in your Jira configuration; it cannot be modified from this page.
- **Work Days per Week**: How many days are considered working days in a week. This value reflects the working days per week as set in your Jira configuration; it cannot be modified from this page.

![Power Scripts for Jira Cloud SSL certificate settings](/cms_trial/assets/847aa378-cd71-4a54-9912-77d6dab91955.png)

The **Work Hours per Day** and **Work Days per Week** settings are synchronized with your Jira's time tracking configuration and cannot be changed from the *Time Configuration**page*. To modify them, navigate to the *Time tracking* page in your Jira admin settings.

---

## More configuration guides