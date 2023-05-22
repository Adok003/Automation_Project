from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

import time


driver = webdriver.Chrome()
driver.get('https://evrika.com/')
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, '/html/body/div[4]/div/div[3]/button[1]').click()
driver.implicitly_wait(10)


def test_product_catalog():
    product_catalog = driver.find_element(By.XPATH,
                                          '/html/body/div[3]/div[1]/div[3]/div/div/div[1]/div/nav/span/div/div')
    print(product_catalog.text)  # assert product_catalog
    product_catalog.click()

    assert product_catalog.text == 'Каталог товаров'


def test_choose_product():
    product = driver.find_element(By.XPATH,
                                  '/html/body/div[3]/div[1]/div[4]/div/div/div[1]/nav/div[3]/div[1]/ul/li[1]/a/span[2]')
    print(product.text)  # assert product
    product.click()
    driver.implicitly_wait(10)

    assert 'smartfony-i-gadzhety' in driver.current_url


def test_product_apple():
    product_apple = driver.find_element(By.LINK_TEXT, 'Смартфоны Apple')
    print(product_apple.text)
    product_apple.click()
    driver.implicitly_wait(10)

    assert 'brand=apple-1' in driver.current_url


def test_first_product():
    first_product = driver.find_element(By.XPATH,
                                        '/html/body/div[3]/div[1]/main/div[2]/div[1]/div[4]/div[2]/div[1]/div[1]/div/div/div[3]/a')
    print("Add to compare first product")
    first_product.click()
    like1 = driver.find_element(By.XPATH,
                                '/html/body/div[3]/div[1]/main/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[1]/div/button/span').click()
    print("Added to favorites")
    counter_liked1 = driver.find_element(By.XPATH,
                                         '/html/body/div[3]/div[1]/div[2]/div/div/div[3]/div/div[3]/a/div/span[2]').text
    print(counter_liked1)  # assert for liked

    compare1 = driver.find_element(By.XPATH,
                                   '/html/body/div[3]/div[1]/main/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/button/span').click()
    print("Added to compare")
    counter_compared1 = driver.find_element(By.XPATH,
                                            '/html/body/div[3]/div[1]/div[2]/div/div/div[3]/div/div[2]/a/div/span[2]').text
    print(counter_compared1)  # assert for compared
    # driver.implicitly_wait(10)
    time.sleep(5)

    assert counter_liked1 == '1' and counter_compared1 == '1'


def test_second_product():
    driver.back()
    driver.implicitly_wait(10)

    second_product = driver.find_element(By.XPATH,
                                         '/html/body/div[3]/div[1]/main/div[2]/div[1]/div[4]/div[2]/div[1]/div[2]/div/div/div[3]/a')
    print("Add to compare second product")
    second_product.click()
    like2 = driver.find_element(By.XPATH,
                                '/html/body/div[3]/div[1]/main/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[1]/div/button/span').click()
    print("Added to favorites")
    counter_liked2 = driver.find_element(By.XPATH,
                                         '/html/body/div[3]/div[1]/div[2]/div/div/div[3]/div/div[3]/a/div/span[2]').text
    print(counter_liked2)  # assert for liked

    compare2 = driver.find_element(By.XPATH,
                                   '/html/body/div[3]/div[1]/main/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/button/span').click()
    print("Added to compare")
    counter_compared2 = driver.find_element(By.XPATH,
                                            '/html/body/div[3]/div[1]/div[2]/div/div/div[3]/div/div[2]/a/div/span[2]').text
    print(counter_compared2)  # assert for compared
    # driver.implicitly_wait(10)
    time.sleep(5)

    assert counter_liked2 == '1' and counter_compared2 == '1'


def test_go_to_compare():
    compare_page = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div/div/div[3]/div/div[2]/a/div')
    compare_page.click()
    time.sleep(5)

    assert 'comparison' in driver.current_url


def test_show_differences():
    show_differences = driver.find_element(By.XPATH,
                                           '/html/body/div[3]/div[1]/main/div/div[2]/div/div[3]/div[1]/div[1]/div[1]/div/div[5]/ul/li[2]/label/span')
    print(show_differences.text)  # assert show_differences
    show_differences.click()
    time.sleep(5)

    assert show_differences.text == 'Различия в характеристиках'


def test_delete_items():
    delete_items = driver.find_element(By.XPATH,
                                       '/html/body/div[3]/div[1]/main/div/div[2]/div/div[3]/div[1]/div[1]/div[1]/div/div[3]/span')
    print(delete_items.text)  # assert delete_items
    delete_items.click()
    time.sleep(5)

    assert delete_items.text == 'Очистить список'


def test_go_to_favorites():
    liked_page = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div/div/div[3]/div/div[3]/a/div')
    liked_page.click()
    time.sleep(5)

    assert 'favorites' in driver.current_url


def test_delete_one_item():
    driver.find_element(By.XPATH,
                        '/html/body/div[3]/div/main/div/div[3]/div/div[2]/div[1]/div/div/div[2]/label/span').click()
    delete_item = driver.find_element(By.XPATH,
                                      '/html/body/div[3]/div/main/div/div[3]/div/div[1]/div[1]/div/div[2]/button')
    print(delete_item.text)
    delete_item.click()
    time.sleep(5)

    assert delete_item.text == 'Удалить'


def test_click_product():
    ActionChains(driver).scroll_by_amount(0, 200).perform()
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[3]/div/main/div/div[3]/div/div[2]/div/div/div/div[4]/a').click()
    time.sleep(5)

    assert 'iphone-14-plus-128gb-purple' in driver.current_url


def test_click_image():
    ActionChains(driver).scroll_by_amount(0, 200).perform()
    image = driver.find_element(By.XPATH, '//*[@id="photo__gallery"]/div/div/div/div[1]/img')
    print("click the image")
    image.click()
    time.sleep(5)

    assert True


def test_scroll_all_images():
    scroll = driver.find_element(By.XPATH,
                                 '/html/body/div[3]/div[1]/main/div[2]/div[2]/div[2]/div[1]/div[1]/div/div[3]/div[3]/div/div[2]/div/div[1]/div[3]')
    scroll.click()
    time.sleep(5)
    scroll.click()
    time.sleep(5)

    assert True


def test_close_image():
    close = driver.find_element(By.XPATH,
                                '/html/body/div[3]/div[1]/main/div[2]/div[2]/div[2]/div[1]/div[1]/div/div[3]/div[3]/div/div[1]')
    close.click()
    time.sleep(5)

    assert True


def test_delete_from_favorites():
    driver.back()
    driver.find_element(By.XPATH,
                        '/html/body/div[3]/div/main/div/div[3]/div/div[2]/div/div/div/div[2]/label/span').click()
    driver.implicitly_wait(10)
    remove = driver.find_element(By.XPATH, '/html/body/div[3]/div/main/div/div[3]/div/div[1]/div[1]/div/div[2]/button')

    assert remove.text == 'Удалить'
