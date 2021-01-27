with open('vocabulary.txt', 'r', encoding="utf-8") as f:
    for line in f:
        voca_list = line.strip().split(": ")

        korean_word = input(f"{voca_list[1]}: ")
        english_word = voca_list[0]

        if korean_word == english_word:
            print("맞았습니다!")
        else:
            print(f"아쉽습니다. 정답은 {english_word}입니다.")
