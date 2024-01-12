# from talon import Context, Module
# mod, ctx = Module(), Context()
# mod.list("modifies")

# ctx.lists["self.modifies"] = {
#   "com": "cmd",
#   "controll": "ctrl",
#   "shift": "shift",
#   "option": "alt",
#   "cord": "cmd-shift",
#   "troll": "ctrl-shift",
# }

# @mod.capture(rule="{self.modifies}+")
# def modifies(m) -> str:
#   return str(m).replace(" ", "-")
