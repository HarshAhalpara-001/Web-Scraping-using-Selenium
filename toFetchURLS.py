from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
search = ['laptop',1]
for i in range(1,search[1]+1):
    print(f"https://www.amazon.in/s?k={search[0]}&page=2&qid=1721577246&ref=sr_pg_{i}")
    driver.get(f"https://www.amazon.in/s?k={search[0]}&page=2&qid=1721577246&ref=sr_pg_{str(i)}")
    try:
        elems = driver.find_elements(By.CLASS_NAME, "a-link-normal.s-no-outline")
        with open('output.txt', 'w', encoding='utf-8') as file:     #write not append for now
            for elem in elems:
                file.write(elem.get_attribute('href') + '\n')
    except Exception as e:
        print(f"An error occurred: {e}")
# assert "Amazon" in driver.title

# for elem in elems:
#     print(elem.innerHTML)
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
time.sleep(5)
driver.close()