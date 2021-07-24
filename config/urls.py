"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('', TemplateView.as_view(template_name='home.html'),
    #      name='home'),
    # در این قسمت ما pages app را برای این ساختیم که از ویوهای و url های که توسط جنگو ساخته شده استفاده نکنیم
    # خودمان برای هر کاری که انجام میدهیم به عنوان مثال عوض کردن پسورد: فایل html که برای آن نوشتیم در اون صفحه نشان داده شود
    path('articles/', include('articles.urls')),
    path('', include('pages.urls')),

]