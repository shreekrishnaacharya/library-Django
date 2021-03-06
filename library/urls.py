from django.urls import path,re_path
from . import views

urlpatterns = [
    path("home", views.index, name="index"),
    path("book_list", views.book_list, name="book_list"),
    path("", views.book_list, name="book_list"),
    path("books_view/", views.home_books_view, name="books_view"),
    path("upload_book/", views.upload_book, name="upload_book"),
    path("add_book/", views.add_book, name="add_book"),
    
    re_path(r'^getbooks/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', views.getbooks,name='getbooks'),
    path("view_students/", views.view_students, name="view_students"),
    path("issue_book/", views.issue_book, name="issue_book"),
    path("view_issued_book/", views.view_issued_book, name="view_issued_book"),
    path("search_book_issue/", views.search_book_issue, name="search_book_issue"),
    path("search_student_issue/", views.search_student_issue, name="search_student_issue"),
    path("recommended/", views.recommended, name="recommended"),
    path("student_books_list/", views.student_books_list, name="student_books_list"),
    path("student_books_view/", views.student_books_view, name="student_books_view"),
    re_path(r'^student_books_search/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', views.student_books_search,name='student_books_search'),
    path("student_issued_books/", views.student_issued_books, name="student_issued_books"),
    path("student_favourite_book/", views.student_favourite_book, name="student_favourite_book"),
    path("student_add_favourite/", views.student_add_favourite, name="student_add_favourite"),
    path("student_delete_favourite/", views.student_delete_favourite, name="student_delete_favourite"),
    path("profile/", views.profile, name="profile"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),

    path("student_registration/", views.student_registration, name="student_registration"),
    path("change_password/", views.change_password, name="change_password"),
    path("student_login/", views.student_login, name="student_login"),
    path("admin_login/", views.admin_login, name="admin_login"),
    path("logout/", views.Logout, name="logout"),

    path("delete_issue/<int:myid>/", views.delete_issue, name="delete_issue"),
    path("delete_book/<int:myid>/", views.delete_book, name="delete_book"),
    path("delete_student/<int:myid>/", views.delete_student, name="delete_student"),
]