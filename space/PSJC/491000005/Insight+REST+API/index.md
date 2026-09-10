# Insight REST API

### **Insight Inclusion Script**

The following code is a library of functions that works with the Insight (Jira Assets) REST API using manual HTTP requests.

```java
struct objectType {
    number id;
    string name;
    number type;
    string created;
    string updated;
    number parentObjectTypeId;
    number objectSchemeid;
    boolean inherited;
}

struct referenceObj {
    number id;
    string label;
    string objectKey;
    objectType objectType;
    string created;
    string updated;
}

struct attributeValue {
    string value;
    string displayValue;
    referenceObj referencedObject;
    
}
struct attribute {
    number id;
    number objectTypeAttributeId;
    attributeValue[] objectAttributeValues;
    number objectId;
    number position;
}

struct objectEntry {
    number id;
    string label;
    string name;
    string objectKey;
    objectType objectType;
    attribute[] attributes;
}

struct defaultType {
    number id;
    string name;
}

struct objectTypeAttribute {
  number id;
  string name;
  string label;
  number type;
  defaultType defaultType;
  boolean editable;
  boolean system;
  boolean sortable;
  boolean summable;
  number minimumCardinality;
  number maximumCardinality;
  boolean removable;
  boolean hidden;
  boolean includeChildObjectTypes;
  boolean uniqueAttribute;
  string options;
  number position;
}

struct insightQueryResult {
    objectEntry[] objectEntries;
    objectTypeAttribute[] objectTypeAttributes;
}

/*
* Retrieves the Insight object key of a Jira issue custom field.
* @param fieldValue (string) The value of a custom field.
* @return (string) The object key of the insight object. Example: ABC-123
*/
function getCustomFieldInsightKey(string fieldValue) {
    return matchText(fieldValue, "(?<=\\().+?(?=\\))");
}

/**
* Runs a query against a specified insight schema to gather object(s) using the
* IQL query language. See https://bit.ly/2OI5QVt for more info about IQL.
* @param schemeId (string) The id of the insight schema to query. Example: "2"
* @param iqlQuery (string) The IQL query string to return the desired objects. Example: 'Key in ("ABC-1", "ABC-2")'
* @param username (string) Username of user of Insight schema.
* @param password (string) Password that corresponds to the 'username' parameter.
* @return insightQueryResult representation of query result.
*/
function getInsightObject(string schemeId, string iqlQuery, string username, string password) {
    string insightURL = getJIRABaseUrl()+"/rest/insight/1.0/iql/objects";

    HttpRequest request;
    request.headers += httpBasicAuthHeader(username, password);
    request.parameters += httpCreateParameter("objectSchemaId", schemeId);
    request.parameters += httpCreateParameter("iql", iqlQuery);
    
    insightQueryResult result = httpGet(insightURL, request);
    
    return result;
}

/*
* Retrieves the value of an attribute based on the provided attribute name.
* @param obj (insightQueryResult) Insight object to retrieve value from
* @param attributeName (string) The name of the attribute to retrieve.
* @return string representation of attribute value if found. Otherwise, null if attribute is not found.
*/
function getInsightObjectAttribute(insightQueryResult obj, string attributeName) {
    string[] result;
    if(isNotNull(obj)) {
    
        // Determines if an attribute with propvided 'attributeName' exists.
        // If true, saves the corresponding id of attritute to search for value.
        number attributeId = 0;
        for(objectTypeAttribute t in obj.objectTypeAttributes) {
            if(t.name == attributeName) {
                attributeId = t.id;
                break;
            }
        }
    
        // If attribute exists, finds the corresponding value of the attribute.
        if(attributeId != 0) {
            for(objectEntry o in obj.objectEntries) {   // Possible multiple objects
                for(attribute a in o.attributes) {      // Possible multiple attribute values
                    if(a.objectTypeAttributeId == attributeId) { 
                        for(attributeValue v in a.objectAttributeValues) {
                            result += v.displayValue;
                            break;
                        }
                    }
                }
            }
        }
    }
    return result;
}
```