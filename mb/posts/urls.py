from django.urls import path
from.views import HomepagView

urlpatterns = [
	path('', HomepagView.as_view(), name='home')
]