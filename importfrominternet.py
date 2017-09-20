import random
import urllib.request

def download_web_image(url): #eg downloading image from internt
    name=random.randrange(1,1000)
    full_name=str(name)+".jpg" #since adding number to string is not feasible , we convert name into string using str()
    urllib.request.urlretrieve(url,full_name) #this downloads the image

download_web_image("https://avashadhikari.com.np/storage/cover_images/image2_1505744597.jpg")

