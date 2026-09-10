# Cloning and importing problems

Exception when trying to create JIRA issue project key

The most common reason for the cloning/import process to fail is related to **Jira Field Configuration.**

The "Required" fields must be changed to "Optional" when the App is cloning/importing the program.

Keep in mind the change of the Field Configuration scheme has to be applied to the target Jira project (the project issues get copied to).

![contentId-1918406270](/cms_trial/assets/4aefcb3a-26f3-4489-a6dc-9fb58ad8e3d1.png)

We recommend creating a temporary scheme instead of changing an existing one. This way, other projects will not be affected. Then, when needed, you apply a "temporary" configuration to a project instead of changing an existing configuration (many projects may use that) to minimize the impact.

![contentId-1918406270](/cms_trial/assets/d3e0e9e3-29ec-4cc9-9bf5-8afb900ec72c.png)

To make things easier, you may copy an existing configuration:

![View-Field-Configurations-partyzant2 (2).png](/cms_trial/assets/c75657da-1954-4751-9882-726c3da89d3d.png)

Name it to make things clear for other users:

![Copy-Field-Configuration-partyzant2.png](/cms_trial/assets/b95975f0-9332-4ca7-a071-e4dc0a5bcff4.png)

Click on the field configuration name and change all items to **"optional"** within it:

![View-Field-Configurations-partyzant2 (1).png](/cms_trial/assets/eaddc8b7-dd71-4872-b244-57c1726b9fec.png)![contentId-1918406270](/cms_trial/assets/270c3b1a-a7c8-4a6c-bc3a-57fe0ceb7cfa.png)

Add a new field configuration scheme:

![contentId-1918406270](/cms_trial/assets/e9cfc927-dd19-4f6f-893e-f62ceb9d3528.png)![contentId-1918406270](/cms_trial/assets/ff8c089b-06f7-46e9-a6d8-5f75112f30c2.png)

Make sure that the correct field configuration is associated with the scheme:

![contentId-1918406270](/cms_trial/assets/e78a19dd-2c5e-4eeb-bfe5-4ea704e72407.png)![contentId-1918406270](/cms_trial/assets/b6197672-98db-4bf6-86d9-16a397a47355.png)![contentId-1918406270](/cms_trial/assets/34ada788-a9ec-49f2-b7f1-ff12d4a1ac17.png)

Go to the Jira project that is added to the Box scope (the project Jira issues will be copied to):

![contentId-1918406270](/cms_trial/assets/e5ca9adb-05e7-41f1-914e-cd199dd79ae6.png)

Find the field configuration:

![contentId-1918406270](/cms_trial/assets/aded25b7-b914-4735-98b2-8bf8e6177d39.png)

Change the scheme:

![contentId-1918406270](/cms_trial/assets/46a5f2b1-52de-4b95-8bf0-210b460d40cf.png)![contentId-1918406270](/cms_trial/assets/f3da91a4-3b9e-40e3-93ed-ab19695d9a42.png)

You can proceed with the cloning after changing the Field Configuration.