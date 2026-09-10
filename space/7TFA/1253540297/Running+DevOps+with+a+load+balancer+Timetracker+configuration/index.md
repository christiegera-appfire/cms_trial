# Running DevOps with a load balancer Timetracker configuration

Timetracker is not designed for load balancing, so installing Timetracker in a load-balanced DevOps environment is not officially supported.

However, we have seen the following configuration of Timetracker to work within a load-balanced environment.

## Install Timetracker

Timetracker must be installed and running only on one server in your environment. Running multiple instances of Timetracker services will cause issues.

## Configuration Tool: Recommended configuration

Set the Timetracker Configuration Tool DevOps Server URL field to an actual DevOps server URL, preferably the one where Timetracker is installed and not to have the load balancer URL set in that field:

![FAQ_Running_DevOps.png](/cms_trial/assets/68fc6f53-5dd2-4779-9b26-30aa8b4e5f37.png)

## Service Account: Recommended configuration

Set up a default application pool identity in IIS for Timetracker which will then act as the Service Account:

![AQ_Running_DevOps_Service_Acc.png](/cms_trial/assets/85a17e9b-576f-4aeb-a239-379da8abadfc.png)

This is the configuration we have seen will work as was confirmed by several of our customers. However, please note that there is a possibility that even this will not work for you, since load balancer is not officially supported by 7pace Timetracker.