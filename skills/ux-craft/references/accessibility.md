# Accessibility checks

Treat accessibility as part of task correctness, not a final polish pass. This reference is implementation guidance, not a WCAG conformance certificate.

Check semantic headings and landmarks, keyboard reachability, visible focus, meaningful control names, persistent form labels, associated errors/help, sufficient contrast, non-color-only state communication, enlarged text, responsive reflow, reduced motion, and modal focus management.

Prefer native elements before ARIA. Buttons perform actions; links navigate. Do not disable zoom. Do not hide required instructions inside placeholders or hover-only tooltips. Ensure status and error messages are discoverable without repeatedly interrupting assistive technology.

For consequential flows, test keyboard-only completion, error recovery and focus restoration. Screen-reader behavior requires an actual screen reader test; resizing a browser or running an automated scanner is not equivalent.

Primary references: [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [WAI-ARIA APG](https://www.w3.org/WAI/ARIA/apg/), and [MDN prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion).
