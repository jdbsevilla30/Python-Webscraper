from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Data import people

driver = webdriver.Chrome()

try: 
  
  for data in people:
       
       firstName = data["firstname"]
       lastName = data["lastname"]
       age = data["age"]
       birthday = data["date"]
       gender = data["gender"]

       genderRadio = ""

       if gender.lower() == 'male':
           genderRadio = '//*[@id="i22"]'
       elif gender.lower() == 'female':
           genderRadio = '//*[@id="i25"]'
       elif gender.lower() == 'non-binary':
           genderRadio = '//*[@id="i28"]'
       else:
           genderRadio = '//*[@id="i31"]'
   
       print(data)
       driver.get("https://docs.google.com/forms/d/e/1FAIpQLSf3FfgJlMs2bg_pBZbyjvRG0UffjAh22iV0lB_aJVvxU7IeDA/viewform?vc=0&c=0&w=1&flr=0")
       driver.implicitly_wait(1)
       driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(firstName)
       driver.implicitly_wait(1)
       driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(lastName)
       driver.implicitly_wait(1)
       driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(age)
       driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input').send_keys(birthday)
       driver.implicitly_wait(1)
       driver.find_element(By.XPATH, genderRadio).click()
       driver.implicitly_wait(5)
       driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
 
except Exception as e:
    print(e)
finally:
    driver.quit()

    