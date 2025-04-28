from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time



#set up firefox 
options = Options()
options.binary_location = "C:\drivers\chrome-win64\chrome-win64\chrome.exe"


#set up geckdriver
service = Service(executable_path="C:\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe"
                )


driver = webdriver.Chrome(service=service, options=options)

driver.get("https://admissions.colostate.edu/contact-us/subscribe/")

#TC01
def TC01_all_fields_valid_data(): 
    fname = "ali"
    lname = "assiri"
    email = "student123@gmail.com"
    phonenumber = "+966558496032"
    print("writng the first name")              
    driver.find_element("id", "form_b3a5249d-7a6c-485b-82ba-1b6f1ba71d69").send_keys(fname)
    print("done writing the first name")
    time.sleep(1)

    print("writng the last name")
    driver.find_element("id", "form_12a6942d-a034-9052-e00c-dd7f1622f1e3").send_keys(lname)
    print("done writing the last name")
    time.sleep(1)

    print("writng the email")
    driver.find_element("id", "form_144964db-a073-47c2-2e41-6cea312bd874").send_keys(email)
    print("done writing the email")
    time.sleep(1)

    print("writng the phone number")
    driver.find_element("id", "form_10fa90c2-c750-e090-de5c-bacc00bff967").send_keys(phonenumber)
    print("done writing the phone number")
    time.sleep(1)

    #select yes from the radio button 
    radio_button = driver.find_element("id", "form_fc5b720d-4c35-5afa-7ad6-03fde4e789ac_2")
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", radio_button)
    time.sleep(1)
    radio_button.click()
    time.sleep(1)

    #select entry term
    driver.find_element("xpath","/html/body/div[2]/div/div/main/div[2]/section[1]/div/div/div/div[2]/div/div/div/form/div[4]/div[1]/div/div/div/div[9]/div/select/option[8]").click()

    #select freshman from the drop down menu
    driver.find_element("xpath","/html/body/div[2]/div/div/main/div[2]/section[1]/div/div/div/div[2]/div/div/div/form/div[4]/div[1]/div/div/div/div[11]/div/select/option[2]").click()
    time.sleep(1)

    #click the submit button
    driver.find_element("class name", "form_button_submit").click()
    time.sleep(50)
TC01_all_fields_valid_data()
#TC02
def TC02_all_valid_data_except_fname(): 
    fname = ""
    lname = "assiri"
    email = "student123@gmail.com"
    phonenumber = "+966558496032"
    print("writng the first name")              
    driver.find_element("id", "form_b3a5249d-7a6c-485b-82ba-1b6f1ba71d69").send_keys(fname)
    print("done writing the first name")
    time.sleep(1)

    print("writng the last name")
    driver.find_element("id", "form_12a6942d-a034-9052-e00c-dd7f1622f1e3").send_keys(lname)
    print("done writing the last name")
    time.sleep(1)

    print("writng the email")
    driver.find_element("id", "form_144964db-a073-47c2-2e41-6cea312bd874").send_keys(email)
    print("done writing the email")
    time.sleep(1)

    print("writng the phone number")
    driver.find_element("id", "form_10fa90c2-c750-e090-de5c-bacc00bff967").send_keys(phonenumber)
    print("done writing the phone number")
    time.sleep(1)

    #select yes from the radio button 
    radio_button = driver.find_element("id", "form_fc5b720d-4c35-5afa-7ad6-03fde4e789ac_2")
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", radio_button)
    time.sleep(1)
    radio_button.click()
    time.sleep(1)

    #select entry term
    driver.find_element("xpath","/html/body/div[2]/div/div/main/div[2]/section[1]/div/div/div/div[2]/div/div/div/form/div[4]/div[1]/div/div/div/div[9]/div/select/option[8]").click()

    #select freshman from the drop down menu
    driver.find_element("xpath","/html/body/div[2]/div/div/main/div[2]/section[1]/div/div/div/div[2]/div/div/div/form/div[4]/div[1]/div/div/div/div[11]/div/select/option[2]").click()
    time.sleep(1)

    #click the submit button
    driver.find_element("class name", "form_button_submit").click()
    time.sleep(50)

#TC03
def TC03_fname_boundary(): 
    fname = "alialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialialiali"
    lname = "assiri"
    email = "student123@gmail.com"
    phonenumber = "+966558496032"
    print("writng the first name")              
    driver.find_element("id", "form_b3a5249d-7a6c-485b-82ba-1b6f1ba71d69").send_keys(fname)
    print("done writing the first name")
    time.sleep(1)

    print("writng the last name")
    driver.find_element("id", "form_12a6942d-a034-9052-e00c-dd7f1622f1e3").send_keys(lname)
    print("done writing the last name")
    time.sleep(1)

    print("writng the email")
    driver.find_element("id", "form_144964db-a073-47c2-2e41-6cea312bd874").send_keys(email)
    print("done writing the email")
    time.sleep(1)

    print("writng the phone number")
    driver.find_element("id", "form_10fa90c2-c750-e090-de5c-bacc00bff967").send_keys(phonenumber)
    print("done writing the phone number")
    time.sleep(1)

    #select yes from the radio button 
    radio_button = driver.find_element("id", "form_fc5b720d-4c35-5afa-7ad6-03fde4e789ac_2")
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", radio_button)
    time.sleep(1)
    radio_button.click()
    time.sleep(1)

    #select entry term
    driver.find_element("xpath","/html/body/div[2]/div/div/main/div[2]/section[1]/div/div/div/div[2]/div/div/div/form/div[4]/div[1]/div/div/div/div[9]/div/select/option[8]").click()

    #select freshman from the drop down menu
    driver.find_element("xpath","/html/body/div[2]/div/div/main/div[2]/section[1]/div/div/div/div[2]/div/div/div/form/div[4]/div[1]/div/div/div/div[11]/div/select/option[2]").click()
    time.sleep(1)

    #click the submit button
    driver.find_element("class name", "form_button_submit").click()
    time.sleep(50)

#TC04
def TC04_lname_empty():
    fname = "ali"
    lname = ""
    email = "student123@gmail.com"
    phonenumber = "+966558496032"
    print("writng the first name")              
    driver.find_element("id", "form_b3a5249d-7a6c-485b-82ba-1b6f1ba71d69").send_keys(fname)
    print("done writing the first name")
    time.sleep(1)

    print("writng the last name")
    driver.find_element("id", "form_12a6942d-a034-9052-e00c-dd7f1622f1e3").send_keys(lname)
    print("done writing the last name")
    time.sleep(1)

    print("writng the email")
    driver.find_element("id", "form_144964db-a073-47c2-2e41-6cea312bd874").send_keys(email)
    print("done writing the email")
    time.sleep(1)

    print("writng the phone number")
    driver.find_element("id", "form_10fa90c2-c750-e090-de5c-bacc00bff967").send_keys(phonenumber)
    print("done writing the phone number")
    time.sleep(1)

    #select yes from the radio button 
    radio_button = driver.find_element("id", "form_fc5b720d-4c35-5afa-7ad6-03fde4e789ac_2")
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", radio_button)
    time.sleep(1)
    radio_button.click()
    time.sleep(1)

    #select entry term
    driver.find_element("xpath","/html/body/div[2]/div/div/main/div[2]/section[1]/div/div/div/div[2]/div/div/div/form/div[4]/div[1]/div/div/div/div[9]/div/select/option[8]").click()

    #select freshman from the drop down menu
    driver.find_element("xpath","/html/body/div[2]/div/div/main/div[2]/section[1]/div/div/div/div[2]/div/div/div/form/div[4]/div[1]/div/div/div/div[11]/div/select/option[2]").click()
    time.sleep(1)

    #click the submit button
    driver.find_element("class name", "form_button_submit").click()
    time.sleep(50)
 
#TC05
def TC05_lname_boundary():
    fname = "ali"
    lname = "assiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiriassiri"
    email = "student123@gmail.com"
    phonenumber = "+966558496032"
    print("writng the first name")              
    driver.find_element("id", "form_b3a5249d-7a6c-485b-82ba-1b6f1ba71d69").send_keys(fname)
    print("done writing the first name")
    time.sleep(1)

    print("writng the last name")
    driver.find_element("id", "form_12a6942d-a034-9052-e00c-dd7f1622f1e3").send_keys(lname)
    print("done writing the last name")
    time.sleep(1)

    print("writng the email")
    driver.find_element("id", "form_144964db-a073-47c2-2e41-6cea312bd874").send_keys(email)
    print("done writing the email")
    time.sleep(1)

    print("writng the phone number")
    driver.find_element("id", "form_10fa90c2-c750-e090-de5c-bacc00bff967").send_keys(phonenumber)
    print("done writing the phone number")
    time.sleep(1)

    #select yes from the radio button 
    radio_button = driver.find_element("id", "form_fc5b720d-4c35-5afa-7ad6-03fde4e789ac_2")
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", radio_button)
    time.sleep(1)
    radio_button.click()
    time.sleep(1)

    #select entry term
    driver.find_element("xpath","/html/body/div[2]/div/div/main/div[2]/section[1]/div/div/div/div[2]/div/div/div/form/div[4]/div[1]/div/div/div/div[9]/div/select/option[8]").click()

    #select freshman from the drop down menu
    driver.find_element("xpath","/html/body/div[2]/div/div/main/div[2]/section[1]/div/div/div/div[2]/div/div/div/form/div[4]/div[1]/div/div/div/div[11]/div/select/option[2]").click()
    time.sleep(1)

    #click the submit button
    driver.find_element("class name", "form_button_submit").click()
    time.sleep(50)

#TC06
def TC06_email_format_wrong():
    fname = "ali"
    lname = "assiri"
    email = "student123gmail.com"
    phonenumber = "+966558496032"
    print("writng the first name")              
    driver.find_element("id", "form_b3a5249d-7a6c-485b-82ba-1b6f1ba71d69").send_keys(fname)
    print("done writing the first name")
    time.sleep(1)

    print("writng the last name")
    driver.find_element("id", "form_12a6942d-a034-9052-e00c-dd7f1622f1e3").send_keys(lname)
    print("done writing the last name")
    time.sleep(1)

    print("writng the email")
    driver.find_element("id", "form_144964db-a073-47c2-2e41-6cea312bd874").send_keys(email)
    print("done writing the email")
    time.sleep(1)

    print("writng the phone number")
    driver.find_element("id", "form_10fa90c2-c750-e090-de5c-bacc00bff967").send_keys(phonenumber)
    print("done writing the phone number")
    time.sleep(1)

    #select yes from the radio button 
    radio_button = driver.find_element("id", "form_fc5b720d-4c35-5afa-7ad6-03fde4e789ac_2")
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", radio_button)
    time.sleep(1)
    radio_button.click()
    time.sleep(1)

    #select entry term
    driver.find_element("xpath","/html/body/div[2]/div/div/main/div[2]/section[1]/div/div/div/div[2]/div/div/div/form/div[4]/div[1]/div/div/div/div[9]/div/select/option[8]").click()

    #select freshman from the drop down menu
    driver.find_element("xpath","/html/body/div[2]/div/div/main/div[2]/section[1]/div/div/div/div[2]/div/div/div/form/div[4]/div[1]/div/div/div/div[11]/div/select/option[2]").click()
    time.sleep(1)

    #click the submit button
    driver.find_element("class name", "form_button_submit").click()
    time.sleep(50)

#TC07
def TC07_email_boundary():
    fname = "ali"
    lname = "assiri"
    email = "a@a.a"
    phonenumber = "+966558496032"
    print("writng the first name")              
    driver.find_element("id", "form_b3a5249d-7a6c-485b-82ba-1b6f1ba71d69").send_keys(fname)
    print("done writing the first name")
    time.sleep(1)

    print("writng the last name")
    driver.find_element("id", "form_12a6942d-a034-9052-e00c-dd7f1622f1e3").send_keys(lname)
    print("done writing the last name")
    time.sleep(1)

    print("writng the email")
    driver.find_element("id", "form_144964db-a073-47c2-2e41-6cea312bd874").send_keys(email)
    print("done writing the email")
    time.sleep(1)

    print("writng the phone number")
    driver.find_element("id", "form_10fa90c2-c750-e090-de5c-bacc00bff967").send_keys(phonenumber)
    print("done writing the phone number")
    time.sleep(1)

    #select yes from the radio button 
    radio_button = driver.find_element("id", "form_fc5b720d-4c35-5afa-7ad6-03fde4e789ac_2")
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", radio_button)
    time.sleep(1)
    radio_button.click()
    time.sleep(1)

    #select entry term
    driver.find_element("xpath","/html/body/div[2]/div/div/main/div[2]/section[1]/div/div/div/div[2]/div/div/div/form/div[4]/div[1]/div/div/div/div[9]/div/select/option[8]").click()

    #select freshman from the drop down menu
    driver.find_element("xpath","/html/body/div[2]/div/div/main/div[2]/section[1]/div/div/div/div[2]/div/div/div/form/div[4]/div[1]/div/div/div/div[11]/div/select/option[2]").click()
    time.sleep(1)

    #click the submit button
    driver.find_element("class name", "form_button_submit").click()
    time.sleep(50)


#TC08
def TC08_phonenumber_format_wrong():
    fname = "ali"
    lname = "assiri"
    email = "student123@gmail.com"
    phonenumber = "+966558g96032"
    print("writng the first name")              
    driver.find_element("id", "form_b3a5249d-7a6c-485b-82ba-1b6f1ba71d69").send_keys(fname)
    print("done writing the first name")
    time.sleep(1)

    print("writng the last name")
    driver.find_element("id", "form_12a6942d-a034-9052-e00c-dd7f1622f1e3").send_keys(lname)
    print("done writing the last name")
    time.sleep(1)

    print("writng the email")
    driver.find_element("id", "form_144964db-a073-47c2-2e41-6cea312bd874").send_keys(email)
    print("done writing the email")
    time.sleep(1)

    print("writng the phone number")
    driver.find_element("id", "form_10fa90c2-c750-e090-de5c-bacc00bff967").send_keys(phonenumber)
    print("done writing the phone number")
    time.sleep(1)

    #select yes from the radio button 
    radio_button = driver.find_element("id", "form_fc5b720d-4c35-5afa-7ad6-03fde4e789ac_2")
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", radio_button)
    time.sleep(1)
    radio_button.click()
    time.sleep(1)

    #select entry term
    driver.find_element("xpath","/html/body/div[2]/div/div/main/div[2]/section[1]/div/div/div/div[2]/div/div/div/form/div[4]/div[1]/div/div/div/div[9]/div/select/option[8]").click()

    #select freshman from the drop down menu
    driver.find_element("xpath","/html/body/div[2]/div/div/main/div[2]/section[1]/div/div/div/div[2]/div/div/div/form/div[4]/div[1]/div/div/div/div[11]/div/select/option[2]").click()
    time.sleep(1)

    #click the submit button
    driver.find_element("class name", "form_button_submit").click()
    time.sleep(50)


#TC09
def TC09_phonenumber_boundary():
    fname = "ali"
    lname = "assiri"
    email = "student123@gmail.com"
    phonenumber = "+96655849603012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"
    print("writng the first name")              
    driver.find_element("id", "form_b3a5249d-7a6c-485b-82ba-1b6f1ba71d69").send_keys(fname)
    print("done writing the first name")
    time.sleep(1)

    print("writng the last name")
    driver.find_element("id", "form_12a6942d-a034-9052-e00c-dd7f1622f1e3").send_keys(lname)
    print("done writing the last name")
    time.sleep(1)

    print("writng the email")
    driver.find_element("id", "form_144964db-a073-47c2-2e41-6cea312bd874").send_keys(email)
    print("done writing the email")
    time.sleep(1)

    print("writng the phone number")
    driver.find_element("id", "form_10fa90c2-c750-e090-de5c-bacc00bff967").send_keys(phonenumber)
    print("done writing the phone number")
    time.sleep(1)

    #select yes from the radio button 
    radio_button = driver.find_element("id", "form_fc5b720d-4c35-5afa-7ad6-03fde4e789ac_2")
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", radio_button)
    time.sleep(1)
    radio_button.click()
    time.sleep(1)

    #select entry term
    driver.find_element("xpath","/html/body/div[2]/div/div/main/div[2]/section[1]/div/div/div/div[2]/div/div/div/form/div[4]/div[1]/div/div/div/div[9]/div/select/option[8]").click()

    #select freshman from the drop down menu
    driver.find_element("xpath","/html/body/div[2]/div/div/main/div[2]/section[1]/div/div/div/div[2]/div/div/div/form/div[4]/div[1]/div/div/div/div[11]/div/select/option[2]").click()
    time.sleep(1)

    #click the submit button
    driver.find_element("class name", "form_button_submit").click()
    time.sleep(50)


#TC10
def TC10_text_update_not_slected():
    fname = "ali"
    lname = "assiri"
    email = "student123@gmail.com"
    phonenumber = "+966558496032"
    print("writng the first name")              
    driver.find_element("id", "form_b3a5249d-7a6c-485b-82ba-1b6f1ba71d69").send_keys(fname)
    print("done writing the first name")
    time.sleep(1)

    print("writng the last name")
    driver.find_element("id", "form_12a6942d-a034-9052-e00c-dd7f1622f1e3").send_keys(lname)
    print("done writing the last name")
    time.sleep(1)

    print("writng the email")
    driver.find_element("id", "form_144964db-a073-47c2-2e41-6cea312bd874").send_keys(email)
    print("done writing the email")
    time.sleep(1)

    print("writng the phone number")
    driver.find_element("id", "form_10fa90c2-c750-e090-de5c-bacc00bff967").send_keys(phonenumber)
    print("done writing the phone number")
    time.sleep(1)

    #select yes from the radio button 
    radio_button = driver.find_element("id", "form_fc5b720d-4c35-5afa-7ad6-03fde4e789ac_2")
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", radio_button)
    time.sleep(1)
    #radio_button.click()
    time.sleep(1)

    #select entry term
    driver.find_element("xpath","/html/body/div[2]/div/div/main/div[2]/section[1]/div/div/div/div[2]/div/div/div/form/div[4]/div[1]/div/div/div/div[9]/div/select/option[8]").click()

    #select freshman from the drop down menu
    driver.find_element("xpath","/html/body/div[2]/div/div/main/div[2]/section[1]/div/div/div/div[2]/div/div/div/form/div[4]/div[1]/div/div/div/div[11]/div/select/option[2]").click()
    time.sleep(1)

    #click the submit button
    driver.find_element("class name", "form_button_submit").click()
    time.sleep(50)

#TC11
def TC11_entry_term_not_selected():
    fname = "ali"
    lname = "assiri"
    email = "student123@gmail.com"
    phonenumber = "+966558496032"
    print("writng the first name")              
    driver.find_element("id", "form_b3a5249d-7a6c-485b-82ba-1b6f1ba71d69").send_keys(fname)
    print("done writing the first name")
    time.sleep(1)

    print("writng the last name")
    driver.find_element("id", "form_12a6942d-a034-9052-e00c-dd7f1622f1e3").send_keys(lname)
    print("done writing the last name")
    time.sleep(1)

    print("writng the email")
    driver.find_element("id", "form_144964db-a073-47c2-2e41-6cea312bd874").send_keys(email)
    print("done writing the email")
    time.sleep(1)

    print("writng the phone number")
    driver.find_element("id", "form_10fa90c2-c750-e090-de5c-bacc00bff967").send_keys(phonenumber)
    print("done writing the phone number")
    time.sleep(1)

    #select yes from the radio button 
    radio_button = driver.find_element("id", "form_fc5b720d-4c35-5afa-7ad6-03fde4e789ac_2")
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", radio_button)
    time.sleep(1)
    radio_button.click()
    time.sleep(1)

    #select entry term
    #driver.find_element("xpath","/html/body/div[2]/div/div/main/div[2]/section[1]/div/div/div/div[2]/div/div/div/form/div[4]/div[1]/div/div/div/div[9]/div/select/option[8]").click()

    #select freshman from the drop down menu
    driver.find_element("xpath","/html/body/div[2]/div/div/main/div[2]/section[1]/div/div/div/div[2]/div/div/div/form/div[4]/div[1]/div/div/div/div[11]/div/select/option[2]").click()
    time.sleep(1)

    #click the submit button
    driver.find_element("class name", "form_button_submit").click()
    time.sleep(50)

#TC12
def TC12_student_type_not_selected():
    fname = "ali"
    lname = "assiri"
    email = "student123@gmail.com"
    phonenumber = "+966558496032"
    print("writng the first name")              
    driver.find_element("id", "form_b3a5249d-7a6c-485b-82ba-1b6f1ba71d69").send_keys(fname)
    print("done writing the first name")
    time.sleep(1)

    print("writng the last name")
    driver.find_element("id", "form_12a6942d-a034-9052-e00c-dd7f1622f1e3").send_keys(lname)
    print("done writing the last name")
    time.sleep(1)

    print("writng the email")
    driver.find_element("id", "form_144964db-a073-47c2-2e41-6cea312bd874").send_keys(email)
    print("done writing the email")
    time.sleep(1)

    print("writng the phone number")
    driver.find_element("id", "form_10fa90c2-c750-e090-de5c-bacc00bff967").send_keys(phonenumber)
    print("done writing the phone number")
    time.sleep(1)

    #select yes from the radio button 
    radio_button = driver.find_element("id", "form_fc5b720d-4c35-5afa-7ad6-03fde4e789ac_2")
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", radio_button)
    time.sleep(1)
    radio_button.click()
    time.sleep(1)

    #select entry term
    driver.find_element("xpath","/html/body/div[2]/div/div/main/div[2]/section[1]/div/div/div/div[2]/div/div/div/form/div[4]/div[1]/div/div/div/div[9]/div/select/option[8]").click()

    #select freshman from the drop down menu
    #driver.find_element("xpath","/html/body/div[2]/div/div/main/div[2]/section[1]/div/div/div/div[2]/div/div/div/form/div[4]/div[1]/div/div/div/div[11]/div/select/option[2]").click()
    time.sleep(1)

    #click the submit button
    driver.find_element("class name", "form_button_submit").click()
    time.sleep(50)