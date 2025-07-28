from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CarouselSlide, ServiceCategory, Service, TeamMember, AboutContent, JointVenture, ContactInfo, CropCycle, CropCycleImage, CropCycleVideo, Irrigation, IrrigationImage, IrrigationVideo,ExtremeWeather, ExtremeWeatherImage, ExtremeWeatherVideo,Livestock,LivestockImage,LivestockVideo, ServiceBulletin, Automation, AutomationImage, AgrometProduct, CropWeatherCalender, RemoteSensing, GeoInfo, GeoInfoImage, PestDisease, Guidance, AgrometAdaption, AgrometAdaptionImage, WeatherStation, WeatherStationImage, WebPortal, WebDevelopment, AISolution, AISolutionImage, ITConsultancy, ITConsultancyImage, NewsUpdate

@admin.register(CarouselSlide)
class CarouselSlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'description')

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'description')

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'has_cv', 'created_at', 'updated_at')
    search_fields = ('name', 'role')
    list_display_links = ('name',)

    def has_cv(self, obj):
        return bool(obj.cv)
    has_cv.boolean = True
    has_cv.short_description = 'CV Uploaded'

@admin.register(AboutContent)
class AboutContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'description')

@admin.register(JointVenture)
class JointVentureAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    
@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'mobile', 'updated_at')
    search_fields = ('email', 'address', 'mobile')

@admin.register(CropCycle)
class CropCycleAdmin(admin.ModelAdmin):
    list_display = ('description', 'updated_at')
    search_fields = ('description',)

@admin.register(CropCycleImage)
class CropCycleImageAdmin(admin.ModelAdmin):
    list_display = ('crop_cycle', 'caption', 'created_at')
    search_fields = ('caption',)

@admin.register(CropCycleVideo)
class CropCycleVideoAdmin(admin.ModelAdmin):
    list_display = ('crop_cycle', 'caption', 'created_at')
    search_fields = ('caption',)

@admin.register(Irrigation)
class IrrigationAdmin(admin.ModelAdmin):
    list_display = ('description', 'updated_at')
    search_fields = ('description',)

@admin.register(IrrigationImage)
class IrrigationImageAdmin(admin.ModelAdmin):
    list_display = ('irrigation', 'caption', 'created_at')
    search_fields = ('caption',)

@admin.register(IrrigationVideo)
class IrrigationVideoAdmin(admin.ModelAdmin):
    list_display = ('irrigation', 'caption', 'created_at')
    search_fields = ('caption',)
    

@admin.register(ExtremeWeather)
class ExtremeWeatherAdmin(admin.ModelAdmin):
    list_display = ('description', 'updated_at')
    search_fields = ('description',)

@admin.register(ExtremeWeatherImage)
class ExtremeWeatherImageAdmin(admin.ModelAdmin):
    list_display = ('extreme_weather', 'caption', 'created_at')
    search_fields = ('caption',)

@admin.register(ExtremeWeatherVideo)
class ExtremeWeatherVideoAdmin(admin.ModelAdmin):
    list_display = ('extreme_weather', 'caption', 'created_at')
    search_fields = ('caption',)

@admin.register(Livestock)
class LivestockAdmin(admin.ModelAdmin):
    list_display = ('description', 'updated_at')
    search_fields = ('description',)

@admin.register(LivestockImage)
class LivestockImageAdmin(admin.ModelAdmin):
    list_display = ('livestock', 'caption', 'created_at')
    search_fields = ('caption',)

@admin.register(LivestockVideo)
class LivestockVideoAdmin(admin.ModelAdmin):
    list_display = ('livestock', 'caption', 'created_at')
    search_fields = ('caption',)

@admin.register(ServiceBulletin)
class ServiceBulletinAdmin(admin.ModelAdmin):
    list_display = ('description', 'diagram_caption', 'updated_at')
    search_fields = ('description', 'diagram_caption')
    
@admin.register(Automation)
class AutomationAdmin(admin.ModelAdmin):
    list_display = ['description', 'created_at', 'updated_at']
    list_filter = ['created_at']
    search_fields = ['description']

@admin.register(AutomationImage)
class AutomationImageAdmin(admin.ModelAdmin):
    list_display = ['automation', 'caption', 'image']
    list_filter = ['automation']
    search_fields = ['caption']

@admin.register(AgrometProduct)
class AgrometProductAdmin(admin.ModelAdmin):
    list_display = ['pdf', 'caption', 'created_at', 'updated_at']
    list_filter = ['created_at']
    search_fields = ['caption']

@admin.register(CropWeatherCalender)
class CropWeatherCalenderAdmin(admin.ModelAdmin):
    list_display = ['description', 'image_caption', 'created_at', 'updated_at']
    list_filter = ['created_at']
    search_fields = ['description', 'image_caption']

@admin.register(RemoteSensing)
class RemoteSensingAdmin(admin.ModelAdmin):
    list_display = ['pdf', 'created_at', 'updated_at']
    list_filter = ['created_at']
    search_fields = ['pdf']


@admin.register(GeoInfo)
class GeoInfoAdmin(admin.ModelAdmin):
    list_display = ['description', 'created_at', 'updated_at']
    list_filter = ['created_at']
    search_fields = ['description']

@admin.register(GeoInfoImage)
class GeoInfoImageAdmin(admin.ModelAdmin):
    list_display = ['geo_info', 'image', 'caption']
    list_filter = ['geo_info']
    search_fields = ['caption']
    
@admin.register(PestDisease)
class PestDiseaseAdmin(admin.ModelAdmin):
    list_display = ['description', 'created_at', 'updated_at']
    list_filter = ['created_at']
    search_fields = ['description']

@admin.register(Guidance)
class GuidanceAdmin(admin.ModelAdmin):
    list_display = ['description', 'created_at', 'updated_at']
    list_filter = ['created_at']
    search_fields = ['description']

@admin.register(AgrometAdaption)
class AgrometAdaptionAdmin(admin.ModelAdmin):
    list_display = ['description', 'created_at', 'updated_at']
    list_filter = ['created_at']
    search_fields = ['description']

@admin.register(AgrometAdaptionImage)
class AgrometAdaptionImageAdmin(admin.ModelAdmin):
    list_display = ['agromet_adaption', 'image', 'caption']
    list_filter = ['agromet_adaption']
    search_fields = ['caption']

@admin.register(WeatherStation)
class WeatherStationAdmin(admin.ModelAdmin):
    list_display = ['description', 'created_at', 'updated_at']
    list_filter = ['created_at']
    search_fields = ['description']

@admin.register(WeatherStationImage)
class WeatherStationImageAdmin(admin.ModelAdmin):
    list_display = ['weather_station', 'image', 'caption']
    list_filter = ['weather_station']
    search_fields = ['caption']

@admin.register(WebPortal)
class WebPortalAdmin(admin.ModelAdmin):
    list_display = ('id',)

@admin.register(WebDevelopment)
class WebDevelopmentAdmin(admin.ModelAdmin):
    list_display = ('id',)

@admin.register(AISolution)
class AISolutionAdmin(admin.ModelAdmin):
    list_display = ('id',)

@admin.register(AISolutionImage)
class AISolutionImageAdmin(admin.ModelAdmin):
    list_display = ('ai_solution', 'caption')
    search_fields = ('caption',)

@admin.register(ITConsultancy)
class ITConsultancyAdmin(admin.ModelAdmin):
    list_display = ('id',)

@admin.register(ITConsultancyImage)
class ITConsultancyImageAdmin(admin.ModelAdmin):
    list_display = ('it_consultancy', 'caption')
    search_fields = ('caption',)

@admin.register(NewsUpdate)
class NewsUpdateAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    list_filter = ('created_at',)
    search_fields = ('title',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)