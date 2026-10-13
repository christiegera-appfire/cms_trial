# I want to track SLAs during planned work outside business hours

🤔 **Context:** A support team provides planned after-hours coverage during peak periods, on-call rotations, or special events. The team works standard business hours most days but occasionally supports customers outside those hours.

🌧️ **User problem:** We sometimes work outside our regular business hours, but our SLAs don’t reflect that. If we extend business hours permanently, SLAs become inaccurate on normal days. If we don’t, SLAs pause even when agents are actively working.

☔ **Solution:** Creating **Exceptions** in the calendar.

With [Exceptions](/cms_trial/space/TTSC/35750012/Create+calendars/) in Time to SLA, you can define additional working hours outside your standard business hours, without changing your regular schedule or holidays.

![Time to SLA planned work schedule configuration outside business hours](/cms_trial/assets/a36da8e6-8b4c-4f03-9b3d-196f81823cf6.png)

By adding exceptions to your calendar, you can:

- Track SLAs during planned overtime or special support coverage
- Keep standard business hours intact for normal days
- Add break times within exception hours, if needed
- Create one-time or recurring exceptions
- Share exceptions across calendars or keep them team-specific

When an SLA runs during an exception, an indicator appears in the SLA panel so agents clearly understand why the SLA is progressing outside normal hours.

![Time to SLA planned work calendar selection for SLA tracking](/cms_trial/assets/e0263c49-af0e-4103-8a18-fd30fa6cb029.png)

You can create an exception for after-hours support (for example, 18:00–22:00) and optionally add break times. SLAs count only during the defined exception hours.

## Order of priority for SLA calculation

Depending on your configuration, Time to SLA evaluates working time in the following order:

- **Exceptions → Holidays → Business hours**, or
- **Holidays → Exceptions → Business hours**

You can control this per calendar using the **SLA calculation behavior on exceptions** setting.

## Example: Support shift on a public holiday (Exceptions override holidays)

**Scenario**  
Your team works a planned support shift on a public holiday.

**Configuration**

- Date: 31 December 2025
- Holiday: All day
- Exception: 09:00–17:00
- Break: 10:00–11:00
- SLA behaviour: **Exceptions override holidays**

**How SLA calculation works**

- 08:30 → ❌ SLA does not run (before exception hours)
- 09:30 → ✅ SLA runs (exception hours override the holiday)
- 10:30 → ❌ SLA pauses (break time)

**Result**  
SLAs count only during the defined exception hours, even though the day is a holiday.