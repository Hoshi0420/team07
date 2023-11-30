import socks
import socket
from stem import Signal
from stem.control import Controller
import requests

# Tor 프록시 설정
def set_tor_proxy():
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050, True)
    socket.socket = socks.socksocket

# 새로운 IP 주소 얻기
def renew_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)

def get_current_ip():
    response = requests.get("http://httpbin.org/ip")
    return response.json()["origin"]


if __name__ == "__main__":
    # 초기 IP 주소 확인
    initial_ip = get_current_ip()
    print("초기 IP 주소:", initial_ip)


    # Tor 프록시 설정
    set_tor_proxy()

    # 웹 페이지에 접근
    url = "https://www.youtube.com/"
    response = requests.get(url)
    #print("첫 번째 요청 결과:", response.text)
    # 현재 IP 주소 확인
    current_ip_after_first_request = get_current_ip()
    print("첫 번째 요청 후 IP 주소:", current_ip_after_first_request)
    
    
    
    
    
    
    
    
    
    
    
    
from stem import Signal
from stem.control import Controller
from selenium import webdriver
import time

# Tor 프록시 설정
tor_proxy = {
    'proxy': {
        'http': 'socks5://127.0.0.1:9050',
        'https': 'socks5://127.0.0.1:9050',
    }
}

# Tor 컨트롤러 설정
def renew_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)

# Selenium Firefox 드라이버 설정
def create_webdriver():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--proxy-server=socks5://127.0.0.1:9050')
    return webdriver.Firefox(options=firefox_options)

# Tor를 사용하여 IP 변경 및 Selenium으로 Firefox 실행
try:
    renew_tor_ip()

    # 몇 초 동안 기다려서 IP가 변경되기를 기다립니다.
    time.sleep(5)

    # Selenium으로 Firefox 실행
    driver = create_webdriver()
    driver.get('https://youtube.com')

    # 여기에 웹 페이지를 조작하는 코드를 추가하세요.

finally:
    # Selenium 드라이버 종료
    if 'driver' in locals():
        driver.quit()
        
        
from stem import Signal
from stem.control import Controller
from selenium import webdriver
import time

# Tor 프록시 설정
tor_proxy = {
    'proxy': {
        'http': 'socks5://127.0.0.1:9050',
        'https': 'socks5://127.0.0.1:9050',
    }
}

# Tor 컨트롤러 설정
def renew_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)

# Selenium Firefox 드라이버 설정
def create_webdriver():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--proxy-server=socks5://127.0.0.1:9050')
    firefox_options.add_argument('--headless')
    return webdriver.Firefox(options=firefox_options)

# Tor를 사용하여 IP 변경 및 Selenium으로 Firefox 실행
#try:
renew_tor_ip()

    # 몇 초 동안 기다려서 IP가 변경되기를 기다립니다.
time.sleep(5)

    # Selenium으로 Firefox 실행
driver = create_webdriver()
driver.get('https://www.youtube.com')
print(1)
    # 여기에 웹 페이지를 조작하는 코드를 추가하세요.
time.sleep(5)

#except Exception as e:
 #   print(f"An error occurred: {e}")

#finally:
    # Selenium 드라이버 종료
driver.quit()
