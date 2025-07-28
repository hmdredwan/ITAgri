from django.db import models
from django.utils.text import slugify

class CarouselSlide(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='carousel/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='services')
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/', blank=True, null=True)
    bio = models.TextField(blank=True)
    cv = models.FileField(upload_to='team/cvs/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class AboutContent(models.Model):
    title = models.CharField(max_length=200, default="About Us")
    description = models.TextField()
    images = models.ImageField(upload_to='about/images/', blank=True, null=True)
    videos = models.FileField(upload_to='about/videos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

# class JointVenture(models.Model):
#     title = models.CharField(max_length=200, default="Joint Venture")
#     description = models.TextField()
#     images = models.ImageField(upload_to='joint_venture/images/', blank=True, null=True)
#     videos = models.FileField(upload_to='joint_venture/videos/', blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title

class JointVenture(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class JointVentureImage(models.Model):
    joint_venture = models.ForeignKey(JointVenture, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='joint_venture/images/', blank=True, null=True)
    caption = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.joint_venture.title}"

class JointVentureVideo(models.Model):
    joint_venture = models.ForeignKey(JointVenture, related_name='videos', on_delete=models.CASCADE)
    video = models.FileField(upload_to='joint_venture/videos/', blank=True, null=True)
    caption = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Video for {self.joint_venture.title}"
    

class ContactInfo(models.Model):
    address = models.TextField()
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    location_url = models.URLField(blank=True, help_text="Google Maps embed URL or link")
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Contact Info - {self.email}"

class CropCycle(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Crop Cycle"

class CropCycleImage(models.Model):
    crop_cycle = models.ForeignKey(CropCycle, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='crop_cycle/images/', blank=True, null=True)
    caption = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for Crop Cycle"

class CropCycleVideo(models.Model):
    crop_cycle = models.ForeignKey(CropCycle, related_name='videos', on_delete=models.CASCADE)
    video = models.FileField(upload_to='crop_cycle/videos/', blank=True, null=True)
    caption = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Video for Crop Cycle"
    

class Irrigation(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Irrigation"

class IrrigationImage(models.Model):
    irrigation = models.ForeignKey(Irrigation, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='irrigation/images/', blank=True, null=True)
    caption = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for Irrigation"

class IrrigationVideo(models.Model):
    irrigation = models.ForeignKey(Irrigation, related_name='videos', on_delete=models.CASCADE)
    video = models.FileField(upload_to='irrigation/videos/', blank=True, null=True)
    caption = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Video for Irrigation"
    
class ExtremeWeather(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Extreme Weather"

class ExtremeWeatherImage(models.Model):
    extreme_weather = models.ForeignKey(ExtremeWeather, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='extreme_weather/images/', blank=True, null=True)
    caption = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for Extreme Weather"

class ExtremeWeatherVideo(models.Model):
    extreme_weather = models.ForeignKey(ExtremeWeather, related_name='videos', on_delete=models.CASCADE)
    video = models.FileField(upload_to='extreme_weather/videos/', blank=True, null=True)
    caption = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Video for Extreme Weather"
    
class Livestock(models.Model):
    description = models.TextField()
    diagram = models.ImageField(upload_to='livestock/diagrams/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Livestock"

class LivestockImage(models.Model):
    livestock = models.ForeignKey(Livestock, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='livestock/images/', blank=True, null=True)
    caption = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for Livestock"

class LivestockVideo(models.Model):
    livestock = models.ForeignKey(Livestock, related_name='videos', on_delete=models.CASCADE)
    video = models.FileField(upload_to='livestock/videos/', blank=True, null=True)
    caption = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Video for Livestock"

class ServiceBulletin(models.Model):
    description = models.TextField()
    diagram = models.ImageField(upload_to='service_bulletin/diagrams/', blank=True, null=True)
    diagram_caption = models.CharField(max_length=200, blank=True, null=True)
    # caption = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='service_bulletin/pdfs/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Service Bulletin"
    
class Automation(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Automation"

class AutomationImage(models.Model):
    automation = models.ForeignKey(Automation, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='service_bulletin/images/')
    caption = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Image for Automation: {self.caption or self.image.name}"

class AgrometProduct(models.Model):
    pdf = models.FileField(upload_to='agromet_products/pdfs/', blank=True, null=True)
    caption = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Agromet Product"

class CropWeatherCalender(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='crop_weather_calender/images/', blank=True, null=True)
    image_caption = models.CharField(max_length=200, blank=True, null=True)
    pdf = models.FileField(upload_to='crop_weather_calender/pdfs/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Crop Weather Calender"

class RemoteSensing(models.Model):
    pdf = models.FileField(upload_to='remote_sensing/pdfs/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Remote Sensing"


class GeoInfo(models.Model):
    description = models.TextField()
    pdf = models.FileField(upload_to='geo_info/pdfs/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Geo Info"

class GeoInfoImage(models.Model):
    geo_info = models.ForeignKey(GeoInfo, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='geo_info/images/')
    caption = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Image for Geo Info: {self.caption or self.image.name}"

class PestDisease(models.Model):
    description = models.TextField()
    pdf = models.FileField(upload_to='pest_disease/pdfs/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Pest Disease"

class Guidance(models.Model):
    description = models.TextField()
    pdf = models.FileField(upload_to='guidance/pdfs/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Guidance"
    
class AgrometAdaption(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Agromet Adaption"

class AgrometAdaptionImage(models.Model):
    agromet_adaption = models.ForeignKey(AgrometAdaption, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='agromet_adaption/images/')
    caption = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Image for Agromet Adaption: {self.caption or self.image.name}"

class WeatherStation(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Weather Station"

class WeatherStationImage(models.Model):
    weather_station = models.ForeignKey(WeatherStation, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='weather_station/images/')
    caption = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Image for Weather Station: {self.caption or self.image.name}"

class WebPortal(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Web Portal (Updated: {self.updated_at})"

class WebDevelopment(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Web Development (Updated: {self.updated_at})"

class AISolution(models.Model):
    description = models.TextField(blank=True)
    
    def __str__(self):
        return "AI Solution"

class AISolutionImage(models.Model):
    ai_solution = models.ForeignKey(AISolution, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ai_solution/')
    caption = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.caption or f"Image for AI Solution {self.ai_solution_id}"

class ITConsultancy(models.Model):
    description = models.TextField(blank=True)
    
    def __str__(self):
        return "IT Consultancy"

class ITConsultancyImage(models.Model):
    it_consultancy = models.ForeignKey(ITConsultancy, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='it_consultancy/')
    caption = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.caption or f"Image for IT Consultancy {self.it_consultancy_id}"

class NewsUpdate(models.Model):
    title = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='news_updates/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
