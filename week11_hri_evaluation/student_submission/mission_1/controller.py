
"""Complete decide() using the transition requirements in the Lab 10 guide."""


def decide(state, event):
    phase = state["phase"]
    kind = event["kind"]
    target = event["target"]

    if kind == "CANCEL":
        if phase not in ("IDLE", "COMPLETE"):
            return "cancel"
        return "hold"

    if kind in ("REQUEST", "CORRECT"):
        if kind == "REQUEST" and phase in ("EXECUTING", "WAIT_READY"):
            return "hold"

        if not target:
            return "clarify"

        return "select"

    if kind == "CONFIRM" and phase == "CONFIRM":
        return "begin"

    if phase == "WAIT_READY" and kind == "READY":
        return "release"

    if kind == "TIMEOUT" and phase == "WAIT_READY":
        return "timeout"

    if kind == "TICK" and phase == "EXECUTING":
        return "advance"

    return "hold"
