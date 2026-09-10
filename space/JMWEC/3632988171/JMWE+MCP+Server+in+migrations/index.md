# JMWE MCP Server in migrations

**The JMWE MCP server is currently in Beta** and is intended for internal and partner use. Anyone testing the MCP server should expect breaking changes and limited, if any, support through Appfire. It is highly recommended that you thoroughly test any scripts written with the JMWE MCP in a test environment.

## Using the MCP server

Before using the MCP server, you must add the connection. See [Using the JMWE MCP server](/cms_trial/space/JMWEC/3594617123/Using+the+JMWE+MCP+Server/) for more information.

The JMWE MCP server can assist with script translations during a migration from Jira Data Center to Jira Cloud. In Jira Data Center, all JMWE scripted extensions use Groovy. However, in Jira Cloud, only Nunjucks is supported for scripted extensions, with JQL also supported for some scripted configurations. In order to complete a migration, scripted extensions and configurations will need to be converted from Groovy to Nunjucks or JQL. After you run a migration, JMWE provides additional resources to streamline the process:

- The post-migration page in JMWE Cloud provides a JSON export of migration data, including automations and workflow actions.
- JMWE MCP can use this file to translate legacy Groovy scripts into Cloud-compatible Nunjucks format while preserving custom field ID mappings (converting Data Center custom field IDs to Cloud custom field IDs).
- The translation output provides both a validation report and a JSON file for direct system import.

## Translating migrated scripts

After you have completed a migration using JMCA, use the Post migration page to start the script translation process. You will need access to an AI tool such as ChatGPT, Claude, or Cursor, and you will need to be able to [add the JMWE MCP server](/cms_trial/space/JMWEC/3594617123/Using+the+JMWE+MCP+Server/) to that tool.

The **JMWE MCP server** is still in beta. You should thoroughly test using this tool in your migration process before implementing it in a production environment!

Once you’ve added the MCP server, follow these steps:

![The JMWE Cloud Post migration administration page including MCP export and import](/cms_trial/assets/111d18c1-a438-4f4a-839c-962c0397ff48.png)

1. First, export your JMWE configuration. From the **Post migration** page, click **Export configuration** in the upper right corner of the page (Figure 1, right).
2. Save the JSON file to your machine.
3. In your AI tool with the JMWE MCP server configured, add the downloaded JSON file to a new chat. Prompt the AI to convert the file using the JMWE MCP.   
   [note icon] **Note**: Make sure you have verified the connection to the MCP server and have added it to the chat, if necessary.
4. When the conversion is complete, your AI tool will provide a new JSON file with the converted scripts included. Save that file so you can upload it to your JMWE instance.
5. In the **Post migration** page, click **Import configuration** and select the converted JSON file.
6. Review each outlined change and select the changes you want to apply. Click **Apply selected changes**.

When the update is complete, return to the [Post migration](/cms_trial/space/JMWEC/465473765/Post+migration/) page to address any remaining errors. Thoroughly test your migration before moving it into Production.