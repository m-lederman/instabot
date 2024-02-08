from PIL import Image
from PIL import ImageDraw
import textwrap
from urllib import request
from urllib.request import Request, urlopen
import re
import selenium
import bs4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import os
import random
from selenium.webdriver.chrome.options import Options
from PIL import ImageEnhance

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

f = open("nouns.txt", "r")
input_word = []
for x in f:
    input_word.append(x)
    
    
# Creating an instance
driver = webdriver.Chrome(options=options)

# Logging into Instagram
driver.get("https://www.instagram.com/")
time.sleep(3)

username = driver.find_element(By.XPATH, (".//*[@aria-label='Phone number, username, or email']"))
username.send_keys('')  # Enter What you want for username


pword = driver.find_element(By.XPATH, (".//*[@aria-label='Password']"))
pword.send_keys("")        # Enter Your Password


driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(5)

#driver.find_element(By.XPATH, (".//*[@aria-label='Decline optional cookies']")).click()

#time.sleep(5)

driver.find_element(By.XPATH, "//button").click()

#time.sleep(5)

#driver.find_element(By.XPATH, "//button[@class='_a9-- _ap36 _a9_1']").click() 



time.sleep(6)


while True:
    for i in range(1):
        num = random.randrange(0, 118998)
        print(num)
        

        word = input_word[num]
        word2 = word
        line = "generate a fun fact you've never written before about " + word
        print(line)
        
        #driver = webdriver.Chrome(options=options)
        
        driver.get("https://deepai.org/chat/text-generator")
        time.sleep(3)
        text = driver.find_element(By.CLASS_NAME, "chatbox")
        text.send_keys(line) 
        #driver.find_element(By.ID, "chatSubmitButton").click()


        time.sleep(15)
        output = driver.find_element(By.XPATH, "//div[@class='outputBox']")
        output_content = output.get_attribute('innerHTML').split("<")[0]
        
        word_list = output_content.split(" ")
        print(word_list)
        bad_word = 0
        for j in range (len(word_list)):
            if word_list[j] == "derogatory": #make sure no bad words since the words file is off the internet
                bad_word = 1
        if len(output_content) < 100 or bad_word == 1:
            break
        print(output_content)



        time.sleep(5)
        #driver.close()



        
        driver.get('https://images.google.com/')
        time.sleep(5)

        box = driver.find_element(By.CLASS_NAME, "gLFyf")
        
        # Type the search query in the search box
        box.send_keys(word)
        
        # Pressing enter
        #box.send_keys(Keys.ENTER)
        
        time.sleep(2) 
        img = driver.find_element(By.XPATH, "//a[@class='FRuiCf islib nfEiy']")

        img.click()

        
        time.sleep(5)
        img = driver.find_element(By.XPATH, "//div[@class='p7sI2 PUxBg']")
        img.screenshot('pic.png')
  
        # Just to avoid unwanted errors
        time.sleep(5) 

    

        # Open an Image
        img = Image.open('pic.png')
        img = img.crop((0, 0, img.width, img.height-50))
        img = img.resize((img.width*2,img.height*2))
        enhancer = ImageEnhance.Sharpness(img)

        factor = 5
        img = enhancer.enhance(factor)
        img.save('original-image-1.png')
        
        W = img.width 
        txt = output_content
        ad = "" #put in an extra text at the bottom if i want
        text_split = textwrap.wrap(txt, width=W/15)
        H = len(text_split)*30+45
        ad_split = textwrap.wrap(ad, width=W/10)
        H_ad = len(ad_split)*20+20
        color_num = random.randrange(0,359)
        col1 = 'hsl(%d, %d%%, %d%%)' % (color_num, 100, 80)
        col2 = 'hsl(%d, %d%%, %d%%)' % (540-color_num, 100, 20)
        #img2 = Image.new("RGB", (W,H), col1)
        #img3 = Image.new("RGB", (W,H_ad), col1)

        #print((text_split[0]))

        new_image = Image.new('RGB',(W, H+img.height+H_ad), col1)
        #new_image.paste(img2,(0,0))
        new_image.paste(img,(0, H))
        #new_image.paste(img3,(0, H+img.height))

        I1 = ImageDraw.Draw(new_image)
        # Add Text to an image
        for i in range (len(text_split)):
            w = I1.textlength(text_split[i]) 
            I1.text(((W-w)/10-30,i*35), text_split[i], fill=(col2), font_size = 30)

        for i in range (len(ad_split)):
            w = I1.textlength(ad_split[i]) 
            I1.text(((W-w)/4,H+img.height+H_ad-20-((len(ad_split)-i)*22)), ad_split[i], fill=(col2), font_size = 20)
            

        # Save the edited image
        new_image.save('final.png')
        
        driver.get("https://www.instagram.com/")
        time.sleep(5)
        driver.find_element(By.XPATH, (".//*[@aria-label='New post']")).click() 

        time.sleep(5)


        upload_file = os.path.abspath("final.png")
        print(upload_file)
        file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        file_input.send_keys(upload_file)
        time.sleep(6)
        driver.find_element(By.XPATH, "//div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1xmf6yo x1emribx x1e56ztr x1i64zmx x10l6tqk x1ey2m1c x17qophe x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1']").click() 
        time.sleep(6)
        driver.find_element(By.XPATH, "//div[@class='x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x3nfvp2 x1q0g3np x87ps6o x1lku1pv x1a2a7pz']").click() 
        time.sleep(6)
        driver.find_element(By.XPATH, "//div[@class='_ac7b _ac7d']").click() 
        time.sleep(6)
        driver.find_element(By.XPATH, "//div[@class='_ac7b _ac7d']").click() 
        time.sleep(6)
        comment = driver.find_element(By.XPATH, (".//*[@aria-label='Write a caption...']"))
        comment.send_keys("#funfact #wtfmemes #wtffacts #knowledge #memes") 
        print(comment.get_attribute('innerHTML').split("<")[0])
        
        time.sleep(6)
        driver.find_element(By.XPATH, "//div[@class='_ac7b _ac7d']").click() 
        time.sleep(10)
        print('1')
        time.sleep(20)
