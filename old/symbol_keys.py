# from talon import Context, Module

# mod, ctx = Module(), Context()

# mod.list("symbol_keys")
# mod.list("extra_symbol_keys")
# mod.list("custom_symbols")

# ctx.lists["self.symbol_keys"] = {
#   "slash": "/",
#   "tick": "`",
#   "single": "'",
#   "comma": ",",
#   "span": ", ",
#   "point": " .",
#   "dot": ".",
#   "semi": ";",
#   "backslash": "\\",
#   "dash": "-",
#   "square open": "[",
#   "square close": "]",
#   "equal": "=",
# }

# ctx.lists["self.extra_symbol_keys"] = {
#   "wave": "~",
#   "quest": "?",
#   "dollar": "$",
#   "star": "*",
#   "hash": "#",
#   "percent": "%",
#   "spin": "@",
#   "double": '"',
#   "plus": "+",
#   "floor": "_",
#   "stack": ":",
#   "amper": "&",
#   "pound sign": "£",
#   "peren open": "(",
#   "peren close": ")",
#   "brace open": "{",
#   "brace close": "}",
#   "angle": "<",
#   "rangle": ">",
#   "minus": " -",
# }
# ctx.lists["self.custom_symbols"] = {
#   "not equal": " !=",
#   "arrow": " ->",
#   "fat arrow": " =>",
# }

# @mod.capture(rule="{user.symbol_keys} | {user.extra_symbol_keys}")
# def symbol_keys(m) -> str:
#   return str(m)

# @mod.capture(rule="{user.symbol_keys}")
# def unshifted_symbol_keys(m) -> str:
#   return str(m)

# @mod.capture(rule="{user.symbol_keys}")
# def custom_symbols(m) -> str:
#   return str(m)
