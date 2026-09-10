# getCustomerDetails

## Description

Returns the detail fields for a customer.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getCustomerDetails(customerId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| customerId | string | Yes | The customer id |

## Return Type

[**JSMCustomerDetailField[]**](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=psjc&title=Predefined%20Structure%20Types&linkCreation=true&fromPageId=1818067270)

Returns a list of JSMCustomerDetailField structures for the given customer id

## Example

```javascript
JSMCustomerDetailField[] customerDetailsFields = getCustomerDetails("qm:afdc53a9-c5f4c08de195:16ce414a-e682a47faccc");
for(JSMCustomerDetailField customerDetailField in customerDetailsFields) {
    runnerLog(customerDetailField.name + " = " + customerDetailField.values);
}
```

Returns the detail fields for the specified customer.

## See also