from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Post





def home(request):
    context ={
        'posts': Post.objects.all()
    }
    return render(request, 'Storehuz/home.html', context)



class PostListView(ListView):
    model = Post
    template_name = 'Storehuz/home.html'
    context_object_name = 'posts'
    paginate_by = 5
    


class UserPostListView(ListView):
    model = Post
    template_name = 'Storehuz/user_post.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')



class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'body', 'header_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post =self.get_object()
        if self.request.user == post.author:
            return True
        return False    


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post   
    success_url = '/'


    def test_func(self):
        post =self.get_object()
        if self.request.user == post.author:
            return True
        return False        

    




def about(request):
    return render(request,'Storehuz/about.html', {'title': 'About'})




def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
       # subject = request.POST.get('subject')
        message = request.POST.get('message')
        send_mail('New Contact Form Submission',
                  f'Name: {name}\nEmail: {email}\n\n{message}', 'direction4rmthestorehouse@gmail.com', 
                  ['direction4rmthestorehouse@gmail.com'],
                  fail_silently=False,)
        return HttpResponse('Thanks for contacting us!')
    return render(request, 'Storehuz/contact.html')
    
    
     