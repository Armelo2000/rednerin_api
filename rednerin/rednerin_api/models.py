from django.db import models

# Create your models here.
#from django.contrib.postgres.fields import ArrayField

class Rednerin(models.Model):

    class Partition(models.IntegerChoices):
        BASIS = 1
        PREMIUM = 2
        COMPANY = 3
    
    """ Alternative

        partition = {
        'Basis': 1,
        'Premium': 2,
        'Company': 3
    }
    
    """
    #rednerin_Id = models.BigAutoField(primary_key=True, db_column='rednerin_Id')
    #info = models.OneToOneField("RednerinInfo", on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    street = models.CharField(max_length=100, blank=True)
    houseNr = models.CharField(max_length=10, blank=True)
    zipCode = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=25, blank=True)
    phonePublish = models.BooleanField(default=False)
    option = models.IntegerField(choices=Partition.choices, default=Partition.BASIS)

    image = models.ImageField(upload_to='images/', default=None, null=True, blank=True)
    #Datenschutz
    policy = models.BooleanField(default=False)

    def __str__(self):
        return self.firstname + ' ' + self.lastname


class RednerinInfo(models.Model):

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
    subject = models.ManyToManyField('Subject', blank=True, related_name='subject')
    rednerin_Id = models.OneToOneField(Rednerin, related_name='information', on_delete=models.CASCADE)
    

    def __str__(self):
        return str(self.rednerin_Id)


class Subject(models.Model):
    subjectname = models.CharField(max_length=50, blank=True)
    #rednerinInfo = models.ForeignKey(RednerinInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.subjectname


class Url(models.Model):
    urlLink = models.CharField(max_length=100)
    rednerinInfo = models.ForeignKey(RednerinInfo, related_name='url', on_delete=models.CASCADE)

    def __str__(self):
        return self.urlLink

class SocialNetwork(models.Model):
    socialNetworkName = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='icons/', default=None, null=True, blank=True)
    rednerinInfo = models.ForeignKey(RednerinInfo, related_name='socialnetwork', on_delete=models.CASCADE)

    def __str__(self):
        return self.socialNetworkName


class Video(models.Model):
        caption = models.CharField(max_length=50)
        video = models.FileField(upload_to='videos_uploaded/', null=True) #allowed_extensions=['MOV','avi','mp4','webm','mkv'])
        rednerinInfo = models.ForeignKey(RednerinInfo, related_name='video', on_delete=models.CASCADE)

        def __str__(self):
            return self.caption
