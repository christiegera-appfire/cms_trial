# Script Security configuration

The *Script Security* page in Power Scripts for Jira Cloud enables you to control who can access and execute scripts, especially through remote REST API calls.

By default, only administrators have permission to execute any script. However, you might need to grant specific execution permissions to other users or systems for particular scenarios. External systems and users can run scripts remotely by calling the script engine using REST.

Carefully consider security implications before granting additional permissions

To access the *Script Security* page, click **Power Scripts** > **Settings** > **Security**. The security configuration offers three main permission types, accessible by clicking the respective button:

| **Permission type** | **Description** |
| --- | --- |
| **Grant inline exec** | Controls who can execute code that is passed remotely (not stored in the system). The system identifies this type of code execution with the internal identifier `kepler://inline-source`.  While it’s always recommended to be wary of granting execution rights to non-privileged users, take particular caution with the **Grant inline exec** permissions, as these allow users to run any code they submit, not just pre-approved scripts. |
| **Grant read** | Controls who can view script content; can be assigned to specific users or groups for individual pre-approved scripts. |
| **Grant exec** | Controls who can execute stored scripts via REST and applies specifically to remote execution [scenarios.](http://scenarios.It) It can be assigned to specific users or groups for individual pre-approved scripts. |

If the *Script Security*page displays a *Nothing here* message, this indicates that no additional permissions have been granted beyond the defaults.

![Power Scripts for Jira Cloud snippet configuration dialog](/cms_trial/assets/905483e1-3a0f-4cd2-b52b-f77d5de5136a.png)

- The *Nothing here* message indicates no additional permissions have been granted beyond the defaults

---

## More configuration guides