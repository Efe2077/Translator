from googletrans import Translator
from get_words import kit

translator = Translator(service_urls=['translate.google.com', 'translate.google.co.kr'])
for word in kit:
    print(f'Как переводится "{word}"')
    if word[-1] == '?':
        word = word[0:-1]
    ans = translator.translate(word, src='de', dest='ru').text

    user_ans = input().capitalize()
    if user_ans[-1] == '?':
        user_ans = user_ans[0:-1]
        print(user_ans)
    words_in_answer = ans.split()
    split_user = user_ans.split()
    count = 0
    for pos in range(0, len(split_user)):
        if split_user[pos] in words_in_answer:
            count += 1

    if user_ans != ans and count != len(split_user):
        print(f'Неправильно, "{word}" - это "{ans}"')
    else:
        print('Richtig')


# Привет
# Яблоко
# Банан
# Лампа
