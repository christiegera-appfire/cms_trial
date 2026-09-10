# SQL Monitoring

System performance is like a double sided coin with the application server performance on one side and on the other would be database monitoring.

Since the Power Apps give you the ability to connect to other databases and not just the one used by the core application, this tool gives you the ability to monitor multiple databases. The chart displays both active and idle times in such a way that large utilization spikes will be easy to visually identify. If you are finding that your database is being overrun by activity it could be that adjustments will need to be made to the database connection pool. See [this link](https://confluence.atlassian.com/adminjiraserver/tuning-database-connections-938846864.html) for more information about database tuning.

However, in order for this monitoring to take place a data source must be created in the Power Apps configuration for each database to be monitored. See [this page](/cms_trial/space/PSJC/490996148/SQL+Datasource+configuration/) for more information about configuring data sources for the Power Apps.

![Power Scripts for Jira Cloud system performance monitoring interface](/cms_trial/assets/f66daf4b-dac7-46be-95e4-20e1973fdca2.png)

**See More**