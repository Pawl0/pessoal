import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
import time

string=''

def case_1():
    string = input('Digite sua mensagem (entre aspas): ')
    inp_xpath = '//div[@class="input"][@data-tab="1"]'
    input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))
    input_box.send_keys(string + Keys.RETURN)
def case_2():
    target = input('Digite o alvo(sem aspas): ')
    print("Target: ") 
    print(target)
    try:       
        x_arg = '//span[contains(@title,' + target + ')]'      
        group_title = wait.until(EC.presence_of_element_located((
        By.XPATH, x_arg)))
        print("Element located")
        group_title.click()
        inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
        input_box = wait.until(EC.presence_of_element_located((
        By.XPATH, inp_xpath)))
    except WebDriverException:
        print('\n\nElemento não visível na tela!\n\n')

def case_3():
    target = input('Digite o alvo: ')
    print("Target: ") 
    print(target)
    try:
        inp_xpath_search = '//*[@id="side"]/div[2]/div/label/input'
        input_box_search = wait.until(EC.presence_of_element_located((
        By.XPATH, inp_xpath_search)))
        input_box_search.click()
        input_box_search.send_keys(target + Keys.RETURN)
        x_arg = '//span[contains(@title,' + target + ')]'   
        print("Element located!")
        inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
        input_box = wait.until(EC.presence_of_element_located((
        By.XPATH, inp_xpath)))
    except WebDriverException:
        print('\n\nElemento não encontrado!\n\n')

def case_4():
    message_xpath= '//*[@id="main"]/div[2]/div/div/div[3]/div[last()]/div/div/div/div[1]/span[2]' 
    mensagem = driver.find_element_by_xpath(message_xpath)
    print(mensagem.text)
    
def case_default():
    print('Opção inválida')
    try:
        driver.close()
    except WebDriverException:
        print('Sessão encerrada')

#cria um dicionário que relaciona cada função com a opção desejada
dict = {'1' : case_1, '2' : case_2, '3' : case_3, '4' : case_4, '0' : case_default}

driver = webdriver.Chrome()
driver.get("http://web.whatsapp.com")
wait = WebDriverWait(driver, 100)
print("Ready")

while True:
    num = input('Digite sua opção \n(1) Digitar mensagem \n(2) Escolher novo alvo \n(3) Buscar contato \n(4) Ler última mensagem\n(0) Sair\nOpção: ')
    dict[num]()
    #time.sleep(1)
    if num == '0':
        break
