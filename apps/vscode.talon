app: code
-

# user.vscode("")

# Cursor`
cursor next: key(ctrl-n)
cursor last: key(ctrl-p)
cursor up: user.vscode("editor.action.insertCursorAbove")
cursor down: user.vscode("editor.action.insertCursorBelow")

# Terminal
terminal: key(ctrl-t)

# Sidbar
bar files: key(shift-ctrl-f)
bar close: key(shift-ctrl-c)
bar plug: key(shift-ctrl-x)
bar search: key(shift-ctrl-s)
save file: key(cmd-s)
undo that: key(cmd-z)

# Window
window reload: user.vscode("workbench.action.reloadWindow")
split right: user.vscode("workbench.action.splitEditor`")
split down: user.vscode("workbench.action.splitEditorDown")
split left: user.vscode("workbench.action.splitEditorLeft")
split right: user.vscode("workbench.action.splitEditorUp")

line up: user.vscode("editor.action.moveLinesUpAction")
line down: user.vscode("editor.action.moveLinesDownAction")
replace: user.vscode("editor.action.startFindReplaceAction")

# Open Settings
open (setting | settings): user.vscode("workbench.action.openGlobalSettings")
open (setting | settings) json: user.vscode("workbench.action.openSettingsJson")
open (setting | settings) keyboard: user.vscode("workbench.action.openGlobalKeybindings")
open (setting | settings) keyboard json: user.vscode("workbench.action.openGlobalKeybindingsFile")
show snippets: user.vscode("workbench.action.openSnippets")

# Extras
comment this: user.vscode("editor.action.commentLine")
definition: user.vscode("editor.action.revealDefinition")
show files: user.vscode("workbench.action.quickOpen")
show command: user.vscode("workbench.action.showCommands")
open recent: user.vscode("workbench.action.openRecent")

# manipulation
select line:
  key(end)
  key(shift-home)