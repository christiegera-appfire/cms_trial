# Jira slow-down caused by BigPicture

## When to use master-slave mode

**Applies to Jira Data Center only.**

**Avoid Jira slow-downs caused by BigPicture consuming resources on all nodes**. The setup described on this page can be helpful when you have **issues with Jira performance that do not occur when the BigPicture app is disabled**.

The master-slave mode should be treated **as the last resort.**

To improve performance, first upgrade BigPicture to version **8.37 or higher** and set the [‘Updates processing control’](/cms_trial/space/SPM/1918537987/Sync+rules/) to **Optimized updates processing** or **Limited updates processing.** You can also [adjust the database parameters](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=DLP&title=Data%20Center%20-%20directly%20adjust%20database%20parameters) directly.

We recommend reaching out to the [Appfire Support Team](https://appfire.atlassian.net/servicedesk/customer/portal/11) for help with the configuration change.

## How does it work

This setup helps **minimize BigPicture's impact on Jira Data Center performance.**

Aload balancer redirects requests to BigPicture—changing node configuration requires changing load balancer configuration.

After the change, BigPicture will **run only on the primary node.** Other nodes (secondary nodes) will seamlessly redirect users' requests to the first node. As a result, only the primary node will be impacted by BigPicture’s load (processor usage, memory usage, etc.). Other nodes remain unaffected and handle Jira users' requests as usual.

![Screenshot 2024-04-22 at 10.54.22.png](/cms_trial/assets/3cbef4d3-905e-4cd6-8287-f6d86deb907f.png)

### BigPicture availability after the change

**BigPictrue will still be accessible on all nodes**, but requests will be handled only by the primary node. **Secondary nodes** will be responsible only forBigPicture menu-based actions like calculating which boxes should be shown as recently visited or menu options based on permissions. These actions don’t require a lot of resources, so the impact on secondary nodes is negligible**.**

## You will need

- competences with load balancers and access to your load balancer configuration
- BigPicture in version at least **8.32**, containing Master-Slave solution
- testing/preprod environment to safely check configuration
- decide which node will be the Master node, check its ID (defined in load balancer configuration), and ensure its hardware meets the requirements given below in this document

## Steps

1. **Prepare the load balancer configuration** that is appropriate for your load balancer technology. Below, you can find an example of such a configuration. Master-Slave mode requires a load balancer to:

   1. redirect requests containing `/rest/softwareplant-bigpicture` in path to one (Master) node,
   2. **DO NOT** redirect requests containing any of `rest/softwareplant-bigpicture/1.0/system/auth` or `rest/softwareplant-bigpicture/1.0/system/reauth` in path,
   3. delete HTTP header `Cookie` from redirected requests
   4. delete HTTP header `Set-Cookie` from responses to redirected requests
2. **Set the Master node ID using the endpoint below**. After that, other nodes will act as Slave nodes.

   1. enabling Master-Slave occurs by setting Master node id:   
      On the node you want to set as Master node call:  
      HTTP method: PUT   
      path: `<BASE>/rest/softwareplant-bigpicture/1.0/util/cluster/configuration`
   2. checking Master-Slave configuration:  
      HTTP method: GET   
      path: `<BASE>/rest/softwareplant-bigpicture/1.0/util/cluster/configuration`
   3. disabling Master-Slave configuration occurs by deleting Master node id:  
      HTTP method: DELETE  
      path: `<BASE>/rest/softwareplant-bigpicture/1.0/util/cluster/configuration`
3. BigPicture should work in Master-Slave mode now. Check if both Jira and BigPicture work on all nodes. Jira user experience remains the same, except for better Jira performance. You can observe how Master-Slave redirects HTTP traffic, e.g., by observing HTTP headers in the browser. Depending on your load balancer solution, this could be visible by different node IDs in the BigPicture HTTP request and its response.

## Load balancer configuration example

Example of load balancer configuration in standard and Master-Slave configuration for haproxy technology. If you need help with other load balancers, write to us at ~~support@softwareplant.com~~ <https://appfire.atlassian.net/servicedesk/customer/portal/11> with the topic: “**DC Master-Slave configuration example request**“.

## **DO NOT COPY THIS AS READY SOLUTION - USE FOR REFERENCE ONLY**

## haproxy.cfg - Standard configuration (before change):

```text
defaults
    (...)
frontend jira_dc
  bind 0.0.0.0:80
  default_backend jira_dc_ha
backend jira_dc_ha
  balance roundrobin
  option httpchk HEAD /dev-jira8dc/psql1/status
  cookie JSESSIONID prefix nocache
  server node01 host.docker.internal:44081 check cookie node01
  server node02 host.docker.internal:45081 check cookie node02
```

## haproxy.cfg - Master-Slave configuration (after change) with node01 set as Master node:

```text
defaults
    ...
frontend jira_dc
  bind 0.0.0.0:80
  default_backend jira_dc_ha
  acl is_bigpicture path_reg .*rest/softwareplant-bigpicture.*
  acl is_bigpicture_auth path_reg .*rest/softwareplant-bigpicture/1.0/system/auth.*
  acl is_bigpicture_reauth path_reg .*rest/softwareplant-bigpicture/1.0/system/reauth.*
  use_backend jira_dc_node01_ha if is_bigpicture !is_bigpicture_auth !is_bigpicture_reauth
backend jira_dc_ha
  balance roundrobin
  option httpchk HEAD /dev-jira8dc/psql1/status
  cookie JSESSIONID prefix nocache
  server node01 host.docker.internal:44081 check cookie node01
  server node02 host.docker.internal:45081 check cookie node02
backend jira_dc_node01_ha
  option httpchk HEAD /dev-jira8dc/psql1/status
  http-request del-header Cookie
  http-response del-header Set-Cookie
  server node01 host.docker.internal:44081 check
```

## Master node hardware requirements

1. The server chosen to be the Master node for BigPicture should be at least as powerful as other servers.

   1. If your servers differ in hardware, it is best to choose the most powerful one as Master.
2. If you experience any issues with BigPicture performance after the change and the lack of server resources is confirmed as the cause, it is enough to boost only the Master server.
3. See also [BigPicture Sizing Guide | How powerful server do I need for my company?](https://appfire.atlassian.net/wiki/spaces/DLP/pages/297831345/BigPicture+Sizing+Guide#How-powerful-server-do-I-need-for-my-company%3F).