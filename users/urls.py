from django.urls import path
from .import views

urlpatterns = [
    path('', views.home,name="home"),
    path('about/', views.about,name="about"),
    path('contact/', views.contact,name="contact"),
    path('signout/', views.signout,name="signout"),
    path('logout/', views.logout_request,name="logout"),

    
    
    
    path('prisonerdashboard/', views.prisonerdashboard,name="prisonerdashboard"),
    path('prisonerdetails/', views.prisonerdetails,name="prisonerdetails"),
    path('prisonersaccount/', views.prisonersaccount,name="prisonersaccount"),
    path('psettingaccount/', views.psettingaccount,name="psettingaccount"),
    path('prisonersignup/', views.prisonersignup,name="prisonersignup"),
    path('prisonerlogin/', views.prisonerlogin,name="prisonerlogin"),
    path('prisonersreport/', views.prisonersreport,name="prisonersreport"),
    path('prisonerreg/', views.prisonerreg,name="prisonerreg"),
    path('prisonerpdf/', views.prisonerpdf,name="prisonerpdf"),
    
    # path('pcreate/', views.pcreate,name="pcreate"),
    path('pupdate/<str:pk>', views.pupdate,name="pupdate"),
    path('pdelete/<str:pk>', views.pdelete,name="pdelete"),
    
    path('prisonerupdate/<str:pk>', views.prisonerupdate,name="prisonerupdate"),
    path('prisonerdelete/<str:pk>', views.prisonerdelete,name="prisonerdelete"),
    
    path('approve/<int:pk>', views.approve,name="approve"),
    path('reject/<int:pk>', views.reject,name="reject"),
    
    path('visitorsdashboard/', views.visitorsdashboard,name="visitorsdashboard"),
    path('visitorsaccount/', views.visitorsaccount,name="visitorsaccount"),
    path('settingaccount/', views.settingaccount,name="settingaccount"),
    path('visitorsreport/', views.visitorsreport,name="visitorsreport"),
    path('vlogin/', views.vlogin,name="vlogin"),
    path('vregister/', views.vregister,name="vregister"),
    path('vcreate/', views.vcreate,name="vcreate"),
    path('vdelete/<int:pk>', views.vdelete,name="vdelete"),
    path('vupdate/<str:pk>', views.vupdate,name="vupdate"),
    path('visitorpdf/', views.visitorpdf,name="visitorpdf"),
    
    path('viewvisitation/', views.viewvisitation,name="viewvisitation"),
    
]