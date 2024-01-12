from talon import Module, Context, ui

mod, ctx = Module(), Context()
mod.list("application_name")
ctx.lists["self.application_name"] = {
  "slack": "/Applications/Slack.app",
  "chrome": "/Applications/Google Chrome.app",
  "web": "/Applications/Google Chrome.app",
  "browser": "/Applications/Google Chrome.app",
  "code": "/Applications/Visual Studio Code.app",
  "safari": "/Applications/Safari.app",
  "terminal": "/Applications/iterm.app",
  "finder": "/System/Library/CoreServices/Finder.app",
  "draft": "/Applications/Drafts.app",
  "reminders": "/Applications/Reminders.app",
  "deck": "/Applications/Elgato Stream Deck.app",
}

@mod.capture(rule="{self.application_name}")
def application_name(m) -> str:
  return str(m)

@mod.action_class
class Actions:
  def focus_or_launch(s: str):
    ""
    ui.launch(path=s)

