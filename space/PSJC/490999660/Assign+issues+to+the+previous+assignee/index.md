# Assign issues to the previous assignee

## Assign an issue to the previous assignee

```text
string [] testers = usersInRole("TEST", "Product Development Tester");
assignee = testers[0];
```

## Action

```text
string [] h = fieldHistory(key, "assignee");
string a;

if(isNotNull(h[1])) {
    a = h[1];
}
else {
    a = h[3];
}

assignee = a;
```