from talon import Context, Module, actions
from ...comunity.format_phrase import format_phrase
mod, ctx = Module(), Context()
mod.list("text_replacements")
mod.list("phrase_punctuation")

ctx.lists["self.text_replacements"] = {
  "che": "key",
  "ki": "key",
  "nat left": "natleft",
  "fis buzz": "fizzbuzz",
  "fis": "fizz",
  "tmux": "tmux",
  "t mux": "tmux",
  "foo": "foo",
  "un": "un",
}

ctx.lists["self.phrase_punctuation"] = {
  "space": " ",
  "enter": "\n",
  "tab": "\t",
}

@mod.capture(
  rule="""(
    {self.text_replacements} |
    {user.phrase_punctuation} |
    {user.unshifted_symbols} |
    {user.shifted_symbols} |
    {user.custom_symbols} |
    short {user.abbreviations} |
    <phrase>)+""")
def text(m) -> str:
  return format_phrase(m)
