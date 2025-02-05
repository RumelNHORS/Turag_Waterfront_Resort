from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from .models import GalleryImage, AboutSection, CarouselItem, RoomFeature, RoomOffer, Blog, ResortInfo, HomeContent, ServiceMeta, HomeMeta, BlogMeta
from .forms import ContactForm, BookingForm
from django.views import View



def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('index')
    else:
        form = ContactForm()

    # Fetch the meta data for the home page
    meta_data = HomeMeta.objects.first()    

    # Collect data for the template
    gallery_images = GalleryImage.objects.all()
    about_section = AboutSection.objects.first()
    carousel_items = CarouselItem.objects.all()
    room_features = RoomFeature.objects.all()
    room_offers = RoomOffer.objects.all()
    blog_posts = Blog.objects.all().order_by('-created_at')
    social_media_info = ResortInfo.objects.first()
    content = HomeContent.objects.first()

    # Render the template with the collected data
    return render(request, 'index.html', {
        'form': form,
        'gallery_images': gallery_images,
        'about_section': about_section,
        'carousel_items': carousel_items,
        'room_features': room_features,
        'room_offers': room_offers,
        'blog_posts': blog_posts,
        'social_media_info': social_media_info,
        'content': content,

        'meta_title': meta_data.title if meta_data else 'Turag Water Front Resort',
        'meta_keywords': meta_data.keywords if meta_data else 'Keywords',
        'meta_description': meta_data.description if meta_data else 'Meta Description',

    })




def about(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('index')
    else:
        form = ContactForm()
    
    about_section = AboutSection.objects.first()
    social_media_info = ResortInfo.objects.first() 
    return render(request, 'about.html', {
        'form': form,
        'about_section': about_section,
        'social_media_info': social_media_info,
    })


def services(request):
    # Assuming you have a model for services
    room_offers = RoomOffer.objects.all()
    room_features = RoomFeature.objects.all()
    social_media_info = ResortInfo.objects.first() 

    # Fetch the meta data for the services page
    meta_data = ServiceMeta.objects.first() 
    
    return render(request, 'services.html', {
        'room_offers': room_offers,
        'room_features': room_features,
        'social_media_info': social_media_info,

        # Pass the meta data to the template
        'meta_title': meta_data.title if meta_data else 'Turag Water Front Resort',
        'meta_keywords': meta_data.keywords if meta_data else 'Keywords',
        'meta_description': meta_data.description if meta_data else 'Meta Description',
    })

def gallery(request):
    gallery_images = GalleryImage.objects.all()
    social_media_info = ResortInfo.objects.first() 
    return render(request, 'gallery.html', {
        'gallery_images': gallery_images,
        'social_media_info': social_media_info,
    })

def blog(request):
    blog_posts = Blog.objects.all().order_by('-created_at')
    social_media_info = ResortInfo.objects.first()
    # Fetch the meta data for the blog page
    meta_data = BlogMeta.objects.first()

    return render(request, 'blog.html', {
        'blog_posts': blog_posts,
        'social_media_info': social_media_info,

        # Pass the meta data to the template
        'meta_title': meta_data.title if meta_data else 'Turag Water Front Resort',
        'meta_keywords': meta_data.keywords if meta_data else 'Keywords',
        'meta_description': meta_data.description if meta_data else 'Meta Description',
    })


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('contact')  # Redirect to a new URL after POST
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})




class RoomDetailView(DetailView):
    model = RoomOffer
    template_name = 'room_detail.html'
    context_object_name = 'room'
    social_media_info = ResortInfo.objects.first() 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_rooms'] = RoomOffer.objects.exclude(id=self.object.id)
        context['social_media_info'] = ResortInfo.objects.first() 
        return context
    
    

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    context_object_name = 'blog_post'

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Blog, slug=slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['other_blogs'] = Blog.objects.exclude(id=self.object.id)[:5]
        context['social_media_info'] = ResortInfo.objects.first()

        # Fetch dynamic meta tags for the blog detail page
        meta_data = BlogMeta.objects.first()
        context['meta_title'] = meta_data.title if meta_data else 'Turag Water Front Resort'
        context['meta_keywords'] = meta_data.keywords if meta_data else 'Keywords'
        context['meta_description'] = meta_data.description if meta_data else 'Meta Description'

        return context
    

class BookingCreateView(View):
    def get(self, request, room_id):
        room = get_object_or_404(RoomOffer, id=room_id)
        form = BookingForm(initial={'room': room})
        return render(request, 'room_detail.html', {'form': form, 'room': room})

    def post(self, request, room_id):
        room = get_object_or_404(RoomOffer, id=room_id)
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.room = room
            booking.save()
            return redirect('booking_success')  # Redirect to a success page or another page of your choice
        return render(request, 'room_detail.html', {'form': form, 'room': room})