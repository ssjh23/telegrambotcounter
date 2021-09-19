import pyrebase
import fbaseConfig

firebaseConfig = fbaseConfig.firebaseConfig
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
route_data = db.child("Route_Data").get()
route_list = None
for data in route_data.each():
    if data.key() == 'Route_List':
        route_list = data.val()
print(route_list)