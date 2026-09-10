# Script Snippets

Script snippets are small sections of code that can be inserted into a larger script. They are typically used to perform specific tasks or functions within the overall automation script, and they allow you to reuse code and save time by not having to write everything from scratch.

## Using Script Snippets

There are two types of script snippets: syntax snippets and functional script snippets.

- **Syntax snippets** are bits of code used to create common code syntaxes like loops or conditional statements.
- **Functional snippets** are bits of code used to perform a function or operation, such as creating a new Jira issue.

There are two ways to use the snippets feature. The first way is when you want to create a new script from a snippet. The second method is to insert code into existing scripts.

## New scripts from snippets

To use this, ensure you don’t have any scripts open in the SIL Manager. With all scripts closed, you will see a **Quick Start** button in the editor panel of the SIL Manager. In this introductory video, you will learn how to create a SIL file from a snippet:

Clicking the Quick Start button will launch a new menu to create a new script from a code snippet. To create the script, you will need to provide the following information:

- **Script folder** – this required field specifies which folder the script will be created in. All scripts can be created directly in the *silprograms* folder, but we recommend using subfolders.
- **File name** – this is the name you wish to give to the new file and is also required. We suggest using intuitive names and including the .sil extension in the file name (not mandatory).
- **Snippet** - this is the bit of reusable code you wish to start writing the script with.

![Power Scripts for Jira Cloud snippet settings interface](/cms_trial/assets/0f719ac0-8db7-4810-8a21-f8f793f59c33.png)

## Inserting snippet code

If a script is already open, there will be two options in the menu bar for inserting snippets:

1. **Insert** - this menu contains the snippets specifically designed for syntax code, such as loops and conditional statements. See the Syntax Snippets section of the [Script Snippets Code](/cms_trial/space/PSJC/723320880/Script+Snippets+Code/) page for more information about these snippets.

   ![Power Scripts for Jira Cloud script storage configuration interface](/cms_trial/assets/5419a8ba-9b04-452c-83ae-b6b00c4007f8.png)
2. **Snippets** - this menu contains the functional code snippets, such as creating a new Jira issue. See the Functional Snippets section of the [Script Snippets Code](/cms_trial/space/PSJC/723320880/Script+Snippets+Code/) page below for more information about these snippets.

   ![Power Scripts for Jira Cloud SIL configuration panel](/cms_trial/assets/28e49ee7-bcb8-4066-9ebb-2a90a3a63052.png)

**Note:** The same snippets exist between these two menus, and the menu shown for creating a new file from a snippet.

Once a snippet has been selected, the snippet code will be inserted into the existing file.

Multiple snippets can be inserted into a single file to be combined by the user into custom scripts.