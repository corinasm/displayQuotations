from __future__ import unicode_literals
from django.db import models
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
 
class UserManager(models.Manager):
    def validate_registration(self, postData):
        errors = {}
        
        try:
            first_name = postData['first_name']
            last_name = postData['last_name']
            email = postData['email'].lower()
            password = postData['password']
            cpassword = postData['cpassword']


            if len(first_name) < 2:
                errors['inFirstName'] = 'First Name is too short; minimum 2 characters are required!'

            if len(last_name) < 2: 
                errors['inLastName'] = 'Last Name is too short; minimum 2 characters are required!'

            if len(email) < 1: 
                errors['inEPLength'] = 'Email is required!'
            elif not EMAIL_REGEX.match(email):
                errors['inEmail'] = 'Invalid email address!' 
            
            if len(password) < 8:
                errors['inPassword'] = "Pasword must be minimum 8 characters long!"  
            elif password != cpassword:
                errors['inCPassword'] = 'Passwords do not match!'    

            if not errors:
                if User.objects.filter(email=email).exists():
                    errors['user_found'] = 'User already exists'
                else:
                    # if no errors and new user, add user to the database
     
                    hashpass = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

                    user = User()
                    user.first_name = first_name
                    user.last_name = last_name
                    user.email = email
                    user.password = hashpass
                    user.save()

                    return user

        except:
            errors['userInput'] = 'An error has occured. Please fill the form again.'

        return errors    

    def validate_login(self, postData):
        errors = {}

        try:
            email = postData['email']
            password = postData['password']

            crt_user=User.objects.filter(email=email)
            if len(crt_user) == 1: # because crt_user is a list with 1 element 
                hashpassdb = crt_user[0].password
                print "hashpassdb:", hashpassdb
                if bcrypt.checkpw(password.encode(), hashpassdb.encode()):
                    return crt_user[0]
                else:
                    error['login'] = 'Email or password not valid '
                
            else:
                error['emailInp'] = 'Wrong email or password'
        
        except: 
            errors['userInput'] = 'An error has occured. Please try again.'
        
        return errors        

class QuoteManager(models.Manager):            
    def validate_contribution(self, postData):
        errors = {}
        
        try:
            author_name = postData['author_name']
            message = postData['message']
  
            if len(author) < 3:
                errors['inAuthName'] = 'Author Name too short; minimum 3 characters are required!'

            if len(last_name) < 10: 
                errors['inQMessage'] = ' A quote must be minimum 10 characters!'

            if not errors:

                quote=Quote()
                quote.message = message
                quote.posted_by = User.objects.get(id=user_id)
                quote.save()
                
                
                author= Author()
                author_name = author_name
                author.save()

                print 'My quote is:'
                print messsage

            return quote

        except:
            errors['userInput'] = 'An error has occured. Please add the quote again.'

        return errors   

class User(models.Model):
    first_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True) 
    objects = UserManager()        
    def __str__(self):
        return self.email 


class Author(models.Model):
    author_name = models.CharField(max_length=255) 
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True) 
    objects = UserManager()  
    def __str__(self):
        return self.name 

class Quote(models.Model):
    message = models.TextField() 
    author= models.ForeignKey(Author, related_name="quotes")
    posted_by = models.ForeignKey(User, related_name="users")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True) 
    objects = UserManager()  
    def __str__(self):
        return self.content                
         
'''
class FavQuote(models.Model): 
    fav_quote = models.ManyToManyField     
'''    