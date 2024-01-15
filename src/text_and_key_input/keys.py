from talon import Context, Module
mod, ctx = Module(), Context()
mod.list("alphabet")
mod.list("number_key")
mod.list("unshifted_symbols")
mod.list("shifted_symbols")
mod.list("custom_symbols")
mod.list("system_keys")
mod.list("modifies")

ctx.lists["self.alphabet"] = {
  "air": "a",
  "bat": "b",
  "cap": "c",
  "drum": "d",
  "each": "e",
  "fake": "f",
  "gust": "g",
  "harp": "h",
  "sit": "i",
  "jack": "j",
  "crunch": "k",
  "look": "l",
  "made": "m",
  "near": "n",
  "odd": "o",
  "pit": "p",
  "quench": "q",
  "red": "r",
  "sun": "s",
  "trap": "t",
  "urge": "u",
  "vest": "v",
  "wet": "w",
  "plex": "x",
  "yank": "y",
  "zip": "z",
}

ctx.lists["self.number_key"] = {
  name: str(i) for i, name in enumerate("zero one two three four five six seven eight nine".split())
}

ctx.lists["self.unshifted_symbols"] = {
  "slash": "/",
  "tick": "`",
  "single": "'",
  "comma": ",",
  "span": ", ",
  "point": " .",
  "dot": ".",
  "semi": ";",
  "backslash": "\\",
  "dash": "-",
  "square open": "[",
  "square close": "]",
  "equal": "=",
}

ctx.lists["self.shifted_symbols"] = {
  "wave": "~",
  "quest": "?",
  "dollar": "$",
  "star": "*",
  "hash": "#",
  "percent": "%",
  "spin": "@",
  "double": '"',
  "plus": "+",
  "floor": "_",
  "stack": ":",
  "amper": "&",
  "pound sign": "£",
  "peren open": "(",
  "peren close": ")",
  "brace open": "{",
  "brace close": "}",
  "angle": "<",
  "rangle": ">",
  "minus": " -",
}

ctx.lists["self.custom_symbols"] = {
  "not equal": " !=",
  "arrow": " ->",
  "fat arrow": " =>",
}

ctx.lists["self.system_keys"] = {
  "up": "up",
  "right": "right",
  "down": "down",
  "left": "left",
  "space": "space",
  "enter": "enter",
  "delete": "backspace",
  "escape": "escape",
  "tab": "tab",
  "upper": "pageup",
  "downer": "pagedown",
  "function one": "f1",
  "function two": "f2",
  "function three": "f3",
  "function four": "f4",
  "function five": "f5",
  "function six": "f6",
  "function seven": "f7",
  "function eight": "f8",
  "function nine": "f9",
  "function ten": "f10",
  "function eleven": "f11",
  "function twelve": "f12",
}

ctx.lists["self.modifies"] = {
  "command": "cmd",
  "controll": "ctrl",
  "shift": "shift",
  "option": "alt",
  "cord": "cmd-shift",
  # "troll": "ctrl-shift",
}

@mod.capture(rule="{self.alphabet}")
def alphabet(m) -> str: return str(m).replace(" ", "")

@mod.capture(rule="{self.number_keys}")
def number_key(m) -> str: return str(m)

@mod.capture(rule="{user.shifted_symbols}")
def shifted_symbols(m) -> str: return str(m)

@mod.capture(rule="{user.unshifted_symbols}")
def unshifted_symbols(m) -> str: return str(m)

@mod.capture(rule="{user.unshifted_symbol_keys} {user.shifted_symbols}")
def symbol_keys(m) -> str: return str(m)

@mod.capture(rule="{user.unshifted_symbol_keys} | {user.shifted_symbols} | {user.custom_symbols}")
def all_symbols(m) -> str: return str(m)

@mod.capture(rule="{self.system_keys}")
def system_keys(m) -> str: return m.system_keys

@mod.capture(rule="{self.modifies}+")
def modifies(m) -> str: return str(m).replace(" ", "-")

@mod.capture(rule="{self.alphabet} | {user.number_keys} | {user.unshifted_symbols} | {user.system_keys}")
def all_unshifted_keys(m) -> str: return str(m)

# For CursorLess
@mod.capture(rule="{self.alphabet} | {self.unshifted_symbols} | {self.shifted_symbols} | {self.number_keys}")
def any_alphanumeric_key(m) -> str: return str(m)



