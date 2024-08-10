from django.shortcuts import render
import random

def home(request):
    choices = ['rock', 'paper', 'scissors']
    if request.method == 'POST':
        user_choice = request.POST['choice']
        computer_choice = random.choice(choices)
        if user_choice == computer_choice:
            result = 'It\'s a tie!'
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            result = 'You win!'
        else:
            result = 'You lose!'
        return render(request, 'game/result.html', {
            'user_choice': user_choice,
            'computer_choice': computer_choice,
            'result': result
        })
    return render(request, 'game/home.html')

