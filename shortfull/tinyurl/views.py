from django.shortcuts import render
from .forms import  Loginform
from django.contrib.auth import authenticate, login


def pagelogin(request):
    uservalue = ''
    passwordvalue = ''

    form = Loginform(request.POST or None)
    if form.is_valid():
        uservalue = form.cleaned_data.get("username")
        passwordvalue = form.cleaned_data.get("password")

        user = authenticate(username=uservalue, password=passwordvalue)
        if user is not None:  #  Удачная авторизация
            login(request, user)
            context = {'form': form,
                       'error': 'Приветствуем вас на нашей странице ! '}

            return render(request, 'tinyurl/login2.html', context)
        else:  #   Неудачная авторизация
            context = {'form': form,
                       'error': 'Ошибочка в имени или пароле !'}

            return render(request, 'tinyurl/login1.html', context)

    else:
        context = {'form': form}   #  Страница авторизации
        return render(request, 'tinyurl/login.html', context)