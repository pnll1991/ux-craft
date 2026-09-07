# UX Craft principle library

These 30 principles are decision prompts, not universal laws. Use only the principles that explain an observed problem, then connect **problem → implementation → trade-off → verification**. Source inspiration: [Laws of UX](https://lawsofux.com/es/), reviewed 2026-09-06.

| Principle | Apply | Avoid | Verify |
| --- | --- | --- | --- |
| Selective attention | Keep critical information near the current task | Banner-like noise and animation-only signals | Run the task without hints and record missed information |
| Cognitive load | Remove duplicate decisions and internal jargon | Deleting necessary context merely to look minimal | Compare errors and clarification needs |
| Aesthetic–usability effect | Use coherent typography, spacing and states | Treating visual praise as usability evidence | Test task completion separately from visual preference |
| Serial position effect | Put the proposition early and the next step clearly | Hiding important conditions in the middle | Ask users to restate offer, conditions and next action |
| Goal-gradient effect | Show truthful completed and remaining work | Fake progress or moving the finish line | Compare displayed progress with actual required steps |
| Von Restorff effect | Make the primary action meaningfully distinctive | Making every element visually special | Check hierarchy in grayscale and reduced motion |
| Zeigarnik effect | Support save, resume and deliberate abandonment | Manufactured unfinished tasks or guilt loops | Interrupt and resume a real draft |
| Flow | Support focused first-use and repeat-use paths | Equating long sessions with success | Count unnecessary interruptions and repeated actions |
| Chunking | Group information by meaning | Arbitrary cards or steps | Check whether users can locate an item in the expected group |
| Working memory | Keep comparison information visible | Requiring users to remember identifiers across screens | Complete the task without external notes |
| Occam’s razor | Prefer the simplest complete interaction | Removing labels, context or recovery in the name of minimalism | Compare each extra mechanism with a simpler complete alternative |
| Uniform connectedness | Use connectors for real relationships and sequences | Decorative arrows implying false process | Ensure order remains understandable without the connector |
| Fitts’s law | Give controls adequate hit areas and spacing | Confusing icon size with target size | Test adjacent controls on narrow touch layouts |
| Hick–Hyman law | Organize decisions by relevant differences | Hiding legitimate options only to reduce count | Test whether people can choose an appropriate option |
| Jakob’s law | Preserve familiar conventions unless novelty has a task benefit | Blindly copying competitors | Observe a first-use task without onboarding |
| Similarity | Give equivalent actions equivalent visual treatment | Making static content look interactive | Audit repeated components for semantic consistency |
| Miller’s law | Chunk and label information for recognition | Treating seven as a universal menu limit | Test findability rather than item count |
| Parkinson’s law | Remove avoidable repetition and approvals | Artificial countdowns or weakened safeguards | Count necessary versus avoidable steps |
| Postel’s law | Accept harmless input variation when meaning is clear | Relaxing permissions or integrity validation | Try localized, malformed and ambiguous values |
| Proximity | Keep labels, help and errors near their controls | Relying on whitespace as the only semantic relationship | Check mobile and enlarged-text association |
| Prägnanz | Make groups and layers visually unambiguous | Simplifying into unlabeled icon-only ambiguity | Inspect at small sizes and low visual detail |
| Common region | Use containers for meaningful units | Wrapping everything in nested cards | Explain what each container represents |
| Tesler’s law | Let the system handle repetition while exposing important assumptions | Pretending unavoidable domain complexity disappeared | List who handles each remaining domain decision |
| Mental models | Use the audience’s language for navigation and states | Exposing implementation or database terminology | Ask users to predict an action before triggering it |
| Paradox of the active user | Make the first task usable without a mandatory tour | Putting essential information only in onboarding | Skip onboarding and attempt the core task |
| Pareto principle | Prioritize using observed severity, reach and frequency | Inventing an 80/20 split | Revisit priorities with actual evidence |
| Peak–end rule | Design irreversible moments and completion states carefully | Polishing the ending while ignoring earlier blockers | Test recovery and ask what users believe happened |
| Cognitive bias | Separate observation from interpretation | Cherry-picking feedback or manipulating consent | State a competing explanation and seek disconfirming evidence |
| Choice overload | Expose differentiators and useful comparison tools | Assuming fewer choices always improve decisions | Evaluate suitability and understanding, not speed alone |
| Doherty threshold | Acknowledge actions promptly and support retry/cancel | Fake progress or deliberate delay | Test throttling, timeouts and failure states |

## How to use this library

Start from the user task and an observed issue. Choose approximately 1–5 relevant principles depending on scope. Never justify a design with a principle name alone. Record the concrete change, what it costs, and how you will know whether it helped.
