app: code
-

# user.vscode("")

# Cursor`
cursor next:                user.vscode("editor.action.addSelectionToNextFindMatch")
cursor last:                user.vscode("editor.action.addSelectionToPreviousFindMatch")
cursor up:                  user.vscode("editor.action.insertCursorAbove")
cursor down:                user.vscode("editor.action.insertCursorBelow")

# Terminalfkeyboard
terminal:                   user.vscode("workbench.action.terminal.toggleTerminal")
terminal new:               user.vscode("workbench.action.terminal.new")
terminal next:              user.vscode("workbench.action.terminal.focusNext")
terminal last:              user.vscode("workbench.action.terminal.focusPrevious")

# Sidbar
bar close:                  user.vscode("workbench.action.closeSidebar")
bar files:                  user.vscode("workbench.view.explorer")
bar (plug | plugins):       user.vscode("workbench.view.extensions")
bar search:                 user.vscode("workbench.view.search")
bar replace:                user.vscode("workbench.action.replaceInFiles")
bar files:                  user.vscode("workbench.view.explorer")

new file:                   user.vscode("explorer.newFile")
delete file:                user.vscode("deleteFile")
new directory:              user.vscode("explorer.newFolder")
rename file:                user.vscode("renameFile")

# Window
window reload:              user.vscode("workbench.action.reloadWindow")
split right:                user.vscode("workbench.action.splitEditor`")
split down:                 user.vscode("workbench.action.splitEditorDown")
split left:                 user.vscode("workbench.action.splitEditorLeft")
split right:                user.vscode("workbench.action.splitEditorUp")

line up:                    user.vscode("editor.action.moveLinesUpAction")
line down:                  user.vscode("editor.action.moveLinesDownAction")
replace:                    user.vscode("editor.action.startFindReplaceAction")

# Open Settings
open (setting | settings):  user.vscode("workbench.action.openGlobalSettings")
open (setting | settings) json: user.vscode("workbench.action.openSettingsJson")
open (setting | settings) keyboard: user.vscode("workbench.action.openGlobalKeybindings")
open (setting | settings) keyboard json: user.vscode("workbench.action.openGlobalKeybindingsFile")
show snippets:              user.vscode("workbench.action.openSnippets")

# Extras
comment this:               user.vscode("editor.action.commentLine")
definition:                 user.vscode("editor.action.revealDefinition")
show files:                 user.vscode("workbench.action.quickOpen")
show command:               user.vscode("workbench.action.showCommands")
open recent:                user.vscode("workbench.action.openRecent")
