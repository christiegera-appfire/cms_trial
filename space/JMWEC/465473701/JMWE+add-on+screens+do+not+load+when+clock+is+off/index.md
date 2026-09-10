# JMWE add-on screens do not load when clock is off

## Problem

All add-on pages (such as post-function configuration panels) stop loading. You just see the loading icon and message. This happens when the clock of the computer you use to connect to JIRA is off by more than 2 minutes.

This is caused by a JIRA bug (<https://ecosystem.atlassian.net/browse/AC-2205>).

## Solution

Make sure you update your system clock (using automatic time setting through NTP is recommend) on the computer you use to connect to JIRA. If your PC is on a domain, make sure you update the time on the domain server.

## Related articles

|  |  |
| --- | --- |
| **Related issues** |  |