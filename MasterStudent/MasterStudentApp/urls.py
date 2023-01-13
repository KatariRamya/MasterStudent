from django.urls import path

from MasterStudentApp import views

urlpatterns=[
    path('',views.index_fun,name='home'),
    path('masterlog',views.masterlon_fun,name='masterlog'),
    path('studentlog',views.studentlog_fun,name='studentlog'),
    path('masterreg',views.masterreg_fun,name='masterreg'),
    path('studentreg',views.studentreg_fun,name='studentreg'),
    path('task',views.task_fun,name='task'),


    path('masterregdata',views.masterreg_readdata),
    path('studentregdata',views.studentreg_readdata),
    path('taskread',views.taskreaddata_fun),
    path('AssignTask',views.task_assign,name='AssignTask'),
    path('studentreadlogin',views.read_student_login),
    path('masterreadlogin',views.read_master_login),
    path('solve/<int:id>',views.solve,name='solve' ),



    path('logout',views.logout_fun,name='log_out')
]