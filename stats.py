def get_number_wordcount(contents):
    words = contents.split()
    return len(words)

def get_character_count(contents):
    words = contents.split()
    count = {}
    
    for word in words:
        word = word.lower()
        for character in word:
            if character in count:
                count[character] += 1
            else:
                count[character] = 1

    return count

def sort_on(items):
    return items["num"]