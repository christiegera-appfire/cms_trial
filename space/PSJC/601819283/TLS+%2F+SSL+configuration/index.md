# TLS / SSL configuration

If you’re concerned about resource security, Power Scripts has you covered!

Starting with engine version 3.0.13, support was added for:

- Deploying a private key with TLS/SSL configuration.
- Secure Cloud communications with various resources, including databases, LDAP, and other REST endpoints.

![Power Scripts for Jira Cloud listener issue update interface](/cms_trial/assets/cc2bb821-7893-46c5-8b56-dd84bf18c3be.png)

The following components are required to use this feature:

1. A unique configuration name.

   - Note: Configurations with duplicate names are overwritten.
2. PEM content with your certificates and/or private key.

   - Appfire recommends encrypted private keys.

     - However, plain private keys (PEM encoded) are acceptable.
   - Private keys and certificates are retained and placed in secure storage.
3. If your key is encrypted, please provide thepassword for decryption.

   - This password is not stored and is only used to install the private key. Afterward, it is discarded.

You must restart the engine for the settings to take effect. Keys and certificates are global components in the SIL Engine and may be used in the database configuration files and for HTTPS access.

Note: Uploading the wrong TLS info may render your engine unusable. If this happens, contact technical support to reset the TLS configuration. Appfire also recommends testing your configurations on a non-production system.

## PEM content

The **Certificate** field can contain a certificate, several X.509 certificates (intermediates and the end one), and the private key if it exists.

Note: Only one private key per PEM is processed. If you have multiple configurations, upload them individually and assign unique names.

Note: The logs on the SIL Engine contain valuable information about the uploaded PEM content. If there is missing information or partially imported configurations, check the log files. In some cases, the parser used for PEMs skips invalid content without generating an error.

Note: To configure the proper authorization chain, a private key must be accompanied by the corresponding public key or certificate. However, it is possible to only upload certificates, if necessary.

### Example: Encrypted private key

```text
Bag Attributes
    localKeyID: 08 C1 70 AF 8E E2 3F F8 06 B4 67 DF 8C 88 82 39 C3 5D B4 BD 
subject=/CN=Client Certificate
issuer=/CN=MyCompany Client Root Certificate Authority
-----BEGIN CERTIFICATE-----
MIIFnTCCAoWgAwIBAgIJALxpUC0CV4frMA0GCSqGSIb3DQEBCwUAMH4xCzAJBgNV
[//....rest of the base64 encoded certificate .....]
PfhN7Mmzvs8csDAjv9zgZWtA0PURUqrvcOVrcpGEehVD
-----END CERTIFICATE-----
Bag Attributes
    localKeyID: 08 C1 70 AF 8E E2 3F F8 06 B4 67 DF 8C 88 82 39 C3 5D B4 BD 
Key Attributes: <No Attributes>
-----BEGIN ENCRYPTED PRIVATE KEY-----
MIIFnjBABgkqhkiG9w0BBQ0wMzAbBgkqhkiG9w0BBdFwDgQIJNNXqbGQn38CAggA
[//....rest of the base64 encrypted key  .....]
Be0=
-----END ENCRYPTED PRIVATE KEY-----
```

In the example above, you must provide the password to decrypt the private key. For a more secure environment, Appfire recommends using encrypted private keys.

### Example: Plain private key

```text
-----BEGIN CERTIFICATE-----
MIIFnTCCAoWgAwIBAgIJALxpUC0CV4frMA0GCSqGSIb3DQEBCwUAMH4xCzAJBgNV
[//....rest of the base64 encoded certificate .....]
PfhN7Mmzvs8csDAjv9zgZWtA0PURUqrvcOVrcpGEehVD
-----END CERTIFICATE-----

-----BEGIN PRIVATE KEY-----
MIIFnjBABgkqhkiG9w0BBQ0wMzAbBgkqhkiG9w0BBdFwDgQIJNNXqbGQn38CAggA
[//....rest of the base64 encoded plain private key  .....]
GTH3fhaM/pZZGdIC75x/69Y=
-----END PRIVATE KEY-----
```

In the example above, the bag attribute information was removed. However, the process works identically, and the password is not required because the private key is not encrypted.

## Managing certificates and private keys

After successfully uploading PEM content, the screen looks similar to the following example:

![Power Scripts for Jira Cloud script execution success display](/cms_trial/assets/78583926-f591-4bae-ba50-782a275f6b8b.png)

The **Delete** icon removes the entire configuration, including the certificate and private key.

Note: You are responsible for updating certificates and will not receive a notification when they are about to expire.