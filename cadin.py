from selenium import webdriver
from selenium.webdriver.common.keys import Keys


if __name__ == '__main__':
    driver = webdriver.Chrome()    driver.get(
        'https://siafi.tesouro.gov.br/senha/public/pages/security/login.jsf'
    )
    assert driver.title == 'Privacy error'
    driver.find_element_by_id('details-button').click()
    driver.find_element_by_id('proceed-link').click()
    driver.implicitly_wait(5)

    assert 'SIAFI' in driver.title
    username = driver.find_element_by_id('j_username')
    username.send_keys('')
    password = driver.find_element_by_id('j_password')
    password.send_keys('')
    captcha = driver.find_element_by_id('j_captcha')
    captcha.click()
    captcha.send_keys(input('Digite o captcha: '))
    driver.find_element_by_id('submitNormal').click()
    driver.find_element_by_id('frmTemplateAcesso:btnConcordar').click()
    search = driver.find_element_by_id('frmMenu:acessoRapido')
    search.send_keys('cadin')
    driver.find_element_by_id(
        'frmMenu:botaoAcessoRapidoVerificaTipoTransacao'
    ).click()
    driver.find_element_by_id(
        'formCadin:inputCodigo_input'
    ).send_keys(input('Digite o radical do CNPJ: '))
    driver.find_element_by_id('formCadin:btnPesquisar').click()
    driver.find_element_by_id('formCadin:btnGerarArquivo').click()
    driver.find_element_by_class_name('exit').click()
    pass
