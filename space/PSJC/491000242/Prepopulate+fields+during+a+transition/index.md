# Prepopulate fields during a transition

This script is called on the create transition and prepopulates the description fields

```text
string steps;

steps = "The following steps must occur in order to complete this task:\n";
steps += "# Make an Observation. Scientists are naturally curious about the world. ...\n";
steps += "# Form a Question. After making an interesting observation, a scientific mind itches to find out more about it. ...\n";
steps += "# Form a Hypothesis. ...\n";
steps += "# Conduct an Experiment. ...\n";
steps += "# Analyse the Data and Draw a Conclusion.\n";

desc = steps;
```