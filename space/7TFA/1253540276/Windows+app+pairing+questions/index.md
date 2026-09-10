# Windows app pairing questions

## Question

I'm having difficulties pairing the Timetracker Windows Apps with DevOps. After selecting the 'pair client' option on the Timetracker "Apps" page and confirming the prompts, an error pops up in the client application with the message 'An error occurred while sending the request'. What should I do?

### Answer

Sometimes, the combination of certain configurations in Windows, Firewall and Active Directory security can prevent the Timetracker Windows Client from properly authorizing in DevOps.

Please perform the following steps to see if this solves the problem:

1. Navigate to "Control Panel -> "Credential Manager".

2. Select the "Windows Credentials" tab.

3. Scroll to the "Generic Credential" group and see if you have any credentials stored there that are starting with "timetracker4:[DevOps address]".

4. If you do, please delete them and then try to authorize the Windows Client again.

5. If you're still having challenges, manually add new credentials with value at address "timetracker4:[your DevOps address with collection name]" with your login and password.

Example:

![Windows_App_Pairing.png](/cms_trial/assets/5d573564-99f0-476b-8e6b-de04a4c5dcbc.png)

## Question

I am trying to pair the 7pace Windows App but it keeps asking for my credentials and then doesn't accept them. I keep seeing the “Pairing” screen but nothing happens and then I receive an error message that says, “Could not authorize with current credentials.” Can you help?

### Answer

​​This may occur because you are missing Windows authentication in IIS. Please follow the steps outlined in the following article to troubleshoot and solve the issue:

[In IIS, why doesn't Window Authentication show up as one of the options for my web application?](https://stackoverflow.com/questions/8067448/in-iis-why-doesnt-window-authentication-show-up-as-one-of-the-options-for-my-w)

## Question

When I try to pair my desktop app with my Azure DevOps (ADO) org, I get a message that says “Pairing … Please click **Open Timetracker or Yes** to pair your client. If nothing prompts from browser, download it and run 7pace Timetracker.”

![App_Pairing.png](/cms_trial/assets/19c86076-a78f-4188-9741-33821cb12a6e.png)

But there is no extra “window” or prompts from the browser. Can you help?

### Answer

To successfully pair your 7pace Timetracker desktop app with the ADo org of your choice, please ensure that your browser’s security settings are set to allow pop-ups and prompts for external apps.

If you use Safari, for example,  go to **Settings** > **Privacy** > **Disable: Prevent cross-site tracking**. Now return to the 7pace Timetracker **Apps** page, , select **Pair Desktop App** and the popup will display. Once pairing is complete, you can re-enable the prevent cross-site tracking setting.