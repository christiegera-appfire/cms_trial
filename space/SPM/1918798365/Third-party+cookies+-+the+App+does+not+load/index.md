# Third-party cookies - the App does not load

If BigPicture doesn't load (even though your Jira instance works), check your browser settings to ensure `softwareplant` third-party cookies are enabled. Third-party cookies are necessary for BigPicture to load properly.

`http://cloud.softwareplant.com/`has to be whitelisted in the browser.

![Screenshot of BigPicture having problems with loading.](/cms_trial/assets/d562a0d1-bbeb-4ef0-b45c-7a067cae591d.png)

## Google Chrome

1. Go to browser **Settings**.
2. Select **Privacy and security**.
3. Go to the **Third-party cookies** section.

   ![Screenshot of Google Chrome Settings.](/cms_trial/assets/b767e8c1-0c91-4884-8c0a-8b7f2b166580.png)
4. You can either:

   1. **Allow all cookies**, or
   2. **Block third-party cookies** and selectively allow `softwareplant` cookies

      1. Add either `[*.]softwareplant.com` or `http://cloud.softwareplant.com/` to sites that can always use cookies.

         ![Screenshot of Google Chrome Settings.](/cms_trial/assets/0ac3f708-8bcc-450c-9009-6a81ebe2c827.png)
      2. Or,add your cloud instance and check the Including third-party cookies on this site (warning: as you use the website, this will allow all third-party cookies, not just `softwareplant`).

         ![Screenshot of adding a site allowed to use third-party cookies.](/cms_trial/assets/fb456cb7-0c0d-4c33-a056-bd6df7d16642.png)![Screenshot of adding a site allowed to use third-party cookies.](/cms_trial/assets/a6c7b53e-84a2-4f28-a596-c5bfaec2a0f4.png)

## Mozilla Firefox

1. Go to browser **Settings**.
2. Select **Privacy and security**.
3. Scroll down to the **Cookies and Site Data** section.
4. Click **Manage Exceptions...**button.

   ![Screenshot of the Privacy and Security settings in Firefox.](/cms_trial/assets/bf022292-87f4-4dd3-a1f4-fdadb7762ecf.png)
5. Add `http://cloud.softwareplant.com/`and click **Allow.**
6. To confirm, click **Save Changes**.

   ![Screenshot of adding an exception to a Firefox browser.](/cms_trial/assets/74085697-5965-46fc-a90c-dee9de40a596.png)

## Safari

For official Apple information with instructions for different OS versions, see the [Safari User Guide](https://support.apple.com/guide/safari/manage-cookies-sfri11471/mac) page.

1. Go to **Safari** > **Preferences** and select **Privacy**.

   1. Disable **Cookies and website data** by selecting **Block all cookies**.
   2. Go to **Manage Website Data** and click **Remove All**.
2. Go to **Safari** > **Preferences**, select **Extensions**, and ensure all extensions are turned off.
3. Go to **Safari** > **Clear History**, select **All History**, and confirm by clicking **Clear History**.
4. Restart Safari (CMD + Q).

After successful completion, your **Cookies and website data** section should look like this:

![Screenshot of the Privacy tab in Safari.](/cms_trial/assets/f40fd0a4-e847-49f3-b21f-293194804a0a.png)

## Microsoft Edge

1. Go to browser **Settings**.
2. Select **Cookies and Site Preferences**.
3. Click **Manage and delete cookies and site data**.

   ![Screenshot of the Microsoft Edge Settings.](/cms_trial/assets/b07a03d4-2bf4-4f6c-a4d5-f4f869551513.png)
4. Under the **Allow** section, click **Add**.

   ![Screenshot of the Microsoft Edge Settings.](/cms_trial/assets/5a279332-d68e-4c16-8e32-7a264ff0f477.png)
5. `http://cloud.softwareplant.com/`has to be whitelisted in the browser.

   1. Add a site to the list, or
   2. Add your cloud instance and check the **Include third-party cookies on this site** box.
   3. To confirm, click **Add**.

      ![Screenshot of including third-party cookies on a site in Microsoft Edge.](/cms_trial/assets/c88fd265-63b0-453c-85c9-6acd17372156.png)