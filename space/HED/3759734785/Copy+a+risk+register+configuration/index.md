# Copy a risk register configuration

When you create a risk register in Hedge, you can copy settings from an existing register. This helps you apply a consistent configuration across multiple registers without setting up every option again.

## Copy settings from another risk register

1. In Jira, open Hedge and start creating a risk register.
2. Search the list for an existing risk register and select it as your configuration source.

1. Review the preselected template and issue types. When using a source register, you can adjust issue types, but you can't change the matrix template.
2. Complete the remaining settings and create the risk register. Hedge copies the configuration from your selected source, using the issue types you specified.

Selecting a source register is optional. If you don't select one, the standard risk register creation process applies.

![Risk register creation screen showing the Copy configuration from another register option.](/cms_trial/assets/948e525e-3f6b-40ed-bee2-2f6dad0b0c18.png)

## Settings copied to the new risk register

Hedge copies the following settings from the selected risk register:

- Probability field settings
- Impact field settings
- Risk score formula
- Risk matrix settings, including matrix size and values
- Issue types, which you can modify during creation
- Added columns

If the source register has multiple risk calculation tabs, Hedge copies all of them.