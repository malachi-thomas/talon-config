from talon import Context, Module
mod, ctx = Module(), Context()
mod.list("tmux_shortcuts")

ctx.lists["self.tmux_shortcuts"] = {
  "window reload": "ctrl-r",
  "new window": "ctrl-n",
  "next window": "ctrl-b",
  "close window": "ctrl-w",
  "split up": "alt-up",
  "split down": "alt-down",
  "split left": "alt-left",
  "split right": "alt-right",
}

@mod.capture(rule="{self.tmux_shortcuts}")
def tmux_shortcuts(m) -> str:
  return str(m.tmux_shortcuts)
