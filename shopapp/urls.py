from django.urls import path
from . import views


urlpatterns = [
    path("",views.index,name= "index"),
    path("aboutus/",views.aboutus,name = "About Us"),
    path("contactus/",views.contactus,name = "Contactus"),
    path("tracker/",views.tracker,name = "tracker"),
    path("search/",views.search,name = "search"),
    path("productview/",views.productview,name = "productviews"),
    path("checkout/",views.checkout,name = "checkouts")
    
]  