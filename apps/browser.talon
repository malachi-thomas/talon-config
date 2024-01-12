app: safari
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

# tab <number_small>: key("cmd-{number_small}")

# tab new : key("cmd-t")
# tab close: key("cmd-w")
# history: key(cmd-y)
# private: key(cmd-shift-n)
# go back: key(cmd-left)
# go next: key(cmd-right)
# make bookmark: key(cmd-d)
