from django.db import models

# Create your models here.
#from django.contrib.postgres.fields import ArrayField

class Contact(models.Model):
    street = models.CharField(max_length=100, blank=True)
    houseNr = models.CharField(max_length=10, blank=True)
    zipCode = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return f'{self.street} {self.houseNr}'

class SpeacherInfo(models.Model):

    #language = ArrayField(models.CharField(max_length=200), blank=True)
    language = models.CharField(max_length=500, blank=True)
    profession = models.CharField(max_length=100, blank=True)
    reference = models.TextField(max_length=500, blank=True)
    publication = models.TextField(max_length=500, blank=True)
    contactdetail = models.TextField(max_length=500, blank=True)
    contactform = models.TextField(max_length=500, blank=True)
    exampleLecture = models.TextField(max_length=500, blank=True)
    shortBiography = models.TextField(max_length=500, blank=True)
    longBiography = models.TextField(max_length=5000, blank=True)
    #subject = models.ManyToManyField('Subject', blank=True, related_name='subject')
    #rednerin_Id = models.OneToOneField(Rednerin, related_name='information', on_delete=models.CASCADE)

    def __str__(self):
        return self.profession

#Rednerin Tabelle
class Speacher(models.Model):
    BASIS = "BA"
    PREMIUM = "PR"
    COMPANY = "CO"
 
    ACCOUNT_TYP_CHOICES = [
        (BASIS, "Basis"),
        (PREMIUM, "Premium"),
        (COMPANY, "Company"),
    ]
    
    #rednerin_Id = models.BigAutoField(primary_key=True, db_column='rednerin_Id')
    #info = models.OneToOneField("RednerinInfo", on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phonePublish = models.BooleanField(default=False)
    accountType = models.CharField(
        max_length=2, 
        choices=ACCOUNT_TYP_CHOICES, 
        default=BASIS)

    #Datenschutz
    policy = models.BooleanField(default=False)
    info = models.OneToOneField(SpeacherInfo, on_delete=models.CASCADE)
    contact = models.OneToOneField("Contact", on_delete=models.CASCADE)
    subject = models.ManyToManyField('Subject', blank=True, related_name='subject')

    def __str__(self):
        return self.firstname + ' ' + self.lastname


class Subject(models.Model):
    subjectname = models.CharField(max_length=50, blank=True)
    #rednerinInfo = models.ForeignKey(RednerinInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.subjectname


class Url(models.Model):
    urlLink = models.URLField('url')
    speacher = models.ForeignKey(Speacher, related_name='url', on_delete=models.CASCADE)

    def __str__(self):
        return self.urlLink

class SocialNetwork(models.Model):
    socialNetworkName = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='icons/', default=None, null=True, blank=True)
    speacher = models.ForeignKey(Speacher, related_name='socialnetwork', on_delete=models.CASCADE)

    def __str__(self):
        return self.socialNetworkName

class Photo(models.Model):
        caption = models.CharField(max_length=50)
        photo = models.ImageField(upload_to='photos_uploaded/', null=True) #allowed_extensions=['MOV','avi','mp4','webm','mkv'])
        speacher = models.ForeignKey(Speacher, related_name='photo', on_delete=models.CASCADE)

        def __str__(self):
            return self.caption

class Video(models.Model):
        caption = models.CharField(max_length=50)
        video = models.FileField(upload_to='videos_uploaded/', null=True) #allowed_extensions=['MOV','avi','mp4','webm','mkv'])
        speacher = models.ForeignKey(Speacher, related_name='video', on_delete=models.CASCADE)

        def __str__(self):
            return self.caption


