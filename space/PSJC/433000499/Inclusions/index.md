# Inclusions

This page explains how to use include statements in Simple Issue Language (SIL) programs.

The `include` statement in SIL lets you import and execute code from other SIL files. This can improve readability and make your code more manageable.

You can use the `include` statement to:

- Import entire libraries of user-defined functions (UDFs).
- Break down large programs into manageable components.
- Share common functionality across multiple scripts.

## Syntax

Inclusions in SIL use the following syntax:

```text
include "path/to/file.incl";
```

Here are some key points to remember when using inclusions in your SIL programs:

- Include statements must appear at the beginning of your program before any user-defined function definitions.
- File paths can be relative or absolute.
- Relative paths are resolved relative to the defined `sil.home` environment variable (typically the **silprograms** directory in the SIL Manager).
- To maintain consistency, consider using the `.incl` extension for included files.

For more information, see  [Structure of a SIL program](/cms_trial/space/PSJC/435028021/Structure+of+a+SIL+program/).

---

## Variable visibility

There are two categories of variables you can use in the **included programs**.

| **Variable category** | **Definition** | **Example** |
| --- | --- | --- |
| Local | These are the variables you define in the body of the included program. They are accessible throughout the included file, the main program, and any other program that uses the included code. | **file.incl** ```text // Define a simple increment function function increment(int x) {   return x + 1; }  // Create and initialize a variable using the function // This variable will be accessible to any program that includes this file number a = increment(0);  // a is now equal to 1 ``` **program.sil** ```text // Import the contents of file.incl include "file.incl"; //resolved relative to the 'sil.home'  // We can use both the 'a' variable and increment() function defined in file.incl number b = a + increment(2);  // Here's what happens: // 1. 'a' has value 1 from file.incl // 2. increment(2) returns 3 // 3. b becomes 1 + 3 = 4 ``` |
| Global | These are the variables that are already defined and can be used right away (issue fields and custom fields). You can use these anywhere in your code without having to declare them. | **file.incl** ```text function getKey() {   return key;    // 'key' is a global issue field } ``` |

---

## Header guards

Header guards prevent duplicate inclusion of the same code, which is particularly important when you have complex include relationships. They automatically handle situations where the same code might be included multiple times (accidentally or intentionally) through different paths.

Here’s how header guards work:

- When you include a file, SIL first checks if this file has already been processed.
- If it's the first time, the code is included.
- If the file has been previously included, SIL skips it.
- This happens automatically - no additional syntax is required.

#### Example

In this scenario the **main.sil** program uses **A.incl** and **B.incl** files. Both are using include file **C.incl**. Even though file C is referenced twice (through both **A.incl** and **B.incl**):

- it will only be loaded the first time it's encountered.
- it will be automatically skipped on subsequent includes, preventing any errors in your program.

```text
main.sil
│
├── A.incl
│   └── C.incl    // First time included
│
└── B.incl
    └── C.incl    // Skipped, already included
```