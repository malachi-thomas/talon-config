from talon import Module, actions

mod = Module()

@mod.capture(rule='<user.text>')
def all_caps(m) -> str:
  result = str(m).upper()
  actions.user.add_phrase_to_history(result)
  return result

@mod.capture(rule='<user.text>')
def dot_case(m) -> str:
  result = str(m).replace(' ', '.')
  actions.user.add_phrase_to_history(result)
  return result

@mod.capture(rule='<user.text>')
def kebab_case(m) -> str:
  result = str(m).replace(' ', '-')
  actions.user.add_phrase_to_history(result)
  return result

@mod.capture(rule='<user.text>')
def path_case(m) -> str:
  result = str(m).replace(' ', '/')
  actions.user.add_phrase_to_history(result)
  return result

@mod.capture(rule='<user.text>')
def smash_case(m) -> str:
  result = str(m).replace(' ', '')
  actions.user.add_phrase_to_history(result)
  return result

@mod.capture(rule='<user.text>')
def sentence_case(m) -> str:
  result = str(m).capitalize()
  actions.user.add_phrase_to_history(result)
  return result

@mod.capture(rule='<user.text>')
def snake_case(m) -> str:
  result = str(m).replace(' ', '_')
  actions.user.add_phrase_to_history(result)
  return result

@mod.capture(rule='<user.text>')
def camel_case(m) -> str:
  words = str(m).split(' ')
  result = words[0]
  for word in words[1:]:
    result += word.capitalize()
  actions.user.add_phrase_to_history(result)
  return result

@mod.capture(rule='<user.text>')
def pascal_case(m) -> str:
  words = str(m).split(' ')
  capitalized_words = []
  for word in words:
    capitalized_words.append(word.capitalize())
  result = ''.join(capitalized_words)
  actions.user.add_phrase_to_history(result)
  return result

@mod.capture(rule='<user.text>')
def title_case(m) -> str:
  words = m.split(' ')
  title_words = [words[0].capitalize()]
  for word in words[1:]: title_words.append(word.capitalize())
  result = ' '.join(title_words)
  actions.user.add_phrase_to_history(result)
  return result

@mod.action_class
class Actions:
  def last_phrase_to_all_caps() -> None:
    ""
    new_phrase = actions.user.get_last_phrase().upper()
    actions.user.clear_last_phrase()
    actions.user.add_phrase_to_history(new_phrase)
    actions.insert(actions.user.get_last_phrase())

  def last_phrase_to_dot_case() -> None:
    ""
    new_phrase = actions.user.get_last_phrase().replace(' ', '.')
    actions.user.clear_last_phrase()
    actions.user.add_phrase_to_history(new_phrase)
    actions.insert(actions.user.get_last_phrase())

  def last_phrase_to_kebab_case() -> None:
    ""
    new_phrase = actions.user.get_last_phrase().replace(' ', '-')
    actions.user.clear_last_phrase()
    actions.user.add_phrase_to_history(new_phrase)
    actions.insert(actions.user.get_last_phrase())

  def last_phrase_to_path_case() -> None:
    ""
    new_phrase = actions.user.get_last_phrase().replace(' ', '/')
    actions.user.clear_last_phrase()
    actions.user.add_phrase_to_history(new_phrase)
    actions.insert(actions.user.get_last_phrase())

  def last_phrase_to_smash_case() -> None:
    ""
    new_phrase = actions.user.get_last_phrase().replace(' ', '')
    actions.user.clear_last_phrase()
    actions.user.add_phrase_to_history(new_phrase)
    actions.insert(actions.user.get_last_phrase())

  def last_phrase_to_sentence_case() -> None:
    ""
    new_phrase = actions.user.get_last_phrase().capitlise()
    actions.user.clear_last_phrase()
    actions.user.add_phrase_to_history(new_phrase)
    actions.insert(actions.user.get_last_phrase())

  def last_phrase_to_snake_case() -> None:
    ""
    new_phrase = actions.user.get_last_phrase().replace(' ', '_')
    actions.user.clear_last_phrase()
    actions.user.add_phrase_to_history(new_phrase)
    actions.insert(actions.user.get_last_phrase())

  def last_phrase_to_camel_case() -> None:
    ""
    words = actions.user.get_last_phrase().split(' ')
    new_phrase = words[0]
    for word in words[1:]: new_phrase += word.capitalize()
    actions.user.clear_last_phrase()
    actions.user.add_phrase_to_history(new_phrase)
    actions.insert(actions.user.get_last_phrase())

  def last_phrase_to_pascal_case() -> None:
    ""
    words = actions.user.get_last_phrase().split(' ')
    capitalized_words = []
    for word in words: capitalized_words.append(word.capitalize())
    new_phrase = ''.join(capitalized_words)
    actions.user.clear_last_phrase()
    actions.user.add_phrase_to_history(new_phrase)
    actions.insert(actions.user.get_last_phrase())

  def last_phrase_to_title_case() -> None:
    ""
    words = actions.user.get_last_phrase().split(' ')
    title_words = [words[0].capitalize()]
    for word in words[1:]: title_words.append(word.capitalize())
    new_phrase = ' '.join(title_words)
    actions.user.clear_last_phrase()
    actions.user.add_phrase_to_history(new_phrase)
    actions.insert(actions.user.get_last_phrase())
