# Thread pool configuration

The Thread pool configuration (formerly known as asynchronous runner) is a component that manages the execution of background tasks. These background tasks use SIL scripts in a controlled environment separate from the main Jira processes, enabling automated operations to be performed without impacting the performance or stability of the core Jira functionality.

## How to access the Thread Pool Configuration

To access the Thread Pool Configuration, click **Power Scripts** > **Settings** > **Thread pool**.

![Power Scripts for Jira Cloud TLS SSL configuration interface](/cms_trial/assets/10591f2b-0b9c-450a-901e-c99665a5f45d.png)

---

## Key configuration parameters

To optimize your Thread Pool Configuration for your specific environment and workload requirements, it's essential to understand how each parameter affects the execution and resource consumption of background SIL scripts. Each parameter directly impacts script processing capacity, execution duration limits, and system resource management.

### Threads

This is the number of running threads (number of SIL scripts running at the same time). Each script runs as a separate process in the thread pool.

|  |  |
| --- | --- |
| **Default value** | 10 threads |
| **Higher value impact** | ✅ With a higher number of threads, scripts will complete faster because more scripts can run simultaneously. | ❌ This places more demand on system processor and memory resources. |
| **Lower value impact** | ✅ With fewer threads, scripts might need to wait in a queue before processing. | ❌ This can delay task completion. |

### Max Script Runtime

This is the maximum amount of time a SIL script can run before it’s automatically terminated. This setting prevents scripts from running indefinitely, particularly when they might be waiting on external systems that have stopped responding.

|  |  |
| --- | --- |
| **Default value** | 1 hour |
| **Higher value impact** | ✅ With a higher **Max Script Runtime**, scripts have more time to complete complex tasks, which is useful for processes that interact with external systems or handle large datasets. | ❌ System resources (processors and memory) remain allocated to scripts for longer periods. |
| **Lower value impact** | ✅ With a lower **Max Script Runtime**, system resources are released quicker, which is better for environments where resource availability is critical. | ❌ This can cause legitimate long-running scripts to terminate before completion. |

### Checkpoint Interval

This is the interval at which the system checks for and cleans up expired tasks (SIL scripts that exceed the configured **Max Script Runtime**).

The thread pool is maintained by a watchdog thread, a background process that monitors running scripts and reclaims resources from expired tasks. The **Checkpoint Interval** determines how often this watchdog performs its checks.

|  |  |
| --- | --- |
| **Default value** | 1 minute |
| **Longer interval impact** | ✅ With a longer interval, the system checks less frequently for expired tasks, reducing the resource impact of the monitoring process itself. | ❌ Resources from terminated scripts may remain allocated longer before being released back to the system. |
| **Shorter interval impact** | ✅ With a shorter interval, the system checks more frequently for expired tasks, allowing resources to be returned to Jira faster. | ❌ The monitoring process itself consumes more system resources with frequent checks. |

While **Max Script Runtime** and **Checkpoint Interval** are configured in hours and minutes respectively, most scripts complete in milliseconds.

---

## Monitor and optimize

The *Queued Tasks* and *SIL Threads* pages in *Performance Monitoring* display key metrics to help you optimize settings:

- **Running tasks** (In **Performance Monitoring** > **Queued Tasks**): Displays the number of scripts currently executing.
- **SIL Executions** (In **Performance Monitoring** > **SIL Threads**): The largest number of tasks waiting to be processed.

Use these metrics and considerations to adjust your configuration:

|  |  |
| --- | --- |
| **Threads** | - If the number of threads is consistently below the **Maximum Queue Length** listed in **Performance Monitoring** > **Queued Tasks**, consider increasing the number of **Threads** (**Settings** > **Thread Pool** > **Threads**). - For reporting tasks that gather data from multiple sources, increase **Threads** if the pool is frequently at capacity. |
| **Max Script Runtime** | - For long-running tasks (like complex reports or multi-system integrations), increase the **Max Script Runtime**. - Ensure resource-intensive tasks have sufficient time to complete without termination. |

By regularly monitoring these metrics and applying these guidelines, you can maintain optimal performance while ensuring background tasks complete successfully.

---

## More configuration guides