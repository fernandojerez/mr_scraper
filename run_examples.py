from example import dispatchers
from mr_scraper import api

# Uncomment this line to set the chrome path by default is chromium-browser
api.PUPPETEER_CHROME_PATH = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

if __name__ == '__main__':
    dispatchers.levels_fyi()
