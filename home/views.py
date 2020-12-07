from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import post,likes
from login.models import customuser
import cv2
from django.contrib.auth.models import User
from .forms import ImageFrom

def index(request):
    user_name=request.user
    print(user_name.username)
    posts_to_show=[]
    posts_query=post.objects.all()
    print(posts_query)
    for i in posts_query:
        owner=i.user_fk.username
        location=i.location
        caption=i.caption
        date_posted=i.date_posted
        likedby='You Jenil'+' and '+'3 others'
        image_url=i.photo.url
        current_user=i.user_fk
        current_user_profile=customuser.objects.filter(user_inher=current_user)
        user_image_url=current_user_profile[0].Image.url
        # just send 3-4 comments over here and then make another app for viewing whole full page posts
        comments=[{'name':'jenil','comment':'Wow when did you go here'},{'name':'Kenil','comment':'Take us also'}]
        quer=likes.objects.filter(post_id=i.post_id,liker_user=user_name)
        final_bool=False
        if len(quer)==0:
            final_bool=False
        else:
            final_bool=True
        print(current_user_profile)
        posts_to_show.append({'owner':owner,'location':location,'caption':caption,'date':date_posted,'likedby':likedby,'image_url':image_url,'post_id':i.post_id,'poster_image_url':user_image_url,'comments':comments,'isliked':final_bool})
        print(caption)
        
    user_details_dict={
        'name':str(user_name.username),
        'posts':posts_to_show,
    }
    return render(request,'home/home.html',user_details_dict)

@csrf_exempt
def add_like_to_post(request):
    if request.method =='POST':
        print(request.POST)
        pid=request.POST['post_liked']
        liker=request.POST['liker_name']
        post_given=post.objects.filter(post_id=pid)[0]
        # print(type(post_given[0]))
        liker=User.objects.filter(username=liker)[0]
        like_given=likes(post_id=post_given,liker_user=liker)
        like_given.save()
        return HttpResponse("recieved post")
    else:
        return HttpResponse("<h1>404 Page not found</h1>")

@csrf_exempt
def add_unlike_to_post(request):

    #just check the unliker name as in reponsive we were getting \n\n jenil \n\n just remove \n
    if request.method =='POST': 
        print(request.POST)
        pid=request.POST['post_unliked']
        unliker=request.POST['unliker_name']
        unliker=User.objects.filter(username=unliker)[0]
        post_given=post.objects.filter(post_id=pid)[0]
        remove_like=likes.objects.filter(liker_user=unliker,post_id=post_given)[0]
        remove_like.delete()
        print("post unliked")
        return HttpResponse("recieved post")
    else:
        return HttpResponse("<h1>404 Page not found</h1>")

@csrf_exempt
def comment(request):
    json_data={'comments':[
        {'name':'user_1','comment':'jenil is a boy'},
        {'name':'user_1','comment':'jenil is a boy'},
        {'name':'user_1','comment':'jenil is a boy'},
        {'name':'user_1','comment':'jenil is a boy'},
        
    ]}
    print(request.POST)
    return JsonResponse(json_data)
def search(request):
    #let us consider that the search user 
    json_data={
        'users':[
            {
                'name':'Jenik Vekariya',
                'photo':'https://source.unsplash.com/1600x900/?nature,mountain',
                'occupation':'SDE at Google'
            },
            {
                'name':'Harshvardhan Sharma',
                'photo':'https://source.unsplash.com/1600x900/?nature,water',
                'occupation':'SDE at Amazon'
            }
        ]
    }
    return JsonResponse(json_data)


@csrf_exempt
def add_comment(request):
    if request.method=='GET':
        return HttpResponse("<h1>404 Page Not Found</h1>")
    else:
        print(request.POST)
        return HttpResponse("comment added")

def profile(request):
    return render(request,'home/profile_base.html')


def add_post(request):
    if request.method=='POST':
        form=ImageFrom(request.POST,request.FILES)
        # print(form.errors())
        if form.is_valid():
            print(form.cleaned_data['Caption'])
            print(form.cleaned_data['Image'])
        else:
            print("invalid")
        return HttpResponse("YAY")
        img=request.method.POST['img']

    else:
        form=ImageFrom()
    return render(request,'home/add_post_1.html',{'form':form})



