# Remote systems configuration

You can trigger remote SIL script execution using the `call()` function, specifying the configured remote system name as a parameter, creating a powerful option for coordinating workflows across multiple Atlassian instances.

---

## How to add a remote system

1. In your Jira Cloud instance, go to **Power Scripts** > **Configurations**.
2. Click **Integrations** > **Remotes**.
3. Click **Add Remote** andfill in the required fields:

   1. **Name**: Create a unique name for this remote system.
   2. **Remote URL**: Enter the base URL of the remote system following the format `https://<server>:<port>/<context>`.
   3. **Username** and **Password**: Provide your credentials for authenticating with the remote system.
   4. (Optional) **Timeout**: Specify the initial response time limit in milliseconds before the system considers the remote connection attempt failed.
   5. (Optional) **Check result**: Define the interval in milliseconds between polling attempts for asynchronous remote execution results; lower values may reduce overall execution time but increase CPU usage.
   6. (Optional) **Use Proxy**: Enable proxy server configuration for connecting to remote systems outside your network. When turned on, the proxy settings become available for setup.  
      See [How to configure the proxy settings](/cms_trial/space/PSJC/490996050/Remote+systems+configuration/) below for additional information.
4. Click **Save**.  
   The integration displays as a new entry on the *Slack Configurations*page.

---

## How to manage remote systems

You can modify or remove a configuration at any time by clicking the **Edit** or **Delete** icons. Changes to the configuration are applied immediately.

---

## How to configure the proxy settings

If your network requires a proxy server to reach remote systems, you must configure the following proxy settings:

- **Proxy URL**: Enter the complete URL of the proxy server.
- **Realm**: Specify the authentication realm if required by your proxy.
- **Proxy host** and **Proxy port**: Provide the hostname/IP address and port number of the proxy server.
- **Proxy username** and **Proxy user password**: Enter the username and password for proxy authentication.

Contact your network administrators to obtain the correct proxy configuration details for your environment. Simply entering placeholder values will not establish a working connection.

---

## More configuration guides