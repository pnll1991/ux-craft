# Example: service landing brief + decisions

This is an illustrative project fixture, not a customer case.

## Brief

- **Audience:** a small business owner evaluating a specialist service.
- **Primary task:** understand the offer and decide whether to request a consultation.
- **Known constraints:** existing brand and stack must remain; no invented testimonials or metrics.
- **Journey:** arrive → understand problem/offer → inspect scope → evaluate conditions → request consultation → receive truthful feedback.

## Decision 1 · Put scope before persuasion density

- **Problem:** the visitor cannot tell what is actually included.
- **Principles:** cognitive load, chunking, mental models.
- **Implementation:** introduce a compact scope section with included work, boundaries and what is defined after discovery.
- **Trade-off:** slightly more content above the final CTA.
- **Verification:** ask a reviewer to explain what is included and what is not before contacting the business.

## Decision 2 · Repeat the same CTA contextually

- **Problem:** users ready after the scope section must traverse unrelated content.
- **Principles:** selective attention, serial position.
- **Implementation:** one primary action appears after the offer and again at the end; both lead to the same form.
- **Trade-off:** repetition is intentional and limited to the same action.
- **Verification:** check hierarchy on narrow/wide layouts and confirm secondary links remain distinguishable.

## Decision 3 · Design failure before celebration

- **Problem:** the happy-path success state is polished, but network failure loses confidence.
- **Principles:** peak–end, working memory, Doherty threshold.
- **Implementation:** preserve valid input, show a specific inline/global error, expose retry, and confirm success only after the request completes.
- **Verification:** simulate timeout, failure, retry and duplicate activation.
