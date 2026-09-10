# Create an issue score custom field

```text
int score = 0;

if(isNotNull(assignee)) {
    score += 10;
}
if(isNotNull(dueDate)){
    score += 10;
}
if(isNotNull(description)) {
    score += 10;
}

if(score < 10) {
    return "Bad";
}
else if(score >= 10 and score < 20) {
    return "OK";
}
else if(score >= 20 and score < 30) {
    return "Good";
}
else {
    return "Great";
}
```