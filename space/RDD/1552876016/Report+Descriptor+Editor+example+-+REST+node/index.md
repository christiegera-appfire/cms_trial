# Report Descriptor Editor example - REST node

This example illustrates how to use a REST node in the Report Descriptor Editor to access an external data source and display the retrieved data in a table. The completed sample table is displayed below.

![The completed table that will be completed following the steps on this page.](/cms_trial/assets/9d4a723e-ce56-4033-b18b-64b5d8fad4fc.png)

To begin, open the editor and define:

1. The type of connection.
2. The location of the external data source.

This example uses an external open API (randomuser.me) that returns fictional user information:

![Define the type of connection and location](/cms_trial/assets/5d0ef238-c805-4aa9-966a-594c94fd3b15.png)

At the end of the uri statement, specify the number of results required, 21 in this example.

Next, add a JSON child node under the REST node:

![Set the type to JSON](/cms_trial/assets/6abedbef-d936-4bc1-9ca1-0789ed4b3cf3.png)

This statement renders the external information in an object and array, and each position of the array represents a unique fictional user. In the *Preview* window, there is a separate results section for each user.

![Fictional user information displays in the Preview window.](/cms_trial/assets/97542898-474a-45ce-8d58-e05202b89ffa.png)

Now, indicate that the data returned from the API should be formatted in a table.

![Specify that the data will be displayed in a table.](/cms_trial/assets/0e9a1e8b-47ac-4a0c-b6e4-36ec74271cd9.png)

Table nodes:

- Path: Specifies that the results section is being used for each fictional user.
- Style

  - flex: 1 (use the entire page)

The table columns are defined in lines 14 - 52 below.

![Define the column headings.](/cms_trial/assets/b1c98f74-33f2-44f6-9b83-ca1d6ada71c2.png)

The header statements define the column headings in the table, including:

- Name and thumbnail image (rows 16 - 40)
- Birth (rows 41 - 45)
- Gender (rows 46 - 52)

Column nodes:

- The src statement on line 32 (above) indicates the column displays the thumbnail picture from the results file.

  ![The thumbnail data displayed in the Preview window.](/cms_trial/assets/4efde241-3283-4860-b6cd-0ff171c6637e.png)
- Row 35 specifies the results used for the Name field.

  ![Data from the Preview window, including title, first, and last.](/cms_trial/assets/3d27dfcc-5d9d-4114-ae65-b98480710863.png)
- The Birth column, rows 41 - 43, uses an accessor attribute that manipulates the date of birth and age fields using the $formatDate function to concatenate it with the user’s age in parentheses and the letter “y” at the end, indicating years.

  ![The formatDate function.](/cms_trial/assets/d0b7f661-5a0a-4088-87a1-36f1f87cce11.png)![The birth and age information in the Preview window.](/cms_trial/assets/9d95c876-265c-46cd-a181-f13ad17a27f6.png)
- The gender column displays the fictional user’s gender.

  ![Display the user's gender in the third column.](/cms_trial/assets/b2ac97df-8d5b-4918-9e2f-519661b63ee6.png)

The completed table is displayed below.

![The sample table generated in this example.](/cms_trial/assets/2ef427c2-ccd9-4c03-a9c3-22cb20963c41.png)

Download the JSON descriptor here:

![contentId-1552876016](/cms_trial/assets/2979799e-b718-46b6-82f8-568fd7c9686e.json5)