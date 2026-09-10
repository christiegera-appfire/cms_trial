# Structure of a SIL program

This page provides a foundational overview of how Simple Issue Language (SIL™) programs are organized and gives a concrete example of the structure of a SIL program. Understanding the basic components of the structure will help you contextualize all other concepts introduced later in this guide.

SIL programs can be simple or more elaborate. Regardless of their complexity, the structural components of a SIL program are the same. A SIL program follows a clear top-to-bottom structure:

```text
[inclusions]
[use declarations]
[variable declarations]
[user-defined functions declarations]
[actual code]
```

It starts with inclusions and uses declarations to import libraries and packages, followed by variable declarations and user-defined functions. The program concludes with the main body containing the actual processing logic, local variables, and a return statement that provides the output. Following this structure ensures a well-organized and maintainable codebase.

Let's break down the key aspects of each component.

| **On this page:** |
| --- |

## Structural components

### Inclusions

Include statements must appear first or after use declarations.

- They use the `#include` directive.
- They allow you to import libraries of user-defined functions or add code fragments to your program.
- Imported files' names typically end with the `.sil` extension.

#### Learn more

For more information, see [Inclusions](/cms_trial/space/PSJC/433000499/Inclusions/).

### Use declarations

SIL uses packages to streamline function naming and usage and make code more concise.

- Packages allow functions to be called by short names, reducing typing effort.
- To use short names for functions, you must declare package uses.

#### Learn more

For more information and usage, see [Packages](/cms_trial/space/PSJC/493944881/Packages/).

### Variable declarations

In this section of the SIL program, you declare global variables available throughout the program.

- You can declare various types of variables, such as `string`, `number`, and `array`.
- Variables can be initialized with default values.
- It is a best practice to group related variables together.

#### Learn more

For more information and usage, see the [Variables](/cms_trial/space/PSJC/434602568/Variable+types+and+reference+methods/) section on the [SIL Syntax and types introduction](/cms_trial/space/PSJC/435028043/Syntax+and+types+introduction/) page.

### User-defined functions declarations

In this section of your SIL program, you can define any functions you want to use in the main code. These user-defined functions (UDFs) can considerably improve the readability and maintainability of the code.

- UDRs must be defined before use, and their names cannot contain spaces.
- Each function should have:

  - Clear name indicating its purpose
  - Defined parameter types
  - Return type specification
  - Proper documentation

#### Learn more

For more information, see  [User-defined functions (UDFs)](/cms_trial/space/PSJC/433000514/User-defined+functions+(UDRs)/).

### Actual code

This is the main body of the program, which contains the primary logic. This is where you input the modifications you want the program to accomplish. The main body can also contain the definition of local variables and calls to the imported or user-defined functions in the steps above. It should end with a `return` statement.

---

## SIL program example

This SIL program example demonstrates the basic structure of a SIL program while performing a common task:

- Process an issue record to ensure its description field doesn't exceed a maximum length.
- Truncate the text and add an ellipsis if the description field exceeds the maximum length.

```text
// ================== INCLUSIONS ==================
include "custom_utils.incl"

// ================== USE DECLARATIONS ==================
use "file";

// ================== VARIABLE DECLARATIONS ==================
const int max_length = 50;

// ================== USER-DEFINED functionS ==================
function truncateDescription(string desc) {
    if (length(desc) > max_length) {
        return substring(desc, 0, max_length) + "...";
    }
    return desc;
}

// ================== ACTUAL CODE (MAIN BODY) ==================
description = truncateDescription(description);

int fid = open(key + "-file.txt");
write(fid, description);
close(fid);
```

The use of inclusions, standard packages, global variables, and custom functions in this example demonstrates the structural organization and modularity of SIL programs.

This breakdown highlights how the different sections of the SIL program work together to achieve the overall goal of truncating long issue descriptions:

| **Component** | **Description** |
| --- | --- |
| **Inclusions** | The `#include "custom_utils.incl"` statement allows the program to access custom functions defined in an external file named `custom_utils.incl`. This is a common way to organize and reuse functionality across multiple SIL programs. We do not impose extensions, but we recommend using `.incl` for includes and `.sil` for SIL files.  Files must exist in the root of the hierarchy (that is *silprograms* directory). |
| **Package declarations** | - The `use "file";` statement brings in the standard file package, providing access to text manipulation functions like `open()` and `write()`, used in the program in their short form. They still exist in the library of standard functions, but their full name is `fileOpen()` and `fileWrite()`. Using packages is just a convenience or a shrothand. |
| **Variable declarations** | The `const int max_length = 50` declaration defines a global variable that stores the maximum allowed length for issue descriptions. This can be adjusted as needed. Note that this is a constant and cannot be altered. |
| **User-defined functions** | The `truncateDescription()` function is a custom function created within this SIL program. It takes a string parameter `desc` and returns a truncated version of the description if it exceeds the `max_length` limit. |
| **Actual code (main body)** | - The main body tells us that this script must be run in an issue context. - `description` is never declared because it’s an implicit field in an issue. The line`description = truncateDescription(description);` calls the `truncateDescription()` function and saves the truncated value back in the current issue. - Finally, we open a file, write the new description from the issue into it, and close it. `int fid = open(key + "-file.txt");` represents a declaration of the file identifier, initialized with the return of the call to open the file. `key` is another standard field of the issue, read-only, and is not declared, because it is injected into the script at runtime. `key + "-file.txt"` is a concatenation operation between two strings. |