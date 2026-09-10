# Post-functions fail with a security error if the add-on user does not belong to the Issue security schemes of the project

## Problem

If the add-on user does not belong to the Issue Security schemes of your project, the add-on loses access to the project and therefore the post-function will fail with a security error.

## Solution

Manually add the add-on user to each security level of every Issue security scheme. See [here](/wiki/spaces/JMWEC/pages/78481262/Verifying+Your+JIRA+Instance#%5BinlineExtension%5D3.-Check-your-Issue-Security-schemes) to know how to fix it.

## Related articles

|  |  |
| --- | --- |
| Related issues |  |