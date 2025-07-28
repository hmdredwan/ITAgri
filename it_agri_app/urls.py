from django.urls import path
from . import views

app_name = 'it_agri_app'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('services/', views.ServicesView.as_view(), name='services'),
    path('board-of-directors/', views.BoardOfDirectorsView.as_view(), name='board_of_directors'),
    path('joint-venture/', views.JointVentureView.as_view(), name='joint_venture'),
     path('contact/', views.contact_view, name='contact'),
    path('crop-cycle/', views.CropCycleView.as_view(), name='crop_cycle'),
    path('irrigation/', views.IrrigationView.as_view(), name='irrigation'),
     path('extreme-weather/', views.ExtremeWeatherView.as_view(), name='extreme_weather'),
     path('livestock/', views.LivestockView.as_view(), name='livestock'),
     path('service-bulletin/', views.ServiceBulletinView.as_view(), name='service_bulletin'),
     path('automation/', views.AutomationView.as_view(), name='automation'),
     path('agromet-products/', views.AgrometProductView.as_view(), name='agromet_products'),
     path('crop-weather-calender/', views.CropWeatherCalenderView.as_view(), name='crop_weather_calender'),
     path('remote-sensing/', views.RemoteSensingView.as_view(), name='remote_sensing'),
    path('geo-info/', views.GeoInfoView.as_view(), name='geo_info'),
    path('pest-disease/', views.PestDiseaseView.as_view(), name='pest_disease'),
    path('guidance/', views.GuidanceView.as_view(), name='guidance'),
    path('agromet-adaption/', views.AgrometAdaptionView.as_view(), name='agromet_adaption'),
    path('weather-station/', views.WeatherStationView.as_view(), name='weather_station'),
    path('agro-meteoro-system-development/', views.AgroMeteoroSystemDevelopmentView.as_view(), name='agro_meteoro_system_development'),
     path('web-portal/', views.WebPortalView.as_view(), name='web_portal'),
    path('web-development/', views.WebDevelopmentView.as_view(), name='web_development'),
    path('ai-solution/', views.AISolutionView.as_view(), name='ai_solution'),
    path('it-consultancy/', views.ITConsultancyView.as_view(), name='it_consultancy'),
    path('news-update/<int:pk>/', views.NewsUpdatePDFView.as_view(), name='news_update_pdf'),
]