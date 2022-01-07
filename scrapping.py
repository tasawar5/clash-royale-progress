from selenium import webdriver
from selenium.webdriver.common.keys import Keys

webdriverPath = './chromedriver'
driver = webdriver.Chrome(webdriverPath)

DOMAIN = 'https://royaleapi.com/'
PLAYER_ID = '9ULUJCPGY'

driver.get(DOMAIN + 'player/'+ PLAYER_ID +'/cards/levels')

cards_image = driver.find_elements_by_xpath("//div[@class='player_cards__card_item']/img")
cards_level = driver.find_elements_by_xpath("//div[@class='player_cards__card_item']/div[1]")
cards_rarity = driver.find_elements_by_xpath("//a[@class='player_card_link player_card_item']")
cards_count = driver.find_elements_by_xpath("//div[@class='ui link card_upgrades']")

index = 0
while index < len(cards_image):
    print(index+1, cards_rarity[index].get_attribute('data-rarity-id'), cards_level[index].text, cards_count[index].text, cards_image[index].get_attribute('alt'))
    index += 1

driver.close()