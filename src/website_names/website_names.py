from talon import Context, Module

mod, ctx = Module(), Context()
mod.list("website_names")

ctx.lists["user.website_names"] = {
  "google": "google.com",
  "talon": "docs,talon.wiki/unofficial_talon_docs",
  "youtube": "youtube.com",
  "github": "github.com",
  "rust crates": "crates.io",
  "cursor": "cursorless.org/docs/"
}

@mod.capture(rule="{self.website_names}")
def website_names(m) -> str:
  return str(m)



