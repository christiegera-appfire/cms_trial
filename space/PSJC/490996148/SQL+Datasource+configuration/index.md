# SQL Datasource configuration

Data sources allow scripts to connect to external databases, expanding the possible use cases available with Power Scripts for Jira Cloud.

You can define your SQL data source in two ways:

1. A Java Naming and Directory Interface (JNDI) resource.
2. Directly through the Power Scripts for Jira Cloud interface.

This guide focuses on configuring SQL connection pools through the Power Scripts interface.

JNDI is a Java API that allows applications to look up data sources that are configured at the server level. When you create a data source directly through Power Scripts, it exists only within Power Scripts for Jira Cloud and cannot be accessed by other applications.

If both a JNDI resource and a Power Scripts interface-defined data source share the same name, the Power Scripts version takes precedence. For example, if a JNDI datasource named 'customer\_database' exists and you create a Power Scripts datasource with the same name, scripts will connect to the Power Scripts-defined database source.

## How to access the Datasources configuration

To access the Datasources configuration:

1. Click **Settings** > **Marketplace Apps**.
2. Go to **Power Scripts** > **Configurations** > **Integrations** > **Datasources**.

   ![Power Scripts for Jira Cloud comment synchronization configuration](/cms_trial/assets/908df257-355c-44d4-9a95-3d27cc92fe37.png)
3. Click **Add Datasource**.

---

## Key configuration settings

To create your datasource configuration, fill in the required fields (marked with an asterisk **\***) and any optional parameters.

| **Configuration setting** | **Description** |
| --- | --- |
| **Name** **\*** | A unique identifier for your data source. This name must be unique within Power Scripts. |
| **Database type** **\*** | The type of database system you're connecting to. Select from popular options like PostgreSQL, MySQL, Oracle, or SQL Server. |
| **JDBC URL** **\*** | The connection string that specifies how to connect to your database. This should follow the syntax required by the selected database driver. For example: jdbc:postgresql://localhost/mydb |
| **Username** **\*** | If applicable, the authentication username for connecting to your database. |
| **Password** **\*** | If applicable, the authentication password associated with the username for database access. |
| **Validation query** | The SQL query used to validate connections from the pool to ensure they're still active. |
| **Initial size** | The number of database connections created when the pool is initialized. |
| **Max Active** | The maximum number of database connections that can be allocated and used simultaneously. |
| **Max Idle** | The maximum number of database connections allowed to remain unused in the connection pool. |
| **Min Idle** | The minimum number of database connections that should be maintained in the unused connection pool. |

After completing the datasource configuration settings and parameters:

- Click **Test** to verify your connection settings before saving. This will attempt to establish a connection with your database using the provided parameters and display any errors that might occur.
- Click **Save** once your connection test succeeds to create the datasource, making it immediately available for use in your scripts.

---

## Manage datasources

The datasources screen lists all configured datasources and lets you modify, test, and remove them as needed. Changes to datasources are applied immediately. There are currently no built-in tools for monitoring SQL connection pool performance, so you'll need to use external monitoring tools specific to your database system.

**Important notes:**

- The appropriate JDBC driver must be installed in your Jira instance before creating a datasource.
- There is no warning when removing a datasource that is in use by your scripts, so take care when performing these operations.

---

## More configuration guides