import urllib.request

import pyrebase

firebaseConfig = {

  'apiKey': "AIzaSyBzNZlMtHKE_pRILf_y9Edi2cQc7a6ocsM",

  'authDomain': "fir-course-4a47b.firebaseapp.com",

  'projectId': "fir-course-4a47b",

  'storageBucket': "fir-course-4a47b.appspot.com",

  'messagingSenderId': "636092634333",

  'databaseURL': "https://fir-course-4a47b-default-rtdb.firebaseio.com",

  'appId': "1:636092634333:web:c66c9a0b6e659ace757734",

  'measurementId': "G-W9EY705K9C"

};
firebase = pyrebase.initialize_app(firebaseConfig)
#
# auth = firebase.auth()
# storage = firebase.storage()
db = firebase.database()

# Login
# email = input("Enter your email")
# password = input("Enter your password")
#
# try:
#   auth.sign_in_with_email_and_password(email, password)
#   print("Successfully logged in")
# except:
#   print("Invalid")

#Signup
# email = input("Enter your email")
# password = input("Enter your password")
# confirmpass = input("Confirm you password")
# if password == confirmpass:
#   try:
#     auth.create_user_with_email_and_password(email,password)
#     print("Success")
#   except:
#     print("Email already exists")

#storage
# upload
# filename = input("Enter name of file to upload ")
# cloudfilename = input("Enter the name of the file on the cloud ")
# storage.child(cloudfilename).put(filename)
#
# print(storage.child(cloudfilename).get_url(None))

#download
# cloudfilename = input("enter the name of the file you want to download ")
# storage.child(cloudfilename).download("", "download.txt")
# url = storage.child(cloudfilename).get_url(None)
# f = urllib.request.urlopen(url).read()
# print(f)

#database
data = {'username':'Soomimasen', 'user_id':'3213213219', 'Count': 1, 'admin':True}
users = db.child("users").get()
for user in users.each():
  if user.val()['username'] == 'Soomimasen':
    db.child("users").child(user.key()).update({'Count': 2})

#delete
db.child("users").child(user.key()).child("admin").remove()

