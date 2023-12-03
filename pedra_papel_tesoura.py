import random

user_points = 0
computer_points = 0

options = ['r', 't', 'p']

while True:
    user_choice = input('Escolha R(Pedra)/T(Tesoura)/P(Papel) ou Q para sair. ').lower()

    if user_choice == 'q':
        break

    if user_choice not in options:
        continue

    computer_choice = random.randint(0, 2)
    computer_options = options[computer_choice]

    print('O computador escolheu ' + computer_options)

    if user_choice == computer_options:
        print('Empate!')
    elif user_choice == 'r' and computer_options == 't':
        print('Você ganhou!')
        user_points = user_points + 1
    elif user_choice == 't' and computer_options == 'p':
        print('Você ganhou!')
        user_points = user_points + 1
    elif user_choice == 'p' and computer_options == 'r':
        print('Você ganhou!')
        user_points = user_points + 1

    else:
        print('Você perdeu!')
        computer_points = computer_points + 1

print('/---------------------------------/')
print('  Sua pontuação: ' + str(user_points))
print('  Pontuação do computador ' + str(computer_points))
print('/---------------------------------/')

if computer_points > user_points:
    print('/-------------/')
    print(' Você perdeu!!')
    print('/-------------/')
elif computer_points == user_points:
    print('/=======/')
    print(' Empate!')
    print('/=======/')
else:
    print('/****** Congratulation! ********')
    print('--------Você venceu!!!----------')
    print('/******************************/')
