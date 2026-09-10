# LDAP configuration

Through this integration, SIL scripts can authenticate users, retrieve user information, query organizational structures, and synchronize user attributes with your LDAP directory. This functionality supports automation workflows that leverage your existing user management infrastructure, enforce security policies, and maintain consistency across enterprise systems without manual intervention.

---

## Prerequisites

Before configuring LDAP for Power Scripts for Jira Cloud, please ensure you have:

- **Active Directory Access**: Access to your organization's MS Active Directory system.

Other LDAP systems like OpenDS might work, but are not officially supported.

- **Service Account**: An LDAP account with read permissions for directory information.
- **Connection Details**:

  - Server hostname/IP address
  - Correct port number
  - Base DN information
- **Network Access**: Ensure your Jira Cloud instance can connect to your LDAP server.
- **Schema Knowledge**: Basic understanding of your directory structure to properly query attributes.

This preparation helps you successfully establish and test your LDAP connection.

---

## Procedure

1. In your Jira Cloud instance, go to **Settings** > **Marketplace Apps** > **Power Scripts** > **Configurations**.
2. Click **Integrations** > **LDAP**.

   ![Power Scripts for Jira Cloud LDAP configuration interface](/cms_trial/assets/41263f4b-65c1-4127-a59a-018c0192b727.png)
3. Click **Add LDAP** and provide the required information:

   1. Type a unique name for your LDAP configuration.
   2. Keep the default **Directory** type selection.  
      Microsoft Active Directory is pre-selected by default as it's the only officially supported directory type. If you're using a different LDAP type, contact support for assistance.
   3. Enter the **URL** and **Base DN** for your LDAP server.
   4. In the **User** and **Password** fields, provide the credentials for the LDAP service account.  
      The username is typically in the format of a Distinguished Name or User Principal Name (e.g., "CN=ServiceAccount,OU=ServiceAccounts,DC=example,DC=com" or "[serviceaccount@example.com](mailto:serviceaccount@example.com)").
4. (Optional) In the **Connection timeout** field, set the duration in milliseconds before connection attempts timeout.  
   The default value is suitable for most environments, but you may need to increase it for slower network connections or heavily loaded directory servers.
5. Click the **Test** button to verify your configuration.  
   The system will attempt to connect to your LDAP server and display any errors directly on the page. You can make adjustments based on these error messages and test again until a successful connection is established.

Once created, the LDAP configurations can be edited, removed, and tested from the *LDAP Configuration* page.

---

## Default LDAP

You can create multiple LDAP configurations and designate one as the default by clicking the **Make Default** icon. This default configuration will be used automatically when scripts call LDAP functions without explicitly specifying a configuration name.

The default LDAP setting ensures backward compatibility with existing scripts. When older scripts that were written before the introduction of multiple LDAP configurations run, they will automatically use the default configuration without requiring modifications.

Only one LDAP configuration can be marked as default at any time.

---

## More configuration guides

## LDAP-specific functions