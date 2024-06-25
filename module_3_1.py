calls = 0
def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return f'({len(string)}, {string.lower()}, {string.upper()})'


def is_contains(string, list_to_search):
    count_calls()
    lower_list = [item.lower() for item in list_to_search]
    return string.lower() in lower_list


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)
