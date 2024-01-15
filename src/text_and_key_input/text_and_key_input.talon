# ===== Phrase Input =====

say <user.text>:
  user.add_phrase_to_history(text)
  "{text}"

word <word>:
  user.add_phrase_to_history(text)
  "{text}"

# ===== Key Input =====
<user.alphabet>: "{alphabet}"
<user.shifted_symbols>: "{shifted_symbols}"
<user.unshifted_symbols>: "{unshifted_symbols}"
<user.system_keys>: key(system_keys)
<user.file_extentions>: "{file_extentions}"
short <user.abbreviations>: "{abbreviations}"


go up: key(up)
go down: key(down)
go left: key(left)
go right: key(right)

# ===== Modifires =====

<user.modifies> <user.all_unshifted_keys>: key("{modifies}-{all_unshifted_keys}")

# ===== Text Manipulation =====

go back: user.clear_last_phrase()
go select: select_last_phrase()
go before: before_last_phrase()

