import os
import hashlib
import urllib2

from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# App specific imports
from images.image.models import Image
from images.image.base62 import base62
from images import settings

@login_required
def upload(request):
    if request.method == 'GET':
        return render_to_response('upload.html', {'url': request.GET.get('url', ''),}, context_instance=RequestContext(request))
    elif request.method == 'POST':
        if request.POST['upload_type'] == 'file':
            file = request.FILES['upload_file']
            img = Image()
            try:
                next_id = Image.objects.order_by('-id')[0].id + 1
            except IndexError:
                next_id = settings.IMAGE_ID_OFFSET + 1
            
            img.base62 = base62(next_id)
            img.filename = base62(next_id) + "." + file.name[-3:]
            img.orig_filename = file.name
            img.type = file.content_type
            img.description = '' # not implemented yet.
            img.uploader = request.user

            image_file = os.path.join(settings.MEDIA_ROOT,img.filename)
            thumbnail = os.path.join(settings.MEDIA_ROOT, 'thumbs', img.filename)
            
            md5 = hashlib.md5()
            f = open(image_file, "wb+")
            for chunk in file.chunks():
                f.write(chunk)
                md5.update(chunk)
            f.close()
            img.md5sum = md5.hexdigest()

            os.system("/usr/bin/convert %s -thumbnail 150x150 %s" % (image_file, thumbnail))
            img.save()

            return HttpResponseRedirect('/i/' + img.base62)

        elif request.POST['upload_type'] == 'url':
            remote_image = urllib2.urlopen(request.POST['upload_url'])
            md5 = hashlib.md5()
            
            data = remote_image.read()
            md5.update(data)

            img = Image()
            try:
                next_id = Image.objects.order_by('-id')[0].id + 1
            except IndexError:
                next_id = settings.IMAGE_ID_OFFSET + 1
            
            img.base62 = base62(next_id)
            img.filename = base62(next_id) + "." + request.POST['upload_url'][-3:]
            img.orig_filename = request.POST['upload_url']
            img.type = ''
            img.description = '' # not implemented yet.
            img.uploader = request.user
            img.md5sum = md5.hexdigest()

            image_file = os.path.join(settings.MEDIA_ROOT,img.filename)
            thumbnail = os.path.join(settings.MEDIA_ROOT, 'thumbs', img.filename)
            f = open(image_file, "wb+")
            f.write(data)
            f.close()
            
            img.save()
            os.system("/usr/bin/convert %s -thumbnail 150x150 %s" % (image_file, thumbnail))

            return HttpResponseRedirect('/i/' + img.base62)

@login_required
def view_image(request, id):
    return render_to_response('view_image.html', 
            {'image': Image.objects.get(base62=id)}, context_instance=RequestContext(request))

@login_required
def list_images(request, page=0):
    return render_to_response('list_images.html', 
            {'page':page, 'images': Image.objects.all()}, context_instance=RequestContext(request))

@login_required
def user_images(request, user=None):
    if user == None:
        user = request.user
    else:
        user = User.objects.get(username=user)
    
    return render_to_response('list_images.html',
            {'images': Image.objects.filter(uploader=user), }, context_instance=RequestContext(request))
