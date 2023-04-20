from selenium import webdriver
import time
web = webdriver.Chrome()

web.get('https://docs.google.com/forms/d/e/1FAIpQLSf9nNqyKg17EUyGOCz2nL_HrV0L_sHpyAMkEC3tVwfyVkZBvA/viewform?fbzx=5189519002433997994')

names=[  "Neha Sharma",  "Shreya Singh",  "Riya Gupta",  "Ananya Desai"]

for i in names:
    web.get('https://docs.google.com/forms/d/e/1FAIpQLSf9nNqyKg17EUyGOCz2nL_HrV0L_sHpyAMkEC3tVwfyVkZBvA/viewform?fbzx=5189519002433997994')
    time.sleep(5)
    name=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    name.send_keys(i)
   

    age=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[3]/label/div')
    age.click()

   
   
    gender=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[2]/label/div')
    gender.click()
   
    H1=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[1]/label/div')
    H1.click()
   
    D1=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[3]/label/div')
    D1.click()
   
    Ho=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]')
    Ho.click()
   
    D2=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/span/div/div[4]/label/div')
    D2.click()
   
    Ho2=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[1]/label/div')
    Ho2.click()
   
    W1=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[5]/label/div')
    W1.click()
   
    Wh=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[1]/label/div')
    Wh.click()
   
    D3=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div/span/div/div[5]/label/div')
    D3.click()
   
    I1=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div/span/div/div[2]/label/div')
    I1.click()
   
    Ho3=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]')
    Ho3.click()
   
    W2=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div/span/div/div[4]/label/div')
    W2.click()
   
    A1=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/div/span/div/div[2]/label/div')
    A1.click()

   
    G1=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div/div[1]/div[2]/textarea')
    G1.send_keys("From an aesthetic standpoint, some brands may prefer to maintain a specific visual identity that may not be compatible with body positive mannequins. This could include concerns about how the mannequins may appear in store displays, or how they may affect the overall look and feel of a brand's products.")



    sub=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    sub.click()
    
    
print("TEST")