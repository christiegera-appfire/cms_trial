# Environment variables

In addition to the local variables defined in a SIL™ program and issue variables (Variable Resolution), there are environment variables. These are global constants you can access in any SIL™ program using the silEnv function.

In addition to the local variables defined in a SIL™ program and issue variables ([Variable Resolution](/cms_trial/space/PSJC/434602568/Variable+types+and+reference+methods/)), there are environment variables. These are global constants you can access in any SIL™ program using the [silEnv](/cms_trial/space/PSJC/434602941/silEnv/) function.

## Declaring Environment Variables

To be able to use these variables, you have to follow two steps:

1. Environment variables must be defined in a special file named sil.properties. This file is placed in the same directory designated as sil.home (for instance the one that contains all your scripts). You must create this file manually.

#### **sil.properties**

```text
VAT=0.24
```

2. Retrieve the value in the SIL™ program and then use it just like any other variable. Make sure you cast it to your designated type (in our case, a number).

```text
number VAT = silEnv("VAT");
number price = customfield_10019;
print("VAT is:" + (price * VAT));
```