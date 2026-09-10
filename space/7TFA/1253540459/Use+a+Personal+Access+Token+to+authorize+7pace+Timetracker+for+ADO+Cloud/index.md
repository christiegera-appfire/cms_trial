# Use a Personal Access Token to authorize 7pace Timetracker for ADO Cloud

Use the following steps to authorize 7pace Timetracker using a personal access token:

1. Install 7pace Timetracker.

   ![7pace Timetracker installer with the Install button.](/cms_trial/assets/fe65eabe-0648-4870-8d1e-d09b1b2b2a3a.png)
2. Specify where you want to store your data and click **Continue** to agree to the EULA.

   ![Installation options page with the Continue button.](/cms_trial/assets/1d3024ca-4399-4b4e-97b3-81b5eb968a28.png)
3. Click **Authorize now**.

   ![7pace Timetracker prompting the user to authorize the application.](/cms_trial/assets/93404f4e-0515-4c84-95a7-36eae8324054.png)
4. Open the *Authorize (Personal Access Token)* tab and then click the **Personal Access Token in DevOps User Settings** link. Note that 7pace Timetracker requires the following scopes:

   1. User Profile (read)
   2. Work Item (read & write)
   3. Identity (read)![Authorization window showing the Personal Access Token tab and the link to Azure DevOps user settings.](/cms_trial/assets/9e7bc9d2-89ce-4b51-8eec-d05215538c7c.png)
5. Click the **+ New Token** button.
6. Enter a name for the new token, check the **Read** box under **Work Items**, and then click **Show all scopes** at the bottom of the page.

   ![Azure DevOps page for creating a new personal access token.](/cms_trial/assets/61423072-f198-4c60-a0d5-7faa9d0d2e5f.png)
7. Scopes are listed in alphabetical order. Select the following permissions:

   1. **Identity** > **Read**
   2. **User Profile** > **Read**
8. Click **Create**.
9. Copy the token.

   ![Success window showing the newly created personal access token.](/cms_trial/assets/db488531-e4be-4546-bec2-512b9faaf3d6.png)
10. Close the token window.
11. Open the **Authorize 7pace Timetracker** browser window and paste the token.
12. Click **Authorize**.

    ![Authorization page with the personal access token entered and the Authorize button available.](/cms_trial/assets/896c57e2-6e68-4352-891b-ddcddeea128a.png)