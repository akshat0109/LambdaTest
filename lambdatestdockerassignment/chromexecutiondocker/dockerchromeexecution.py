import time
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import boto3

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_KEY_ID = ''
AWS_BUCKET = ''


def chrome_browser(url):
    try:
        options = Options()
        options.headless = True
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get(url)
        time.sleep(10)
        temp_path = 'pic2.png'
        driver.get_screenshot_as_file(temp_path)
        driver.quit()
        print("Chrome process executed successfully")
        key_name = str(int(time.time())) + '.png'
        s3_client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_KEY_ID)
        s3_client.upload_file(temp_path, AWS_BUCKET, key_name)
        url = s3_client.generate_presigned_url(ClientMethod='get_object', Params={'Bucket': AWS_BUCKET, 'Key': key_name},
                                               ExpiresIn=1800)
        print(url)
    except Exception as e:
        print("Error in chrome browser execution {}".format(e))
        print(traceback.format_exc())

with open('output.txt', 'r') as file:
    data = file.read().replace('\n', '')
    chrome_browser(data)
    file.close()

