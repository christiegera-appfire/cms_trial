# API Rate Limiting

To ensure stable and reliable performance for all customers, 7pace applies API request limits, also known as throttling. This is a common industry practice that helps maintain consistent system performance, prevent service disruptions, and ensure fair usage of shared infrastructure.

Learn why throttling exists, how it works, and how to avoid reaching API limits.

## What is API throttling?

API throttling limits the number of requests that can be sent to the 7pace API within a specific time period. If you send too many requests in a short timeframe, the system may temporarily slow down processing or return an error.

If you exceed a rate limit, the API returns **HTTP 429 — Too Many Requests**.

Example response:

```json
{
  "statusCode": 429,
  "errorDescription": "The request has been canceled because your API usage was exceeded.",
  "fields": {
    "retryAfter": "37"
  }
}
```

The `retryAfter` value (in seconds) indicates how long to wait before sending another request.

## Why we use API rate limits

API rate limits help us:

- Maintain consistent performance for all customers.
- Protect the platform from traffic spikes.
- Prevent unintended overuse, like infinite loops.
- Ensure usage aligns with your selected subscription plan.

Throttling keeps the 7pace API stable and responsive across all organizations.

## How throttling works in 7pace

There are two main types of limits.

### Plan-based limits

Each 7pace Timetracker plan includes API request limits appropriate for that tier. For example, the Free plan includes:

- 50 requests per hour.
- 5 requests per minute.

### General system limits

In addition to plan-based limits, general system limits apply across organizations to protect overall platform performance. These limits may differ depending on the type of endpoint being used. If multiple limits apply, the most restrictive one applies.

## Common usage scenarios

The current rate limits are generally high enough to accommodate standard integration use cases.

| Use case | Rate limiting |
| --- | --- |
| CRUD operations | Minimal rate limiting. Hundreds of requests per user per hour are typically safe, provided they aren't sent in a short burst. See [7pace Timetracker REST CRUD API Version 3](https://support.appfire.com/space/7TFA/1253540003/7pace+Timetracker+REST+CRUD+API+Version+3). |
| One-time or incremental data sync | Moderate rate limiting may apply due to larger response sizes. Limits are sufficient for initial data loads and scheduled incremental refreshes. |
| Repeated full historical data loads | Repeatedly requesting all historical data multiple times per day is likely to exceed rate limits. We recommend redesigning the integration to use incremental updates. |

## Best practices to avoid API rate limiting

To reduce the risk of hitting rate limits:

- **Use incremental refresh** instead of repeatedly retrieving full historical datasets. See [How to Avoid API Rate Limiting](https://support.appfire.com/space/7TFA/1253539907/How+to+Avoid+API+Rate+Limiting) for implementation guidance.
- **Respect the** `retryAfter` **value** when receiving a 429 response.
- **Implement retry logic** with exponential backoff.
- **Avoid tight polling loops.**
- **Distribute requests over time** instead of sending them in bursts.
- **Cache frequently accessed data** where possible.

## Excessive usage

If we detect extremely excessive usage — such as infinite loops or intentional abuse — we may temporarily increase throttling for the affected organization to protect system stability. When possible, we'll try to contact you before applying stricter limits.

## Need higher limits?

If your current or planned integration requires higher API throughput than the default limits support, contact us via the [Support Portal](http://appf.re/support) with details about your use case and expected request volume. We review requests on a case-by-case basis.