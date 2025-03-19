def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered.isalpha():
            chars[lowered] = chars.get(lowered, 0) + 1
    return chars

def sort_on(chars_dict):
	sorted_chars = list(chars_dict.items())
	sorted_chars.sort(key=lambda x: x[1], reverse=True)
	return sorted_chars
