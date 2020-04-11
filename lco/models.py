from django.db import models

# Create your models here.
class Frequentlyaskquest(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=300)
    def __str__(self):
        return self.question

class TeamMember(models.Model):
    player_num = models.IntegerField(default='')
    player_image = models.ImageField(default='')
    player_f_name = models.CharField(max_length=50,default='')
    player_l_name = models.CharField(max_length=50,default='')
    player_pos = models.CharField(max_length=25,default='')
    player_height_f = models.IntegerField(default='')
    player_height_i = models.IntegerField(default='')
    player_weight = models.IntegerField(default='')
    def __str__(self):
        return self.player_f_name

class Story(models.Model):
    our_story = models.TextField()
    
class Moments(models.Model):
    gallery = models.ImageField()