# silEnv

## Description

Returns the variable as presented in the environment. A special variable is set 'sil.home' that will point to the actual location of the SIL programs. You can configure this folder from the [SIL configuration](/cms_trial/space/PSJC/490996120/SIL+configuration/) page.

Valid variables:

1. **sil.home**  points to the folder keeping the SIL programs
2. Any Java environment variable (such as 'java.home', 'os.arch', etc )
3. Any environment variable, exported in the operating system (XX =aa ; export XX )

Additionally, the function looks in the 'sil.home ' directory after a file called 'sil.properties '.

You can put all your host -dependent variables in here, and create easy-transferable scripts. This file contains key -value pairs (name =value ).

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | silEnv(variable\_name) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| variable\_name | String | Yes | Env variable name. |

## Return Type

**String**

## Example

```javascript
print("Your SIL programs are in " + silEnv("sil.home"));
```

Every time the sil.home is changed, the contents of the old 'sil.properties' file will not be taken into account by this function. You must copy the contents of the old file in the new location manually.

See  [Environment Variables](/cms_trial/space/PSJC/496206033/Environment+variables/) for more details.

## See also