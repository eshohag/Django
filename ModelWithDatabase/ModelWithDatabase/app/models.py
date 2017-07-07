"""
Definition of models.
"""

from django.db import models

# Create your won models here.
#class Artist(models.Model):                            #Here is the Class declear
#    name=models.CharField(max_length=50);              #Here is the field or Properties declear
#    year_formed=models.PositiveIntegerField();         #Here is the field or Properties declear

#class Album(models.Model):                             #Here is the Class declear
#    name=models.CharField(max_length=50);              #Here is the field or Properties declear







class Artist(models.Model):                            #Here is the Class declear
    name=models.CharField("artist",max_length=50);     #Here is the field or Properties declear
    year_formed=models.PositiveIntegerField();         #Here is the field or Properties declear


class Album(models.Model):                             #Here is the Class declear
    name=models.CharField("album",max_length=50);      #Here is the field or Properties declear    
    artist=models.ForeignKey(Artist);                  #Relation Album Class foreginkey is artist to Artist Class 