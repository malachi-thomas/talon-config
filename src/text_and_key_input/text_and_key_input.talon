# ===== Phrase Input =====

say <user.text>:
  user.add_phrase_to_history(text)
  "{text}"

word <word>:
  user.add_phrase_to_history(text)
  "{text}"

# ===== Key Input =====
<user.alphabet>: "{alphabet}"
<user.symbol_keys>: "{symbol_keys`}"
<user.system_keys>: key(system_keys)
<user.file_extentions>: "{file_extentions}"
short <user.abbreviations>: "{abbreviations}"

# ===== Modifires =====

<user.modifies> <user.all_unshifted_keys>: key("{modifies}-{all_unshifted_keys}")

# ===== Text Manipulation =====

go back: user.clear_last_phrase()
go select: select_last_phrase()
go before: before_last_phrase()

