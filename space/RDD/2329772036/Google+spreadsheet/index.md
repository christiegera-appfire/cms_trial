# Google spreadsheet

## Overview

The Google spreadsheet template lets you render a table in your dashboard based on data from a connected Google spreadsheet.

It uses the Google Spreadsheets API and processes cells to form an array based on the headers.

![Dashboard Hub Dashboard Hub Google spreadsheet example](/cms_trial/assets/1a47c6c6-54e2-4d9e-ad71-a4bf4b4dfb22.png)

## Requirements

This template uses an API key; you don’t need to configure a datasource.

- **Google sheet**: The spreadsheet must be shared with Viewer permissions set to Anyone with the link.

This option is available only for personal accounts; it doesn’t work with organization accounts.

- **Google Cloud project**
- **Google API key**
- **Dashboard Hub dashboard**

## Setup

### Create the Google spreadsheet

1. Go to <https://docs.google.com/spreadsheets>.
2. Select **Blank spreadsheet**.
3. Enter a name for the spreadsheet so you can share it later.
4. Add the data you want to display in the dashboard:

   1. Enter the column headers in the first row, for example, `Product`, `Description`, `Category`.
   2. Add the corresponding data in the subsequent rows.
5. Copy the spreadsheet ID from the URL; you will need it later. For example, in the URL format: `<https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/edit`>, where `SPREADHSHEET_ID` = `1Fl8TqeZigVHGuAFxXTgGgra_DSUq0nXTMbWQOZCRNdA`.

### Make your spreadsheet public

1. Click **Share** in the top right of the spreadsheet.
2. Select **Anyone with the link**. If the Google Sheets account belongs to an organization, for example, a work or school account, this option isn’t available.
3. Set permission to **Viewer**.
4. Click **Done**.

The spreadsheet must be publicly readable for API key authentication to work. If you need help with sharing a file publicly, see Google’s [support documentation](https://support.google.com/docs/answer/2494822?sjid=4802021623131138639-EU#basics&zippy=%2Cshare-a-single-file%2Callow-general-access-to-the-file%2Cshare-a-file-or-folder-publicly).

### Create a Google Cloud project

1. Go to [Google Cloud console](https://console.cloud.google.com/welcome/new).
2. Click **Select Project**.
3. In the *Select a resource* page, click **New project**.
4. In the *New Project* page, enter a project name, then click **Create**.
5. Select the new project in the *Select a resource* page to open the project.

### Create a Google Sheets API key

1. Go to [Google Sheets API](https://console.cloud.google.com/marketplace/product/google/sheets.googleapis.com?q=search&referrer=search&organizationId=0) in the Google console.
2. Click **Enable**.
3. Go to [Google APIs & Services Credentials](https://console.cloud.google.com/apis/credentials).
4. Click **Create credentials**, then select **API key**. A key will be generated.
5. Copy the API key. You will need this later.
6. On the *Edit API key* page, select **Restrict key**.
7. Select the Google Sheets API.
8. (optional) Under *Application restrictions*, select the relevant restriction you want to apply, for example, **IP addresses**.

## Add the Google Spreadsheet gadget to your dashboard

1. Navigate to your **Dashboard Hub** dashboard.
2. Click **Edit**.
3. Click **Add Gadget**.
4. Navigate to the **Custom Reports** section in the left side navigation panel.
5. Locate the **Google Spreadsheet** gadget, click **Add,** and click **Open Editor**.

## Configure the table

1. Determine what data you want to display from your Google spreadsheet and edit the URI line in the editor. Use the format: `{SheetName}!{StartCell}:{EndCell}`  
   **Examples**:  
   `A1:Z42`: Reads columns A through Z, rows 1 through 42.  
   `Sheet1!A1:Z100`: Reads from a specific sheet.  
   `A1:Z`: Reads all rows in columns A through Z.
2. Build the API URL. Combine the sheet ID, table values, and API key that you created in Google Cloud console. Use the following format:

   ```text
   https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/{RANGE}?key={API_KEY}
   ```

**Example**:

```text
https://sheets.googleapis.com/v4/spreadsheets/1Fl8TqeZigVHGuAFxXTgGgra_DSUq0nXTMbWQOZCRNdA/values/A1:Z42?key=AIzaSyAl5NAfVNCXP4MIgsaFH4WYsVt7_6J-59g
```

## How to test the API integration

1. Copy your complete URL.
2. Paste it into a web browser.
3. You should see JSON data with your spreadsheet values.
4. If you get an error, check the following:

   - The Google spreadsheet is set to **Anyone with the link can view**.
   - The API key is correct. You can confirm this by checking the Credentials in your Google project.
   - The Google Sheets API is enabled.
   - The spreadsheet ID and range are correct.

## Troubleshooting

| **Error** | **Solution** |
| --- | --- |
| `403 Forbidden` | Make sure the spreadsheet is publicly shared |
| `400 Bad Request` | Check your spreadsheet ID and range format |
| `401 Unauthorized` | Verify your API key is correct and the Sheets API is enabled |
| `404 Not Found` | Check the spreadsheet ID exists and is accessible |

## Related pages

[Custom Reports - REST API integration](/cms_trial/space/RDD/1529219266/Custom+Reports+-+REST+API+integration/)

[Get started with Custom Reports](/cms_trial/space/RDD/1528825149/Get+started+with+Custom+Reports/)