from talon import Context, Module
mod, ctx = Module(), Context()
mod.list("abbreviations")
ctx.lists["self.abbreviations"] = {
  "string": "str",
  "interger": "int",
  "email": "malachithomas110@gmail.com",
  "number": "num",
  'numbers': 'nums',
}

@mod.capture(rule="{self.abbreviations}")
def abbreviations(m) -> str:
  return str(m)
