# Common installation issues and errors

## ⚠️ ERROR: 500 - Internal Server Error

### ❓ Problem

Why am I getting "Server Error - 500 - Internal Server Error" after a new on-premises Timetracker installation?

![Internal_Server_Error.png](/cms_trial/assets/5596f4c5-0e58-4a8e-83a0-3bce4fdcef23.png)

### 💡 Resolution

This error appears when the required version of ASP.NET Core Runtime - Windows Hosting Bundle is not installed.

| **7pace Timetracker version** | **Required minimal bundle version** | **Download link** |
| --- | --- | --- |
| 5.53 and up | 8.0.103 | [ASP.NET Core Runtime Hosting Bundle 8.0.103](https://dotnet.microsoft.com/en-us/download/dotnet/8.0) |
| 5.46 to 5.52 | 6.0.21 | [ASP.NET Core Runtime Hosting Bundle 6.0.21](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) |
| 5.11 to 5.45 | 3.1.32 | [ASP.NET Core 3.1 runtime Windows Hosting bundle](https://dotnet.microsoft.com/en-us/download/dotnet/3.1) |

Please refer to [this](/cms_trial/space/7TFA/1253539922/Installation+guide/) article to check all of the requirements for the Timetracker installation.

## ⚠️ ERROR: Could not grant access to 7pace Timetracker database for user

### ❓ Problem

During the installation and configuration process of 7pace Timetracker (on-prem), while "Applying Settings", an error appears: "*Could not grant access to 7pace Timetracker database for user ..."*

### ❗ Cause

This error displays when granting access to the 7pace Timetracker SQL database has failed. When you configure SQL connection settings as Windows Authentication, the Application Pool has to have access to TimetrackerOnlineDb on the SQL Server. the Configuration tool tries to apply these permissions during setup, but it can fail due to some specific environmental conditions (e.g. lack of permissions to do this).

The following SQL statements are being run:

```text
IF NOT EXISTS
 (SELECT name
    FROM master.sys.server_principals
   WHERE name = 'SERVICE_ACCOUNT_USER_NAME')
BEGIN
 CREATE LOGIN [SERVICE_ACCOUNT_USER_NAME] FROM WINDOWS
END

SELECT su.name AS DatabaseUsername 
  FROM sys.sysusers su 
  JOIN sys.syslogins sl ON sl.sid = su.sid WHERE sl.name = 'SERVICE_ACCOUNT_USER_NAME'

IF NOT EXISTS (
SELECT su.name as DatabaseUsername
  FROM sys.sysusers su
  JOIN sys.syslogins sl on sl.sid = su.sid
 WHERE sl.name = 'SERVICE_ACCOUNT_USER_NAME' )
BEGIN
 CREATE USER [SERVICE_ACCOUNT_USER_NAME] FOR LOGIN [SERVICE_ACCOUNT_USER_NAME] WITH DEFAULT_SCHEMA=[db_owner]
END

ALTER ROLE [db_owner] ADD MEMBER [SERVICE_ACCOUNT_USER_NAME]
```

### 💡 Resolution

- Preferred: Change the Application Pool Account user and ensure that the current user running the Configuration tool has permissions to execute the SQL statements, above.
- It is also possible to skip the step by clicking "Skip database permissions modification" and configure permissions manually after installation.

## ❓ Why can’t 7pace Timetracker find my TFS installation?

### ❓ Problem

We are unable to install 7pace Timetracker (on-prem) to our TFS 2018 (Update3) server. We’re stuck at the step: "What Microsoft Team Foundation Server should we use?" No matter what TFS Server URL we enter (we tried http, https, direct IP, localhost and combinations of these), we get an error message:

*A valid version of TFS was not found or connection to it has failed. 7pace Timetracker supports TFS 2015 Update 2 and higher. Please check that the TFS server is available and your user has rights to access it.*

How can we install this successfully?

### 💡 Resolution

The reason this issue is occurring is because of security/crypto policies. The solution is to check your security policies.

Please temporarily enable all the weak cryptos (like TLS 1.0, TLS 1.2), to check if this solves the issue with installation. You can then disable them back after configuration has completed successfully.

## ⚠️ Why do I get a Network Error/Access Denied message when trying to access Timetracker Hubs?

### ❓ Problem

Why do I get a Network Error/Access Denied message when trying to access Timetracker Hubs?

### 💡 Resolution

This error has occurred when a user attempts to access any of the TFS Timetracker hubs within the application.

Technically, this results when the browser blocks cross-domain requests (CORS) because of iframe sandboxing or to put it another way, when the target (extension) origin \***starts with**\* the TFS origin, then it is treated as being the same-origin. In this case, TFS being on the default SSL port means the port will be omitted and this defect will result.

Until this defect is fixed by Microsoft, we are recommending the current workaround to assist in alleviating the resulting network error/access denied messaging:

- Create different URL addresses for TFS in the TFS Administration Console and Timetracker in Timetracker Configuration Tool respectively, i.e. webapptfstest for TFS and webapptttest for Timetracker.

OR

- Create non-standard, differing ports for TFS in the TFS Administration Console and Timetracker in the Timetracker Configuration Tool, e.e. 4433 for TFS and 8090 for Timetracker. IMPORTANT: Please make sure that the TFS port number doesn’t start with Timetracker's port number, i.e. TFS: 844 and Timetracker: 8443; this will generate the error.

## ⚠️ Required SQL Server Permissions for Timetracker for DevOps Server

### ❓ Problem

When installing Timetracker, I get the error, below, when I run the 7pace Timetracker for DevOps Server Configuration Tool:

```text
Initializing ...OK
Setting up the extension ...OK
Setting up the legacy extension ...OK
Patching the web.config file ...OK
Creating the database ...OK
Creating the website ...ERROR
Error message:
Could not get access to the database users
InnerException: User does not have permission to perform this action.
Could not get access to the database users
InnerException: User does not have permission to perform this action.
```

Can you help?

### 💡 Resolution

If a user does not have sufficient permissions to create a user on SQL server and to add this user to the Timetracker database Configuration Tool, the error you described, above, will display.

To successfully complete the installation of Timetracker, the user making the SQL connection should have access to the following:

- **sys.database\_principals**
- **sys.sysusers**
- **sys.syslogins**

tables in SQL Server.

Additionally, this user should have permissions to Create Logins in SQL Server.

**Please note:** These permissions are required only for the configuration step, and can be reduced, if necessary, after successful setup.

## ⚠️ Why are we are getting CorruptedAuthorization errors after a fresh install of 7pace Timetracker on-prem?

### ❓ Problem

After installing Timetracker on-prem, we get the error below, many of them within the browser console:

*Error: Connection disconnected with error 'Error: Server returned an error on close: Connection closed with an error. HttpException: CorruptedAuthorization'.*

### 💡 Resolution

This error usually appears when [the IIS webSocket protocol](https://learn.microsoft.com/en-us/iis/configuration/system.webserver/websocket) is not installed and enabled on the server running 7pace Timetracker. In order to resolve it, please install the protocol and ensure that it is enabled. This protocol is a requirement for DevOps server and without it, both DevOps and Timetracker will not function correctly.