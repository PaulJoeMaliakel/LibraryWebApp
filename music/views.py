from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.forms.models import model_to_dict
from .models import Post, Book


def createpost(request):
	if request.method == 'POST':
		print request.POST
		post=Post()
		post.author= request.POST.get('author')
		post.age= request.POST.get('age')
		post.gender= request.POST.get('gender')
		post.Born_in= request.POST.get('Born_in')
		post.abt_author= request.POST.get('abt_author')
		post.save()
	authors = Post.objects.values()
	print authors
	return render(request,'index4.html', {'authors': authors})


def createbooks(request):
	if request.method == 'POST':
		print request.POST
		book=Book()
		book.Book_name= request.POST.get('bname')
		book.author= Post.objects.get(author = request.POST.get('aname'))
		book.isbn= request.POST.get('ino')
		book.desp= request.POST.get('dname')

		book.save()
	books = Book.objects.values()
	return render(request,'index.html', {'books': books})

def bookview(request, bookname):
	book = get_object_or_404(Book, Book_name = bookname)
	author = book.author.author
	print model_to_dict(book)
	return render(request,'index2.html', {'book': model_to_dict(book), 'author': author})


def booklist(request, authorname):
  authorObject = get_object_or_404(Post, author = authorname)
  book1 = Book.objects.filter(author = authorObject).values
  return render(request,'index3.html', {'books':book1,'author':authorObject})


