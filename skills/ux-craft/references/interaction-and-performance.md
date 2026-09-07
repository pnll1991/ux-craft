# Interaction and performance

Responsive UX means preserving task meaning across widths, input methods and system conditions.

Test a narrow phone, a wider phone/tablet, and a desktop layout. Useful fixtures are roughly 320, 390, 768 and 1440 CSS pixels; these are test widths, not mandatory production breakpoints. Preserve reading order and avoid visual reordering that contradicts document order.

Every interactive component should account for relevant states: default, hover, focus-visible, active, selected, disabled, loading, empty, success and error. Do not show success before the system confirms the operation. Preserve valid input after recoverable errors and prevent duplicate consequential actions while a real request is pending.

Performance feedback must be truthful. Acknowledge actions promptly, avoid layout jumps where practical, support retry/cancel when meaningful, and measure actual responsiveness separately from visual feedback. Historical UX heuristics are not substitutes for field performance metrics such as Core Web Vitals.

Respect `prefers-reduced-motion`, avoid motion as the only state signal, and keep essential content usable without animation.
