# Packages

With the advent of SIL 5.8.0.0 we introduced packages for our ever-growing library of functions. The logic behind it is that for many of the addons what we already had, we had to introduce functions / functions following some naming convention ( for instance, for Power Dashboards Reports and Gadgets all functions started with ‘*reporting\_’*). We really hope to save you some typing.

A function must have a name, but it may also have a package and a ‘short’ name. To call it, either

1. you must declare that you use that package and simply call it by the ‘short’ name, or
2. you may simply call it by its 'long' name, as you did before introduction of packages.

As it is now, you cannot introduce yourself a new package via the language itself. If you really need such a feature, let us know.

## Example

Let’s see a very simple example: [fileOpen](/cms_trial/space/PSJC/434602716/fileOpen/) function lives within the ‘*file*' package, and has the short name ‘*open*’. The full name of the function is actually '*fileOpen*’. Check the docs, people, we added for such functions the package information in that little table above!

To use it by the short name, all we have to do is:

```java
use "file"; //announce the package usage

const string filename = "afile.txt";

int fid = open(filename); //short name
// the following line will still work, but the above seems IOHO cleaner:
//int fid = fileOpen(filename); //long name
```

That may not seem much, but, if you look at the Excel Connector, for instance, you will see why we love this feature.

```java
use "excel";

int fid = openWorkbook("test.xlsx"); //excelOpenWorkbook

addSheet(fid, "Data" , true); //makes it current, full name 'excelAddSheet'
addRow(fid, 0); //excelAddRow

setCurrentSheet(fid, "Sheet1"); //excel....you got the point!
addRow(fid, 0);

setCell(fid, "Value 1", "A1");
setCell(fid, 12001, 0, 1);

setCell(fid, "Value 2", "Data", 0, 0);
setCell(fid, 20010, "Data", 0, 1);

closeWorkbook(fid); //save it
```