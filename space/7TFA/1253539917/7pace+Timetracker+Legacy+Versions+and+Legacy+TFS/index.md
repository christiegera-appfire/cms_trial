# 7pace Timetracker Legacy Versions and Legacy TFS

Use this page to locate 7pace Timetracker versions compatible with legacy Team Foundation Server (TFS) before 2015 Update 2.1 and where to access our legacy docs wiki.

## Legacy 7pace Timetracker documentation

Access our legacy documentation wiki [here](https://dev.azure.com/7pace-docs/Timetracker/_wiki/wikis/Timetracker.wiki).

## Legacy Team Foundation Server (TFS) versions

Microsoft introduced the Team Foundation Server (TFS) Extension Model in the fall of 2015, with the release of 2015 Update 2. Before that, TFS libraries and interfaces changed frequently. The Extension Model guarantees a stable interface for extension publishers. This interface was adjusted for the last time in 2015 Update 2.1.

All releases of 7pace Timetracker marked as "for the Extension Model" are compatible with every release of TFS, starting from 2015 Update 2.1 - including TFS 2017, TFS 2018, Azure DevOps Server 2019, and Azure DevOps Server 2020 (following the new naming introduced by Microsoft in late 2018).

If you are using a version of TFS before 2015 Update 2.1, please identify your version of Team Foundation Server from the list below to see what versions of 7pace Timetracker are available.

[Downloads for TFS 2015 Update 2](https://dev.azure.com/7pace-docs/Timetracker/_wiki/wikis/Timetracker.wiki/162/Download-Timetracker-for-TFS-2015-Update-2)

[Downloads for TFS 2015 Update 1](https://dev.azure.com/7pace-docs/Timetracker/_wiki/wikis/Timetracker.wiki/164/Download-Timetracker-for-TFS-2015-Update-1)

[Downloads for TFS 2015 RTM](https://dev.azure.com/7pace-docs/Timetracker/_wiki/wikis/Timetracker.wiki/166/Download-Timetracker-for-TFS-2015-RTM)

[Downloads for TFS 2013 Update 2 - Update 5](https://dev.azure.com/7pace-docs/Timetracker/_wiki/wikis/Timetracker.wiki/168/Download-Timetracker-for-TFS-2013-Update-2-5)

[Downloads for TFS 2013 RTM and Update 1](https://dev.azure.com/7pace-docs/Timetracker/_wiki/wikis/Timetracker.wiki/159/Download-Timetracker-for-TFS-2013-RTM-and-Update-1)

[Downloads for TFS 2012 Update 4](https://dev.azure.com/7pace-docs/Timetracker/_wiki/wikis/Timetracker.wiki/161/Download-Timetracker-for-TFS-2012-Update-4)

## Update procedure for DevOps Server (on-prem) with Timetracker 2.x

You can update ADO Server while keeping 7pace Timetracker 2.x installed if you are not crossing releases/updates of Microsoft Team Foundation Server with architecture changes.

Before you update DevOps Server, please carefully read the information in this article. If you are not sure what to do, always use the "Safe Update" as explained below.

Please note that Microsoft introduced architecture changes in the following versions of ADO Server:

- Microsoft DevOps Server 2012 Update 3
- Microsoft DevOps Server 2013 RTM
- Microsoft DevOps Server 2013 Update 2
- Microsoft DevOps Server 2015 RTM
- Microsoft DevOps Server 2015 Update 1

Microsoft DevOps Server 2012 Update 3 is the initial platform supported by 7pace Timetracker for DevOps Server.

If you are updating ADO Server and crossing one of these milestone releases, please uninstall 7pace Timetracker before you update ADO Server using the steps explained in the Safe Update of Microsoft Team Foundation Server section.

### **Safe Update of Microsoft Team Foundation Server**

Here are detailed steps on how to proceed:

1. Uninstall 7pace Timetracker from installed programs.
2. Perform the want update of Microsoft ADO Server.
3. Visit www.7pace.com/download to download the latest version of 7pace Timetracker for the updated platform of ADO Server.
4. Install 7pace Timetracker.

## Update procedure for DevOps Server with Timetracker version 3 and above

Before 7pace Timetracker version 3, you had to uninstall 7pace Timetracker before updating your ADO Server.

You can now update the ADO Server while keeping 7pace Timetracker installed. With version 3.0 and above, you don’t have to uninstall 7pace Timetracker before beginning your ADO Server update.

You might, however, need to reapply the 7pace Timetracker extension after the update. To do this, simply run the 7pace Timetracker configuration tool, open any setting without changing it, and click Save.

For more information on 7pace Timetracker for DevOps Server (on-prem) Installation and Configuration, check out our user documentation [here](/cms_trial/space/7TFA/1253539922/Installation+guide/).