import sys
import random
# че так больно...
questions = ["cat", "hamster", "otter", "way"] # здесь вопросы лежат
answers = ["кот", "хомяк", "выдра", "путь"] # здесь ответы
size = len(questions)
print("хаюшки, это викторина на знание английского!")
while True:
    print("вы хотите начать игру - введите 1; вам нужна помощь с игрой - введите 2; хотите выйти - QUIT")
    nom = input("> ")
    nom = nom.lower()
    if nom == '1':
        pos_mask = [False for i in range(size)]  # тут будем помечать вопросы, на которые ответили, убого, зато без словарей
        count_correct = 0 # тут считаем правильные
        print("начинаем!")
        steps = 0
        while count_correct != size and steps != 10:
            num = random.randint(1, size - count_correct) # сначала выбираем из 4 вопросов, потом из 3 и тд...
            pos = 0
            count = 0
            for j in range(size):
                if not pos_mask[j]:
                    count += 1
                if count == num:
                    pos = j
                    break
            print("введите перевод данного слова: " + questions[j])
            answer = input("> ")
            if answer == answers[j]:
                print("верно")
                count_correct += 1
                pos_mask[pos] = True
            else:
                print("неверно")
            steps += 1
        print("вы угадали {} из {} слов".format(count_correct, size))
        print("хорошего дня!")
        break
    elif nom == '2':
        print("Зачем вам помощь?")
    elif nom == 'quit':
        break
    else:
        print("И че ты ввел????")

