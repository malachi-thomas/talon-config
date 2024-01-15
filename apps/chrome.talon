app: google chrome
-

bar:
  key("cmd-l")
  key("backspace")

bar <user.website_names>:
  key("cmd-l")
  key("backspace")
  insert(website_names)
  key("enter")

new <user.website_names>:
  key("cmd-t")
  insert(website_names)
  key("enter")

tab <number_small>: key("cmd-{number_small}")

tab new : key("cmd-t")
tab close: key("cmd-w")
show history: key(cmd-y)
open private: key(cmd-shift-n)
open bookmarks: key(alt-cmd-b)
go backwards: key(cmd-left)
go forwards: key(cmd-right)
(make | add) bookmark: key(cmd-d)
