# Warning log (Jira)

## Plugin timeout

If the App is not visible after installation (it isn't on the header at the top of the page; it's also absent in the "manage apps” section of Jira), you may need to increase the plugin timeout period. Jira must allow at least 300 seconds (preferably 600 seconds) for an installation.

### Indications

**Jira logs** show a message in the following format:

Unable to start the following plugins due to timeout while waiting for plugin to enable: eu.softwareplant.bigpicture

```text
org.eclipse.gemini.blueprint.context.support.OsgiBundleXmlApplicationContext.loadBeanDefinitions(OsgiBundleXmlApplicationContext.java:140)
   at org.springframework.context.support.AbstractRefreshableApplicationContext.refreshBeanFactory(AbstractRefreshableApplicationContext.java:129)
   at org.springframework.context.support.AbstractApplicationContext.obtainFreshBeanFactory(AbstractApplicationContext.java:537)
   at org.eclipse.gemini.blueprint.context.support.AbstractDelegatedExecutionApplicationContext.access$800(AbstractDelegatedExecutionApplicationContext.java:60)
   at org.eclipse.gemini.blueprint.context.support.AbstractDelegatedExecutionApplicationContext$3.run(AbstractDelegatedExecutionApplicationContext.java:242)
   at org.eclipse.gemini.blueprint.util.internal.PrivilegedUtils.executeWithCustomTCCL(PrivilegedUtils.java:85)
   at org.eclipse.gemini.blueprint.context.support.AbstractDelegatedExecutionApplicationContext.startRefresh(AbstractDelegatedExecutionApplicationContext.java:220)
   at org.eclipse.gemini.blueprint.extender.internal.dependencies.startup.DependencyWaiterApplicationContextExecutor.stageOne(DependencyWaiterApplicationContextExecutor.java:224)
   at org.eclipse.gemini.blueprint.extender.internal.dependencies.startup.DependencyWaiterApplicationContextExecutor.refresh(DependencyWaiterApplicationContextExecutor.java:177)
   at org.eclipse.gemini.blueprint.context.support.AbstractDelegatedExecutionApplicationContext.refresh(AbstractDelegatedExecutionApplicationContext.java:157)
   at org.eclipse.gemini.blueprint.extender.internal.activator.LifecycleManager$1.run(LifecycleManager.java:207)
   at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)
   at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617)
   at java.lang.Thread.run(Thread.java:745)
```

As you can see below, the countdown starts with 60 - it should start with at least 300. Preferably 600.

```text
Plugins that have yet to be enabled: (1): [eu.softwareplant.bigpicture], 60 seconds remaining
Plugins that have yet to be enabled: (1): [eu.softwareplant.bigpicture], 59 seconds remaining
(...)
Plugins that have yet to be enabled: (1): [eu.softwareplant.bigpicture], 0 seconds remaining
```

### Cause

As the JIRA app starts up, it goes through the following steps when starting the Plugin System:

1. `$JIRA_INSTALL/atlassian-jira/WEB-INF/classes/atlassian-bundled-plugins.zip` is extracted to `$JIRA_HOME/plugins/.bundled-plugins`.
2. `$JIRA_HOME/plugins/installed-plugins` is extracted to `$JIRA_HOME/plugins/.osgi-plugins`.

This is a reasonably resource-intensive process and can place a sizeable load on the I/O of the disk and CPU of the machine hosting the JIRA app instance. If the required resources aren't available, the plugins may timeout and cause the app to be left in an unusable state.

⚠️ This error can happen relatively often on servers with only a single-core vCPU available - JIRA applications are multi-threaded, and there will be CPU contention on startup, which can subsequently cause timeouts.

### Solution

It is possible to increase the plugin timeout period by adding the `-Datlassian.plugins.enable.wait=600` argument to the JIRA app startup arguments, as in [Setting Properties and Options on Startup](https://confluence.atlassian.com/display/AdminJIRAServer070/Setting+properties+and+options+on+startup).

ℹ️ This will increase the time it takes to start the JIRA app, and it addresses the symptom rather than the root cause. If the machine is not powerful enough to run the application, we suggest upgrading to a more powerful host.

source: <https://confluence.atlassian.com/display/JIRAKB/JIRA+applications+System+Plugin+Timeout+While+Waiting+for+Add-ons+to+Enable>

## BigTemplate pdf export does not work due to problem with SSL certificate

If logs contain errors like this:

```text
// -------------------------- Shell output --------------------------
ERROR! Error: net::ERR_SSL_CLIENT_AUTH_CERT_NEEDED
at navigate (/usr/lib/node_modules/puppeteer/lib/Page.js:526:37)
at <anonymous>
at process._tickCallback (internal/process/next_tick.js:189:7)
// -------------------------- Shell output --------------------------
```

The old puppeteer version might cause it.

To fix this, upgrade puppeteer by executing the command below on the server with your Jira instance:

```text
sudo npm -g update puppeteer --unsafe-perm=true
```