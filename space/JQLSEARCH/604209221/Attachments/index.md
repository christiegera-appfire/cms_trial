# Attachments

The examples on this page describe how to build a JQL search using [JQL Search Extensions](https://marketplace.atlassian.com/plugins/jql-extensions/cloud/overview).

## Attachments JQL keywords

### attachmentContent

Search for issues with attachments containing the provided phrase. The search functionality will find the provided phrase in PDF, Word (doc, docx), PowerPoint (ppt, pptx), Excel (xls and xslx), OpenOffice, and PlainText.

It is not always possible to extract text from files. Complex PDFs and Excel files are the most problematic, however, in 99% of cases, indexing is successful.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Examples**

Find issues with attachments containing the phrase `specification`.

```text
attachmentContent ~ "specification"
```

### attachmentsCount

Search for issues that have a specific number of attachments.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Examples**

Find issues with attachments:

```text
attachmentsCount > 0 
```

### attachedByUser

Search for issues with attachments added by a particular user.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Examples**

Find issues with attachments added by "Jane Potter".

```text
attachedByUser = "Jane Potter"
```

### attachedOnDate

Search for issues with attachments added on a particular date. This JQL keyword works with date-related JQL functions:

- endOfDay()
- endOfMonth()
- endOfWeek()
- endOfYear()
- lastLogin()
- now()
- startOfDay()
- startOfMonth()
- startOfWeek()
- startOfYear()

**See also**:

- [Note on aggregation of dates](/cms_trial/space/JQLSEARCH/604209257/Aggregation+of+dates/)
- [Note on dates with timestamps](/cms_trial/space/JQLSEARCH/604209245/Dates+with+time/)

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Examples**

Find issues with attachments attached on particular dates.

```text
attachedOnDate >= "2016/03/14" and attachedOnDate < "2016/03/15" 
attachedOnDate < now()
```

### attachmentExtension

Search for issues with attachments with a particular extension.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Examples**

Find issues with attachments with PNG or JPG extensions.

```text
attachmentExtension = "png" OR attachmentExtension = "jpg"
```

### attachmentName

Search for issues with attachments with a particular name.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Examples**

Find issues with an attachment name containing `screenshot`.

```text
attachmentName ~ "screenshot"
```