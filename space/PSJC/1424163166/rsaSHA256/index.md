# rsaSHA256

## Description

Computes a signature over the data using RSA - SHA256

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | rsaSHA256(data, key) | **Package** |  |
| **Alias** |  | **Pkg Usage** | rsaSHA256(data, key) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| data | string or byte[] | Yes | the data |
| key | string | Yes | the private key that you want to use to compute the signature |

## Return Type

**byte []**

Signature, empty if not ok (empty data)

## See also