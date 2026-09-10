# Background and design philosophy of SIL

## Origins and development

The development of Simple Issue Language (SIL) emerged from real-world challenges in Jira customization projects. Initially, our team found ourselves creating numerous similar workflow actions, conditions, and validators that were essentially performing the same operations but on different fields.

This approach resulted in significant limitations:

- Reduced flexibility in configuration options
- Increased maintenance overhead
- Difficulty adapting to changing requirements
- Version compatibility challenges during Jira upgrades

## Key design principles

Based on these challenges, we established several core design principles for SIL.

|  |  |
| --- | --- |
| Simplicity first | Existing scripting solutions required users to understand Jira's internal API structure and write verbose code for simple operations. SIL was designed to enable users to perform common actions with minimal syntax. For example, setting an assignee can be done with a simple assignment statement rather than complex API calls. |
| Field independence | Rather than creating separate functions for each field type, SIL provides a unified approach to field manipulation that works consistently across standard and custom fields. |
| Jira abstraction | SIL insulates users from Jira's internal implementation details. This provides two significant benefits:   - Simpler scripts that focus on business logic rather than technical details - Better resilience to Jira version changes, reducing upgrade-related maintenance |
| Platform independence | From its inception, SIL was designed as a standalone language that could operate outside of Jira. This architectural decision has enabled us to use SIL for multiple purposes, including installation scripts for our apps. |

This approach has enabled the successful implementation of complex Jira customizations that would have been challenging with traditional approaches. The language's focus on simplicity and abstraction makes it accessible to a wider range of users while still providing the power needed for sophisticated business logic.

## Further development

Over time, SIL has evolved significantly:

- Enhanced syntax for improved readability
- Expanded function library for more complex operations
- Broader support for custom field types
- Improved development tools and editors

SIL continues to evolve based on user feedback and emerging requirements while maintaining its core philosophy of simplifying Jira customization through an intuitive, purpose-built scripting language.