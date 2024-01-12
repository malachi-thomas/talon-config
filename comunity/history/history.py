from talon import Module, actions

mod = Module()

# list of recent phrases, most recent first
phrase_history = []
phrase_history_length = 40
phrase_history_display_length = 40


@mod.action_class
class Actions:
    def get_last_phrase() -> str:
        """Gets the last phrase"""
        return phrase_history[0] if phrase_history else ""

    def get_recent_phrase(number: int) -> str:
        """Gets the nth most recent phrase"""
        try:
            return phrase_history[number - 1]
        except IndexError:
            return ""

    def clear_last_phrase():
        ""
        if not phrase_history:
            return
        for _ in phrase_history.pop(0):
            actions.key("backspace")

    def select_last_phrase():
        ""
        if not phrase_history:
            return
        for _ in phrase_history[0]:
            actions.edit.extend_left()

    def before_last_phrase():
        """Moves left before the last phrase"""
        try:
            for _ in phrase_history.pop(0):
                actions.edit.left()
        except IndexError:
            return

    def add_phrase_to_history(text: str):
        """Adds a phrase to the phrase history"""
        global phrase_history
        phrase_history.insert(0, text)
        phrase_history = phrase_history[:phrase_history_length]


