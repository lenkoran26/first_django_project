from django.shortcuts import render
from .models import Post
# Create your views here.


menu = [{"title": "Посты", "url_name": "main:post_list"},
        # {"title": "Добавить пост", "url_name": "main:post_add"},
        # {"title": "О сайте", "url_name": "main:about"},
        # {"title": "Контакты", "url_name": "main:contacts"},
]

def index_root(request):
    return render(request, 'main/index.html')

def index(request):
    return render(request, 'main/index.html')

def about_site(request):
    pass

# отображение списка постов
def post_list(request):
    # получаем все объекты таблицы(модели) Post
    posts = Post.objects.all()
    # заносим их в объект контекста для передачи в шаблон
    context = {'posts': posts, 'menu': menu}
    return render(request, template_name='main/post_list.html', context=context)