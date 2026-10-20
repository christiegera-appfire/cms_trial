# Writing Scripted Custom Fields

Writing SIL scripts for Scripted Custom Fields is fairly basic. There are two main concepts to know when writing a script:

1. The script runs in the context of an issue. This means that all the [standard variables](/cms_trial/space/PSJC/434602568/Variable+types+and+reference+methods/) are available and pre-populated with the data from the issue that triggers the script.
2. The custom field value gets updated during the **return** statement at the end of the script. See the basic example below to see how the value is set.

**Basic text field example**

```text
return "simple text field";
```

The value of this custom field for all issues would be “simple text field”.

## Other examples

### Setting the value of a cascading select field

```text
return {"Option 2", "sub-opt-2-2"};
```

For field like cascading select lists, regular select lists, checkboxes, bullets, etc., the predefined options used in those fields should be preconfigured. The script can set the value of the field to one of the available options, but it can not create the option and add it to the fields configuration.

### Setting the value of a checkbox field

```text
return "option1";
```

### Using rich text when setting the value of a text field

```text
return "And another paragraph containing emojis: {{emoji}}🙂||:slight_smile:||1f642{{/emoji}}";
```

## More examples

For more Scripted Custom Field examples see [this page](/cms_trial/space/PSJC/854327327/Scripted+Custom+Field+recipes/) within the Tutorials and Recipes section.