def erasing(word):
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            new_word = word[:i] + word[i+2:]
            return erasing(new_word)
    return len(word)


T = int(input())
for tc in range(T):
    word = input()

    print(f'#{tc+1} {erasing(word)}')