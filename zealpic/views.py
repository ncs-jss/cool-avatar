from django.shortcuts import render
from django.http import Http404
from django.core.files import File

from avatar.settings import BASE_DIR
from .models import Zealicon

from allauth.socialaccount.models import SocialToken

from PIL import Image

import requests
import shutil
import os


def index(request, template_name='index.html'):
    return render(request, template_name,)


def home(request, template_name = "zeal.html"):
    if request.user.is_authenticated():
        user = request.user
        try:
            zeal_obj = Zealicon.objects.get(user_id=request.user.id)
            return render(request, template_name, {'zeal_obj': zeal_obj})
        except:
            try:
                social_token = SocialToken.objects.get(account__user__id = user.id)
                access_token = social_token.token
            except:
                pass
            parameters = {'access_token': access_token}
            r = requests.get("https://graph.facebook.com/v2.5/me/picture?width=800&height=800", params = parameters, stream=True)
            if r.status_code == 200:
                with open(request.user.username+'.jpg', 'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)
                dp = create_new_dp(request.user.username+'.jpg', request.user.id)
            else:
                return HttpResponse("Image cannot be downloaded. Try some other time.")
            return render(request, template_name, {"zeal_obj": dp})
    else:
        return HttpResponseRedirect("/")


def create_new_dp(img_path, user_id):
    import os, sys
    img = Image.open(img_path)
    size = img.size[0], img.size[1]
    infile = img.filename
    outfile = os.path.splitext(infile)[0] + ".thumbnail"
    if infile != outfile:
        try:
            frame = Image.open('static/images/cover.png')
            frame = frame.resize((size), Image.ANTIALIAS)
            img_dest = img.copy().convert('RGBA')
            img_dest.paste(frame, (0, 0, img.size[0], img.size[1]), frame)
            img_dest = img_dest.convert('RGB')
            img_dest.save(img_path)
            dp = Zealicon()
            dp.user_id = user_id
            dp.image.save(img_path, File(open(img_path, 'r')))
            dp.save()
            os.remove(img_path)
            return dp
        except IOError:
            print "cannot create thumbnail for '%s'" % infile
