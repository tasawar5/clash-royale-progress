# Clash Royale Progress

## Requirements
- requires chrome driver in the same directory
- install packages
```
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

## Some useful selenium functions
```
Useful Functions
driver.get(URL)
element = driver.find_element_by_id("elementID")
element.send_keys("entering text in text field")
element.send_keys(Keys.RETURN)
element.click()
driver.switch_to.frame(driver.find_element_by_id("iframeID"))
driver.switch_to.frame(0)
element = driver.find_element_by_class_name("className")
element.text
driver.switch_to.parent_frame()
driver.close()
```