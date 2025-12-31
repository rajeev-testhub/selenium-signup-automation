from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from xlrd import open_workbook

# ---------------- READ TEST DATA FROM EXCEL ----------------
path = r"C:\Users\Rajeev Mishra\OneDrive\Documents\sign up page.xlsx"

workbook = open_workbook(path)
sheet = workbook.sheet_by_name("Sign_Up")

test_data = {}
for i in range(1, sheet.nrows):
    row = sheet.row_values(i)
    test_data[row[0]] = row[1]

print("Test Data Loaded:", test_data)

# ---------------- BROWSER SETUP ----------------
options = ChromeOptions()
options.add_experimental_option("detach", True)

driver = Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.zomato.com/hyderabad/delivery")

# Click on Sign Up
driver.find_element(By.XPATH, "//a[text()='Sign up']").click()
sleep(3)

# ---------------- TEST EXECUTION ----------------
for first_name, email in test_data.items():

    # Enter First Name
    first_name_field = driver.find_element(By.XPATH, "(//input[@type='text'])[1]")
    first_name_field.send_keys(first_name)

    # Enter Email
    email_field = driver.find_element(By.XPATH, "(//input[@type='text'])[2]")
    email_field.send_keys(email)

    # Click Checkbox
    checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
    checkbox.click()

    # Validate Create Account button state
    create_btn = driver.find_element(By.XPATH, "//span[text()='Create account']")
    btn_state = create_btn.get_attribute("aria-disabled")

    if btn_state == "true":
        print("❌ Invalid data - Create Account button is disabled")
    else:
        print("✅ Create Account button enabled")

    # Clear fields for next iteration
    first_name_field.send_keys(Keys.CONTROL, "a", Keys.DELETE)
    email_field.send_keys(Keys.CONTROL, "a", Keys.DELETE)
    checkbox.click()
    sleep(1)

driver.close()















# from selenium.webdriver import Chrome,ChromeOptions
# from time import sleep
# from selenium.webdriver.common.keys import Keys
# from xlrd import open_workbook
# path =r"C:\Users\Rajeev Mishra\OneDrive\Documents\sign up page.xlsx"
# workbook = open_workbook(path)
# sheet = workbook.sheet_by_name("Sign_Up")
# row_count = sheet.nrows
# d = {}
# for i in range(1,row_count):
#     data = sheet.row_values(i)
#     d[data[0]] = data[1]
# print(d)
# opts = ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = Chrome(options=opts)
# driver.get("https://www.zomato.com/hyderabad/delivery")
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.find_element("xpath","//a[text()='Sign up']").click()
# sleep(3)
# for ln,lv in d.items():
#     FN = driver.find_element("xpath", "(//input[@type='text'])[1]")
#     FN.send_keys(ln)
#     sleep(1)
#     EM = driver.find_element("xpath","(//input[@type='text'])[2]")
#     EM.send_keys(lv)
#     sleep(1)
#     CB = driver.find_element("xpath","//input[@type='checkbox']")
#     CB.click()
#     FN.send_keys(Keys.CONTROL, "a")
#     FN.send_keys(Keys.DELETE)
#     EM.send_keys(Keys.CONTROL, "a")
#     EM.send_keys(Keys.DELETE)
#     CB.click()
#     button = driver.find_element("xpath","//span[text()='Create account']")
#     btn = button.get_attribute("aria-disable")
#     if btn == "True":
#         button.click()
#         sleep(2)
#         print("Invalid datas.....")
#         break
#     else:
#         print("Create Account Button Enabled & User Account Created Successfully....")
#
# driver.close()
