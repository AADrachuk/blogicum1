"""Функции-обработчики для приложения pages."""
from django.shortcuts import render  # type: ignore


def about(request):
    """Функция-обработчик для страницы about."""
    template = 'pages/about.html'
    return render(request, template)


def rules(request):
    """Функция-обработчик для страницы rules."""
    template = 'pages/rules.html'
    return render(request, template)
