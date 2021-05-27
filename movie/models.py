from django.db import models
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.title


class Seat(models.Model): #chỗ ngồi
    seat_name=models.CharField(max_length=10)
    seat_detail=models.CharField(max_length=200)

    def __str__(self):
        return self.seat_name

class Room(models.Model): #phòng chiếu
    room_name= models.CharField(max_length=20)
    room_detail=models.CharField(max_length=200)


    class Meta:
        verbose_name_plural = 'Room'

    def __str__(self):
        return self.room_name

class MoviePost(models.Model): #film
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


    class Meta:
        verbose_name_plural = 'MoviePost'

    def __str__(self):
        return self.name

class ShowTime(models.Model):  # Suất chiếu
    time = models.TimeField()
    movie = models.ForeignKey(MoviePost, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return str(self.time)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return str(self.fullname)

class BookMovie(models.Model): #Đặt vé
    title = models.ForeignKey(MoviePost, on_delete=models.CASCADE)
    time = models.ManyToManyField('ShowTime', blank=True)
    booked_seats = models.ManyToManyField('Seat', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.title} "




