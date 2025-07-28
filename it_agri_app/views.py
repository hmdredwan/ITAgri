from django.views.generic import TemplateView, View
from .models import ServiceCategory, CarouselSlide, Service, AboutContent, TeamMember, JointVenture, ContactInfo, CropCycle, CropCycleImage, CropCycleVideo, Irrigation, IrrigationImage, IrrigationVideo, ExtremeWeather, ExtremeWeatherImage, ExtremeWeatherVideo,Livestock, ServiceBulletin,Automation,AgrometProduct, CropWeatherCalender, RemoteSensing, GeoInfo, PestDisease, Guidance, AgrometAdaption,  WeatherStation,WebPortal, WebDevelopment, AISolution, AISolutionImage, ITConsultancy, ITConsultancyImage, NewsUpdate
from django.core.mail import send_mail
from django import forms
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import FileResponse
from django.shortcuts import get_object_or_404

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carousel_slides'] = CarouselSlide.objects.filter(is_active=True)
        # Get up to 3 services from major-services and other-services
        major_services = ServiceCategory.objects.filter(slug='major-services').first()
        other_services = ServiceCategory.objects.filter(slug='other-services').first()
        featured_services = []
        if major_services:
            featured_services.extend(major_services.services.all()[:2])  # Get 2 from major
        if other_services and len(featured_services) < 3:
            featured_services.extend(other_services.services.all()[:3 - len(featured_services)])  # Fill up to 3
        context['featured_services'] = featured_services
        # context['news_updates'] = NewsUpdate.objects.all()
        context['news_updates'] = NewsUpdate.objects.order_by('-created_at') 
        return context

class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_contents'] = AboutContent.objects.all()
        context['news_updates'] = NewsUpdate.objects.order_by('-created_at')  # Add news updates
        return context

class ServicesView(TemplateView):
    template_name = 'services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['major_services'] = ServiceCategory.objects.filter(slug='major-services').first()
        context['other_services'] = ServiceCategory.objects.filter(slug='other-services').first()
        context['carousel_slides'] = CarouselSlide.objects.filter(is_active=True)
        context['news_updates'] = NewsUpdate.objects.order_by('-created_at')  # Add news updates
        return context

class BoardOfDirectorsView(TemplateView):
    template_name = 'it_agri_app/board_of_directors.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team_members'] = TeamMember.objects.all()
        context['news_updates'] = NewsUpdate.objects.order_by('-created_at')  # Add news updates
        return context

class JointVentureView(TemplateView):
    template_name = 'it_agri_app/joint_venture.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['joint_ventures'] = JointVenture.objects.all()
        context['news_updates'] = NewsUpdate.objects.order_by('-created_at')  # Add news updates
        return context
    

#contact view
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}))
    subject = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600', 'rows': 5}))

def contact_view(request):
    contact_info = ContactInfo.objects.first()  # Get the first contact info entry
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Send email
            try:
                send_mail(
                    subject=f"Sub: {subject}",
                    message=f"From: {name} <{email}>\n\n{message}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.ADMIN_EMAIL],
                    fail_silently=False,
                )
                messages.success(request, 'Your message has been sent successfully.')
            except Exception as e:
                messages.error(request, f'Error sending message: {str(e)}')
            return redirect('it_agri_app:contact')
    else:
        form = ContactForm()
    
    return render(request, 'it_agri_app/contact.html', {
        'form': form,
        'contact_info': contact_info,
        'news_updates': NewsUpdate.objects.order_by('-created_at'),  # Add news updates
    })
    
class CropCycleView(TemplateView):
    template_name = 'it_agri_app/crop_cycle.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['crop_cycle'] = CropCycle.objects.first()
        context['news_updates'] = NewsUpdate.objects.order_by('-created_at')
        return context
    
class IrrigationView(TemplateView):
    template_name = 'it_agri_app/irrigation.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['irrigation'] = Irrigation.objects.first()
        context['news_updates'] = NewsUpdate.objects.order_by('-created_at')
        return context
    
class ExtremeWeatherView(TemplateView):
    template_name = 'it_agri_app/extreme_weather.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['extreme_weather'] = ExtremeWeather.objects.first()
        context['news_updates'] = NewsUpdate.objects.order_by('-created_at')
        return context

class LivestockView(TemplateView):
    template_name = 'it_agri_app/livestock.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['livestock'] = Livestock.objects.first()
        context['news_updates'] = NewsUpdate.objects.order_by('-created_at')
        return context

class ServiceBulletinView(TemplateView):
    template_name = 'it_agri_app/service_bulletin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service_bulletin'] = ServiceBulletin.objects.first()
        context['news_updates'] = NewsUpdate.objects.order_by('-created_at')
        return context

class AutomationView(TemplateView):
    template_name = 'it_agri_app/automation.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['automation'] = Automation.objects.first()
        context['news_updates'] = NewsUpdate.objects.order_by('-created_at')
        return context
    
class AgrometProductView(TemplateView):
    template_name = 'it_agri_app/agromet_products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['agromet_product'] = AgrometProduct.objects.first()
        context['news_updates'] = NewsUpdate.objects.order_by('-created_at')
        return context

class CropWeatherCalenderView(TemplateView):
    template_name = 'it_agri_app/crop_weather_calender.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['crop_weather_calender'] = CropWeatherCalender.objects.first()
        context['news_updates'] = NewsUpdate.objects.order_by('-created_at')
        return context

class RemoteSensingView(TemplateView):
    template_name = 'it_agri_app/remote_sensing.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['remote_sensing'] = RemoteSensing.objects.first()
        context['news_updates'] = NewsUpdate.objects.order_by('-created_at')
        return context

class GeoInfoView(TemplateView):
    template_name = 'it_agri_app/geo_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['geo_info'] = GeoInfo.objects.first()
        context['news_updates'] = NewsUpdate.objects.order_by('-created_at')
        return context
    
class PestDiseaseView(TemplateView):
    template_name = 'it_agri_app/pest_disease.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pest_disease'] = PestDisease.objects.first()
        context['news_updates'] = NewsUpdate.objects.order_by('-created_at')
        return context

class GuidanceView(TemplateView):
    template_name = 'it_agri_app/guidance.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['guidance'] = Guidance.objects.first()
        context['news_updates'] = NewsUpdate.objects.order_by('-created_at')
        return context

class AgrometAdaptionView(TemplateView):
    template_name = 'it_agri_app/agromet_adaption.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['agromet_adaption'] = AgrometAdaption.objects.first()
        context['news_updates'] = NewsUpdate.objects.order_by('-created_at')
        return context

class WeatherStationView(TemplateView):
    template_name = 'it_agri_app/weather_station.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['weather_station'] = WeatherStation.objects.first()
        context['news_updates'] = NewsUpdate.objects.order_by('-created_at')
        return context

class AgroMeteoroSystemDevelopmentView(TemplateView):
    template_name = 'it_agri_app/agro_meteoro_system_development.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_updates'] = NewsUpdate.objects.order_by('-created_at')
        return context


class WebPortalView(TemplateView):
    template_name = 'it_agri_app/web_portal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['web_portal'] = WebPortal.objects.first()
        context['news_updates'] = NewsUpdate.objects.order_by('-created_at')
        return context

class WebDevelopmentView(TemplateView):
    template_name = 'it_agri_app/web_development.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['web_development'] = WebDevelopment.objects.first()
        context['news_updates'] = NewsUpdate.objects.order_by('-created_at')
        return context

class AISolutionView(TemplateView):
    template_name = 'it_agri_app/ai_solution.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ai_solution'] = AISolution.objects.first()
        context['news_updates'] = NewsUpdate.objects.order_by('-created_at')
        return context

class ITConsultancyView(TemplateView):
    template_name = 'it_agri_app/it_consultancy.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['it_consultancy'] = ITConsultancy.objects.first()
        context['news_updates'] = NewsUpdate.objects.order_by('-created_at')
        return context

class NewsUpdatePDFView(View):
    def get(self, request, pk):
        news_update = get_object_or_404(NewsUpdate, pk=pk)
        return FileResponse(news_update.pdf, as_attachment=False, filename=f"{news_update.title}.pdf")