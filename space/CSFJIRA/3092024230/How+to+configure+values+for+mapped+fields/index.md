# How to configure values for mapped fields

## Purpose

You can effectively map picklist values in Salesforce integrations by following key rules. These include understanding bi-directional and single-directional mappings, using API names for synchronization, and managing picklist value restrictions to ensure accurate data handling.

## Answer

1. Bi-directional mapping has a one-to-one relationship. 

   ![contentId-3092024230](/cms_trial/assets/15cd913e-8873-4b47-8685-c7d6bb6d69ef.png?version=1&modificationDate=1678861604147&cacheVersion=1&api=v2)
2. If the field binding is in **only** one direction, values could have a one-to-many relationship.

   ![image-20241213-125744.png](/cms_trial/assets/88ef8657-88e6-4809-a683-84b22a60afbb.png)
3. If the same value is mapped twice, it is also impossible to convert from single-directional field mapping to bi-directional.

   ![contentId-3092024230](/cms_trial/assets/12776ee6-83fa-49bf-a996-d82c3afbc7e9.png?version=1&modificationDate=1678861604438&cacheVersion=1&api=v2)![image-20241213-125954.png](/cms_trial/assets/aeaf0f1b-f051-45af-8b06-decc5924a653.png)
4. When mapping picklists values, the sync goes by API name in Salesforce.

Salesforce Picklists fields allow admins to restrict or allow values other than what's defined in the value set. If “**Restrict picklist to the values defined in the value set**” was set to false, values from outside of the list would appear on the dropdown.

![contentId-3092024230](/cms_trial/assets/4a6524ab-8e99-4e26-aa9e-22aca8e6017b.png?version=1&modificationDate=1678861604585&cacheVersion=1&api=v2)