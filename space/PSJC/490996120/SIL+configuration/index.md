# SIL configuration

This basic configuration page lets you specify the charset used to interpret SIL script files and the cache size of the SIL scripts.

To access the page, go to **Power Scripts** > **Settings** > **Basic** > **SIL Configuration.**  Use the respective fields to specify the following:

- The character encoding used to interpret your SIL script files.
- The memory cache size for SIL scripts. The **SIL Cache Size** setting determines how many parsed script trees are kept in memory using a Least Recently Used (LRU) algorithm. To improve performance, the system caches already parsed scripts, enabling the SIL Engine to access these pre-parsed and optimized trees directly from memory instead of reading from disk each time.

  You can disable this cache, but we do not recommend it as it will negatively impact performance. Conversely, if your installation uses many scripts, consider increasing the cache size to accommodate more parsed trees in memory for optimal performance.

![Power Scripts for Jira Cloud SIL Mail configuration interface](/cms_trial/assets/2ca38142-9bbe-4707-8ffa-a6e362680536.png)

The **SIL Home Directory** setting, which used to be part of the SIL configuration, has been moved to the [Script Storage configuration](/cms_trial/space/PSJC/490996090/Script+Storage+configuration/).

---

## More configuration guides