from selenium import webdriver  
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
import requests

def get_chrome_driver():
    """ 
        * This returns the default configuration for scrapping data
            - returns : chrome_driver
            - headless
            - performance": "ALL
    """
    # This Installs the ChromeDriver automatically to cache.
    s = Service(ChromeDriverManager().install())
    # * Chrome Options -
    chrome_options = webdriver.ChromeOptions()
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36"
    chrome_options.add_argument(f"user-agent={user_agent}")
    # chrome_options.add_argument('--disable-logging') 
    chrome_options.add_argument("--headless")  # headless mode

    desired_capabilities = DesiredCapabilities.CHROME
    desired_capabilities["goog:loggingPrefs"] = {"performance": "ALL"}

    driver = webdriver.Chrome(service=s, options=chrome_options, desired_capabilities=desired_capabilities)
    return driver


def scrap_all_index_urls():
    nse_index_stock_url = 'https://www1.nseindia.com/live_market/dynaContent/live_watch/equities_stock_watch.htm?cat=N'

     # return driver
    driver = get_chrome_driver()

    # * Get The Target Page
    driver.get(nse_index_stock_url)

    # dropdown > select-element
    select = Select(driver.find_element(By.ID,"bankNiftySelect"))

    all_index_urls = []

    for opt_ele in select.options:
        opt_ele.click()
        driver.implicitly_wait(3)
        time.sleep(1)
        log_entries = driver.get_log('performance')
      
        for _log in log_entries:
            try:
                message = _log['message'] # log message
                inner_msg = json.loads(message)['message'] # event message
                params = inner_msg['params'] # event params
                request = params['request']
                url = request['url']
                if "https://www1.nseindia.com/live_market/dynaContent/live_watch/stock_watch" in url:
                    # print(url)
                    all_index_urls.append(url)

            except Exception as E:
                # print("[err] : ", E)
                pass

    driver.close()
    driver.quit()

    return all_index_urls





if __name__ == '__main__':
    """
    * Get the page dropdown URLs
    - visit all pages
        - get all data and stocks
            - get those stock's token & market_segment_id
            - add them to mapper table and index table
    """
    print(scrap_all_index_urls())