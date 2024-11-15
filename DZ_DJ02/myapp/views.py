from django.shortcuts import render

# Главная страница
def home(request):
    # Отображает главную страницу
    return render(request, 'myapp/home.html')

# Страница "О нас"
def about(request):
    # Отображает страницу с информацией о компании и командой
    return render(request, 'myapp/about.html')

# Страница "Наши услуги"
def services(request):
    # Отображает страницу с перечнем предоставляемых услуг
    return render(request, 'myapp/services.html')

# Страница "Контакты"
def contact(request):
    # Отображает страницу с контактной информацией
    return render(request, 'myapp/contact.html')
