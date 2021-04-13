from django.urls import path,include


urlpatterns=[
    path('teacher/',include('accounts.teacher.urls')),
    path('teacher/',include('accounts.user.urls')),
    path('students/',include('accounts.students.urls')),
    path('students/',include('accounts.user.urls')),
    path('institute/',include('accounts.institute.urls')),
    path('institute/',include('accounts.user.urls')),
    path('employee/',include('accounts.employee.urls')),
    path('employee/',include('accounts.user.urls')),

]