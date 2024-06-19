from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://amazon.com/")
driver.implicitly_wait(4)

# clicking on try different image
try:
    driver.find_element(By.XPATH, "//div[@class='a-row']/div[2]/a").click()
except:
    print("Not detected as bot !!!")

# Search the Item
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("iphone")
driver.find_element(By.XPATH, "//input[@type='text']").send_keys(Keys.ENTER)

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@data-index]")))

try:
    products = driver.find_elements(By.XPATH, "//div[@data-index]")
    print(products)

    for product in products:
        try:
            productName = product.find_element(By.XPATH, ".//h2/a/span").text
            print(productName)
        except Exception as e:
            print(f"Error extracting product name: {e}")

except Exception as e:
    print(f"An error occurred: {e}")