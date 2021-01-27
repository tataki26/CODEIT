with open('vocabulary.txt', 'r', encoding="utf-8") as f:
    for line in f:
        voca_list = line.strip().split(": ")

        englsh_word = input(f"{voca_list[0]}: ")
        korean_word = voca_list[1]

        if englsh_word == korean_word:
            print("맞았습니다!")
        else:
            print(f"아쉽습니다. 정답은 {korean_word}입니다.")