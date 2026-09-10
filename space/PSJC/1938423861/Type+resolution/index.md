# Type resolution

Details how SIL determines the resulting type from operations involving multiple data types and resolves type conflicts.

When evaluating an operation, SIL follows this three-step type resolution process:

|  |  |
| --- | --- |
| **Step 1:** **Direct match** | If the RHS type is valid for the operation, it proceeds immediately. The result is calculated as described in the operator table. |
| **Step 2:** **Type conversion** | When SIL encounters a convertible type on the right-hand side (RHS), it tries to convert it to valid types in the same order that valid types are listed in the [Operatros reference](/cms_trial/space/PSJC/434962512/Operators+reference/) tables. This is important because it determines which type conversion is attempted first. See [Type conversion example](/cms_trial/space/PSJC/1938423861/Type+resolution/) below. |
| **Step 3:** **Error handling** | If the RHS type is neither valid nor convertible, the program stops with an error. |

### Type conversion example

Here’s a practical example for the `+` operator with LHS type `number`.

```text
// Valid types (in order):
// 1. number
// 2. integer

number x = 10.5;        // LHS is number
x += "42";              // RHS is string (a convertible type)
//The attempted operation is to add 42 to x and assign the new value to x.
```

Here’s what happens:

The conversion attempt follows the order of valid types:

1. First, it tries to convert `string` (“42”) to a `number` and succeeds.
2. Conversion stops at first successful attempt (`number`); no further conversion is attempted.

If the first conversion failed, it would try the next valid type (`integer`). If the second conversion is successful, the operation is carried out.

1. Next, it carries the actual operation and adds 42 to 10.5.   
   If you ask for a return value, it will show 52.5.

   ```text
   runnerLog("After adding \"42\": " + x);
   // Prints result: After adding "42": 52.5
   ```

This ordered approach ensures consistent and predictable type conversion behavior in all SIL operations.

---

### Automatic type conversion

Type conversion in SIL enables variables of different types to be automatically converted when using the assignment (=) operator. This conversion process happens when you assign a value of one type to a variable of another type. When you make such an assignment, the system automatically attempts to convert the source value into a format that matches the target type while keeping its original meaning. For example, when converting a number to an integer, the system preserves the basic numeric value while adapting it to fit integer requirements. To learn more, see [Type conversion](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15488650).