# - 1: Intru pe site-ul https://www.elefant.ro/

from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Initializare chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.maximize_window()

chrome.get('https://www.elefant.ro/')
sleep(5)

accept_button = chrome.find_element(By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')
accept_button.click()
sleep(5)

# - 2: Caut un produs la alegere (iphone 14) si verific ca s-au returnat cel putin 10 rezultate
# ([class="product-title"])
search_box2 = chrome.find_element(By.XPATH, '/html/body/header/div[1]/nav/div/div[4]/div/div[1]/form/input[1]')
search_box2.send_keys('iphone 14')
sleep(5)

search_button2 = chrome.find_element(By.XPATH, '/html/body/header/div[1]/nav/div/div[4]/div/div[1]/form/button/span')
search_button2.click()
sleep(4)
returned_result = chrome.find_element(By.XPATH, '/html/body/div[3]/div/div[14]/div[2]/div[2]/div/div[2]/div[2]').text
        # Definesc o functie for prin care o sa extrag partea numerica din textul afisat ("217 produse")

res = [int(i) for i in returned_result.split() if i.isdigit()]
print(f'{str(res)}')
print(f'----------------------------------------------')
print(f"Numar de produse gasite: {str(res)}")
        # Verific daca au fost gasite mai mult de 10 rezultate
lowest_number = '10'
if str(res) > lowest_number:
    print(f"Au fost gasite mai mult de {lowest_number} produse ce corespund criteriului de cautare.")
else:
    print(f"Nu au fost returnate suficiente rezultate in urma cautarii.")


# - 3: Extrageti din lista produsul cu prețul cel mai mic [class="current-price "]
# (puteti sa va folositi de find_elements)
chrome.find_element(By.ID, 'SortingAttribute').click()
sleep(3)
chrome.find_element(By.CSS_SELECTOR, '#SortingAttribute > option:nth-child(4)').click()
sleep(3)

product_name = chrome.find_element(By.XPATH, '/html/body/div[3]/div/div[14]/div[2]/div[5]/div[1]/div[1]/div/div/div[3]/div[2]').text
print(f'Produsul cel mai ieftin este: ')
print(f'>>> {product_name} <<<')

# - 4: Extrag titlul paginii si verific ca este corect (hint: se foloseste metoda title)
chrome.get('https://www.elefant.ro/')
correct_title = 'elefant.ro - mallul online al familiei tale! • Branduri de top, preturi excelente • Peste 500.000 de produse pentru tine!'
found_title = chrome.title
try:
    assert found_title == correct_title
    print('Titlul este corect.')
except:
    print('Titlul este incorect.')
    print(f'Cautam ca titlul sa fie urmatorul: >>> {correct_title}')

# - 5: Intru pe site si dau click pe butonul conectare. Identific elementele de tip user si parola
# si inserez valori incorecte (valori incorecte inseamna oricare valori care nu sunt recunoscute drept cont valid)
#   Ce tip de testare se aplica aici?
#   - Dam click pe butonul "conectare" si se verifica urmatoarele:
#                 1. Faptul ca nu s-a facut logarea in cont
#                 2. Faptul ca se returneaza eroarea corecta

chrome.get('https://www.elefant.ro/')
connect_button1 = chrome.find_element(By.CSS_SELECTOR, 'span[class = "login-prompt js-login-prompt"')
connect_button1.click()
sleep(3)
connect_button2 = chrome.find_element(By.CSS_SELECTOR, 'a[class = "my-account-login btn btn-primary btn-block"')
connect_button2.click()
sleep(3)
user_email = chrome.find_element(By.CSS_SELECTOR, 'input[placeholder = "Email"')
user_email.send_keys('32321321@gmail.com')
sleep(3)
user_pass = chrome.find_element(By.CSS_SELECTOR, 'input[placeholder = "Parola"')
user_pass.send_keys('23123321')
sleep(3)
connect_user = chrome.find_element(By.CSS_SELECTOR, 'button[name = "login"')
connect_user.click()
sleep(3)

alert = chrome.find_element(By.CSS_SELECTOR, 'div[role = "alert"').text
print(f'{alert}')
assert alert == 'Adresa dumneavoastră de email / Parola este incorectă. Vă rugăm să încercați din nou.'
print(f'Mesajul de eroare este corect.')

# - 6: Sterg valoarea de pe campul email si introduc o valoare invalida (adica fara caracterul "@")
# si verific faptul ca butonul "conectare" este dezactivat (hint: se foloseste metoda isEnabled)

chrome.get('https://www.elefant.ro/')
connect_button3 = chrome.find_element(By.CSS_SELECTOR, 'span[class = "login-prompt js-login-prompt"')
connect_button3.click()
sleep(3)
second_connect_button = chrome.find_element(By.CSS_SELECTOR, 'a[class = "my-account-login btn btn-primary btn-block"')
second_connect_button.click()
sleep(3)
user_email = chrome.find_element(By.CSS_SELECTOR, 'input[placeholder = "Email"')
user_email.send_keys('32321321gmail.com')
sleep(3)
login_button = chrome.find_element(By.CSS_SELECTOR, 'button[value = "Login"')
try:
    assert login_button.is_enabled()
    print("Butonul este activat.")
except:
    print("Butonul este dezactivat.")