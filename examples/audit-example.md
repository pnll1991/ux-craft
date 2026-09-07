# Example: evidence-based UX audit

Scenario: a service landing has a working contact form, but the mobile version places the primary CTA after a long decorative section and validation clears the user's message after a failed request.

## High · Primary action is delayed on mobile

- **Observed evidence:** the CTA appears after non-essential visual content in the narrow layout.
- **Affected task:** request a consultation after understanding the offer.
- **Relevant principles:** selective attention, serial position.
- **Proposed change:** place a contextual CTA after the offer/scope summary and keep the later CTA for users who continue reading.
- **Trade-off:** adds one repeated action, but both actions represent the same next step.
- **Acceptance check:** at 320–390px, a user can identify the offer and reach a consultation action without traversing decorative sections.

## High · Recoverable submission failure discards input

- **Observed evidence:** after a network failure the textarea returns empty.
- **Affected task:** submit an enquiry.
- **Relevant principles:** working memory, peak–end, Postel.
- **Proposed change:** preserve valid entered values, display a specific error and offer retry.
- **Acceptance check:** simulate a failed request; all valid values remain and a successful retry submits once.

This example is illustrative. It is not a measured customer case or conversion claim.
