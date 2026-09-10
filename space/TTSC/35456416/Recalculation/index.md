# Recalculation

After installing Time to SLA and defining your SLAs, the plugin will start calculating when work items change. However, you may also want to see the SLA history on your existing work items, in which case the SLA recalculation tool will be useful.

## When should you use recalculation?

- If you’ve defined a new SLA and want to see it in your old work items,
- If you have made changes in the configurations of the existing SLAs and you want them to be active in your old work items, you should either write the scope of the work item or directly select the SLA, and run the recalculation.

Doing this will prevent any errors from occurring in your existing work items.

## How to use recalculation

On this page, you can recalculate SLA data for work items created before a new SLA definition, update existing SLA data within work items after making changes to SLA definitions, and repair corrupt SLA data.

**Recalculation task limit**

Each recalculation task can handle a maximum of 20,000 work items and 10 SLA configurations. If you have over 20,000 work items or 10 SLA configurations in your recalculation task, please break them down into smaller batches.

![Time to SLA Recalculation page with recalculation settings](/cms_trial/assets/c46f6718-440e-4c37-9f8f-6235971f59f5.png)

1. **Recalculation –** Click to access the recalculation page.
2. **JQL –** Type JQL for the work items that you want to recalculate SLA data for.
3. **SLA(s) –** Select which SLAs to recalculate data for. Leave it empty to recalculate them all.
4. **Exclude Finished SLAs –** Tick this box to exclude completed SLAs from the recalculation.
5. **Start –** Click to start the recalculation.
6. **Recalculation Requests –** You can see the progress and status of your recalculation in this table.

## Related articles

[**FAQ: Recalculation**](/cms_trial/space/TTSC/36241419/FAQ%3A+Recalculation/)