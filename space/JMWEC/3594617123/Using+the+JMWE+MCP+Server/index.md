# Using the JMWE MCP Server

**The JMWE MCP server is currently in Beta** and is intended for internal and partner use. Because it is still in active development, anyone testing the MCP server should expect breaking changes and limited, if any, support through Appfire. It is highly recommended that you thoroughly test any scripts written with the JMWE MCP in a test environment.

**JMWE for Jira Cloud** now offers an MCP server for use with AI agents or through standard chat with your AI tool; the MCP server includes all context relevant to building extensions and translating JMWE-specific scripts from one programming language to another (Groovy to Nunjucks, for example). You can add the MCP server to any AI tool that supports it. The sections below detail how to add it to the most common development tools.

**Note**: The JMWE MCP is currently read-only; it cannot create JMWE extensions and any script translations it provides cannot be inserted directly into your Jira instance - they must be manually copied and pasted. Additionally, the official Atlassian Rovo MCP cannot create JMWE extensions.

### MCP features and limitations

A few details about the current features and limitations of the JMWE MCP:

- The MCP server uses a streamable HTTP URL without authentication or parameters.
- As noted above, the MCP is currently read-only when accessing your Jira instances. It can be used to assist in writing JMWE-specific scripts and, when using the Atlassian MCP, can access custom field information specific to your instance, but it cannot create Jira configurations or JMWE extensions.
- Currently, a primary use for the MCP server is to assist in JMWE migrations - either Data Center to Cloud or Cloud to Cloud. See [JMWE MCP Server in migrations](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=jmwec&title=JMWE%20MCP%20Server%20in%20migrations&linkCreation=true&fromPageId=3594617123) for more information.

## Adding the JMWE MCP server

It isn't possible to provide setup instructions for every supported tool, but the process is generally the same for most. Below are the steps for ChatGPT, Claude, and Cursor. For all tools, the MCP URL is:

```text
https://jmwe.mcp-dev.appfire.net/mcp
```

### ChatGPT

To add the JMWE MCP server to ChatGPT, make sure that Developer Mode is enabled by opening **Account Settings** → **Security and login** and toggling **Developer mode**.

Then, follow these steps:

1. In the left-hand panel, click **Plugins**. If Plugins is not available, go to **Account Settings** → **Plugins** → **Browse Plugins**.
2. Click '**+**' in the upper right corner.
3. In the **New Plugin** window, give the MCP server a Name and, optionally, a Description.
4. Select **Server URL** and enter the URL of the MCP server, listed above.
5. For **Authentication**, select **No Auth**.
6. Check the box for **I understand and want to continue**.
7. Click **Create**.

### Claude

![Customize the JMWE MCP server in Claude](/cms_trial/assets/1f45e47a-5337-46cd-bb7a-864e2a554567.png)

Adding the JMWE MCP server through the Claude web interface adds it to all versions of Claude.

1. Go to the User menu and click **Settings**.
2. In the left-hand panel, click **Connectors**. Click **Add** → **Add custom connector**.
3. In the **Add custom connector** window, give your connector a name.
4. Enter the JMWE MCP URL: `https://jmwe.mcp-dev.appfire.net/mcp`
5. Leave **Advanced settings** blank. The JMWE MCP server does not require authentication at this time.
6. Click **Add**.
7. After adding the connector, you will be prompted to connect to it. Click **Connect**.
8. Test your new connector connection by opening a new chat and asking for the capabilities of the JMWE MCP server.

### Cursor

Adding the JMWE MCP server to Cursor is done by updating `mcp.json` in your Cursor installation directory.

1. In Cursor, if **Customize** is not visible in the left-hand panel, click `Ctrl-Shift-P` to open the Command Palette. Enter “Customize” and select **Open Customize**.
2. In the Customize window, select **MCPs** below the Search bar.
3. Click **New MCP Server**.
4. Cursor opens `mcp.json`. Update it with the following connection information:

   ```json
   {
     "mcpServers": {
       "jmwe": {
         "url": "https://jmwe.mcp-dev.appfire.net/mcp"
       }
     }
   }
   ```
5. Save your changes and restart Cursor to enable your new connection.
6. Verify that **jmwe** (or whatever you named your connection) is available by clicking **+** in the chat and going to **MCP**. Make sure **jmwe** is toggled on.
7. Test your new connector connection by opening a new chat and asking for the capabilities of the JMWE MCP server.

**Success!** The MCP server is now available for use with your AI tools. In addition to the basic connection test above, you can test the MCP server with a simple prompt such as:

```text
Can you connect to the JMWE MCP server and explain its capabilities?
```