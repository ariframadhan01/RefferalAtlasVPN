# Requirements time, requests, colorama, bs4, selenium

import time, requests
from colorama import Fore
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.headless = True
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('--log-level=3')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument('--ignore-certificate-errors')
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        
def main(kode):
    m = 0
    try:
        while True:
        # Generate Random Email
            url = 'https://generator.email/'
            umail = requests.get(url)
            soup = BeautifulSoup(umail.content, 'html.parser')
            email = soup.find(id='email_ch_text').text
            ml = url+email

        # Sennding Reff
            sf = 'https://user.atlasvpn.com/v1/request/join'
            hulu = {"Accept": "application/json, text/plain, */*", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9", "Origin": "https://account.atlasvpn.com", "Referer": "https://account.atlasvpn.com/", "Sec-Ch-Ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Windows\"", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36", "X-Client-Id": "Web", "Content-Type": "application/json;charset=UTF-8"}
            isi = {"email": email,"marketing_consent": True,"referrer_uuid": kode,"referral_offer": "initial"}
            x = requests.post(sf, json=isi, headers=hulu)
            print('[\033[32m', time.strftime('%H:%M:%S', time.localtime()), '\033[93m] Sending Request...')
            time.sleep(2)

        # Getting Token
            browser.get(ml)
            browser.refresh()
            val = browser.find_element(By.XPATH, '//*[@id="email-table"]/div[2]/div[4]/div[3]/center/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table[5]/tbody/tr/td/table/tbody/tr/td/a')
            cek = val.get_attribute('href')
            dor = requests.get(cek)
            tkn = cek.replace('https://account.atlasvpn.com/auth?client=Web&token=', '')
            print('[\033[32m', time.strftime('%H:%M:%S', time.localtime()), '\033[93m] Try Getting Token...')

        # Verified Email
            m += 1
            app = 'https://user.atlasvpn.com/v1/auth/confirm'
            air = {"Accept": "application/json, text/plain, */*", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9", "Authorization": "Bearer "+str(tkn)+"", "Origin": "https://account.atlasvpn.com", "Referer": "https://account.atlasvpn.com/", "Sec-Ch-Ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Windows\"", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
            dor = requests.get(app, headers=air)
            print('[\033[32m', time.strftime('%H:%M:%S', time.localtime()), '\033[93m] Success adding {} refferal!!!'.format(m))
    except:
            print(Fore.RED+'Unknown Error! Restarting Program...')
            return main(kode)
    
if __name__ == '__main__':
    print(Fore.CYAN+'[-]--------------------------AtlasVPN Ultimate Reff--------------------------[-]')
    print(Fore.CYAN+'[-]                              By Arif Ramadhan                            [+]')
    print(Fore.CYAN+'[x]--------------------------------------------------------------------------[x]'+Fore.RESET)
    kode = input('Input your User ID: ')
    main(kode)