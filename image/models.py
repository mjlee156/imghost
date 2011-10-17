from django.db import models

class Image(models.Model):
    id = models.IntegerField(primary_key=True)
    base62 = models.CharField(unique=True, max_length=48)
    filename = models.CharField(max_length=36)
    orig_filename = models.CharField(max_length=765, blank=True)
    type = models.CharField(max_length=192, null=True, blank=True)
    md5sum = models.CharField(unique=True, max_length=96, blank=True)
    description = models.CharField(max_length=765, null=True, blank=True)
    date_added = models.CharField(max_length=765)
    uploader = models.ForeignKey('auth.User', blank=True, null=True)
    
    def __unicode__(self):
            return self.filename

    def delete(*args, **kwargs):
            super(Image, self).delete(*args, **kwargs)
            # todo delete file when model is deleted
    

    class Meta:
        db_table = u'images'

