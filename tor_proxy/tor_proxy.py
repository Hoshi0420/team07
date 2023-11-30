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