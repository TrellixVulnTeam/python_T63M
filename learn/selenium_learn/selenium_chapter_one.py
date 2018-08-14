# -*- utf-8 -*-
import csv
import random
import time

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


def sele_learn():
    csv_file = open("C:/Users/k/gitme/wyy_lg500-8.13.csv", "w", newline='', encoding='utf-8')
    writer = csv.writer(csv_file)
    writer.writerow(["标题", "播放量", "链接"])

    options = Options()
    options.add_argument("-headless")
    driver = Firefox(executable_path="C:\Program Files\Python36\Scripts\geckodriver", firefox_options=options)
    url = "https://music.163.com/#/discover/playlist"
    ia = 1
    while url != 'javascript:void(0)':
        driver.get(url)
        driver.switch_to.frame("contentFrame")
        data = driver.find_element_by_id("m-pl-container").find_elements_by_tag_name("li")
        for i in range(len(data)):
            nb = data[i].find_element_by_class_name("nb").text

            if "万" in nb and 500 < int(nb.split("万")[0]):
                msk = data[i].find_element_by_css_selector("a.msk")
                writer.writerow([msk.get_attribute('title'), nb, msk.get_attribute("href")])
                # driver.get(msk.get_attribute("href"))
                # driver.switch_to.frame("contentFrame")
        ia += 1
        url = driver.find_element_by_css_selector("a.zbtn.znxt").get_attribute("href")
        print(ia)
        time.sleep(random.randint(2, 10))
    driver.close()
    csv_file.close()


if __name__ == "__main__":
    sele_learn()
