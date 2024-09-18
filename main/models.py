import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#models.Model adalah kelas dasar yang digunakan untuk mendefinisikan model dalam Django. MoodEntry adalah nama model yang didefinisikan.
class MoodEntry(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mood = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    feelings = models.TextField()
    mood_intensity = models.IntegerField()

    #menambahkan atribut read-only
    @property 
    def is_mood_strong(self):
        return self.mood_intensity > 5