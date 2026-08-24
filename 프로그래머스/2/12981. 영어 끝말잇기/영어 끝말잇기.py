def solution(n, words):
    passlist = [words[0]]

    for i in range(1, len(words)):
        word = words[i]
        pre = words[i - 1]

        if word in passlist:
            return [i % n + 1, i // n + 1]
        elif pre[-1] != word[0]:
            return [i % n + 1, i // n + 1]

        passlist.append(word)

    return [0, 0]