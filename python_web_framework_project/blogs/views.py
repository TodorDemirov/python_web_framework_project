from django.views import generic as views

from python_web_framework_project.blogs.models import Blog


class BlogListView(views.ListView):
    template_name = 'blogs/list.html'
    model = Blog


class BlogDetailsView(views.DetailView):
    template_name = 'blogs/details.html'
    model = Blog


class CreateBlogView(views.CreateView):
    model = Blog
    template_name = 'blogs/create.html'
    fields = ('name', 'description')
