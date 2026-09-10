# Type handling

This page describes how Simple Issue Language (SIL) determines valid types during operations and manages type conversions.

SIL uses a left-hand side (LHS) driven type system for operations. This means that:

- The type of the left operand (LHS) determines how the operation behaves.
- Operations only proceed under two conditions:

  - The right-hand side (RHS) type is already valid for the operation.
  - The RHS type can be converted to a valid type.
- Type conversion, when needed, only applies to the right operand (RHS); the left operand never changes type.
- Each operator in SIL has its own set of rules depending on the LHS type. These rules are defined using two lists:

|  |  |
| --- | --- |
| **Valid types list** | Types that can be used directly with the operator. The operators tables in the [Operatros reference](/cms_trial/space/PSJC/434962512/Operators+reference/) show the relationships between operators, types, and their valid combinations. |
| **Convertible types list** | Types that can be converted into one of the valid types.  For details, see the [Type Conversion](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15488650) topic. |

Think of it like this:

- Valid types are like having the right key for a lock; they work immediately without modification.
- Convertible types are like having a key that needs some reshaping before use - they require a transformation but can still work.
- Any other type is like having the wrong key entirely - the operation cannot proceed.
- The "lock" (operation) is always determined by the LHS type.

This system helps prevent unexpected type conversions and makes code behavior more predictable. The type conversion rules are consistent across all operators. The reference tables on this page show these relationships in detail, specifying which types are valid for each operator and what conversions are possible.