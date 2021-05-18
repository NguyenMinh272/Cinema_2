from django.db import models
from embed_video.fields import EmbedVideoField

class Category(models.Model):
    title = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.title

class ShowTime(models.Model):
    time = models.TimeField()

    def __str__(self):
        return str(self.time)

class MoviePost(models.Model):
    lang_choice = (
        ('Anh', 'English'),
        ('Việt', 'VietNam'),

    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='')
    detail = models.TextField(default='')
    cast = models.CharField(max_length=100)
    director = models.CharField(max_length=20)
    language = models.CharField(max_length=10, choices=lang_choice)
    public_date = models.DateField()
    run_length = models.IntegerField(help_text="Enter run length in minutes")
    trailer = EmbedVideoField()
    image = models.ImageField(null=True, blank=True, upload_to='media')
    time = models.ManyToManyField(ShowTime)

    class Meta:
        verbose_name_plural = 'MoviePost'

    def __str__(self):
        return self.name

class bookmovie(models.Model):
    name = models.ForeignKey(MoviePost, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.ManyToManyField('ShowTime', blank=True)
    booked_seats = models.ManyToManyField('Seat', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name} ({self.price})"


class Seat(models.Model):
    seat_no=models.IntegerField()
    occupant_first_name=models.CharField(max_length=255)
    occupant_last_name=models.CharField(max_length=255)
    occupant_email=models.EmailField(max_length=555)
    purchase_time=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.occupant_first_name}-{self.occupant_last_name} seat_no {self.seat_no}"
