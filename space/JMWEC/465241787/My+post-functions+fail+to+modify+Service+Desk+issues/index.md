# My post-functions fail to modify Service Desk issues

## Problem

My post-functions don't seem to be doing anything when operating on JIRA Service Desk issues, and I see 403 `You do not have the permission to see the specified issue` errors in the [logs](/cms_trial/space/JMWEC/465503894/Help+and+Support/).

## Solution

Manually fix *Permission Scheme* for the Service Desk projects. See [here](/wiki/spaces/JMWEC/pages/78481262/Verifying+Your+JIRA+Instance#%5BinlineExtension%5D2.-Check-your-Permission-schemes) for instructions.

## More info

[**JSDECO-14**](https://ecosystem.atlassian.net/browse/JSDECO-14)

## Related articles

|  |  |
| --- | --- |
| Related issues |  |