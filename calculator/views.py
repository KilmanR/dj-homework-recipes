from django.shortcuts import render


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def recipe_view(request, recipe):
    serving = int(request.GET.get('servings', 1))
    data = DATA.get(recipe)
    if data is None:
        recipe_context = {}
    else:
        recipe_context = {}
        for ingredient, amount in data.items():
            recipe_context[ingredient] = amount * serving
    context = {'recipe': recipe_context}
    return render(request, 'calculator/index.html', context)

def home(request):
    context = {'recipes': DATA.keys()}
    return render(request, 'calculator/home.html', context)
# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
