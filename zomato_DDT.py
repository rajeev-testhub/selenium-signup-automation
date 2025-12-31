from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from xlrd import open_workbook

path = r"C:\Users\Rajeev Mishra\OneDrive\Documents\sign up page.xlsx"

workbook = open_workbook(path)
sheet = workbook.sheet_by_name("Sign_Up")

test_data = {}
for i in range(1, sheet.nrows):
    row = sheet.row_values(i)
    test_data[row[0]] = row[1]

print("Test Data Loaded:", test_data)
options = ChromeOptions()
options.add_experimental_option("detach", True)

driver = Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.zomato.com/hyderabad/delivery")

driver.find_element(By.XPATH, "//a[text()='Sign up']").click()
sleep(3)
for first_name, email in test_data.items():

    first_name_field = driver.find_element(By.XPATH, "(//input[@type='text'])[1]")
    first_name_field.send_keys(first_name)

    email_field = driver.find_element(By.XPATH, "(//input[@type='text'])[2]")
    email_field.send_keys(email)

    checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
    checkbox.click()

    create_btn = driver.find_element(By.XPATH, "//span[text()='Create account']")
    btn_state = create_btn.get_attribute("aria-disabled")

    if btn_state == "true":
        print("❌ Invalid data - Create Account button is disabled")
    else:
        print("✅ Create Account button enabled")

    first_name_field.send_keys(Keys.CONTROL, "a", Keys.DELETE)
    email_field.send_keys(Keys.CONTROL, "a", Keys.DELETE)
    checkbox.click()
    sleep(1)

driver.close()















