def vowel_filter(function):
    def wrapper():
        char_list = function()
        vowels = 'aeiouy'

        return [el for el in char_list if el.lower() in vowels]
    return wrapper