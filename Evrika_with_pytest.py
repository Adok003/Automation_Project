from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()
driver.get('https://evrika.com/')
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, '/html/body/div[4]/div/div[3]/button[1]').click()
driver.implicitly_wait(10)


def test_category():
    search_input = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div/div/div[2]/div/form/div')
    print('click the search area')
    search_input.click()
    driver.implicitly_wait(10)

    laptops = driver.find_element(By.XPATH,
                                  '/html/body/div[3]/div[1]/div[2]/div/div/div[2]/div/div[2]/div[1]/ul/li[2]/a')
    print(f"Choose category '{laptops.text}'")
    laptops.click()
    driver.implicitly_wait(10)

    assert 'noutbuki' in driver.current_url and 'Ноутбуки' in driver.title


def test_store():
    driver.find_element(By.CLASS_NAME, 'select').click()
    choose_store = driver.find_element(By.XPATH,
                                       '/html/body/div[3]/div[1]/main/div[2]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div[2]/ul/li[6]')
    print(f"store availability - '{choose_store.text}'")
    choose_store.click()
    # driver.implicitly_wait(10)
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, 500)")

    assert "trts-mart" in driver.current_url


def test_cost():
    time.sleep(5)
    print('choose price', end=' ')
    price_from = driver.find_element(By.NAME, "cost_from")
    price = '200000'
    print(price, end=' - ')
    price_from.send_keys(Keys.CONTROL, 'a')
    price_from.send_keys(price)

    price_to = driver.find_element(By.NAME, "cost_to")
    price = '500000'
    print(price, end=' tg \n')
    price_to.send_keys(Keys.CONTROL, 'a')
    price_to.send_keys('500000', Keys.ENTER)
    time.sleep(5)

    assert "cost_from=200000" in driver.current_url and "cost_to=500000" in driver.current_url


def test_brands():
    choose_brand_asus = driver.find_element(By.XPATH,
                                            "/html/body/div[3]/div[1]/main/div[2]/div[1]/div[3]/div[2]/div/div[2]/div[4]/div[2]/div[3]/label/span/i")
    print(f"choose ' {choose_brand_asus.text}", end=' & ')
    choose_brand_asus.click()
    time.sleep(5)

    choose_brand_lenovo = driver.find_element(By.XPATH,
                                              "/html/body/div[3]/div[1]/main/div[2]/div[1]/div[3]/div[2]/div/div[2]/div[4]/div[2]/div[7]/label/span/i")
    print(f"{choose_brand_lenovo.text}'")
    choose_brand_lenovo.click()
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, 900)")
    time.sleep(5)

    assert "asus,lenovo" in driver.current_url


def test_laptop_class():
    choose_laptop_class = driver.find_element(By.XPATH,
                                              "/html/body/div[3]/div[1]/main/div[2]/div[1]/div[3]/div[2]/div/div[2]/div[5]/div[2]/div[2]/label/span/i")
    print(f"laptop class '{choose_laptop_class.text}'")
    choose_laptop_class.click()
    time.sleep(5)

    assert "dlya-raboty-i-ucheby" in driver.current_url


def test_processor_type():
    choose_processor_type = driver.find_element(By.XPATH,
                                                "/html/body/div[3]/div[1]/main/div[2]/div[1]/div[3]/div[2]/div/div[2]/div[6]/div[2]/div[2]/label/span/i")
    print(f"processor type '{choose_processor_type.text}'")
    choose_processor_type.click()
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, 1000)")

    assert "ryzen-5" in driver.current_url


def test_memory_type():
    choose_memory_type = driver.find_element(By.XPATH,
                                             "/html/body/div[3]/div[1]/main/div[2]/div[1]/div[3]/div[2]/div/div[2]/div[7]/div[2]/div[2]/label/span/i")
    print(f"main memory '{choose_memory_type.text}'")
    choose_memory_type.click()
    time.sleep(5)

    assert "8-gb-ozu" in driver.current_url


def test_show_results():
    show_results = driver.find_element(By.XPATH,
                                       "/html/body/div[3]/div[1]/main/div[2]/div[1]/div[3]/div[2]/div/div[3]/button[1]")
    count_filtered_products = driver.find_element(By.XPATH,
                                                  "/html/body/div[3]/div[1]/main/div[2]/div[1]/div[3]/div[2]/div/div[3]/button[1]/span")
    print(f"show the results find {count_filtered_products.text} products, after filtering")
    show_results.click()
    time.sleep(5)

    catalog = driver.find_elements(By.XPATH, '/html/body/div[3]/div[1]/main/div[2]/div[1]/div[4]/div[3]/div[1]/div/div')

    assert str(len(catalog)) == count_filtered_products.text


def test_reset_results():
    reset_all = driver.find_element(By.XPATH,
                                    "/html/body/div[3]/div[1]/main/div[2]/div[1]/div[3]/div[2]/div/div[1]/div/div/a/span")
    print(f"'{reset_all.text}'")
    reset_all.click()
    time.sleep(5)

    assert "evrika.com/catalog/noutbuki/" in driver.current_url


def test_back_main_page():
    back = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div/div/div[1]/div/a")
    print("Back to main page")
    back.click()

    assert "evrika.com/" in driver.current_url
