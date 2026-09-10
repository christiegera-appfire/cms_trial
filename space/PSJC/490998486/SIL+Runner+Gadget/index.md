# SIL Runner Gadget

Another useful feature of Power Scripts™ for Jira is the ability to randomly run SIL™ scripts on demandusing the SIL Runner Gadget. This enables you to configure a list of scripts that can be run at any time directly from your Dashboard.

![Power Scripts for Jira Cloud gadget settings panel](/cms_trial/assets/c64b186e-970e-4c5c-82eb-393b2e91dbb9.png)

### Important!

Note that scripts run this way do not have an issue context. Therefore, constructs and keywords like "key" do not have a meaning here (they are undefined). You need to first select the issues to work with, and prefix any standard variables with the issue key.

The following pages provide information about the SIL Runner Gadget: