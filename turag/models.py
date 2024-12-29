from django.db import models
from django.utils.timezone import now



class HomeContent(models.Model):
    title = models.CharField(max_length=255, default="Turag Waterfront Resort")
    heading = models.CharField(max_length=255, default="Make Memories")
    subheading = models.CharField(max_length=255, default="Discover the place where you have fun & enjoy a lot")

    def __str__(self):
        return self.title
        

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    alt_text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.alt_text or 'Gallery Image'
    

class AboutSection(models.Model):
    heading = models.CharField(max_length=255, help_text="Heading of the About Us section")
    content = models.TextField(help_text="Main content of the About Us section")
    image = models.ImageField(upload_to='about/', help_text="Image for the About Us section")

    def __str__(self):
        return self.heading
    

class CarouselItem(models.Model):
    title = models.CharField(max_length=255, help_text="Title of the carousel item")
    content = models.TextField(help_text="Content of the carousel item")
    image = models.ImageField(upload_to='carousel/', help_text="Image for the carousel item")

    def __str__(self):
        return self.title
    



class RoomFeature(models.Model):
    icon = models.CharField(max_length=255, help_text="Icon class for FontAwesome")
    description = models.CharField(max_length=255, help_text="Short description for the feature")
    title = models.CharField(max_length=255, help_text="Title for the feature")

    def __str__(self):
        return self.title



class RoomOffer(models.Model):
    room_type = models.CharField(max_length=255, help_text="Type of the room")
    room_number = models.CharField(max_length=50, help_text="Room number associated with the offer")
    cost = models.DecimalField(max_digits=10, decimal_places=2, help_text="Cost per night")
    short_description = models.TextField(help_text="Short description of the offer")
    image = models.ImageField(upload_to='room/', help_text="Image for the offer")

    def __str__(self):
        return f"{self.room_type} - {self.room_number} - ${self.cost}"
    

class RoomFacility(models.Model):
    room_offer = models.ForeignKey(RoomOffer, on_delete=models.CASCADE, related_name='facilities')
    facility_name = models.CharField(max_length=255, help_text="Name of the facility")

    def __str__(self):
        return f"{self.facility_name} for {self.room_offer.room_type} - {self.room_offer.room_number}"

    

class Blog(models.Model):
    blog_title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog_title
    


class Booking(models.Model):
    name = models.CharField(max_length=255, help_text="Name of the person making the booking")
    email = models.EmailField(help_text="Email address of the person making the booking")
    phone = models.CharField(max_length=20, help_text="Phone number of the person making the booking")
    room = models.ForeignKey('RoomOffer', on_delete=models.CASCADE, help_text="Room associated with the booking")
    adult = models.PositiveIntegerField(help_text="Number of adults")
    children = models.PositiveIntegerField(help_text="Number of children")
    checkin = models.DateField(help_text="Check-in date")
    checkout = models.DateField(help_text="Check-out date")
    have_to_pay = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text="Amount that needs to be paid")

    def __str__(self):
        return f"Booking by {self.name} for {self.room}"
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


# class SocialMedia(models.Model):
#     logo = models.ImageField(upload_to='logos/', help_text='Upload the resort logo')
#     description = models.TextField(help_text='Resort description')
#     facebook_link = models.URLField(blank=True, help_text='Facebook profile link')
#     instagram_link = models.URLField(blank=True, help_text='Instagram profile link')
#     youtube_link = models.URLField(blank=True, help_text='YouTube channel link')
#     whatsapp_link = models.URLField(blank=True, help_text='WhatsApp link')
#     twitter_link = models.URLField(blank=True, help_text='Twitter profile link')
#     pinterest_link = models.URLField(blank=True, help_text='Pinterest profile link')
#     tiktok_link = models.URLField(blank=True, help_text='TikTok profile link')
#     address = models.CharField(max_length=255, help_text='Resort address')
#     phone_number = models.CharField(max_length=20, blank=True, help_text='Resort phone number')
#     email = models.EmailField(help_text='Resort email address') 

#     def __str__(self):
#         return "Social Media Links and Info"

    # class Meta:
    #     verbose_name = "Social Media Link and Info"
    #     verbose_name_plural = "Social Media Links and Info"



class ResortInfo(models.Model):
    logo = models.ImageField(upload_to='logos/', help_text='Upload the resort logo.')
    description = models.TextField(help_text='A brief description of the resort.')
    facebook_link = models.URLField(blank=True, help_text='Link to the resort’s Facebook page.')
    instagram_link = models.URLField(blank=True, help_text='Link to the resort’s Instagram profile.')
    youtube_link = models.URLField(blank=True, help_text='Link to the resort’s YouTube channel.')
    whatsapp_link = models.URLField(blank=True, help_text='Link to the resort’s WhatsApp contact.')
    twitter_link = models.URLField(blank=True, help_text='Link to the resort’s Twitter profile.')
    pinterest_link = models.URLField(blank=True, help_text='Link to the resort’s Pinterest page.')
    tiktok_link = models.URLField(blank=True, help_text='Link to the resort’s TikTok profile.')
    address = models.CharField(max_length=255, help_text='Resort address.')
    phone_number = models.CharField(max_length=40, blank=True, help_text='Resort phone number.')
    email = models.EmailField(help_text='Resort email address.')

    def __str__(self):
        return f"{self.address} - Contact Info"

    class Meta:
        verbose_name = "Resort Information"
        verbose_name_plural = "Resort Information"


# Meta class for SEO for the Services page
class ServiceMeta(models.Model):
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title
    

# Models for SEO for the Home page
class HomeMeta(models.Model):
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now)

    def save(self, *args, **kwargs):
        self.updated_at = now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


# Models for SEO for the Blog page 
class BlogMeta(models.Model):
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now)

    def save(self, *args, **kwargs):
        self.updated_at = now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

