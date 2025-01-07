from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

images = [
    {
        "src": "https://radiovan.fm/uploads/article/10935f58387584b1a_5f58387581610.jpg",
        "title": "Статуя \"Давид\"",
        "text": "Створена між 1501 і 1504 роками, статуя є символом мужності та краси."
    },
    {
        "src": "https://uploads4.wikiart.org/00255/images/michelangelo/michelangelo-creation-of-adam-cropped.jpg!Large.jpg",
        "title": "\"Сотворення Адама\"",
        "text": "Фреска на стелі Сикстинської капели, яка стала символом божественного творення."
    },
    {
        "src": "https://upload.wikimedia.org/wikipedia/commons/4/4d/Michelangelo%27s_Pieta_5450_cut_out.png",
        "title": "\"П'єта\"",
        "text": "Емоційна скульптура, що зображує Марію, яка тримає тіло Христа."
    },
    {
        "src": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/%27Moses%27_by_Michelangelo_JBU160.jpg/1200px-%27Moses%27_by_Michelangelo_JBU160.jpg",
        "title": "Статуя \"Мойсей\"",
        "text": "Скульптура, створена для гробниці папи Юлія II, показує силу та мудрість."
    },
    {
        "src": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Michelangelo_-_Cristo_Juiz.jpg/300px-Michelangelo_-_Cristo_Juiz.jpg",
        "title": "\"Страшний суд\"",
        "text": "Монументальне зображення кінця світу на вівтарній стіні Сикстинської капели."
    },
    {
        "src": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/LibyanSibyl_SistineChapel.jpg/640px-LibyanSibyl_SistineChapel.jpg",
        "title": "\"Лівійська сивіла\"",
        "text": "Одна з пророчиць, зображених на стелі Сикстинської капели."
    }
]


# def index(request):
#     return HttpResponse("hello, world!")

def index(request):
    return render(request,"index.html")

def art(request):
    return render(request,"art.html",{"images":images})
