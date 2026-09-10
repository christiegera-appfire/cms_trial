# Priority score scripted field

## Problem

Prioritizing the backlog can be time consuming and you may not always have the time to spend on it.

## Solution

Create a script that will automatically calculate the priority score based on a predefined list of parameters. This score would drive the ranking within a projects backlog. The script below will take the following information from the issue/work item into account when calculating a priority score:

- **Priority** - Field value from the issue. High priority will have a higher score while lower priority will have a lower score.
- **Issue type** - Value from the issue. For example, Bugs will have a higher score.
- **Labels** - Field value from the issue. If any of the labels match the predefined value the score will be updated based on the data.
- **Components** - Field value from the issue. If any of the components match the predefined value the score will be updated based on the data.
- **Key words** - If a key words is found in the issues summary or description text the score will be updated based on the data.
- **Due date** - The time frame in which the work is due will be taken into account to calculate the score. Unlike other parameters the due date is a multiplier which means it has a much greater impact on the outcome of the score.

Given that this script would be configured as a scripted custom field the priority score would be recalculated every time the issue data is updated. Or, optionally, it can be recalculated when a parent or child issue is updated as well.

A custom field will need to be created to receive the calculated value of the priority score.

```text
//function to create indexed arrays
function parseRawData(string [] data) {
    string [] tempArray;
    for(string d in data) {
        string [] parts = split(d, ",");
        tempArray[parts[0]] = parts[1];
    }
    
    return tempArray;
}

//---------------------Data used to evaludate score-----------------------------
string [] fieldList = "priority|issueType|labels|components";

string [] priorityRawData = "Lowest,0|Low,1|Medium,2|High,3|Highest,4";
string [] issueTypeRawData = "Sub-Task,0|Spike,0|Task,1|Story,2|Bug,3|Epic,0";
string [] labelsRawData = "label1,0|label2,1|label3,2|label4,3";
string [] componentsRawData = "comp1,0|comp2,1|comp3,2|comp4,3";
string [] keyWordsRawData = "development,0|production,1|blocker,2|outage,3";

string [] priorityScores = parseRawData(priorityRawData);
string [] issueTypeScores = parseRawData(issueTypeRawData);
string [] labelsScores = parseRawData(labelsRawData);
string [] componentsScores = parseRawData(componentsRawData);
string [] keyWordsScores = parseRawData(keyWordsRawData);

//---------------------Start score calculation----------------------------------

number priorityScore = 0;

//loop through list of fields and compare value to data
for(string f in fieldList) {
    string dataName = f + "Scores";
    string [] scores = %dataName%;
    //is value found in data?
    if(isNotNull(scores[%f%])) {
        priorityScore += scores[%f%]; //add to score
    }
}

//loop through list of keywords found in summary and description
for(string kw in arrayKeys(keyWordsScores)) {
    if(contains(toLower(summary), kw)) {
        priorityScore += keyWordsScores[kw];
    } else if(contains(toLower(description), kw)) {
        priorityScore += keyWordsScores[kw];
    }
}

//calculate due date score multiplier
if(isNotNull(dueDate)) {
    if(dueDate >= (currentDate() + "12w")) {
        priorityScore = priorityScore * 1;
    } else if(dueDate >= (currentDate() + "6w")) {
        priorityScore = priorityScore * 1.25;
    } else if(dueDate >= (currentDate() + "3w")) {
        priorityScore = priorityScore * 1.5;
    } else if(dueDate >= (currentDate() + "2w")) {
        priorityScore = priorityScore * 2;
    } else if(dueDate >= (currentDate() + "1w")) {
        priorityScore = priorityScore * 3;
    }
}

return priorityScore;
```

Because all the fields used in the calculation are all contained in the issue, and not on a parent, child, or linked issue, **no additional triggers** settings are needed for the [scripted fields configuration](/cms_trial/space/PSJC/856361791/Scripted+Fields+Configuration/).

The backlog configuration will need to be changed to use the Priority Score custom field for ranking.

## Solution considerations and enhancements

- The script would be much cleaner if the parameter data was kept in a separate CSV data file. However, in order to simplify the solution for this example the data was included in the script itself.
- Additional parameters could be added to increase the accuracy of the score. For example, the script could be enhanced to include:

  - **Assignee** - Score would be higher if issue is assigned
  - **Fix version** - If the work is planned as part of a release it could receive a higher score
  - **Child/linked issue** - Logic could be added to increase the score based on information taken from issues child issues or issues linked to the issue. For example, work linked to customer support requests would receive a higher score.