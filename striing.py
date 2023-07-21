import re

old_string = 'h?ello, my name is nik! how are you?'
new_string = re.sub('[!?]', '', old_string)

print(new_string)
# Returns: hello, my name is nik how are you