def clean(text):
    result = []
    count = 0
    in_garbage = False
    skip_next = False
    for character in text:
        if skip_next:
            skip_next = False
            continue
        if character == "!":
            skip_next = True
            continue
        if in_garbage and character != ">":
            count += 1
            continue
        if in_garbage and character == ">":
            in_garbage = False
            continue
        if character == '<':
            in_garbage = True
            continue
        result.append(character)
    return "".join(result), count


def score(text):
    clean_text, count = clean(text)
    score = 0
    level = 0
    for character in clean_text:
        if character == "{":
            level += 1
            continue
        if character == ",":
            continue
        if character == "}":
            score += level
            level -= 1
            continue
        raise RuntimeError
    return score


if __name__ == "__main__":
    with open('input') as f:
        text = f.read()
    print(clean(text))
    print(score(text))
