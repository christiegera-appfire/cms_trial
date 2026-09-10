# Embed Jira dashboards in Google Sites, SharePoint, and Microsoft Teams

## Overview

Dashboard Hub allows external and secure dashboard sharing with Public Links, which can be used to easily embed these dashboards in your Google Sites, Sharepoint Sites, or Teams.

Learn more about [sharing dashboards externally with secure links](/cms_trial/space/RDD/146310576/Share+a+dashboard+with+a+public+link/).

## How to add a Jira dashboard in Google Sites

1. Create a dashboard in Dashboard Hub and copy your public link.
2. Log in to your Google Sites and click the **Embed** icon.
3. Paste the public link in the URL.
4. Click **Insert**.
5. Click **Publish**.

![Dashboard Hub dashboard embedded in a Google Sites page via public link](/cms_trial/assets/eb1950de-bf24-4ca0-9fe6-a7f0d5db0148.png)

## How to add a Jira Dashboard in SharePoint

1. Copy your public link to the dashboard.

![Dashboard Hub public link copy dialog for sharing dashboards externally](/cms_trial/assets/3411ff5e-7a46-405b-a5c8-472363e5de39.png)

1. Wrap it around an iframe code as shown below:  
   `<iframe src="your public dashboard link" width="100%" height="600px" frameborder="0" allowfullscreen></iframe>`
2. Navigate to Sharepoint, then click **Web links** > **Embed**.
3. Paste the code into the code box, then click any whitespace outside the box.
4. Publish the page.

   ![Dashboard Hub dashboard embedded in a SharePoint page using iframe code](/cms_trial/assets/8a21a81b-4ed2-4f97-9ba7-2f3418ba9a42.png)
5. You should allow the domain under the *Site Settings* to see the dashboard. To do this, click **HTML field Security** and add the domain here.

   ![Dashboard Hub SharePoint HTML field Security settings for allowing embedded dashboard domain](/cms_trial/assets/07a0e94f-b2ec-4442-a459-c25e77bed0f0.png)

For testing purposes, we allowed all domains (the second option).

![Dashboard Hub dashboard successfully displayed in SharePoint after domain configuration](/cms_trial/assets/454a9df2-dc84-4500-b5a3-9826cf953821.png)