from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, Quote
import bcrypt

#============================================================#
#                       RENDER METHODS                       #
#============================================================#

def index(request):
    return render (request, 'quotes/index.html')


def quotes(request):
    try: 
        request.session['user_id']
    except KeyError:
        return redirect('/')  

    user = User.objects.get(id=request.session['user_id'])

    other_quotes = Quote.objects.exclude(id__in=user.favorites.all()) 

    context = {
        'user': user,
        'quotes': other_quotes
    }
    return render(request, 'quotes/quotes.html', context)



def logout(request):
    request.session.clear()
    return redirect('/')    


def show(request, user_id):
    
    user = User.objects.get(id=user_id)
    quotes=Quote.objects.filter(posted_by=user_id)

    context = {
        'user': user,
        'quotes': quotes, 
        'count': len(quotes)

    }
    
    return render(request, 'quotes/show.html', context)    



#============================================================#
#                      PROCESS METHODS                       #
#============================================================#


#New User Validation & Registration 
def registration (request):
    # Register a new user 
    if request.method == "POST":

        result = User.objects.validate_registration(request.POST)
        if type(result) == dict:
            for tag, error_item in result.iteritems():
                messages.error(request, error_item) 
                #print (tag, error_item)

        else:
            request.session['user_id'] = result.id 
            messages.success(request, 'You have succesfully registered.') 
            return redirect('/quotes')  
 
    return redirect ('/')

def login(request):   

    if request.method == "POST":

        result = User.objects.validate_login(request.POST)
        if type(result) == dict:
            for tag, error_item in result.iteritems():
                messages.error(request, error_item) 
                #print (tag, error_item)

        else:
            request.session['user_id'] = result.id 
            messages.success(request, 'You have succesfully logged in.') 
            return redirect('/quotes')  
 
    return redirect ('/')


def contribute(request):   

        user_id = request.session['user_id']

        if request.method == "POST":

            result = Quote.objects.validate_contribution(request.POST)

            if type(result) == dict:
                for tag, error_item in result.iteritems():
                    messages.error(request, error_item) 
                    print (tag, error_item)
            else:
                messages.success(request, 'You have succesfully added the new quote.')       
        else:
            messages.error(request, 'Error. Try again!') 

        return redirect ('/quotes')



def addToFavs(request, quote_id):

    user_id = request.session['user_id']
    user=User.objects.get(id=user_id)
    favorite = Quote.objects.get(id=quote_id)
    user.favorites.add(favorite)

    return redirect ('/quotes')


def removeFromFavs(request, quote_id):

    user_id = request.session['user_id']
    user=User.objects.get(id=user_id)
    favorite = Quote.objects.get(id=quote_id)
    user.favorites.remove(favorite)

    return redirect ('/quotes')