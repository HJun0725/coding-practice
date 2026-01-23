def solution(my_string):
    vowels = ["a", "e", "i", "o", "u"]
    return ''.join([i for i in my_string if i not in vowels])

'''
def solution(my_string):
    vowels = ["a", "e", "i", "o", "u"]
    return my_string.replace("a", '') ~ .replace("u", '')
'''