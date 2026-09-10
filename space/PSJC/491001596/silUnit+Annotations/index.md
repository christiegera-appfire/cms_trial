# silUnit Annotations

## Background

As you may have gathered from the name, "silUnit" was inspired by JUnit, the testing suite for Java. Just as found in JUnit, silUnit makes use of annotations to lets the silUnit suite know which functions are intended as tests or features such as running functions before each tests. Below is a brief description of each supported annotation and what they do.

## /\*\* TEST \*\*/ - Test

This basic annotation lets the silUnit Suite know that the function that follows is intended as a test. For example:

|  |
| --- |
| ```text /** TEST **/ function itSaysHello() {     assertEquals(sayHello(), "hello"); } ``` |

## /\*\* BEFORE \*\*/ - Function to Be Run Once

This annotation tells the silUnit Suite that the function is to be run once before the rest of the tests. This is useful if you would like to set up one scenario before testing functions in a series. For example:

|  |
| --- |
| ```text include "Includes/_silUnit.incl";     number value;     /** BEFORE **/ function runOnce() {     value = 0; }     /** TEST **/ function incrementOnce() {     value++;     assertEquals(value, 1); }     /** TEST **/ function incrementAgain() {     value++;     assertEquals(value, 2); } ``` |

## /\*\* AFTER \*\*/ - Function to Be Run Once After a Series of Tests

The "AFTER" annotation tells the silUnit Suite to run the function after the tests have been completed. This is useful to change the value tested to its original state. Let's say, for example, that we would like to do some testing on a custom field, but would like for that value to return to its original state. We could first use the "BEFORE" annotation to set up the test, then the "AFTER" annotation to set the value back to the original. In the example below, imagine we have a custom field called "textField" and we would like to set the value of textField, test that the transaction was successful, then revert the value of textField to its original state.

|  |
| --- |
| ```text include "Includes/_silUnit.incl";   string key = "DEMO-1"; string originalValue;   /** BEFORE **/ function getOriginalValue() {     originalValue = key.textField; }   /** AFTER **/ function setToOriginalValue() {     %key%.textField = originalValue; }   /** TEST **/ function setTextField() {     %key%.textField = "test";     assertEquals(key.textField, "test"); } ``` |

## /\*\* BEFOREEACH \*\*/ - Function to Be Run Once Before Every Test

The "BEFOREEACH" annotation tells the silUnit Suite to run the following function once before each test. Let's say we wanted to reset the value of a custom field before every test. The code would look something like:

|  |
| --- |
| ```text include "Includes/_silUnit.incl";   string key = "DEMO-1";   /** BEFOREEACH **/ function setToEmptyString() {     %key%.textField = ""; }   /** TEST **/ function setToHello() {     %key%.textField = "hello";     assertEquals(key.textField, "hello"); }   /** TEST **/ function setToTest() {     %key%.textField = "test";     assertEquals(key.textField, "test"); } ``` |

## /\*\* AFTEREACH \*\*/ - Function to Be Run Once After Every Test

The "AFTEREACH" annotation tells the silUnit Suite to run the following function once after every test. This is useful for cleanup after every test.

|  |
| --- |
| ```text include "Includes/_silUnit.incl";   string key = "DEMO-1";   /** AFTEREACH **/ function setToEmptyString() {     %key%.textField = ""; }   /** TEST **/ function setToHello() {     %key%.textField = "hello";     assertEquals(key.textField, "hello"); }   /** TEST **/ function setToTest() {     %key%.textField = "test";     assertEquals(key.textField, "test"); } ``` |

## Additional Help

Need help implementing unit tests on your script? Talk to me directly to me by clicking on the bot on this page.