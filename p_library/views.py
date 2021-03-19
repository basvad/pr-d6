from django.shortcuts import render
from p_library.models import Author, Book , Publish ,Friend
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from p_library.forms import AuthorForm,BookForm,FriendForm
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.forms import formset_factory  
from django.http.response import HttpResponseRedirect


# Create your views here.
def books_list(request):
    books = Book.objects.all()
    return HttpResponse(books)

def publish(request):
    template = loader.get_template('publish.html')
    publish = Publish.objects.all()
    data = {
        "publish": publish,
    }
    return HttpResponse(template.render(data, request))

def friend(request):
    template = loader.get_template('friend.html')
    friend = Friend.objects.all()
    data = {
        "friend": friend,
    }
    return HttpResponse(template.render(data, request))


def index(request):
    template = loader.get_template('index.html')
    #books_count = Book.objects.all().count()
    books = Book.objects.all()
    biblio_data = {"title": "мою библиотеку","books": books,}
    return HttpResponse(template.render(biblio_data, request))

def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')

class AuthorEdit(CreateView):  
    model = Author  
    form_class = AuthorForm  
    success_url = reverse_lazy('p_library:author_list')  
    template_name = 'author_edit.html'  
  
  
class AuthorList(ListView):  
    model = Author  
    template_name = 'authors_list.html'

class BookList(ListView):  
    model = Book 
    template_name = 'books_list.html'

def author_create_many(request):  
    AuthorFormSet = formset_factory(AuthorForm, extra=2)  #  Первым делом, получим класс, который будет создавать наши формы. Обратите внимание на параметр `extra`, в данном случае он равен двум, это значит, что на странице с несколькими формами изначально будет появляться 2 формы создания авторов.
    if request.method == 'POST':  #  Наш обработчик будет обрабатывать и GET и POST запросы. POST запрос будет содержать в себе уже заполненные данные формы
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='authors')  #  Здесь мы заполняем формы формсета теми данными, которые пришли в запросе. Обратите внимание на параметр `prefix`. Мы можем иметь на странице не только несколько форм, но и разных формсетов, этот параметр позволяет их отличать в запросе.
        if author_formset.is_valid():  #  Проверяем, валидны ли данные формы
            for author_form in author_formset:  
                author_form.save()  #  Сохраним каждую форму в формсете
            return HttpResponseRedirect(reverse_lazy('p_library:author_list'))  #  После чего, переадресуем браузер на список всех авторов.
    else:  #  Если обработчик получил GET запрос, значит в ответ нужно просто "нарисовать" формы.
        author_formset = AuthorFormSet(prefix='authors')  #  Инициализируем формсет и ниже передаём его в контекст шаблона.
    return render(request, 'manage_authors.html', {'author_formset': author_formset})

def books_authors_create_many(request):  
        AuthorFormSet = formset_factory(AuthorForm, extra=2)  
        BookFormSet = formset_factory(BookForm, extra=2)  
        if request.method == 'POST':  
           author_formset = AuthorFormSet(request.POST, request.FILES, prefix='authors')  
           book_formset = BookFormSet(request.POST, request.FILES, prefix='books')  
           if author_formset.is_valid() and book_formset.is_valid():  
              for author_form in author_formset:  
                author_form.save()  
              for book_form in book_formset:  
                book_form.save()  
              return HttpResponseRedirect(reverse_lazy('p_library:author_list'))  
        else:  
            author_formset = AuthorFormSet(prefix='authors')  
            book_formset = BookFormSet(prefix='books')  
        return render(
	      request,  
		  'manage_books_authors.html',  
		  {  
	        'author_formset': author_formset,  
			'book_formset': book_formset,  
		  }  
	    )

class FriendEdit(CreateView):  
    model = Friend  
    form_class = FriendForm  
    success_url = reverse_lazy('p_library:friend_list')  
    template_name = 'friend_edit.html'  
  
  
class FriendList(ListView):  
    model = Friend  
    template_name = 'friends_list.html'