"""nr01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include
import nrapp01.views

urlpatterns = [
    #산하
    path('admin/', admin.site.urls),
    path('main/', nrapp01.views.main, name='main'),
    path('', nrapp01.views.preindex, name='preindex'),

    #성준재
    
    #예약하기 버튼이 있는 메인페이지
    path('cal/', nrapp01.views.board, name='cal'), 
    #예약하기 버튼을 누르면 넘어가는 예약페이지
    path('create/', nrapp01.views.create, name='create'),
    #예약내용을 등록하기 위해 views.register로 넘어감
    path('create/register/', nrapp01.views.register, name='register'),
    path('cal/read/', nrapp01.views.read, name="read"),
    path('<int:board_m_d>/', nrapp01.views.read, name="read"),
    path('delete/<int:board_id>/', nrapp01.views.delete, name="delete"),
    path('update/<int:board_id>/', nrapp01.views.update, name="update"),
    path('update/<int:board_id>/register/', nrapp01.views.update_board, name="update_board"),
    


    #재이
    path('post_index', nrapp01.views.post_index, name='post_index'),
    path('post_create', nrapp01.views.post_create, name='post_create'),
    path('post_new', nrapp01.views.post_new, name='post_new'),
    path('post_detail/<int:qa_id>', nrapp01.views.post_detail, name='post_detail'),
    path('post_update/<int:qa_id>', nrapp01.views.post_update, name='post_update'),
    path('post_updat/<int:qa_id>', nrapp01.views.post_updat, name='post_updat'),
    path('post_delete/<int:qa_id>', nrapp01.views.post_delete, name='post_delete'),
    path('ccreate', nrapp01.views.ccreate, name='ccreate'),
    path('cdelete/<int:comment_id>', nrapp01.views.cdelete, name='cdelete'),
    
]
