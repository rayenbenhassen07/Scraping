from django.contrib import messages

from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect,get_object_or_404
from .models import websites

#admin authentication
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User

import subprocess

# Create your views here.






def admin_login(request):
    try:
        if request.user.is_authenticated:
            return redirect('/')
        
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            if not user_obj.exists():
                messages.info(request, 'User not found')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
            user_obj = authenticate(username=username, password=password)

            if user_obj and user_obj.is_superuser:
                login(request, user_obj)
                return redirect('/')
            
            messages.info(request, 'Invalid Credentials')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        return render(request, 'login.html')
            
    except Exception as e:
        print(e)

def admin_logout(request):
    logout(request)
    return redirect('/login/')  # Ensure this URL is correct

def dashboard(request):
    website = websites.objects.all()
    return render(request, 'dashboard.html', {"website": website})

def add_website(request):

    if request.method == 'POST':
        store_type = request.POST.get('store_type')
        store_title = request.POST.get('store_title')
        store_logo = request.POST.get('store_logo')
        store_url = request.POST.get('store_url')
        title_tag = request.POST.get('title_tag')
        title_class = request.POST.get('title_class')
        title_content = request.POST.get('title_content')
        price_tag = request.POST.get('price_tag')
        price_class = request.POST.get('price_class')
        price_content = request.POST.get('price_content')
        availability_tag = request.POST.get('availability_tag')
        availability_class = request.POST.get('availability_class')
        availability_content = request.POST.get('availability_content')
        sku_tag = request.POST.get('sku_tag')
        sku_class = request.POST.get('sku_class')
        sku_content = request.POST.get('sku_content')
        ratings_tag = request.POST.get('ratings_tag')
        ratings_class = request.POST.get('ratings_class')
        ratings_content = request.POST.get('ratings_content')
        nbr_ratings_tag = request.POST.get('nbr_ratings_tag')
        nbr_ratings_class = request.POST.get('nbr_ratings_class')
        nbr_ratings_content = request.POST.get('nbr_ratings_content')
        delivry_price = request.POST.get('delivry_price')
        offre = request.POST.get('offre')
        sitemap = request.POST.get('sitemap')

        website = websites(
            store_type=store_type,
            store_title=store_title,
            store_logo=store_logo,
            store_url=store_url,
            title_tag=title_tag,
            title_class=title_class,
            title_content=title_content,
            price_tag=price_tag,
            price_class=price_class,
            price_content=price_content,
            availability_tag=availability_tag,
            availability_class=availability_class,
            availability_content=availability_content,
            sku_tag=sku_tag,
            sku_class=sku_class,
            sku_content=sku_content,
            ratings_tag=ratings_tag,
            ratings_class=ratings_class,
            ratings_content=ratings_content,
            nbr_ratings_tag=nbr_ratings_tag,
            nbr_ratings_class=nbr_ratings_class,
            nbr_ratings_content=nbr_ratings_content,
            delivry_price=delivry_price,
            offre=offre,
            sitemap=sitemap
        )
        
        website.save()
        return redirect('/')
    else:
        return render(request, 'add_website.html')
    
def delete_website(request, id):
    website = get_object_or_404(websites, id=id)
    website.delete()
    return redirect('/')

def edit_website(request, id):
    website = get_object_or_404(websites, id=id)
    if request.method == 'POST':
        website.store_type = request.POST.get('store_type')
        website.store_title = request.POST.get('store_title')
        website.store_logo = request.POST.get('store_logo')
        website.store_url = request.POST.get('store_url')
        website.title_tag = request.POST.get('title_tag')
        website.title_class = request.POST.get('title_class')
        website.title_content = request.POST.get('title_content')
        website.price_tag = request.POST.get('price_tag')
        website.price_class = request.POST.get('price_class')
        website.price_content = request.POST.get('price_content')
        website.availability_tag = request.POST.get('availability_tag')
        website.availability_class = request.POST.get('availability_class')
        website.availability_content = request.POST.get('availability_content')
        website.sku_tag = request.POST.get('sku_tag')
        website.sku_class = request.POST.get('sku_class')
        website.sku_content = request.POST.get('sku_content')
        website.ratings_tag = request.POST.get('ratings_tag')
        website.ratings_class = request.POST.get('ratings_class')
        website.ratings_content = request.POST.get('ratings_content')
        website.nbr_ratings_tag = request.POST.get('nbr_ratings_tag')
        website.nbr_ratings_class = request.POST.get('nbr_ratings_class')
        website.nbr_ratings_content = request.POST.get('nbr_ratings_content')
        website.delivry_price = request.POST.get('delivry_price')
        website.offre = request.POST.get('offre')
        website.sitemap = request.POST.get('sitemap')


        website.save()
        return redirect('/')
    else:
        return render(request, 'edit_website.html', {'website': website})
    

def run_website(request, id):
    website = get_object_or_404(websites, id=id)
    try:
        
        result = subprocess.run(
                    [
                        "python3",
                        "scrapingWordpress.py",
                        website.store_title,
                        website.store_logo,
                        website.store_url,
                        website.title_tag,
                        website.title_class,
                        website.title_content,
                        website.price_tag,
                        website.price_class,
                        website.price_content,
                        website.availability_tag,
                        website.availability_class,
                        website.availability_content,
                        website.sku_tag,
                        website.sku_class,
                        website.sku_content,
                        website.ratings_tag,
                        website.ratings_class,
                        website.ratings_content,
                        website.nbr_ratings_tag,
                        website.nbr_ratings_class,
                        website.nbr_ratings_content,
                        website.delivry_price,
                        website.offre,
                        website.sitemap,
                    ],
                    capture_output=True,
                    text=True,
                )
                # Check if the script ran successfully
        if result.returncode == 0:
            return HttpResponse("Script executed successfully")
        else:
            return HttpResponse(f"Script execution failed: {result.stderr}")
        
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}")




    print(website.store_title)
    return redirect('/')