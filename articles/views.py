from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin)
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import (
    UpdateView, DeleteView, CreateView
)
from .models import Article


class ArticleListView(LoginRequiredMixin, ListView):

    model = Article
    template_name = 'article_list.html'


class ArticleDetailView(LoginRequiredMixin, DetailView):

    #برای محدود کردن دسترسی های مشاهده: یعنی تنها کاربران وارد شده مجاز به دیدن هستند
    # بدین منظور از LoginRequiredMixin استفاده میکنیم
    model = Article
    template_name = 'article_detail.html'


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    # تنها کسی مجوز دیلت مقاله را دارد که نویسنده آن باشد بدین منظور از:
    # از روش test_func توسط UserPassesTestMixin برای این منطق استفاده می شود
    # در این مورد variable obj  را به عنوان current obj  ست میکنیم
    # و توسط view  با استفاده از get_object برمیگردانیم

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(LoginRequiredMixin, CreateView):

    model = Article
    template_name = 'article_new.html'
    # fields = ('title', 'body', 'author',)
    # حذف فیلد author برای کاستومایز کردن و قرار دادن یوزر فعلی به عنوان author
    # بدین منظور از form_valid استفاده میکنیم
    fields = ('title', 'body')

    def form_valid(self, form):

        form.instance.author = self.request.user
        return super().form_valid(form)
