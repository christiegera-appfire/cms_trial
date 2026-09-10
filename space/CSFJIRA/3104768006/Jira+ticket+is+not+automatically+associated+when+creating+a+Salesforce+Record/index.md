# Jira ticket is not automatically associated when creating a Salesforce Record

## Summary

Using the *Create Salesforce Object* option from a Jira ticket, the Salesforce Record is created. However, it is somehow not associating the Jira Ticket with the newly created Salesforce Record.

This behavior also happens when using the "Post-function" to create the Salesforce Record.

## Environment

Jira DC

## Diagnostics Steps

1. Scan the **atlassian-jira.log** file for the following stack trace:

   ```text
   2021-07-29 16:55:23,824+0800 http-nio-8461-exec-23 WARN user1 1015x1532x1 11x1pch 202.184.223.5,127.0.0.1 /plugins/servlet/streams [c.a.streams.internal.StreamsCompletionService] Registering failure for stream provider Julian SF due to error other
   2021-07-29 16:55:44,494+0800 pool-29-thread-1 ERROR      [c.s.j.s.rest.action.Action$] [UCgjMoPq0F] IllegalArgumentException
   java.lang.IllegalArgumentException
   	at com.google.common.base.Preconditions.checkArgument(Preconditions.java:127)
   	at com.atlassian.jira.entity.property.BaseEntityPropertyService.setProperty(BaseEntityPropertyService.java:96)
   	at com.atlassian.jira.entity.property.DelegatingEntityPropertyService.setProperty(DelegatingEntityPropertyService.java:41)
   	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
   	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
   	at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
   	at java.base/java.lang.reflect.Method.invoke(Method.java:566)
   	at com.atlassian.plugin.util.ContextClassLoaderSettingInvocationHandler.invoke(ContextClassLoaderSettingInvocationHandler.java:26)
   	at com.sun.proxy.$Proxy291.setProperty(Unknown Source)
   	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
   	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
   	at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
   	at java.base/java.lang.reflect.Method.invoke(Method.java:566)
   	at org.springframework.aop.support.AopUtils.invokeJoinpointUsingReflection(AopUtils.java:343)
   	at org.eclipse.gemini.blueprint.service.importer.support.internal.aop.ServiceInvoker.doInvoke(ServiceInvoker.java:56)
   	at org.eclipse.gemini.blueprint.service.importer.support.internal.aop.ServiceInvoker.invoke(ServiceInvoker.java:60)
   	at org.springframework.aop.framework.ReflectiveMethodInvocation.proceed(ReflectiveMethodInvocation.java:186)
   	at org.springframework.aop.support.DelegatingIntroductionInterceptor.doProceed(DelegatingIntroductionInterceptor.java:136)
   	at org.springframework.aop.support.DelegatingIntroductionInterceptor.invoke(DelegatingIntroductionInterceptor.java:124)
   	at org.springframework.aop.framework.ReflectiveMethodInvocation.proceed(ReflectiveMethodInvocation.java:186)
   	at org.eclipse.gemini.blueprint.service.util.internal.aop.ServiceTCCLInterceptor.invokeUnprivileged(ServiceTCCLInterceptor.java:70)
   	at org.eclipse.gemini.blueprint.service.util.internal.aop.ServiceTCCLInterceptor.invoke(ServiceTCCLInterceptor.java:53)
   	at org.springframework.aop.framework.ReflectiveMethodInvocation.proceed(ReflectiveMethodInvocation.java:186)
   	at org.eclipse.gemini.blueprint.service.importer.support.LocalBundleContextAdvice.invoke(LocalBundleContextAdvice.java:57)
   	at org.springframework.aop.framework.ReflectiveMethodInvocation.proceed(ReflectiveMethodInvocation.java:186)
   	at org.springframework.aop.support.DelegatingIntroductionInterceptor.doProceed(DelegatingIntroductionInterceptor.java:136)
   	at org.springframework.aop.support.DelegatingIntroductionInterceptor.invoke(DelegatingIntroductionInterceptor.java:124)
   	at org.springframework.aop.framework.ReflectiveMethodInvocation.proceed(ReflectiveMethodInvocation.java:186)
   	at org.springframework.aop.framework.JdkDynamicAopProxy.invoke(JdkDynamicAopProxy.java:212)
   	at com.sun.proxy.$Proxy2441.setProperty(Unknown Source)
   	at com.servicerocket.jira.salesforce.client.jira.ServerIssueClient.$anonfun$updateProperty$1(ServerIssueClient.scala:252)
   	at com.servicerocket.jira.salesforce.Plugin$AsJiraUser$$anon$1.run(Plugin.scala:90)
   	at java.base/java.lang.Thread.run(Thread.java:834)
   ```
2. Try associating the Jira ticket manually as in ["Associating a Salesforce Object from Jira"](https://appfire.atlassian.net/wiki/spaces/CSFJIRA/pages/470754430/Associating+a+Salesforce+Object+from+Jira).
3. Using the affected user, do the same and check if it is possible to associate a Jira ticket.
4. If not, check if the affected user has the **"Edit Issue"**permission with the ["Jira Permission Helper"](https://support.atlassian.com/jira-cloud-administration/docs/use-the-jira-admin-helper/?__hstc=72543820.ab19c70c621fe76686456a1bcc7fc053.1629983345841.1643094732368.1643096677240.351&__hssc=72543820.46.1643096677240&__hsfp=3471989517).

## Cause

To update the association, the ticket needs to be updated with the Salesforce Record ID created from it. Hence, it is **required for the user that triggers the Jira ticket creation to have "Edit Issue" permission**for the association to happen.

## Workaround

## Resolution

Update the necessary user to have **"Edit Issue"** permission in the project.

1. Navigate to the affected project.
2. Then, in the project sidebar, click **Project Settings**.
3. Select **Permissions.**
4. Click on **Actions > Edit Permissions**.
5. Find **Edit Issues** and click **Edit**.

   ![image-20241217-073700.png](/cms_trial/assets/85c46353-2127-4067-9d66-db6a85435c7e.png)
6. Add the necessary user into the permission.

For example:

- User A is accessing a Jira ticket and uses the "Create Salesforce Object" button to create a Salesforce Record. In this case, User A needs the Edit Issue permission.
- User B is creating a Jira ticket through email in which it will automatically create a Salesforce Record after it. Here, User B needs the Edit Issue permission.