# General Best Practices

The purpose of this document is to describe general best practices to follow while scripting.

## Organizing Folders in the silprograms Directory

- Create a separate folder according to functionality
- Create a separate folder for each project

## Development process

- Develop as much as possible from the SIL Manager. Developing from the SIL Manger tends to give the user a better sense of what the code does and is much faster.
- Start with one function as a proof of concept.
- Add loops and if statements after.
- Hardcode at first to get a result.
- Refactor hardcoded values with with variables.
- If possible, test Live Fields in the edit screen before trying in Jira Service Desk portal or create screen. The JSD portal tends to be more complicated and more can go wrong.

## Looking for Ideas

- Often other users have already done something similar to what you would like to do. Find an example on the Atlassian Community?
- Look for functions.

  - First look for functions in the [Jira Integration Functions](/cms_trial/space/PSJC/434374224/Jira+Integration+Functions/) section of the documentation. Most functions dealing with Jira will be found here.
  - The second place to look is the [Jira Administration Functions](/cms_trial/space/PSJC/434864501/Jira+Administration+Functions/).
  - The last category of functions has to deal with things like [math](/cms_trial/space/PSJC/434439974/Math+Functions/), [string manipulation](/cms_trial/space/PSJC/434930240/String+Functions/) or [array functions](/cms_trial/space/PSJC/434831645/Array+Functions/).
- If the function you are looking for does not exist, consider implementing a script which consumes an Atlassian REST API ([Jira Server/DC](https://docs.atlassian.com/jira-software/REST/latest/)), ([Cloud](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#expansion)).

  - When developing SIL scripts which consume REST API, try using getting results with httpGet().

You are highly encouraged to use a SIL function if at all possible. Atlassian Java methods (and to a lesser extent, REST API) change all the time and can break your code. When using SIL, we take care of deprecated Java methods for you, so if you use SIL functions, you will not need to update your code.

## Things to Think About While Engaging in the Development Process

- I can, but should I?

  - If used incorrectly, certain implementations can result in code that takes to long or takes down your Jira instance.
- Migration minded.

  - Always keep in mind when developing code what it would take to migrate to the next version of Jira or Confluence when they come out.
- Does it scale?

  - Can the process being developed be used on a grand scale?
- Don't bake in bad processes.

  - Bad processes tend to multiply over time. If you do the first thing right, the process will get better over time.
- Leave the smallest footprint.

  - Write code that is direct, to the point and reads well.
  - Avoid code that uses a large amount of system resources.
- Use native Jira features whenever possible.

  - There is no need to reinvent the wheel. Jira is an amazing system, so use those features to accomplish your goals.
- Use Jira in the way it was designed to operate.

  - With scripting, the features you can implement are infinite. However, keep the functionality of your code to be in alignment with Atlassian best practices.