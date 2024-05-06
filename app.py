import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def crawl_products(url):
    """
    셀레니움을 사용하여 제품 정보를 크롤링하고 JSON으로 출력합니다.

    Args:
        url: 크롤링할 URL

    Returns:
        JSON 형식의 제품 정보 문자열
    """

    # 크롬 드라이버 설정 (최신 버전으로 자동 업데이트)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # URL로 이동
    driver.get(url)

    time.sleep(8)

    # 제품 목록 컨테이너 찾기
    product_list = driver.find_elements(By.CSS_SELECTOR, "ul.trading-items-container li")

    products = []
    for product in product_list:
        try:
            # 제품 정보 추출
            name = product.find_element(By.CSS_SELECTOR, ".name").text
            style_code = product.find_element(By.CSS_SELECTOR, ".style-code").text
            option = product.find_element(By.CSS_SELECTOR, ".option").text
            current_price = product.find_element(By.CSS_SELECTOR, ".current-price").text
            change_price = product.find_element(By.CSS_SELECTOR, ".change-price").text
            change_percent = product.find_element(By.CSS_SELECTOR, ".change-percent").text

            # 제품 정보를 사전 형태로 저장
            product_info = {
                "name": name,
                "style_code": style_code,
                "option": option,
                "current_price": current_price,
                "change_price": change_price,
                "change_percent": change_percent
            }
            products.append(product_info)

        except Exception as e:
            print(f"제품 정보 추출 실패: {e}")

    # 드라이버 종료
    driver.quit()

    # 제품 정보를 JSON 형식으로 변환
    json_data = json.dumps(products, ensure_ascii=False, indent=4) 
    
    return json_data

# 크롤링할 URL 입력
url = "https://kream.co.kr/trading-chart"  # 예시 URL

# 제품 정보 크롤링 및 JSON 출력
json_output = crawl_products(url)
print(json_output)