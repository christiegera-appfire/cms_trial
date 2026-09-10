# Automation limits (there are none!)

## Unlike Jira, JMWE does not impose any limits on the number of automations you can execute.

It does not matter if you are using a free tier of Jira or have an enterprise account, there are no limits. It does not matter how many workflow extensions you create, how many actions those extensions perform, or how many times those automations are triggered.

There are only two real limitations when using JMWE:

1. You can only create 100 Event-based actions that utilize dynamic webhooks (see below). This is an Atlassian limitation, not an Appfire or JMWE limitation.
2. The physical limitations of the machine running the extension. As long as the extensions are configured correctly there should not be a time when you discover those limitations. Existing customers have hundreds of extensions running thousands of times an hour without experiencing any performance issues.

If you are experiencing any issues [contact us](https://appfire.atlassian.net/servicedesk/customer/portal/11) and we can help! We will either help you review your scripts and the script logs to help you understand where the issues may be occurring, or increase the physical resources on the machine depending on the circumstances.

**Warning**: JMWE Event-based actions utilize webhooks to enable events to trigger the execution of the Action; **Atlassian has established a limit of 100** ***dynamic*** **webhooks per Connect app, per tenant** (there is no published limit on static webhooks). This means that you will be limited to 100 Event-based actions that utilize dynamic webhooks on your instance. Please refer to the **Events** section below to determine if the events you need to monitor use static or dynamic webhooks.

This is an Atlassian limitation and cannot be overridden by Appfire.

## Why this matters

The absence of execution limits in a cloud-based automation tool is vital for ensuring continuous operations, scalability, efficiency, flexibility, cost-effectiveness, and a positive user experience. It enables users to maximize the utility of the tool, adapt to changing requirements, and achieve their automation goals effectively and reliably.

1. **Continuous Operations**: Users depend on automation tools for consistent and uninterrupted service. Execution limits can disrupt this continuity by imposing restrictions on the number of tasks or processes that can be executed within a given timeframe. Without these limits, users can confidently rely on the tool to perform tasks whenever needed, ensuring continuous operations without interruptions.
2. **Scalability**: Businesses and individuals often require scalable solutions that can accommodate varying workloads. Execution limits can hinder scalability by restricting the tool's ability to handle increased demands during peak times or when executing complex tasks. An absence of execution limits allows users to scale their usage according to their needs without worrying about hitting arbitrary constraints.
3. **Efficiency**: Users expect efficient and timely completion of tasks when utilizing automation tools. Execution limits can introduce delays or force users to prioritize tasks, potentially impacting productivity and efficiency. By removing execution limits, the tool can operate at its full potential, completing tasks promptly without unnecessary delays.
4. **Flexibility**: Users may have diverse needs and preferences when using automation tools. Execution limits can constrain the flexibility of the tool, limiting the types of tasks that can be automated or the frequency at which they can be executed. Without these limitations, users have greater flexibility to automate a wide range of tasks and customize their workflows according to their specific requirements.
5. **Cost-effectiveness**: Some automation service providers impose additional charges or tiered pricing structures based on usage limits. Without execution limits, users can avoid unexpected costs associated with exceeding these limits, promoting cost-effectiveness and predictable pricing for utilizing the automation tool.
6. **User Experience**: Ultimately, the user experience is paramount. Execution limits can frustrate users, leading to dissatisfaction with the service and potentially driving them to seek alternative solutions. By providing an execution-limit-free environment, the automation tool enhances the user experience, fostering satisfaction and loyalty among its users.