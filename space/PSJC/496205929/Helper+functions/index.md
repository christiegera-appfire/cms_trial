# Helper functions

There are two helper routines available to ease your work with persistent variables. These routines allow you to set or retrieve the value of a persistent variable from a script that is not in the context of the issue or just to retrieve a global variable:

Values are treated as strings. For the above example:

```java
string globalCounterVar = getPersistentVar("counter");
number test_one_counter = getPersistentVar("TEST-1", "counter"); //notice the implicit cast! values are treated like strings, though!
```

- Although useful, persistent variables come with a small performance penalty. Don't overuse them!
- There's no way to delete a persistent var (other than direct SQL) at the moment. Think hard if you really need them.

**See More**