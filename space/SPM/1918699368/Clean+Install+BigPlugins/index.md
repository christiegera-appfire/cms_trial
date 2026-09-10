# Clean Install BigPlugins

**For rollback purposes, please back up your database before starting the upgrade process or test the new BigPicture version on an isolated environment.**

## Why?

If you want to start using our plugin afresh, here is how to make sure that there will be no old data interference after reinstall.

Simply follow the procedure below.

|  |  |
| --- | --- |
| **Applies to:** | contentId-1918699368contentId-1918699368contentId-1918699368contentId-1918699368 |

## The Procedure

1. Disable your Plugin
2. In your JIRA database, please delete all the tables, sequences, and other objects which begin with:

   1. AO\_0456E7\_ - for **BigPicture**
   2. AO\_8AC478\_ - for **BigGantt**
   3. AO\_DA6AB9\_ - for **BigTemplate**
3. Execute the following scripts:

   ```text
   select s.id id1, p.id id2
   from propertystring s
   inner join propertyentry p on p.id = s.id
   where p.property_key = 'AO_0456E7_#';



   delete from propertystring where ID = <id1>;



   delete from propertyentry where ID = <id2>;
   ```

Depending on the plugin's database you would like to alter, 'AO\_0456E7\_#' should be replaced with 'AO\_8AC478\_#' or 'AO\_DA6AB9\_#' in the script given above.

1. When the previous query returns result and there were records to delete, you have to restart Jira Server.

## In case of any problems

If you are still having trouble following these steps, or your problem is more complicated, you are always welcome to contact our Support Team via the [Service Desk](https://appfire.atlassian.net/servicedesk/customer/portal/11). We are always more than happy to help.