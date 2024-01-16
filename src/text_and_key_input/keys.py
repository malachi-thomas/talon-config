from talon import Context, Module
mod, ctx = Module(), Context()
mod.list("alphabet")
mod.list("number_keys")
mod.list("unshifted_symbols")
mod.list("shifted_symbols")
mod.list("custom_symbols")
mod.list("movement_keys")
mod.list("system_keys")
mod.list("modifies")

ctx.lists["self.alphabet"] = {
  "art": "a", # art
  "bat": "b", # bat
  "cap": "c", # cap
  "drum": "d", # drum
  "exit": "e", # xit
  "fake": "f", # fAk
  "gust": "g", # gust
  "hop": "h", # hop
  "sit": "i", # sit
  "jack": "j", # jak
  "kit": "k", # kit
  "lick": "l", # lik
  "might": "m", # mIt
  "nag": "n", # nag
  "owl": "o", # oul
  "pit": "p", # pit
  "quiz": "q", #qiz
  "rex": "r", # rex
  "slam": "s", # slam
  "tux": "t", # tux
  "hugo": "u", # gUgo
  "vex": "v", # vex
  "wet": "w", # wet
  "plex": "x", # plex
  "yank": "y", # yank
  "zip": "z",  # zip


}

ctx.lists["self.number_keys"] = {
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
  "less than": "<",
  "greater than": ">",
  "minus": " -",
}
ctx.lists["self.custom_symbols"] = {
  "not equal": " !=",
  "arrow": " ->",
  "fat arrow": " =>",
}

ctx.lists["self.movement_keys"] = {
  "up": "up",
  "down": "down",
  "left": "left",
  "right": "right",
  "home": "home",
  "end": "end",
  "upper": "pageup",
  "downer": "pagedown",
}

ctx.lists["self.system_keys"] = {
  "space": "space",
  "enter": "enter",
  "delete": "backspace",
  "escape": "escape",
  "tab": "tab",
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
  "court": "cmd",

  "cost": "ctrl",
  "shift": "shift",
  "meta": "alt",
  "cord": "cmd-shift",
  "trim": "ctrl-shift",
}

@mod.capture(rule="{self.alphabet}+")
def alphabet(m) -> str: return str(m).replace(" ", "")

@mod.capture(rule="{self.number_keys}")
def number_key(m) -> str: return str(m)

@mod.capture(rule="{self.shifted_symbols}")
def shifted_symbols(m) -> str: return str(m)

@mod.capture(rule="{self.unshifted_symbols}")
def unshifted_symbols(m) -> str: return str(m)

@mod.capture(rule="{self.unshifted_symbol_keys} {self.shifted_symbols}")
def symbol_keys(m) -> str: return str(m)

@mod.capture(rule="{self.unshifted_symbol_keys} | {self.shifted_symbols} | {self.custom_symbols}")
def all_symbols(m) -> str: return str(m)

@mod.capture(rule="{self.movement_keys}")
def movement_keys(m) -> str: return m.movement_keys

@mod.capture(rule="{self.system_keys}")
def system_keys(m) -> str: return m.system_keys

@mod.capture(rule="{self.system_keys} | {self.movement_keys}")
def all_system_keys(m) -> str: return m.system_keys

@mod.capture(rule="{self.modifies}+")
def modifies(m) -> str: return str(m).replace(" ", "-")

@mod.capture(rule="{self.alphabet} | {self.number_keys} | {self.unshifted_symbols} | {self.system_keys} | {self.movement_keys}")
def all_unshifted_keys(m) -> str: return str(m)

# For CursorLess
@mod.capture(rule="{self.alphabet} | {self.unshifted_symbols} | {self.shifted_symbols} | {self.number_keys}")
def any_alphanumeric_key(m) -> str: return str(m)



