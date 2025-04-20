def count_words(text):
    return len(text.split())

def count_chars(text):
    char_count = {}
    for c in text:
        char = c.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def sort_on(dict):
    return dict["count"]

def sorted_by_char_counts(char_counts):
    sorted_counts = []
    for k, v in char_counts.items():
        if not k.isalpha():
            continue
        sorted_counts.append({"char": k, "count": v})

    sorted_counts.sort(key=sort_on, reverse=True)
    return sorted_counts

