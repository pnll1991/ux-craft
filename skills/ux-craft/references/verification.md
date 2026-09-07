# Verification and definition of done

Use four statuses: **passed**, **failed**, **not run**, **not applicable**. Do not turn an unrun check into a pass.

## Core gates

1. **Task:** the intended user can identify and complete the primary task.
2. **Content:** important conditions are visible and proof/metrics are real or clearly illustrative.
3. **Interaction:** keyboard, focus, loading, empty, error, success and recovery work where relevant.
4. **Layout:** narrow/wide layouts and enlarged text retain functionality.
5. **Integrity:** existing integrations, validation and permissions are not weakened for convenience.
6. **Delivery:** changed files and tests actually run are reported accurately.

## Suggested scenarios

Complete the main task without a mouse. Trigger a validation error and recover. Return to an earlier step. Try empty data, network failure and permission-limited states when applicable. Verify reduced motion does not hide content. Check long labels and localized dates/numbers. Confirm repeated activation cannot duplicate a consequential action.

## Audit finding format

`Priority · component/file · observed evidence · affected task · principle · proposed fix · acceptance check · confidence`

Use severity labels as editorial prioritization, not a universal UX score. Keep effort separate from severity.
