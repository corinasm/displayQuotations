from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, Quote, Author
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
    
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'quotes/quotes.html', context)


def logout(request):
    request.session.clear()
    return redirect('/')    


def show(request, user_id):
    
    context = {
        'user': User.objects.get(id=user_id)
    }
    
    return render(request, 'users/show.html', context)    

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

    if request.session['user_id']:
        user_id = request.session['user_id']
        if request.method == "POST":

            print "hello!"
            print user_id

            result = Quote.objects.validate_contribution(request.POST)
            # resultA = Author.objects.validate_contribution(request.POST)
            if type(result) == dict:
                for tag, error_item in result.iteritems():
                    messages.error(request, error_item) 
                    print (tag, error_item)
            else:
                messages.success(request, 'You have succesfully added the new quote.') 
                return redirect('/quotes')  
            
            print " Hello Help!"

            if type(resultA) == dict:
                for tag, error_item in resultA.iteritems():
                    messages.error(request, error_item) 
                    print (tag, error_item)
            else:
                messages.success(request, 'You have succesfully added the author of the quote.') 
                return redirect('/quotes')  
                print " Hello Help! Help!"
                
        else:
            messages.error(request, 'Error. Try again!') 
            return redirect ('/quotes')


def display_quotes(request, quote_id): 
    context = {
        'quote': Quote.objects.get(id=quote_id)
        'author[0]': Author.objects.filter(quotes='quote')
        'posted_by': Quote.objects.get(id=quote_id).posted_by
    }
    return render(request, 'quotes/quotes.html', context)