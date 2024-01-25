from django.shortcuts import render, redirect
from django.http import HttpResponsePermanentRedirect
from .models import Post
from .forms import PostForm
# Create your views here.


menu = [{"title": "Посты", "url_name": "main:post_list"},
        {"title": "Добавить пост", "url_name": "main:post_add"},
        {"title": "О сайте", "url_name": "main:about"},
        {"title": "Контакты", "url_name": "main:contacts"},
]

# главная страница сайта
def index_root(request):
    return redirect(post_list)

# главная страница приложения main
def index(request):
    return HttpResponsePermanentRedirect("/blog/posts/")

def about(request):
    title = "О сайте"
    context = {"menu": menu, "title": title}
    return render(request, 'main/about.html', context=context)

def contacts(request):
    title = "Контакты"
    context = {"menu": menu, "title": title}
    return render(request, 'main/contacts.html', context=context)

# отображение списка постов
def post_list(request):
    # получаем все объекты таблицы(модели) Post
    posts = Post.objects.all()
    # заносим их в объект контекста для передачи в шаблон
    context = {'posts': posts, 'menu': menu}
    return render(request, template_name='main/post_list.html', context=context)

def post_add(request):
    title = "Создать пост"
    if request.method == "GET":
        form = PostForm()
        context = {"title": title, "menu": menu, "form": form}
        return render(request, "main/post_add.html", context)
    
    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        
        if post_form.is_valid():
            post = Post()
            post.author = post_form.cleaned_data['author']
            post.title = post_form.cleaned_data['title']
            post.text = post_form.cleaned_data['text']
            post.image = post_form.cleaned_data['image']
            post.publish()
            
            return post_list(request)
        

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    title = "Информация о посте"
    context = {"post": post, "title": title, "menu": menu}
    return render(request, template_name="main/post_detail.html", context=context)
    