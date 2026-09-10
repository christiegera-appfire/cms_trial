# hmacSHA256

## Description

Computes a signature over the data using HMAC - SHA256

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | hmacSHA256(data, key) | **Package** |  |
| **Alias** |  | **Pkg Usage** | hmacSHA256(data, key) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| data | string or byte[] | Yes | the data |
| key | string | Yes | key that you want to use to compute the signature |

## Return Type

**byte []**

Signature, empty if not ok (empty data)

## See also