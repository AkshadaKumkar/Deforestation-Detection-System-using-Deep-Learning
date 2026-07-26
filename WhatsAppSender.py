import pywhatkit as pwk

import datetime
from geopy.geocoders import Nominatim

def sendInfoWA(mobilenumber,name):
   
    # Initialize Nominatim API
    geolocator = Nominatim(user_agent="MyApp")

    location = geolocator.geocode("pune")
    lat="19.16251"
    longi="73.91382"

    print("The latitude of the location is: ", 19.16251)
    print("The longitude of the location is: ",73.91382)
    #lat=str(location.latitude)
    #longi=str(location.longitude)
    urlstr="https://www.google.com/maps/dir/"+lat+","+longi
    message="ALERT ALERT ALERT !!! \n"+ " Dear "+name+"\n An Deforestation is detected on the Camera for the following location \n ";
    message=message+urlstr+"\n ";
    message=message+". And also attached Surveilliance Image for your reference. PLEASE TAKE ACTION IMMMEDIATLY \n ";
    message=message+" Regards - \n Automatic Deforestation Detection System"
   
 
    reference_image_path="temp.jpg"
    mobilenumber="+91"+mobilenumber;
   # WhatsAppSender.sendImage(mobilenumber, reference_image_path, message)
    datet=str(datetime.datetime.now())
    st=datet.split(" ")
    kt=st[1].split(":")
    hourstr=kt[0]
    minstr=kt[1]
    hr=int(hourstr)
    min=int(minstr)
    if(min<59):
        min=min+1
    else:
        min=1
        hr=hr+1
    print(hr)
    print(min)
    
   
    pwk.sendwhats_image(mobilenumber, reference_image_path,message)
    
 
# if __name__ == '__main__':
#     sendInfoWA()
 
    