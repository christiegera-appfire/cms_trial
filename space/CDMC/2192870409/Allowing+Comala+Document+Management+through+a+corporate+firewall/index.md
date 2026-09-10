# Allowing Comala Document Management through a corporate firewall

## Scenario

Some users access Confluence from behind a corporate firewall that restricts certain URLs.

Recent updates to Comala Document Management rely on asynchronous notifications for state changes, which require access to specific URLs.

Some features may not function as expected if the app is used behind a firewall without the necessary access.

## Solution

To ensure the app functions correctly, add the required URLs to your company’s **URL Allow List** or equivalent firewall settings.

## Comala Document Management URLs that need to be added to the corporate firewall URL Allow List

Add the following URLs to your corporate firewall’s **Allow List**:

- `https://doc-m.comalatech.app`
- `https://doc-m-cdn.comalatech.app`
- `wss://ws.async-notifications-cw.production.comala.zone`

## Comala Publishing URLs that need to be added to the URL Allow List

If you are using **Comala Publishing** for space publishing and page syncing, add these URLs as well:

- `https://publishing.comalatech.app`
- `https://publishing-cdn.comalatech.app`

Adding these URLs ensures uninterrupted access to Comala Document Management and its features.