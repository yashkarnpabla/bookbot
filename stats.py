def count_words(text):
    words = text.split()
    return f"Found {len(words)} total words"


def count_characters(text):
    characters = text.lower()
    chs = {} 
    for c in characters:
        if c in chs:
            chs[c] += 1
        else:
            chs[c] = 1

    return chs

def sort_on(d):
    return d["num"]

def character_report(char_dict):
    report = []
    for char, count in char_dict.items():
        if char.isalpha():
            report.append({"char": char, "num": count})
    report.sort(reverse=True, key=sort_on)
    return report
