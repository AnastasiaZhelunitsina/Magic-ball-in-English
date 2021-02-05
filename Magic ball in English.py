from random import choice
answers = ["Unquestionably", "I think so", "It's not clear yet, try again", "Don't even think about it",
           "It's a foregone conclusion", "Most probably", "Ask me later", "My answer is no",
           "No doubt about it", "Good prospects", "It's better not to tell", "According to my data, no",
           "You can be sure of that", "Yes", "Concentrate and ask again", "Very doubtful"]
print('I\'m a magic ball, and I know the answer to every question you have.')
print()
name = input('Please enter your name: ')
print(f'Hello, {name}! Welcome!')
print(f'{name}, if you want to ask me a question - enter "Yes", if you want to exit, enter - " Exit"')
decision = input().lower()
if decision == 'y' or decision == 'yes' or decision == 'yep' or decision == 'yse' or decision == 'ype':
    print('Wonderful! Then let\'s get started!')
elif decision == 'no' or decision == 'on' or decision == 'n' or decision == 'ex' or decision == 'e' or decision == 'exit' or decision == 'exti':
    print('I was glad to see you! When you have any questions be sure to return!')
    exit()
question = input('Please enter your question:')
print()
print(choice(answers))
while True:
    print()
    again = input('Would you like to ask another question? If you want to continue, enter - "Yes", if you want to exit, enter - "Exit"').lower()
    if again == 'y' or again == 'yes' or again == 'yep' or again == 'yse' or again == 'ype':
        print('Great!')
        question = input('Please enter your question: ')
        print()
        print(choice(answers))
        print()
    elif again == 'no' or again == 'on' or again == 'n' or again == 'ex' or again == 'e' or again == 'exit' or again == 'exti':
        print('Come back if you have any questions!')
        break