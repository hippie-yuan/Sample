#!/usr/bin/python
# -*- coding: UTF-8 -*-
# time: 2021/4/15 17:29
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pandas
import lxml


class Expert(object):
    def __init__(self, data):
        self.index = str(data[0])
        self.name = data[1]
        self.province = data[2]
        self.city = data[3]
        self.university = data[4]
        self.img = data[5]
        self.title = data[6]
        self.area = data[7]
        self.intro = str(data[8])


    def ul_name(self, driver):
        driver.find_element_by_xpath(
            '//*[@id="app"]/section/section/main/div/div/div[2]/form/div[1]/div[1]/div[1]/div/div/input').send_keys(self.name)

    def ul_pcu(self, driver):

        # p

        ActionChains(driver).send_keys_to_element(
            driver.find_element_by_xpath('//*[@id="app"]/section/section/main/div/div/div[2]/form/div[1]/div[1]/div[2]/div/div/div[1]/input'),
            self.province).move_to_element(
            driver.find_element_by_xpath(
                '//span[text()="' + self.province + '"]/..')).click(
                driver.find_element_by_xpath(
                    '//span[text()="' + self.province + '"]/..')).perform()

        # c
        driver.find_element_by_xpath(
            '//*[@id="app"]/section/section/main/div/div/div[2]/form/div[1]/div[1]/div[3]/div/div/div[1]/input').click
        driver.find_element_by_xpath(
            '//*[@id="app"]/section/section/main/div/div/div[2]/form/div[1]/div[1]/div[3]/div/div/div[1]/input').send_keys(self.city)
        time.sleep(2)
        self.list_click(driver, self.city)
        # u
        driver.find_element_by_xpath(
            '//*[@id="app"]/section/section/main/div/div/div[2]/form/div[1]/div[1]/div[5]/div/div/div[1]/input').click
        driver.find_element_by_xpath(
            '//*[@id="app"]/section/section/main/div/div/div[2]/form/div[1]/div[1]/div[5]/div/div/div[1]/input').send_keys(self.university)
        time.sleep(2)
        self.list_click(driver, self.university)

    def ul_img(self, driver):

        driver.find_element_by_xpath(
                '//*[@id="app"]/section/section/main/div/div/div[2]/form/div[1]/div[2]/div/div/div/div/div/input').send_keys(r'C:\Users\\PycharmProjects\crawler\workspace\pic\UniversityLogo\UniversityLogo\ '+self.img)



    def ul_title(self, driver):
        driver.find_element_by_xpath(
            '//*[@id="app"]/section/section/main/div/div/div[2]/form/div[2]/div[4]/div/div/div/div[1]/input').click
        driver.find_element_by_xpath(
            '//*[@id="app"]/section/section/main/div/div/div[2]/form/div[2]/div[4]/div/div/div/div[1]/input').send_keys(self.title)
        self.list_click(driver, self.title)

    def ul_area(self, driver):

        li = [self.area]
        for l in li:
            driver.find_element_by_xpath(
                '//*[@id="app"]/section/section/main/div/div/div[2]/form/div[4]/div[1]/div/div/div/div[1]/input').send_keys(l)
            self.list_click(driver, l)
        driver.find_element_by_xpath('//*[@id="app"]/section/section/main/div/div/div[2]/form/div[4]/div[1]/div/div/div/div[2]/span/span/i').click
    def ul_intro(self, driver):
        driver.find_element_by_xpath(
            '//*[@id="app"]/section/section/main/div/div/div[2]/form/div[5]/div/div/div/div/textarea').click()
        driver.find_element_by_xpath(
            '//*[@id="app"]/section/section/main/div/div/div[2]/form/div[5]/div/div/div/div/textarea').send_keys(self.intro)

    def list_click(self, driver, widget_name):
        ActionChains(driver).move_to_element(
            driver.find_element_by_xpath(
                '//span[text()="' + widget_name + '"]/..')).click(
            driver.find_element_by_xpath(
                '//span[text()="' + widget_name + '"]/..')).perform()

    def form_submit(self,driver):
        driver.find_element_by_xpath("(//button[@type='button']//span)[3]").click();
    def print_self(self):
        print(self.index +
        self.name +
        self.province +
        self.city +
        self.university +
        self.img  +
        self.title +
        self.area +
        self.intro )


def login(driver):
    username = 'username'
    passward = '@passward'
    driver.get('')
    driver.find_element_by_xpath(
        '//*[@id="app"]/div/form/div[2]/div/div[1]/input').send_keys(username)
    driver.find_element_by_xpath(
        '//*[@id="app"]/div/form/div[3]/div/div/input').send_keys(passward)
    driver.find_element_by_xpath(
        '//*[@id="app"]/div/form/div[4]/div/button').click()


def main(expert, driver):
    expert.print_self()
    time.sleep(4)
    driver.get('')

    expert.ul_name(driver)
    expert.ul_pcu(driver)
    expert.ul_img(driver)

    expert.ul_area(driver)
    expert.ul_title(driver)

    expert.ul_intro(driver)
    expert.form_submit(driver)


if __name__ == '__main__':

    driver = webdriver.Chrome(
        r'C:\Users\\PycharmProjects\crawler\workspace\chromedriver.exe')
    driver.implicitly_wait(3)
    login(driver)
    datas = pandas.read_excel(
        r'C:\Users\\PycharmProjects\crawler\workspace\expert.xlsx',
        header=0,
        index_col=0,
        engine='openpyxl')

    for data in datas.iterrows():

        data = Expert([data[0]] + data[1].values.tolist())

        print('start', data.index)
        main(data,driver)
        print('done')
    print('all done')
