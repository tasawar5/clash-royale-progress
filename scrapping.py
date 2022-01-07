from selenium import webdriver
from selenium.webdriver.common.keys import Keys

DOMAIN = 'https://royaleapi.com/'
PLAYER_ID = '9ULUJCPGY'
RARITY = {
    '0': 'Common Card',
    '1': 'Rare Card',
    '2': 'Epic Card',
    '3': 'Legendary Card'
}


def scrap_and_transform_data():
    webdriverPath = './chromedriver'
    driver = webdriver.Chrome(webdriverPath)

    driver.get(DOMAIN + 'player/'+ PLAYER_ID +'/cards/levels')

    cards_image = driver.find_elements_by_xpath("//div[@class='player_cards__card_item']/img")
    cards_level = driver.find_elements_by_xpath("//div[@class='player_cards__card_item']/div[1]")
    cards_rarity = driver.find_elements_by_xpath("//a[@class='player_card_link player_card_item']")
    cards_count = driver.find_elements_by_xpath("//div[@class='ui link card_upgrades']")

    cards_detail = []
    for img, rarity_level, level, card_count in zip(cards_image, cards_rarity, cards_level, cards_count):
        
        name = img.get_attribute('alt')
        rarity_level = rarity_level.get_attribute('data-rarity-id')
        level = int(level.text.split()[1])
        card_count = card_count.text.split(' / ')[0].replace(',', '')
        
        cards_detail.append({
            "Name": name,
            "Rarity Level": int(rarity_level),
            "Rarity": RARITY[rarity_level],
            "Level": level,
            "Card Count":  int(card_count) if card_count != 'MAX' else 0
        })
    
    driver.close()
    return cards_detail

cards_detail = scrap_and_transform_data()
cards_detail.sort(key=lambda card: (int(card["Rarity Level"]), int(card["Level"]), int(card["Card Count"])))

for card in cards_detail:
    print ("{:<20} {:<20} {:<10} {:<20}".format(card['Name'], card['Rarity'], card['Level'], card['Card Count']))
