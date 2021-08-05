#!/usr/bin/python
# -*- coding: UTF-8 -*-
# time: 2021/3/29 10:50
import selenium
import ast
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pandas
import openpyxl


def main(Patent):
    Patent.print_content()
    Patent.OpenPage(driver)
    Patent.Title(driver)
    Patent.Mature(driver)

    Patent.Area(driver)
    Patent.University(driver)
    Patent.Inventer(driver)
    Patent.Introduction(driver)
    Patent.PatentNo(driver)
    Patent.Submit(driver)



def login(driver):
    username = 'username'
    passward = 'passward'
    driver.get('')
    driver.find_element_by_xpath('//*[@id="app"]/div/form/div[2]/div/div[1]/input').send_keys(username)
    driver.find_element_by_xpath('//*[@id="app"]/div/form/div[3]/div/div/input').send_keys(passward)
    driver.find_element_by_xpath('//*[@id="app"]/div/form/div[4]/div/button').click()
    time.sleep(2)


class Patent(object):
    def __init__(self, content):
        self.index = content[0]
        self.name = content[1]
        self.maturity = content[2]
        self.area = content[3]
        self.province = content[4]
        self.city = content[5]
        self.university = content[6]
        self.owners = content[7]
        self.picpath = content[8]
        self.intro = content[9]
        self.no = content[10]
        for i in content[0:10]:
            if i == 'nan':
                print('Please fill the value:', i)

    def print_content(self):
        list = [self.index,
                self.name,
                self.maturity,
                self.area,
                self.province,
                self.city,
                self.university,
                self.owners,
                self.picpath,
                self.intro,
                self.no]
        print(list)

    def OpenPage(self, driver):
        driver.get('')

    def Title(self, driver):
        driver.find_element_by_xpath(
            '//*[@id="app"]/section/section/main/div/div/div[2]/form/div[1]/div[1]/div[1]/div/div/input').send_keys(
            self.name)

    def Mature(self, driver):
        driver.find_element_by_xpath(
            '//*[@id="app"]/section/section/main/div/div/div[2]/form/div[1]/div[1]/div[2]/div/div/div/input').click()
        driver.find_element_by_xpath(
            '//*[@id="app"]/section/section/main/div/div/div[2]/form/div[1]/div[1]/div[2]/div/div/div/input').send_keys(
            self.maturity)
        driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/div[1]/ul/li/span[text()="' + self.maturity + '"]/..').click()

    def Pic(self, driver):
        driver.find_element_by_xpath(
            '//*[@id="app"]/section/section/main/div/div/div[2]/form/div[1]/div[2]/div/div/div/div/div/input').send_keys(
            self.picpath)

    def Area(self, driver):
        driver.find_element_by_xpath(
            '//*[@id="app"]/section/section/main/div/div/div[2]/form/div[1]/div[1]/div[4]/div/div/div[1]/input').click()
        self.list_click(driver,self.area)


    def University(self, driver):
        # province
        driver.find_element_by_xpath('//input[@placeholder="请选择省"]').click()
        time.sleep(2)
        self.list_click(driver, self.province)

        # city
        driver.find_element_by_xpath(
            '//*[@id="app"]/section/section/main/div/div/div[2]/form/div[3]/div[1]/div[2]/div/div/div/input').click()
        driver.find_element_by_xpath(
            '//*[@id="app"]/section/section/main/div/div/div[2]/form/div[3]/div[1]/div[2]/div/div/div/input').send_keys(
            self.city)
        time.sleep(2)
        self.list_click(driver, self.city)
        # university

        driver.find_element_by_xpath(
            '//*[@id="app"]/section/section/main/div/div/div[2]/form/div[3]/div[1]/div[3]/div/div/div[1]/input').click()
        time.sleep(3)
        self.list_click(driver, self.university)

    def Inventer(self, driver):
        # make owners list
        owners = self.owners[0].split(';')
        driver.find_element_by_xpath('//input[@placeholder="请选择专家姓名（单选）"]').click()
        time.sleep(2)
        inventors = [i.text for i in driver.find_elements_by_xpath('/html/body/div[7]/div[1]/div[1]/ul//li')]
        if owners[0] in inventors:
            for i in range(len(inventors)):
                if owners[0] == inventors[i]:
                    driver.find_element_by_xpath('//input[@placeholder="请选择专家姓名（单选）"]').send_keys(inventors[i])
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/div[7]/div[1]/div[1]/ul/li[' + str(i + 1) + ']').click()
                    break
        else:
            driver.find_element_by_xpath('//input[@placeholder="请选择专家姓名（单选）"]').send_keys(self.university)
            time.sleep(2)
            driver.find_element_by_xpath(
                '/html/body/div[7]/div[1]/div[1]/ul/li/span[text()="' + self.university + '"]').click()

    def Introduction(self, driver):
        driver.find_element_by_xpath('//*[@id="quill-container"]/div[1]').send_keys(self.intro)

    def PatentNo(self, driver):
        driver.find_element_by_xpath(
            '//*[@id="app"]/section/section/main/div/div/div[2]/form/div[5]/div/div[5]/div/div/input').send_keys(
            str(self.no))

    def Submit(self, driver):
        driver.find_element_by_xpath(
            '//*[@id="app"]/section/section/main/div/div/div[2]/form/div[10]/div/div/button/span').click()

    def list_click(self, driver, widget_name):

        if widget_name == '其他':
            ActionChains(driver).move_to_element(
                driver.find_element_by_xpath(
                    '(//span[text()="其他"])[2]')).click(
                driver.find_element_by_xpath(
                    '(//span[text()="其他"])[2]')).perform()
        elif widget_name=='华中师范大学':

            try:
                ActionChains(driver).move_to_element(
                    driver.find_element_by_xpath(
                        '//span[text()="华中师范大学"]')).click(
                    driver.find_element_by_xpath(
                        '//span[text()="华中师范大学"]')).perform()
            except Exception as ec:
                print(ec.value)

        else:


            ActionChains(driver).move_to_element(
                driver.find_element_by_xpath(
                    '//span[text()="' + widget_name + '"]')).click(
                driver.find_element_by_xpath(
                    '//span[text()="' + widget_name + '"]')).perform()


if __name__ == '__main__':

    driver = webdriver.Chrome(r'C:\Users\chromedriver.exe')
    driver.implicitly_wait(3)
    login(driver)
    datas = pandas.read_excel(r'C:\Users\\PycharmProjects\crawler\workspace\wu.xlsx', header=0, index_col=0,
                              engine='openpyxl')
    print("开始导入")
    for data in datas.iterrows():
        data = Patent([data[0]] + data[1].values.tolist())
        print('start', data.index)
        main(data)
        print('done')
    print("导入完成")
