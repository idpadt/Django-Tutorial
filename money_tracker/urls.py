from django.urls import path
from money_tracker.views import show_tracker, create_transaction, show_xml, show_json, show_json_by_id, register
from money_tracker.views import login_user, logout_user

app_name = 'money_tracker'

urlpatterns = [
    path('', show_tracker, name='show_tracker'),
    path('create/', create_transaction, name='create_transaction'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>', show_json_by_id, name = 'show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name='logout'),
]