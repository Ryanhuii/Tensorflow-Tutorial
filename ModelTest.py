

''' 
used this commands : 
    py -m pip install selenium
    py -m pip install pillow
    py -m pip install flask
https://bobbyhadz.com/blog/python-no-module-named-selenium
https://selenium-python.readthedocs.io/locating-elements.html
https://testerops.com/selenium-with-python/advanced-topics/cropping-an-image-using-pil/
ChatGPT for creating a live image display with PIL & tkinter
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
from time import sleep
from threading import Thread
# Import the ImageApp class from image_app module
import tkinter as tk
from image_app import ImageApp

# looping this bit to keep reading the live cam feed
# am thinking of putting this in a thread, then creating a website,
# then creating a second thread to update the contents of the website.
def capture_image():
    while True:
        driver.get_screenshot_as_file("screenshot.png")
        #open the image using Pillow
        image = Image.open('screenshot.png')

        #setting the crop attributes using image's location and size.
        left = loc1['x']
        top = loc1['y']
        right = loc1['x'] + size1['width']
        bottom1 = loc1['y'] + size1['height']

        #crop the image using the attributes defined
        image = image.crop((left,top,right,bottom1))
        #use the attribute to save the cropped image
        image.save('cropped-screenshot.png')

        sleep(1) # refresh the camera feed every 10 seconds

# driver.quit()
# print("program has ended...")

if __name__ == "__main__":

    # load the droidcam website
    driver = webdriver.Firefox()
    # enter device id
    driver.get('http://192.168.67.184:4747/')
    sleep(2)
    # target the livefeed image element
    element = driver.find_element(By.ID,"feedimg")
    #getting element's location
    loc1= element.location
    #getting element's size
    size1= element.size
    print(loc1,size1)

    # start capturing image thread
    new_thread = Thread(target=capture_image)
    new_thread.start()

    # display the image and prediction inside the python GUI
    sleep(2)
    image_path = 'cropped-screenshot.png'
    root = tk.Tk()
    app = ImageApp(root, image_path)
    root.mainloop()