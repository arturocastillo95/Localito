from django import forms
from restaurants.models import Restaurant
from PIL import Image, ImageOps
from django.core.files import File

class RestaurantInfoForm(forms.ModelForm):
    name = forms.CharField(label="Nombre de tienda", widget=forms.TextInput(attrs={'class':'input'}))
    address = forms.CharField(label="Dirección", widget=forms.TextInput(attrs={'class':'input'}))
    image = forms.ImageField(label="", widget=forms.FileInput(attrs={'class':'file-input-hidden'}),allow_empty_file=True, required=False)
    
    x = forms.FloatField(label="", widget=forms.HiddenInput(),required=False)
    y = forms.FloatField(label="",  widget=forms.HiddenInput(),required=False)
    height = forms.FloatField(label="",  widget=forms.HiddenInput(),required=False)
    width = forms.FloatField(label="", widget=forms.HiddenInput(),required=False)
    
    class Meta:
        model = Restaurant
        fields = ['image', 'x', 'y', 'height', 'width', 'name', 'address']
    
    def save(self):
        photo = super(RestaurantInfoForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        height = self.cleaned_data.get('height')
        width = self.cleaned_data.get('width')

        try:
            image = Image.open(photo.image)
            
            # Fix image orientation
            image = ImageOps.exif_transpose(image)

            cropped_image = image.crop((x, y, width+x, height+y))
            resized_image = cropped_image.resize((250,250), Image.ANTIALIAS)
            resized_image.save(photo.image.path)
            return photo
        except:
            return photo