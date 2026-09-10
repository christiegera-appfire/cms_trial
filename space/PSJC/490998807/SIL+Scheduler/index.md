# SIL Scheduler

The SIL Scheduler allows you to run scripts at specific time intervals or at various times using CRON.

You can access the SIL™ Scheduler page from **Administration → Manage Apps → Power Apps Config → Advanced → Scheduler**.

![Power Scripts for Jira Cloud schedule settings interface](/cms_trial/assets/06228788-941c-407b-827f-abec89a7b836.png)

## Scheduler Page Columns

| Column | Description |
| --- | --- |
| Script | Full path to the script and the arguments if they exist |
| Schedule | Either the interval on which the script should run or the CRON expression interpreted |
| Next Run | Date and time of the next run |
| Runs as | User to impersonate when running the script |
| Operations | Possible operations to do with a scheduler (delete, in our case) |

## Managing SIL™ Scheduler

The SIL™ Scheduler feature enables you to run SIL™ scripts after a valid Jira interval or using a CRON expression.

Jobs are persistent and survive engine restarts. You can read about scheduling jobs here: [Scheduling functions](/cms_trial/space/PSJC/434507358/Scheduling+Functions/). This mechanism uses the same scheduling engine, thus the same notes apply.

Each scheduled job has the following properties:

- **Job type** - either interval or CRON expression
- **Schedule** - valid Jira interval or a CRON expression
- **Script** - SIL Script that will run using the schedule that you define
- **Arguments** - job arguments
- **Run script as** - if specified, the script will run as if by this user
- **Does this job repeat?** - if you use a Jira interval, you can define whether the job should repeat at the specified interval

![Power Scripts for Jira Cloud scheduler job configuration](/cms_trial/assets/21c62543-4d29-4809-b861-05f0892c7fed.png)

To schedule a CRON job, change the type to "CRON" and enter a valid schedule (Quarts CRON expression).

The Quarts Cron expressions also considers the seconds, unlike the traditional Cron expressions:

**SIL Scheduler**: Sec Min Hour Day Month Day of Week

**Traditional Cron**: Min Hour Day Month Day of Week

![Power Scripts for Jira Cloud scheduler timing configuration](/cms_trial/assets/dca2d75d-47d0-4e83-bce6-e6db0dcd02da.png)

### Info

- To edit the actual scripts, use the [SIL™ Manager](/cms_trial/space/PSJC/490996983/SIL+Manager/).
- Try using sites like <http://www.cronmaker.com/> to help generate a valid Quarts CRON expression

After saving the added job, a new entry is added to the table on the Administration page.

### Editing Scheduler Jobs

Just click on the edit icon, you will be able to reschedule or change any of the parameters you defined the job with:

![Power Scripts for Jira Cloud SIL template editor interface](/cms_trial/assets/770ebef1-6cc0-4eed-8722-1a2b19edca43.png)

### Deleting Scheduled Jobs

Clicking on the bin icon will delete the job.

## The User and the Running Jobs

If you do not specify an user the job will query Jira with the addon user, which is internal to the cloud integration. In other words, you will still be able to perform certain operations, but not all of them.

Functionsfuncncotons like *currentUser()*, *archiveProject()* still require an user to return the right result. If called from the unauthenticated context, they will blow the script, yielding probably undesired results. The script will NOT have the required permissions to fully interact with Jira tickets, unless configured so or script explicitly calls out the user to use within in the script using the [runA](/cms_trial/space/PSJC/434374366/runAs/)ffncunocion.

It is highly recommended to provide a user to the scheduled job when interacting with Jira tickets.

## Processing Issues in Bulk

When changing issues in bulk, remember to create scheduled jobs as efficient as possible. Jira and Power Scripts being two separate entities, your goal is to minimize the number of calls and the data pulled from Jira (same old principle of minimizing the I/O)

A standard scheduled job usually looks like this:

```text
string jql = "project = TEST"; //be more exact here, this JQL is not ok!

for(string k in selectIssues(jql)) {
    //process here the issues, e.g.:
    %k%.priority = "High";
}
```

**Avoid**:

1. *Getting more data than you need*. Tailor your JQL to be as exact as possible, for instance the above JQL takes the issues from an entire project to process!
2. *Getting issues twice*. Getting them in the same script is easily correctable, but getting the same issues twice in two separate scheduled jobs may not be easy to spot. If you need to process issues, do it just once.
3. *Scheduling some data-intensive jobs at the same time*. Suppose you have two jobs, each loading 1000 issues, one scheduled every 2 hours, the other every 3 hours. If the jobs start roughly at the same time, each 6h we will have a spike in memory consumption because both jobs will be active at the same time.

Please take a look on the following article, that offers insights on large batch processing: [Processing large batches](/cms_trial/space/PSJC/913866777/Processing+large+batches/)

## Using Arguments

With arguments a single script can be configured to work in different ways. For example, if you had a script that reopens issues after a specific date or after a period of time has passed, you could use arguments to specify which projects the scripts should operate for.

In the example configuration below, we can see that the project keys TEST, DEV, and SUPPORT are being passed the script.

![Power Scripts for Jira Cloud SIL executions monitoring interface](/cms_trial/assets/eaf1b799-d460-417d-bc2c-781b6dc675ee.png)

The arguments can be accessed in the script by using the **argv variable**. The argv variable is a standard array variable that is used throughout the application. Read more about using the argv variable [here](/cms_trial/space/PSJC/756252819/Arguments+(argv+variable)/).

```text
string firstProject = argv[0];
string secondProjecy = argv[1];
string secondProjecy = argv[3];

//OR

for(string proj in argv) {
    //since the argv variable is an array loops can be used
    //do something with the proj variable
}
```