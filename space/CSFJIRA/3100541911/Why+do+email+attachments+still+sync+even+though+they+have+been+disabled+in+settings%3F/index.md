# Why do email attachments still sync even though they have been disabled in settings?

## Purpose

I have disabled **Sync email attachments** in the feature settings. Why do email attachments still sync?

## Answer

This is likely caused by the **Email-to-Case Settings** in Salesforce. If the **Save email attachments as Salesforce Files** option is enabled, attachments will still get synced because they are Salesforce files.

This occurs even if **Sync email attachments** is disabled in the Connector settings.

To prevent this from happening, you should also disable **Save email attachments as Salesforce Files** (uncheck it) in the Salesforce settings.

![contentId-3100541911](/cms_trial/assets/54b601ff-53cf-4bfd-90ad-a2d2805f220c.png)

The following tables show what happens with various combinations of Salesforce and Connector settings.

| **Save email attachments as Salesforce Files (Salesforce setting)** | **Sync email attachments** **(Connector setting)** | **Result** |
| --- | --- | --- |
| ❌ | ✅ | ✅ Email attachments will sync to Jira |
| ❌ | ❌ | ❌ Email attachments will **NOT**sync to Jira |
| ✅ | ✅ | ✅ Email attachments will sync to Jira |
| ✅ | ❌ | ✅Email attachments will sync to Jira |