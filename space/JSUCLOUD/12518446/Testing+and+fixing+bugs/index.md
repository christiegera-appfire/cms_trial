# Testing and fixing bugs

---

One of our most common use cases is when customers interconnect the workflows of testers and developers to resolve bugs. This is illustrated in the workflow below.

1. When a test fails and the tester clicks the NOK (Not OK) transition, a **new bug issue is created and linked to the test automatically.** With every bug the tester finds, this process can be repeated and a new bug issue is created.  
   See our [Create a Linked Issue](/cms_trial/space/JSUCLOUD/12518348/Create+a+Linked+Issue+post+function/) post function to learn more.
2. The test is automatically set to “Ready for Re-Test” after all the related bugs are fixed. The fix version is copied to the test so the testers know which version needs to be retested.  
   See our [Linked Transition](/cms_trial/space/JSUCLOUD/12518766/Linked+Transition+post+function/) post function to learn more.
3. When a test passes, the tester selects the Ok transition. All the linked bug issues which are now fixed, are closed automatically. The tester additionally adds a Test Script attachment to the linked issues on the transition screen. The Copy or Move Attachments post function is used to move the attachment added on transition to all the linked bug issues.  
   See our [Linked Transition](/cms_trial/space/JSUCLOUD/12518766/Linked+Transition+post+function/) and [Copy or Move Attachments](/cms_trial/space/JSUCLOUD/12518511/Copy+or+move+attachments/) post functions to learn more.

![JSU Cloud interconnected workflows for software testing and bug fixing.](/cms_trial/assets/5ab778bc-e053-46df-876d-ae82c6cd25ff.png)