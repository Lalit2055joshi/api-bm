from django.contrib import admin
from django.urls import path,include
from billing import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/',include('billing.urls'))
    # path('',views.add_show,name='addandshow'),
    # path('delete/<int:id>/',views.delete_data,name='deletedata'),
    # path('<int:id>/',views.update_data,name='updatedata'),
    # path('activecustomer/',views.getactivecustomer,name='activecustomer'),
    # path('inactivecustomer/',views.getinactivecustomer,name='inactivecustomer'),
    # path('addshow/',views.add_show_customer,name='addandshowcustomer'),
    # path('update/<int:id>/',views.update_customer_data,name='updatecustomer'),
    # path('deletecustomer/<int:id>/',views.delete_customer_data,name='deletecustomerdata'),
    # path('addshow/paidsubscriber/',views.getpaidsubscriber,name='paidsubscriber'),
    # path('addshow/unpaidsubscriber/',views.getunpaidsubscriber,name='unpaidsubscriber'),
    # path('lalit/',views.sendemail,name='lalit'),
    # path('signup/',views.get_signup,name='signup'),
    # path('signin/',views.get_signin,name='signin'),
    # path('logout/',views.logoutpage,name='logout'),
    # path('createcustomer/',views.add_customer,name='createcustomer'),
]
