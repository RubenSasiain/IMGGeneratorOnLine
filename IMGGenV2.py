import os
import sys
import tkinter as tk
from datetime import datetime
from time import sleep
from tkinter import *
from tkinter import messagebox, simpledialog

import matplotlib.pyplot as plt
import requests
from PIL import Image
from selenium import webdriver


def saved_path():
   
    if os.path.exists("ImagesPath.txt"): 
        with open("ImagesPath.txt", "r") as archivo:
            save_path = archivo.read()
    else:
       
        save_path = simpledialog.askstring(title="Path", prompt="Insert the path to save the images \n Cancel or white space to save in ./")
        with open("ImagesPath.txt", "w") as archivo:
            archivo.write(save_path)

    return save_path

def getOptionsForChromeDriver():
    opt = webdriver.ChromeOptions()
    opt.add_argument('--headless')
    opt.add_argument('--log-level=3')
    opt.add_argument('--disable--gpu')
    opt.add_argument('--focus-mode')
    return opt

def setPrompt(query,):
    print('setting prompt t001')
    text_box = driver.find_element('class name','model-input-text-input')
    print('get the element t001')
    text_box.clear()
    text_box.send_keys(query)
    print('prompt setted t001')

def generate_image():
    print('executing script to gnerate t001')
    driver.execute_script("highlightAndSelectGenerator('modelHdButton')")
    driver.execute_script("selectShape(2)") #1-2-3-4-5
    driver.execute_script('textModelSubmit()')
    print('script executed t001')

def getImgUrl():
    print('getting img attribute src t001')
    print('Getting img element t001')
    itera = 0
    while (True):
        itera += 1
        
        img = driver.find_element('class name', 'try-it-result-area').find_element('tag name', 'img')
        source = str(img.get_attribute('src'))
        defaultsrc = 'https://images.deepai.org/machine-learning-models/2789de23c1644016b5bc64c22ee144cd/elf.jpg'
        if source == defaultsrc:
            print("\r\033[K", end='', flush=True)
            print(f'\rLoading image... {itera}s', end='', flush=True)
            sleep(1)
        else:
            return img.get_attribute('src'), itera

def getImageName():
    print('getting image namet001')
    now = str(datetime.now()).replace('.', '').replace(':', '').replace(' ', '').replace('-', '')
    print('Image name generated t001')
    return f'generated{now}.jpg'

def saveOrDelete(img_url,image_name):
    print('entering on save or delete t001')
    img_data = requests.get(img_url).content
    with open(image_name, 'wb') as f:
        f.write(img_data)

    img = Image.open(image_name)
    plt.imshow(img)
    plt.axis('off')
    plt.show()

    us_input = input('Save image? (y/n): ')
    
    if us_input == 'y':
       
        img.save(os.path.join(path_to_save_img, image_name))
        print(f'Image saved in {os.path.join(path_to_save_img , image_name)}')
    os.remove(image_name)

def countDown(number):
    print('waiting: '+ str(number) + ' secs' )
    while number > 0:
        if number >= 1:
            number -= 1
            print("\r\033[K", end='', flush=True)
            print(f"\r{number}", end='', flush=True)
            sleep(1)
        elif number < 1:
            number -= 0.1
            print("\r\033[K", end='', flush=True)
            print(f"\r{number}", end='', flush=True)
            sleep(0.1)

def doSearch(query):
    setPrompt(query)
    generate_image()
    expectedT = (5)
    countDown(expectedT)
    print('Count down done t001')
    img_url,extraTime = getImgUrl()
    timeCost = ( extraTime + expectedT)
    print('\n\n\n Expected time:'+str(expectedT) + 's \n Real time: '+str(timeCost)+'s \n\n\n')

    image_name = getImageName()
    saveOrDelete(img_url,image_name)


if __name__ == "__main__":

    print('starting config t001')

    path_to_save_img = saved_path()

    ROOT = tk.Tk()
    ROOT.withdraw()
    opt = getOptionsForChromeDriver()


    opt.enable_downloads = True
    opt.accept_insecure_certs = True

    driver =  webdriver.Chrome(options=opt)

    print('setting the search url t001')
    search_url = f'https://deepai.org/machine-learning-model/fantasy-portrait-generator'

    print('Getting the page t001')
    driver.get(search_url)
    print('Page getted t001')

    print('End of config t001')
    user_inp = ''
    while (True):
        if(user_inp != ''):
            user_inp = simpledialog.askstring(title="Propt", prompt="\nInsert Query:\n cancel to finish\n", initialvalue=f"{user_inp}")
        else:
            user_inp = simpledialog.askstring(title="Propt", prompt="Insert Query:\n cancel to finish")
        query = user_inp
        user_inp.replace(' ','')
        if(user_inp == ''):
            break

        print(user_inp)
        
        doSearch(query)
    
driver.close()