# JQL Support

Power Scripts for Jira Cloud can enhance your ability to search for issues using JQL. It allows you to perform powerful and unique searches, tailored to your specific needs.

However, it’s important to point out the difference between a traditional, server-hosted JQL function and a Cloud-hosted JQL keyword. In Cloud-based environments, everything is asynchronous. Jira and Power Scripts are hosted on different platforms, and they communicate using HTTPS calls.

Integration on Cloud is based on keywords, each of which encompasses specific search functionality. A JQL **keyword** is metadata for an issue that has been evaluated and saved in Jira prior to the JQL search, asynchronously.

By default, auto-synchronization of keywords is disabled. It is recommended to enable auto-synchronization if you want to harness the true power of this feature. Details can be found on the [Keyword Syncing page](/cms_trial/space/PSJC/490997967/Keyword+Syncing/).

![Power Scripts for Jira Cloud JQL support interface](/cms_trial/assets/8b584392-ac6d-44eb-85fd-884400062b5c.png)

Enabling auto-synchronization is not the only required step. For JQL searches to be accurate, you need to synchronize the collections or issues you want to query at least one time. You can complete the synchronization by adding projects and project categories for the entire Jira instance.

![Power Scripts for Jira Cloud JQL project addition dialog](/cms_trial/assets/33c82ff8-4e29-4227-b9c4-88724bb7a04e.png)

The synchronization process can take a long time, depending on the number of enabled JQL keywords and the number of issues.

## What to synchronize

Power Scripts offers you either predefined keywords or custom ones. For optimal performance, only enable the ones you want to use.

The standard keywords can be enabled on a category basis. For example, you can’t control individual keywords; instead, you need to enable the entire category.

![Power Scripts for Jira Cloud standard JQL keywords interface](/cms_trial/assets/f24d8837-c725-40da-9b20-f5277aaa95f7.png)

For a complete list of standard predefined JQL keywords, refer to the [Standard JQL keywords](/cms_trial/space/PSJC/512229945/Standard+JQL+Keywords/) page.

[Custom keywords](/cms_trial/space/PSJC/490997951/Custom+Keywords/) are synchronized only if you enable them from their tab.

### Additional Info

- [Standard JQL Keywords](/cms_trial/space/PSJC/512229945/Standard+JQL+Keywords/)
- [Custom Keywords](/cms_trial/space/PSJC/490997951/Custom+Keywords/)
- [Keyword Syncing](/cms_trial/space/PSJC/490997967/Keyword+Syncing/)
- [Enhanced Search View with JQL Search Extensions](/cms_trial/space/PSJC/1248591910/Enhanced+Search+View+with+JQL+Search+Extensions/)
  - [Build an escalation service](/cms_trial/space/PSJC/1248395291/Build+an+escalation+service/)
  - [Identify issues related to a service desk project](/cms_trial/space/PSJC/1248133124/Identify+issues+related+to+a+service+desk+project/)
  - [Issues in a released version remain open](/cms_trial/space/PSJC/1248526344/Issues+in+a+released+version+remain+open/)
  - [Update remote links](/cms_trial/space/PSJC/1248493583/Update+remote+links/)