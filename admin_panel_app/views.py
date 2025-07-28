from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from it_agri_app.models import CarouselSlide, ServiceCategory, Service, TeamMember, AboutContent, JointVenture, JointVentureImage, JointVentureVideo, ContactInfo, CropCycle, CropCycleImage, CropCycleVideo, Irrigation, IrrigationImage, IrrigationVideo,ExtremeWeather, ExtremeWeatherImage, ExtremeWeatherVideo, Livestock, LivestockImage, LivestockVideo, ServiceBulletin, Automation, AutomationImage, AgrometProduct, CropWeatherCalender, RemoteSensing, GeoInfo, GeoInfoImage, PestDisease, Guidance, AgrometAdaption, AgrometAdaptionImage, WeatherStation, WeatherStationImage,WebPortal, WebDevelopment, AISolution, AISolutionImage, ITConsultancy, ITConsultancyImage, NewsUpdate
from django import forms
from tinymce.widgets import TinyMCE  # Import TinyMCE widget
import os

class CarouselSlideForm(forms.ModelForm):
    class Meta:
        model = CarouselSlide
        fields = ['title', 'description', 'image', 'is_active']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class ServiceCategoryForm(forms.ModelForm):
    class Meta:
        model = ServiceCategory
        fields = ['name', 'slug']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['category', 'title', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ['name', 'role', 'image', 'bio', 'cv']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }

class AboutContentForm(forms.ModelForm):
    class Meta:
        model = AboutContent
        fields = ['title', 'description', 'images', 'videos']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
        
class JointVentureForm(forms.ModelForm):
    class Meta:
        model = JointVenture
        fields = ['title', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
        
class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ['address', 'mobile', 'email', 'location_url', 'facebook_url', 'twitter_url', 'linkedin_url']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 4, 'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
            'mobile': forms.TextInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
            'email': forms.EmailInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
            'location_url': forms.URLInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
            'facebook_url': forms.URLInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
            'twitter_url': forms.URLInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
            'linkedin_url': forms.URLInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
        }

class CropCycleForm(forms.ModelForm):
    class Meta:
        model = CropCycle
        fields = ['description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 6, 'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
        }
        
class IrrigationForm(forms.ModelForm):
    class Meta:
        model = Irrigation
        fields = ['description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 6, 'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
        }
        
class ExtremeWeatherForm(forms.ModelForm):
    class Meta:
        model = ExtremeWeather
        fields = ['description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 6, 'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
        }

class LivestockForm(forms.ModelForm):
    class Meta:
        model = Livestock
        fields = ['description', 'diagram']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 6, 'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
            'diagram': forms.FileInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
        }

class ServiceBulletinForm(forms.ModelForm):
    class Meta:
        model = ServiceBulletin
        fields = ['description', 'diagram', 'diagram_caption', 'pdf']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 6, 'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
            'diagram': forms.FileInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
            'diagram_caption': forms.TextInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
            'pdf': forms.FileInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
        }

class AgrometProductForm(forms.ModelForm):
    class Meta:
        model = AgrometProduct
        fields = ['pdf', 'caption']
        widgets = {
            'pdf': forms.FileInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
            'caption': forms.TextInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
        }
        
class CropWeatherCalenderForm(forms.ModelForm):
    class Meta:
        model = CropWeatherCalender
        fields = ['description', 'image', 'image_caption', 'pdf']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 6, 'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
            'image': forms.FileInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
            'image_caption': forms.TextInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
            'pdf': forms.FileInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
        }

class RemoteSensingForm(forms.ModelForm):
    class Meta:
        model = RemoteSensing
        fields = ['pdf']
        widgets = {
            'pdf': forms.FileInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
        }

class GeoInfoForm(forms.ModelForm):
    class Meta:
        model = GeoInfo
        fields = ['description', 'pdf']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 6, 'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
            'pdf': forms.FileInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
        }
class GeoInfoImageForm(forms.ModelForm):
    class Meta:
        model = GeoInfoImage
        fields = ['image', 'caption']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
            'caption': forms.TextInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
        }

class PestDiseaseForm(forms.ModelForm):
    class Meta:
        model = PestDisease
        fields = ['description', 'pdf']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 6, 'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
            'pdf': forms.FileInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
        }

class GuidanceForm(forms.ModelForm):
    class Meta:
        model = Guidance
        fields = ['description', 'pdf']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 6, 'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
            'pdf': forms.FileInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
        }
class AgrometAdaptionForm(forms.ModelForm):
    class Meta:
        model = AgrometAdaption
        fields = ['description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 6, 'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
        }

class AgrometAdaptionImageForm(forms.ModelForm):
    class Meta:
        model = AgrometAdaptionImage
        fields = ['image', 'caption']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
            'caption': forms.TextInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
        }

class WeatherStationForm(forms.ModelForm):
    class Meta:
        model = WeatherStation
        fields = ['description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 6, 'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
        }

class WeatherStationImageForm(forms.ModelForm):
    class Meta:
        model = WeatherStationImage
        fields = ['image', 'caption']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
            'caption': forms.TextInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
        }
    
class WebPortalForm(forms.ModelForm):
    class Meta:
        model = WebPortal
        fields = ['description']
        widgets = {
            
            'description': forms.Textarea(attrs={'rows': 4, 'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
        }
class WebDevelopmentForm(forms.ModelForm):
    class Meta:
        model = WebDevelopment
        fields = ['description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
        }
# class AISolutionForm(forms.ModelForm):
#     class Meta:
#         model = AISolution
#         fields = ['description']
#         widgets = {
#             'description': forms.Textarea(attrs={'rows': 6, 'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
#         }

# class AISolutionImageForm(forms.ModelForm):
#     class Meta:
#         model = AISolutionImage
#         fields = ['image', 'caption']
#         widgets = {
#             'image': forms.FileInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
#             'caption': forms.TextInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
#         }

# class ITConsultancyForm(forms.ModelForm):
#     class Meta:
#         model = ITConsultancy
#         fields = ['description']
#         widgets = {
#             'description': forms.Textarea(attrs={'rows': 6, 'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
#         }

# class ITConsultancyImageForm(forms.ModelForm):
#     class Meta:
#         model = ITConsultancyImage
#         fields = ['image', 'caption']
#         widgets = {
#             'image': forms.FileInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
#             'caption': forms.TextInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
#         }

class AISolutionForm(forms.ModelForm):
    class Meta:
        model = AISolution
        fields = ['description']
        widgets = {
            'description': TinyMCE(attrs={'rows': 6, 'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
        }

class AISolutionImageForm(forms.ModelForm):
    class Meta:
        model = AISolutionImage
        fields = ['image', 'caption']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
            'caption': forms.TextInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
        }

class ITConsultancyForm(forms.ModelForm):
    class Meta:
        model = ITConsultancy
        fields = ['description']
        widgets = {
            'description': TinyMCE(attrs={'rows': 6, 'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
        }

class ITConsultancyImageForm(forms.ModelForm):
    class Meta:
        model = ITConsultancyImage
        fields = ['image', 'caption']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
            'caption': forms.TextInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
        }
    
class NewsUpdateForm(forms.ModelForm):
    class Meta:
        model = NewsUpdate
        fields = ['title', 'pdf']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-600 focus:ring-green-600'}),
            'pdf': forms.FileInput(attrs={'class': 'mt-1 block w-full'}),
        }

def is_admin(user):
    return user.is_authenticated and user.is_staff

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_panel_app:admin_dashboard')
        else:
            messages.error(request, 'Invalid username or password, or you are not an admin.')
    return render(request, 'admin_login.html')

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    context = {
        'carousel_count': CarouselSlide.objects.count(),
        'category_count': ServiceCategory.objects.count(),
        'service_count': Service.objects.count(),
        'team_count': TeamMember.objects.count(),
        'about_count': AboutContent.objects.count(),
    }
    return render(request, 'admin_dashboard.html', context)

@login_required
@user_passes_test(is_admin)
def carousel_management(request):
    carousel_slides = CarouselSlide.objects.all()
    context = {'carousel_slides': carousel_slides}
    return render(request, 'carousel_management.html', context)

@login_required
@user_passes_test(is_admin)
def carousel_create(request):
    if request.method == 'POST':
        form = CarouselSlideForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Carousel slide created successfully.')
            return redirect('admin_panel_app:carousel_management')
        else:
            messages.error(request, 'Error creating carousel slide. Check the form.')
    else:
        form = CarouselSlideForm()
    return render(request, 'carousel_form.html', {'form': form, 'action': 'Create'})

@login_required
@user_passes_test(is_admin)
def carousel_update(request, pk):
    slide = get_object_or_404(CarouselSlide, pk=pk)
    if request.method == 'POST':
        form = CarouselSlideForm(request.POST, request.FILES, instance=slide)
        if form.is_valid():
            form.save()
            messages.success(request, 'Carousel slide updated successfully.')
            return redirect('admin_panel_app:carousel_management')
        else:
            messages.error(request, 'Error updating carousel slide. Check the form.')
    else:
        form = CarouselSlideForm(instance=slide)
    return render(request, 'carousel_form.html', {'form': form, 'action': 'Update'})

@login_required
@user_passes_test(is_admin)
def carousel_delete(request, pk):
    slide = get_object_or_404(CarouselSlide, pk=pk)
    if request.method == 'POST':
        if slide.image:
            if os.path.isfile(slide.image.path):
                os.remove(slide.image.path)
        slide.delete()
        messages.success(request, 'Carousel slide deleted successfully.')
        return redirect('admin_panel_app:carousel_management')
    return render(request, 'carousel_confirm_delete.html', {'slide': slide})

@login_required
@user_passes_test(is_admin)
def category_management(request):
    service_categories = ServiceCategory.objects.all()
    context = {'service_categories': service_categories}
    return render(request, 'category_management.html', context)

@login_required
@user_passes_test(is_admin)
def category_create(request):
    if request.method == 'POST':
        form = ServiceCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service category created successfully.')
            return redirect('admin_panel_app:category_management')
        else:
            messages.error(request, 'Error creating service category. Check the form.')
    else:
        form = ServiceCategoryForm()
    return render(request, 'category_form.html', {'form': form, 'action': 'Create'})

@login_required
@user_passes_test(is_admin)
def category_update(request, pk):
    category = get_object_or_404(ServiceCategory, pk=pk)
    if request.method == 'POST':
        form = ServiceCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service category updated successfully.')
            return redirect('admin_panel_app:category_management')
        else:
            messages.error(request, 'Error updating service category. Check the form.')
    else:
        form = ServiceCategoryForm(instance=category)
    return render(request, 'category_form.html', {'form': form, 'action': 'Update'})

@login_required
@user_passes_test(is_admin)
def category_delete(request, pk):
    category = get_object_or_404(ServiceCategory, pk=pk)
    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Service category deleted successfully.')
        return redirect('admin_panel_app:category_management')
    return render(request, 'category_confirm_delete.html', {'category': category})

@login_required
@user_passes_test(is_admin)
def service_management(request):
    services = Service.objects.all()
    service_categories = ServiceCategory.objects.all()
    context = {'services': services, 'service_categories': service_categories}
    return render(request, 'service_management.html', context)

@login_required
@user_passes_test(is_admin)
def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service created successfully.')
            return redirect('admin_panel_app:service_management')
        else:
            messages.error(request, 'Error creating service. Check the form.')
    else:
        form = ServiceForm()
    return render(request, 'service_form.html', {'form': form, 'action': 'Create'})

@login_required
@user_passes_test(is_admin)
def service_update(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service updated successfully.')
            return redirect('admin_panel_app:service_management')
        else:
            messages.error(request, 'Error updating service. Check the form.')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'service_form.html', {'form': form, 'action': 'Update'})

@login_required
@user_passes_test(is_admin)
def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.delete()
        messages.success(request, 'Service deleted successfully.')
        return redirect('admin_panel_app:service_management')
    return render(request, 'service_confirm_delete.html', {'service': service})

@login_required
@user_passes_test(is_admin)
def team_management(request):
    team_members = TeamMember.objects.all()
    context = {'team_members': team_members}
    return render(request, 'team_management.html', context)

@login_required
@user_passes_test(is_admin)
def team_member_create(request):
    if request.method == 'POST':
        form = TeamMemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Team member created successfully.')
            return redirect('admin_panel_app:team_management')
        else:
            messages.error(request, 'Error creating team member. Check the form.')
    else:
        form = TeamMemberForm()
    return render(request, 'team_member_form.html', {'form': form, 'action': 'Create'})

@login_required
@user_passes_test(is_admin)
def team_member_update(request, pk):
    member = get_object_or_404(TeamMember, pk=pk)
    if request.method == 'POST':
        form = TeamMemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Team member updated successfully.')
            return redirect('admin_panel_app:team_management')
        else:
            messages.error(request, 'Error updating team member. Check the form.')
    else:
        form = TeamMemberForm(instance=member)
    return render(request, 'team_member_form.html', {'form': form, 'action': 'Update'})

@login_required
@user_passes_test(is_admin)
def team_member_delete(request, pk):
    member = get_object_or_404(TeamMember, pk=pk)
    if request.method == 'POST':
        if member.image:
            if os.path.isfile(member.image.path):
                os.remove(member.image.path)
        member.delete()
        messages.success(request, 'Team member deleted successfully.')
        return redirect('admin_panel_app:team_management')
    return render(request, 'team_member_confirm_delete.html', {'member': member})

@login_required
@user_passes_test(is_admin)
def about_management(request):
    about_contents = AboutContent.objects.all()
    context = {'about_contents': about_contents}
    return render(request, 'about_management.html', context)

@login_required
@user_passes_test(is_admin)
def about_create(request):
    if request.method == 'POST':
        form = AboutContentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'About content created successfully.')
            return redirect('admin_panel_app:about_management')
        else:
            messages.error(request, 'Error creating about content. Check the form.')
    else:
        form = AboutContentForm()
    return render(request, 'about_form.html', {'form': form, 'action': 'Create'})

@login_required
@user_passes_test(is_admin)
def about_update(request, pk):
    content = get_object_or_404(AboutContent, pk=pk)
    if request.method == 'POST':
        form = AboutContentForm(request.POST, request.FILES, instance=content)
        if form.is_valid():
            form.save()
            messages.success(request, 'About content updated successfully.')
            return redirect('admin_panel_app:about_management')
        else:
            messages.error(request, 'Error updating about content. Check the form.')
    else:
        form = AboutContentForm(instance=content)
    return render(request, 'about_form.html', {'form': form, 'action': 'Update'})

@login_required
@user_passes_test(is_admin)
def about_delete(request, pk):
    content = get_object_or_404(AboutContent, pk=pk)
    if request.method == 'POST':
        if content.images and os.path.isfile(content.images.path):
            os.remove(content.images.path)
        if content.videos and os.path.isfile(content.videos.path):
            os.remove(content.videos.path)
        content.delete()
        messages.success(request, 'About content deleted successfully.')
        return redirect('admin_panel_app:about_management')
    return render(request, 'about_confirm_delete.html', {'content': content})

"""
@login_required
@user_passes_test(is_admin)
def joint_venture_management(request):
    joint_ventures = JointVenture.objects.all()
    context = {'joint_ventures': joint_ventures}
    return render(request, 'joint_venture_management.html', context)

@login_required
@user_passes_test(is_admin)
def joint_venture_create(request):
    if request.method == 'POST':
        form = JointVentureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Joint venture content created successfully.')
            return redirect('admin_panel_app:joint_venture_management')
        else:
            messages.error(request, 'Error creating joint venture content. Check the form.')
    else:
        form = JointVentureForm()
    return render(request, 'joint_venture_form.html', {'form': form, 'action': 'Create'})

@login_required
@user_passes_test(is_admin)
def joint_venture_update(request, pk):
    content = get_object_or_404(JointVenture, pk=pk)
    if request.method == 'POST':
        form = JointVentureForm(request.POST, request.FILES, instance=content)
        if form.is_valid():
            form.save()
            messages.success(request, 'Joint venture content updated successfully.')
            return redirect('admin_panel_app:joint_venture_management')
        else:
            messages.error(request, 'Error updating joint venture content. Check the form.')
    else:
        form = JointVentureForm(instance=content)
    return render(request, 'joint_venture_form.html', {'form': form, 'action': 'Update'})

@login_required
@user_passes_test(is_admin)
def joint_venture_delete(request, pk):
    content = get_object_or_404(JointVenture, pk=pk)
    if request.method == 'POST':
        if content.images and os.path.isfile(content.images.path):
            os.remove(content.images.path)
        if content.videos and os.path.isfile(content.videos.path):
            os.remove(content.videos.path)
        content.delete()
        messages.success(request, 'Joint venture content deleted successfully.')
        return redirect('admin_panel_app:joint_venture_management')
    return render(request, 'joint_venture_confirm_delete.html', {'content': content})
"""
@login_required
@user_passes_test(is_admin)
def joint_venture_management(request):
    joint_ventures = JointVenture.objects.all()
    context = {'joint_ventures': joint_ventures}
    return render(request, 'joint_venture_management.html', context)

@login_required
@user_passes_test(is_admin)
def joint_venture_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        joint_venture = JointVenture.objects.create(title=title, description=description)
        
        # Handle multiple images
        images = request.FILES.getlist('images')
        image_captions = request.POST.getlist('image_captions')
        for image, caption in zip(images, image_captions):
            if image:
                JointVentureImage.objects.create(joint_venture=joint_venture, image=image, caption=caption)
        
        # Handle multiple videos
        videos = request.FILES.getlist('videos')
        video_captions = request.POST.getlist('video_captions')
        for video, caption in zip(videos, video_captions):
            if video:
                JointVentureVideo.objects.create(joint_venture=joint_venture, video=video, caption=caption)
        
        messages.success(request, 'Joint Venture created successfully.')
        return redirect('admin_panel_app:joint_venture_management')
    
    return render(request, 'joint_venture_form.html', {'form_type': 'create'})

@login_required
@user_passes_test(is_admin)
def joint_venture_update(request, pk):
    joint_venture = get_object_or_404(JointVenture, pk=pk)
    if request.method == 'POST':
        joint_venture.title = request.POST.get('title')
        joint_venture.description = request.POST.get('description')
        joint_venture.save()
        
        # Handle new images
        images = request.FILES.getlist('images')
        image_captions = request.POST.getlist('image_captions')
        for image, caption in zip(images, image_captions):
            if image:
                JointVentureImage.objects.create(joint_venture=joint_venture, image=image, caption=caption)
        
        # Handle new videos
        videos = request.FILES.getlist('videos')
        video_captions = request.POST.getlist('video_captions')
        for video, caption in zip(videos, video_captions):
            if video:
                JointVentureVideo.objects.create(joint_venture=joint_venture, video=video, caption=caption)
        
        # Handle deletions
        delete_images = request.POST.getlist('delete_images')
        JointVentureImage.objects.filter(id__in=delete_images).delete()
        delete_videos = request.POST.getlist('delete_videos')
        JointVentureVideo.objects.filter(id__in=delete_videos).delete()
        
        messages.success(request, 'Joint Venture updated successfully.')
        return redirect('admin_panel_app:joint_venture_management')
    
    return render(request, 'joint_venture_form.html', {
        'form_type': 'update',
        'joint_venture': joint_venture,
        'images': joint_venture.images.all(),
        'videos': joint_venture.videos.all()
    })

@login_required
@user_passes_test(is_admin)
def joint_venture_delete(request, pk):
    joint_venture = get_object_or_404(JointVenture, pk=pk)
    if request.method == 'POST':
        joint_venture.delete()
        messages.success(request, 'Joint Venture deleted successfully.')
        return redirect('admin_panel_app:joint_venture_management')
    return render(request, 'joint_venture_confirm_delete.html', {'joint_venture': joint_venture})

@login_required
@user_passes_test(is_admin)
def contact_info_update(request):
    contact_info = ContactInfo.objects.first()
    if request.method == 'POST':
        form = ContactInfoForm(request.POST, instance=contact_info)
        if form.is_valid():
            form.save() if contact_info else ContactInfo.objects.create(**form.cleaned_data)
            messages.success(request, 'Contact information updated successfully.')
            return redirect('admin_panel_app:admin_dashboard')
        else:
            messages.error(request, 'Error updating contact information. Check the form.')
    else:
        form = ContactInfoForm(instance=contact_info)
    return render(request, 'contact_info_form.html', {'form': form, 'action': 'Update'})

@login_required
@user_passes_test(is_admin)
def crop_cycle_update(request):
    crop_cycle = CropCycle.objects.first()
    if request.method == 'POST':
        form = CropCycleForm(request.POST, instance=crop_cycle)
        if form.is_valid():
            crop_cycle = form.save() if crop_cycle else CropCycle.objects.create(**form.cleaned_data)
            
            images = request.FILES.getlist('images')
            image_captions = request.POST.getlist('image_captions')
            for image, caption in zip(images, image_captions):
                if image and caption:
                    CropCycleImage.objects.create(crop_cycle=crop_cycle, image=image, caption=caption)
            
            videos = request.FILES.getlist('videos')
            video_captions = request.POST.getlist('video_captions')
            for video, caption in zip(videos, video_captions):
                if video and caption:
                    CropCycleVideo.objects.create(crop_cycle=crop_cycle, video=video, caption=caption)
            
            delete_images = request.POST.getlist('delete_images')
            CropCycleImage.objects.filter(id__in=delete_images).delete()
            delete_videos = request.POST.getlist('delete_videos')
            CropCycleVideo.objects.filter(id__in=delete_videos).delete()
            
            messages.success(request, 'Crop Cycle updated successfully.')
            return redirect('admin_panel_app:admin_dashboard')
        else:
            messages.error(request, 'Error updating Crop Cycle. Check the form.')
    else:
        form = CropCycleForm(instance=crop_cycle)
    return render(request, 'crop_cycle_form.html', {
        'form': form,
        'crop_cycle': crop_cycle,
        'images': crop_cycle.images.all() if crop_cycle else [],
        'videos': crop_cycle.videos.all() if crop_cycle else [],
    })

@login_required
@user_passes_test(is_admin)
def irrigation_update(request):
    irrigation = Irrigation.objects.first()
    if request.method == 'POST':
        form = IrrigationForm(request.POST, instance=irrigation)
        if form.is_valid():
            irrigation = form.save() if irrigation else Irrigation.objects.create(**form.cleaned_data)
            
            images = request.FILES.getlist('images')
            image_captions = request.POST.getlist('image_captions')
            for image, caption in zip(images, image_captions):
                if image and caption:
                    IrrigationImage.objects.create(irrigation=irrigation, image=image, caption=caption)
            
            videos = request.FILES.getlist('videos')
            video_captions = request.POST.getlist('video_captions')
            for video, caption in zip(videos, video_captions):
                if video and caption:
                    IrrigationVideo.objects.create(irrigation=irrigation, video=video, caption=caption)
            
            delete_images = request.POST.getlist('delete_images')
            IrrigationImage.objects.filter(id__in=delete_images).delete()
            delete_videos = request.POST.getlist('delete_videos')
            IrrigationVideo.objects.filter(id__in=delete_videos).delete()
            
            messages.success(request, 'Irrigation updated successfully.')
            return redirect('admin_panel_app:admin_dashboard')
        else:
            messages.error(request, 'Error updating Irrigation. Check the form.')
    else:
        form = IrrigationForm(instance=irrigation)
    return render(request, 'irrigation_form.html', {
        'form': form,
        'irrigation': irrigation,
        'images': irrigation.images.all() if irrigation else [],
        'videos': irrigation.videos.all() if irrigation else [],
    })

@login_required
@user_passes_test(is_admin)
def extreme_weather_update(request):
    extreme_weather = ExtremeWeather.objects.first()
    if request.method == 'POST':
        form = ExtremeWeatherForm(request.POST, instance=extreme_weather)
        if form.is_valid():
            extreme_weather = form.save() if extreme_weather else ExtremeWeather.objects.create(**form.cleaned_data)
            
            images = request.FILES.getlist('images')
            image_captions = request.POST.getlist('image_captions')
            for image, caption in zip(images, image_captions):
                if image and caption:
                    ExtremeWeatherImage.objects.create(extreme_weather=extreme_weather, image=image, caption=caption)
            
            videos = request.FILES.getlist('videos')
            video_captions = request.POST.getlist('video_captions')
            for video, caption in zip(videos, video_captions):
                if video and caption:
                    ExtremeWeatherVideo.objects.create(extreme_weather=extreme_weather, video=video, caption=caption)
            
            delete_images = request.POST.getlist('delete_images')
            ExtremeWeatherImage.objects.filter(id__in=delete_images).delete()
            delete_videos = request.POST.getlist('delete_videos')
            ExtremeWeatherVideo.objects.filter(id__in=delete_videos).delete()
            
            messages.success(request, 'Extreme Weather updated successfully.')
            return redirect('admin_panel_app:admin_dashboard')
        else:
            messages.error(request, 'Error updating Extreme Weather. Check the form.')
    else:
        form = ExtremeWeatherForm(instance=extreme_weather)
    return render(request, 'extreme_weather_form.html', {
        'form': form,
        'extreme_weather': extreme_weather,
        'images': extreme_weather.images.all() if extreme_weather else [],
        'videos': extreme_weather.videos.all() if extreme_weather else [],
    })

@login_required
@user_passes_test(is_admin)
def livestock_update(request):
    livestock = Livestock.objects.first()
    if request.method == 'POST':
        form = LivestockForm(request.POST, request.FILES, instance=livestock)
        if form.is_valid():
            livestock = form.save() if livestock else Livestock.objects.create(**form.cleaned_data)
            
            images = request.FILES.getlist('images')
            image_captions = request.POST.getlist('image_captions')
            for image, caption in zip(images, image_captions):
                if image and caption:
                    LivestockImage.objects.create(livestock=livestock, image=image, caption=caption)
            
            videos = request.FILES.getlist('videos')
            video_captions = request.POST.getlist('video_captions')
            for video, caption in zip(videos, video_captions):
                if video and caption:
                    LivestockVideo.objects.create(livestock=livestock, video=video, caption=caption)
            
            delete_images = request.POST.getlist('delete_images')
            LivestockImage.objects.filter(id__in=delete_images).delete()
            delete_videos = request.POST.getlist('delete_videos')
            LivestockVideo.objects.filter(id__in=delete_videos).delete()
            
            messages.success(request, 'Livestock updated successfully.')
            return redirect('admin_panel_app:admin_dashboard')
        else:
            messages.error(request, 'Error updating Livestock. Check the form.')
    else:
        form = LivestockForm(instance=livestock)
    return render(request, 'livestock_form.html', {
        'form': form,
        'livestock': livestock,
        'images': livestock.images.all() if livestock else [],
        'videos': livestock.videos.all() if livestock else [],
    })

@login_required
@user_passes_test(is_admin)
def service_bulletin_update(request):
    service_bulletin = ServiceBulletin.objects.first()
    if request.method == 'POST':
        form = ServiceBulletinForm(request.POST, request.FILES, instance=service_bulletin)
        if form.is_valid():
            service_bulletin = form.save() if service_bulletin else ServiceBulletin.objects.create(**form.cleaned_data)
            if 'delete_diagram' in request.POST and service_bulletin.diagram:
                if os.path.isfile(service_bulletin.diagram.path):
                    os.remove(service_bulletin.diagram.path)
                service_bulletin.diagram = None
                service_bulletin.diagram_caption = None  # Clear caption when diagram is deleted
            if 'delete_pdf' in request.POST and service_bulletin.pdf:
                if os.path.isfile(service_bulletin.pdf.path):
                    os.remove(service_bulletin.pdf.path)
                service_bulletin.pdf = None
            service_bulletin.save()
            messages.success(request, 'Service Bulletin updated successfully.')
            return redirect('admin_panel_app:admin_dashboard')
        else:
            messages.error(request, 'Error updating Service Bulletin. Check the form.')
    else:
        form = ServiceBulletinForm(instance=service_bulletin)
    return render(request, 'service_bulletin_form.html', {
        'form': form,
        'service_bulletin': service_bulletin,
    })
@login_required
@user_passes_test(is_admin)
def automation_update(request):
    automation = Automation.objects.first()
    images = AutomationImage.objects.filter(automation=automation) if automation else []

    if request.method == 'POST':
        description = request.POST.get('description')
        images_files = request.FILES.getlist('images')
        image_captions = request.POST.getlist('image_captions')
        delete_images = request.POST.getlist('delete_images')

        # Update or create Automation instance
        if not automation:
            automation = Automation.objects.create(description=description)
        else:
            automation.description = description
            automation.save()

        # Handle image deletions
        for image_id in delete_images:
            try:
                image = AutomationImage.objects.get(id=image_id, automation=automation)
                if image.image and os.path.isfile(image.image.path):
                    os.remove(image.image.path)
                image.delete()
            except AutomationImage.DoesNotExist:
                pass

        # Handle new image uploads
        for image_file, caption in zip(images_files, image_captions):
            if image_file:
                AutomationImage.objects.create(
                    automation=automation,
                    image=image_file,
                    caption=caption if caption.strip() else None
                )

        messages.success(request, 'Automation updated successfully.')
        return redirect('admin_panel_app:admin_dashboard')

    return render(request, 'automation_form.html', {
        'automation': automation,
        'images': images,
    })

@login_required
@user_passes_test(is_admin)
def agromet_product_update(request):
    agromet_product = AgrometProduct.objects.first()
    if request.method == 'POST':
        form = AgrometProductForm(request.POST, request.FILES, instance=agromet_product)
        if form.is_valid():
            agromet_product = form.save() if agromet_product else AgrometProduct.objects.create(**form.cleaned_data)
            if 'delete_pdf' in request.POST and agromet_product.pdf:
                if os.path.isfile(agromet_product.pdf.path):
                    os.remove(agromet_product.pdf.path)
                agromet_product.pdf = None
                agromet_product.caption = None
                agromet_product.save()
            messages.success(request, 'Agromet Product updated successfully.')
            return redirect('admin_panel_app:admin_dashboard')
        else:
            messages.error(request, 'Error updating Agromet Product. Check the form.')
    else:
        form = AgrometProductForm(instance=agromet_product)
    return render(request, 'agromet_product_form.html', {
        'form': form,
        'agromet_product': agromet_product,
    })
    
@login_required
@user_passes_test(is_admin)
def crop_weather_calender_update(request):
    crop_weather_calender = CropWeatherCalender.objects.first()
    if request.method == 'POST':
        form = CropWeatherCalenderForm(request.POST, request.FILES, instance=crop_weather_calender)
        if form.is_valid():
            crop_weather_calender = form.save() if crop_weather_calender else CropWeatherCalender.objects.create(**form.cleaned_data)
            if 'delete_image' in request.POST and crop_weather_calender.image:
                if os.path.isfile(crop_weather_calender.image.path):
                    os.remove(crop_weather_calender.image.path)
                crop_weather_calender.image = None
                crop_weather_calender.image_caption = None
                crop_weather_calender.save()
            if 'delete_pdf' in request.POST and crop_weather_calender.pdf:
                if os.path.isfile(crop_weather_calender.pdf.path):
                    os.remove(crop_weather_calender.pdf.path)
                crop_weather_calender.pdf = None
                crop_weather_calender.save()
            messages.success(request, 'Crop Weather Calender updated successfully.')
            return redirect('admin_panel_app:admin_dashboard')
        else:
            messages.error(request, 'Error updating Crop Weather Calender. Check the form.')
    else:
        form = CropWeatherCalenderForm(instance=crop_weather_calender)
    return render(request, 'crop_weather_calender_form.html', {
        'form': form,
        'crop_weather_calender': crop_weather_calender,
    })

@login_required
@user_passes_test(is_admin)
def remote_sensing_update(request):
    remote_sensing = RemoteSensing.objects.first()
    if request.method == 'POST':
        form = RemoteSensingForm(request.POST, request.FILES, instance=remote_sensing)
        if form.is_valid():
            remote_sensing = form.save() if remote_sensing else RemoteSensing.objects.create(**form.cleaned_data)
            if 'delete_pdf' in request.POST and remote_sensing.pdf:
                if os.path.isfile(remote_sensing.pdf.path):
                    os.remove(remote_sensing.pdf.path)
                remote_sensing.pdf = None
                remote_sensing.save()
            messages.success(request, 'Remote Sensing updated successfully.')
            return redirect('admin_panel_app:admin_dashboard')
        else:
            messages.error(request, 'Error updating Remote Sensing. Check the form.')
    else:
        form = RemoteSensingForm(instance=remote_sensing)
    return render(request, 'remote_sensing_form.html', {
        'form': form,
        'remote_sensing': remote_sensing,
    })

@login_required
@user_passes_test(is_admin)
def geo_info_update(request):
    geo_info = GeoInfo.objects.first()
    if request.method == 'POST':
        form = GeoInfoForm(request.POST, request.FILES, instance=geo_info)
        if form.is_valid():
            geo_info = form.save() if geo_info else GeoInfo.objects.create(**form.cleaned_data)
            
            images = request.FILES.getlist('images')
            image_captions = request.POST.getlist('image_captions')
            for image, caption in zip(images, image_captions):
                if image:
                    GeoInfoImage.objects.create(geo_info=geo_info, image=image, caption=caption)
            
            delete_images = request.POST.getlist('delete_images')
            GeoInfoImage.objects.filter(id__in=delete_images).delete()
            
            if 'delete_pdf' in request.POST and geo_info.pdf:
                if os.path.isfile(geo_info.pdf.path):
                    os.remove(geo_info.pdf.path)
                geo_info.pdf = None
                geo_info.save()
            
            messages.success(request, 'Geo Info updated successfully.')
            return redirect('admin_panel_app:admin_dashboard')
        else:
            messages.error(request, 'Error updating Geo Info. Check the form.')
    else:
        form = GeoInfoForm(instance=geo_info)
    return render(request, 'geo_info_form.html', {
        'form': form,
        'geo_info': geo_info,
        'images': geo_info.images.all() if geo_info else [],
    })
    
@login_required
@user_passes_test(is_admin)
def pest_disease_update(request):
    pest_disease = PestDisease.objects.first()
    if request.method == 'POST':
        form = PestDiseaseForm(request.POST, request.FILES, instance=pest_disease)
        if form.is_valid():
            pest_disease = form.save() if pest_disease else PestDisease.objects.create(**form.cleaned_data)
            if 'delete_pdf' in request.POST and pest_disease.pdf:
                if os.path.isfile(pest_disease.pdf.path):
                    os.remove(pest_disease.pdf.path)
                pest_disease.pdf = None
                pest_disease.save()
            messages.success(request, 'Pest Disease updated successfully.')
            return redirect('admin_panel_app:admin_dashboard')
        else:
            messages.error(request, 'Error updating Pest Disease. Check the form.')
    else:
        form = PestDiseaseForm(instance=pest_disease)
    return render(request, 'pest_disease_form.html', {
        'form': form,
        'pest_disease': pest_disease,
    })

@login_required
@user_passes_test(is_admin)
def guidance_update(request):
    guidance = Guidance.objects.first()
    if request.method == 'POST':
        form = GuidanceForm(request.POST, request.FILES, instance=guidance)
        if form.is_valid():
            guidance = form.save() if guidance else Guidance.objects.create(**form.cleaned_data)
            if 'delete_pdf' in request.POST and guidance.pdf:
                if os.path.isfile(guidance.pdf.path):
                    os.remove(guidance.pdf.path)
                guidance.pdf = None
                guidance.save()
            messages.success(request, 'Guidance updated successfully.')
            return redirect('admin_panel_app:admin_dashboard')
        else:
            messages.error(request, 'Error updating Guidance. Check the form.')
    else:
        form = GuidanceForm(instance=guidance)
    return render(request, 'guidance_form.html', {
        'form': form,
        'guidance': guidance,
    })

@login_required
@user_passes_test(is_admin)
def agromet_adaption_update(request):
    agromet_adaption = AgrometAdaption.objects.first()
    if request.method == 'POST':
        form = AgrometAdaptionForm(request.POST, instance=agromet_adaption)
        if form.is_valid():
            agromet_adaption = form.save() if agromet_adaption else AgrometAdaption.objects.create(**form.cleaned_data)
            
            images = request.FILES.getlist('images')
            image_captions = request.POST.getlist('image_captions')
            for image, caption in zip(images, image_captions):
                if image:
                    AgrometAdaptionImage.objects.create(agromet_adaption=agromet_adaption, image=image, caption=caption)
            
            delete_images = request.POST.getlist('delete_images')
            AgrometAdaptionImage.objects.filter(id__in=delete_images).delete()
            
            messages.success(request, 'Agromet Adaption updated successfully.')
            return redirect('admin_panel_app:admin_dashboard')
        else:
            messages.error(request, 'Error updating Agromet Adaption. Check the form.')
    else:
        form = AgrometAdaptionForm(instance=agromet_adaption)
    return render(request, 'agromet_adaption_form.html', {
        'form': form,
        'agromet_adaption': agromet_adaption,
        'images': agromet_adaption.images.all() if agromet_adaption else [],
    })

@login_required
@user_passes_test(is_admin)
def weather_station_update(request):
    weather_station = WeatherStation.objects.first()
    if request.method == 'POST':
        form = WeatherStationForm(request.POST, instance=weather_station)
        if form.is_valid():
            weather_station = form.save() if weather_station else WeatherStation.objects.create(**form.cleaned_data)
            
            images = request.FILES.getlist('images')
            image_captions = request.POST.getlist('image_captions')
            for image, caption in zip(images, image_captions):
                if image:
                    WeatherStationImage.objects.create(weather_station=weather_station, image=image, caption=caption)
            
            delete_images = request.POST.getlist('delete_images')
            WeatherStationImage.objects.filter(id__in=delete_images).delete()
            
            messages.success(request, 'Weather Station updated successfully.')
            return redirect('admin_panel_app:admin_dashboard')
        else:
            messages.error(request, 'Error updating Weather Station. Check the form.')
    else:
        form = WeatherStationForm(instance=weather_station)
    return render(request, 'weather_station_form.html', {
        'form': form,
        'weather_station': weather_station,
        'images': weather_station.images.all() if weather_station else [],
    })

@login_required
@user_passes_test(is_admin)
def web_portal_update(request):
    web_portal = WebPortal.objects.first()
    if request.method == 'POST':
        form = WebPortalForm(request.POST, instance=web_portal)
        if form.is_valid():
            web_portal = form.save() if web_portal else WebPortal.objects.create(**form.cleaned_data)
            messages.success(request, 'Web Portal updated successfully.')
            return redirect('admin_panel_app:admin_dashboard')
        else:
            messages.error(request, 'Error updating Web Portal. Check the form.')
    else:
        form = WebPortalForm(instance=web_portal)
    return render(request, 'web_portal_form.html', {
        'form': form,
        'web_portal': web_portal,
    })

@login_required
@user_passes_test(is_admin)
def web_development_update(request):
    web_development = WebDevelopment.objects.first()
    if request.method == 'POST':
        form = WebDevelopmentForm(request.POST, instance=web_development)
        if form.is_valid():
            web_development = form.save() if web_development else WebDevelopment.objects.create(**form.cleaned_data)
            messages.success(request, 'Web Development updated successfully.')
            return redirect('admin_panel_app:admin_dashboard')
        else:
            messages.error(request, 'Error updating Web Development. Check the form.')
    else:
        form = WebDevelopmentForm(instance=web_development)
    return render(request, 'web_development_form.html', {
        'form': form,
        'web_development': web_development,
    })
    
@login_required
@user_passes_test(is_admin)
def ai_solution_update(request):
    ai_solution = AISolution.objects.first()
    if request.method == 'POST':
        form = AISolutionForm(request.POST, instance=ai_solution)
        if form.is_valid():
            ai_solution = form.save() if ai_solution else AISolution.objects.create(**form.cleaned_data)
            
            images = request.FILES.getlist('images')
            image_captions = request.POST.getlist('image_captions')
            for image, caption in zip(images, image_captions):
                if image:
                    AISolutionImage.objects.create(ai_solution=ai_solution, image=image, caption=caption)
            
            delete_images = request.POST.getlist('delete_images')
            for image_id in delete_images:
                try:
                    image = AISolutionImage.objects.get(id=image_id, ai_solution=ai_solution)
                    if image.image and os.path.isfile(image.image.path):
                        os.remove(image.image.path)
                    image.delete()
                except AISolutionImage.DoesNotExist:
                    pass
            
            messages.success(request, 'AI Solution updated successfully.')
            return redirect('admin_panel_app:admin_dashboard')
        else:
            messages.error(request, 'Error updating AI Solution. Check the form.')
    else:
        form = AISolutionForm(instance=ai_solution)
    return render(request, 'ai_solution_form.html', {
        'form': form,
        'ai_solution': ai_solution,
        'images': ai_solution.images.all() if ai_solution else [],
    })

@login_required
@user_passes_test(is_admin)
def it_consultancy_update(request):
    it_consultancy = ITConsultancy.objects.first()
    if request.method == 'POST':
        form = ITConsultancyForm(request.POST, instance=it_consultancy)
        if form.is_valid():
            it_consultancy = form.save() if it_consultancy else ITConsultancy.objects.create(**form.cleaned_data)
            
            images = request.FILES.getlist('images')
            image_captions = request.POST.getlist('image_captions')
            for image, caption in zip(images, image_captions):
                if image:
                    ITConsultancyImage.objects.create(it_consultancy=it_consultancy, image=image, caption=caption)
            
            delete_images = request.POST.getlist('delete_images')
            for image_id in delete_images:
                try:
                    image = ITConsultancyImage.objects.get(id=image_id, it_consultancy=it_consultancy)
                    if image.image and os.path.isfile(image.image.path):
                        os.remove(image.image.path)
                    image.delete()
                except ITConsultancyImage.DoesNotExist:
                    pass
            
            messages.success(request, 'IT Consultancy updated successfully.')
            return redirect('admin_panel_app:admin_dashboard')
        else:
            messages.error(request, 'Error updating IT Consultancy. Check the form.')
    else:
        form = ITConsultancyForm(instance=it_consultancy)
    return render(request, 'it_consultancy_form.html', {
        'form': form,
        'it_consultancy': it_consultancy,
        'images': it_consultancy.images.all() if it_consultancy else [],
    })

# New view for NewsUpdate
@login_required
@user_passes_test(is_admin)
def news_update_manage(request):
    news_updates = NewsUpdate.objects.all()
    if request.method == 'POST':
        form = NewsUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'News Update added successfully.')
            return redirect('admin_panel_app:news_update_manage')
        else:
            messages.error(request, 'Error adding News Update. Check the form.')
    else:
        form = NewsUpdateForm()
    return render(request, 'news_update_form.html', {
        'form': form,
        'news_updates': news_updates,
    })

@login_required
@user_passes_test(is_admin)
def news_update_edit(request, pk):
    news_update = get_object_or_404(NewsUpdate, pk=pk)
    if request.method == 'POST':
        form = NewsUpdateForm(request.POST, request.FILES, instance=news_update)
        if form.is_valid():
            form.save()
            messages.success(request, 'News Update updated successfully.')
            return redirect('admin_panel_app:news_update_manage')
        else:
            messages.error(request, 'Error updating News Update. Check the form.')
    else:
        form = NewsUpdateForm(instance=news_update)
    return render(request, 'news_update_form.html', {
        'form': form,
        'news_updates': NewsUpdate.objects.all(),
    })

@login_required
@user_passes_test(is_admin)
def news_update_delete(request, pk):
    news_update = get_object_or_404(NewsUpdate, pk=pk)
    if request.method == 'POST':
        if news_update.pdf and os.path.isfile(news_update.pdf.path):
            os.remove(news_update.pdf.path)
        news_update.delete()
        messages.success(request, 'News Update deleted successfully.')
        return redirect('admin_panel_app:news_update_manage')
    return render(request, 'news_update_confirm_delete.html', {'news_update': news_update})

@login_required
@user_passes_test(is_admin)
def admin_logout(request):
    logout(request)
    return redirect('admin_panel_app:admin_login')