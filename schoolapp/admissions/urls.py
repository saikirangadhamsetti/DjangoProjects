from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required,permission_required
urlpatterns=[
    path("",views.send),
    path("kiran/",views.kiran),
    path("addadmission/",views.addadmission),
    path("delete/",views.delete),
    path("update/<int:id>",views.updatestudent),
    path("clsbsdvw/",views.classbasedview.as_view()),
    path("modellist/",views.modellist.as_view(),name="listteachers"),
    path("teacherdetail/<int:pk>",views.singledetail.as_view()),
    path("updateteacher/<int:pk>",permission_required(views.Updateteacher.as_view())),
    path("create/",login_required(views.InsertTeacher.as_view())),
    path("DeleteTeacher/<int:pk>/",views.DeleteTeacher.as_view())
]