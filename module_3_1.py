calls = 0

def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    string_len = len(string)
    string_upper = string.upper()
    string_lower = string.lower()
    return string_len,string_upper,string_lower

def is_contains(string, list_to_search):
    count_calls()
    for _str_ in list_to_search :
        if string.lower() in _str_.lower() :
            return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)