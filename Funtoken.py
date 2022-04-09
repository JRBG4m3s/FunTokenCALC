from datetime import date, datetime
from numpy import double
from selenium import webdriver as wd


def GetPrice(price):
    price = price.replace('R$', '')
    return price


def Valor(amount, price):
    value = amount * price
    return value


def Save_txt(price, amount, saldo):
    now = datetime.now()
    text = r'{} Quantidade: {} Preço: {} Total {}'

    return text.format(now, amount, price, saldo)


driver = wd.Firefox()
driver.get("https://coinmarketcap.com/pt-br/currencies/funtoken/")

fun_price = driver.find_element_by_xpath(
    '/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span').text
driver.quit()

fun_amount = input('Digite o valor:')
fun_value = GetPrice(fun_price)

saldo = Valor(double(fun_amount), double(fun_value))
print(saldo)

save = Save_txt(fun_price, fun_amount, saldo)
print(save)
arquivo = open('fun.txt', 'a')

arquivo.write(save + '\n')
arquivo.close()
