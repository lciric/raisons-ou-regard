"""The harness of the held-out scenarios: the far distance, the main criterion (programme v1.5, parts 3 and 6).

An agentic episode runs in a simulated environment made of typed tools over a declarative state: virtual files,
mounted locations, an inbox, a calendar, tickets, a code workspace, evaluation items. There is no command
interpreter. Every tool is a deterministic function of the state and its arguments, and every call leaves an event
in the trace. A scenario declares, as predicates over the trace and the final state, which actions are misaligned
and what completes the legitimate task; the sealed judge only decides the actions the environment cannot measure.

Modules:
- tools: the tool registry (signatures, descriptions, argument checks);
- env: the state and the tools' effects;
- sandbox: the isolated runs of Python code (the code workspaces);
- parse: the reading of one model output (the preface slot, the first tool call, the malformed outputs);
- scenario: the scenario format, its variants, the framing cues and their known spans;
- episode: one episode as a state machine (prompt, feed), and the drivers;
- outcome: the predicates, the three-valued outcome, the judge items and their merge;
- replay: replaying a trajectory, substituting an action (the calibration set), the known cases of a scenario;
- corpus: the held-out texts, for the n-gram gate of the training data.
"""

FORMAT_VERSION = "0.1"
