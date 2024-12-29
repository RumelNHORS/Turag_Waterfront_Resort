from django.contrib import admin
from django.urls import reverse
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from .models import (
    GalleryImage,
    AboutSection,
    CarouselItem,
    RoomFeature,
    RoomOffer,
    Blog,
    RoomFacility,
    Booking,
    Contact,
    ResortInfo,
    HomeContent,
    ServiceMeta,
)


admin.site.register(GalleryImage)
admin.site.register(AboutSection)
admin.site.register(CarouselItem)
admin.site.register(RoomFeature)
admin.site.register(RoomOffer)
admin.site.register(Blog)
admin.site.register(RoomFacility)
admin.site.register(Booking)
admin.site.register(Contact)
admin.site.register(ResortInfo)
admin.site.register(HomeContent)
admin.site.register(ServiceMeta)




# class GalleryImageAdminForm(forms.ModelForm):
#     class Meta:
#         model = GalleryImage
#         fields = '__all__'

# class AboutSectionAdminForm(forms.ModelForm):
#     content = forms.CharField(widget=CKEditorUploadingWidget())
#     class Meta:
#         model = AboutSection
#         fields = '__all__'

# class CarouselItemAdminForm(forms.ModelForm):
#     content = forms.CharField(widget=CKEditorUploadingWidget())
#     class Meta:
#         model = CarouselItem
#         fields = '__all__'

# class BlogAdminForm(forms.ModelForm):
#     content = forms.CharField(widget=CKEditorUploadingWidget())
#     class Meta:
#         model = Blog
#         fields = '__all__'

# class RoomFeatureAdminForm(forms.ModelForm):
#     class Meta:
#         model = RoomFeature
#         fields = '__all__'

# class RoomOfferAdminForm(forms.ModelForm):
#     class Meta:
#         model = RoomOffer
#         fields = '__all__'

# class RoomFacilityAdminForm(forms.ModelForm):
#     class Meta:
#         model = RoomFacility
#         fields = '__all__'

# class BookingAdminForm(forms.ModelForm):
#     class Meta:
#         model = Booking
#         fields = '__all__'

# class ContactAdminForm(forms.ModelForm):
#     class Meta:
#         model = Contact
#         fields = '__all__'

# class SocialMediaLinkAdminForm(forms.ModelForm):
#     class Meta:
#         model = ResortInfo
#         fields = '__all__'

# # Register your models with their respective Admin Forms
# @admin.register(GalleryImage)
# class GalleryImageAdmin(admin.ModelAdmin):
#     form = GalleryImageAdminForm

# @admin.register(AboutSection)
# class AboutSectionAdmin(admin.ModelAdmin):
#     form = AboutSectionAdminForm

# @admin.register(CarouselItem)
# class CarouselItemAdmin(admin.ModelAdmin):
#     form = CarouselItemAdminForm

# @admin.register(Blog)
# class BlogAdmin(admin.ModelAdmin):
#     form = BlogAdminForm

# @admin.register(RoomFeature)
# class RoomFeatureAdmin(admin.ModelAdmin):
#     form = RoomFeatureAdminForm

# @admin.register(RoomOffer)
# class RoomOfferAdmin(admin.ModelAdmin):
#     form = RoomOfferAdminForm

# @admin.register(RoomFacility)
# class RoomFacilityAdmin(admin.ModelAdmin):
#     form = RoomFacilityAdminForm

# @admin.register(Booking)
# class BookingAdmin(admin.ModelAdmin):
#     form = BookingAdminForm

# @admin.register(Contact)
# class ContactAdmin(admin.ModelAdmin):
#     form = ContactAdminForm

# @admin.register(ResortInfo)
# class SocialMediaLinkAdmin(admin.ModelAdmin):
#     form = SocialMediaLinkAdminForm


