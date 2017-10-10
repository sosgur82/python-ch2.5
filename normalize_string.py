import re

states = [
    'Alabama',
    ' Georgia!',
    'Georgia ',
    'georgia',
    'FlOrIda',
    'south carolina   ',
    'West virginia?']


def clean_strings(strings):
    results = []
    for string in strings:
        string = string.strip()
        string = re.sub('[!#?]', '', string)
        string = string.title()
        results.append(string)

    return results


results = clean_strings(states)
print(results)


def remove_specialchar(string):
    return re.sub('[!#?]', '', string)

def clean_strings2(strings, *funcs):
    results = []
    for string in strings:
        for func in funcs:
            string = func(string)

        results.append(string)

    return results


results = clean_strings2(states, str.strip, str.title, remove_specialchar)
print(results)
