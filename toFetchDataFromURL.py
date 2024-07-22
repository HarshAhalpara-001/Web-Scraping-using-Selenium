import sqlite3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Database setup
db_path = 'web_data.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    brand TEXT,
    manufacturer TEXT,
    series TEXT,
    colour TEXT,
    form_factor TEXT,
    standing_screen_display_size TEXT,
    screen_resolution TEXT,
    resolution TEXT,
    package_dimensions TEXT,
    batteries TEXT,
    item_model_number TEXT,
    processor_brand TEXT,
    processor_type TEXT,
    processor_speed TEXT,
    processor_count TEXT,
    ram_size TEXT,
    memory_technology TEXT,
    computer_memory_type TEXT,
    maximum_memory_supported TEXT,
    memory_clock_speed TEXT,
    hard_drive_size TEXT,
    hard_disk_description TEXT,
    audio_details TEXT,
    graphics_coprocessor TEXT,
    graphics_chipset_brand TEXT,
    graphics_card_description TEXT,
    graphics_ram_type TEXT,
    graphics_card_ram_size TEXT,
    graphics_card_interface TEXT,
    connectivity_type TEXT,
    wireless_type TEXT,
    number_of_usb_2_ports TEXT,
    number_of_usb_3_ports TEXT,
    voltage TEXT,
    optical_drive_type TEXT,
    operating_system TEXT,
    average_battery_life TEXT,
    are_batteries_included TEXT,
    lithium_battery_energy_content TEXT,
    number_of_lithium_ion_cells TEXT,
    included_components TEXT,
    item_weight TEXT
)
""")

# Selenium setup
driver = webdriver.Edge()

def find_element_text(xpath):
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        return element.text
    except Exception as e:
        # print(f"Error finding element with XPath {xpath}: {e}")   # if you want to see error as attribute is not there it will set None but if want to know which attribut it is then uncomment 
        return None

def insert_data(data):
    cursor.execute("""
        INSERT INTO products (
            brand, manufacturer, series, colour, form_factor, standing_screen_display_size, screen_resolution, resolution,
            package_dimensions, batteries, item_model_number, processor_brand, processor_type, processor_speed, processor_count,
            ram_size, memory_technology, computer_memory_type, maximum_memory_supported, memory_clock_speed, hard_drive_size,
            hard_disk_description, audio_details, graphics_coprocessor, graphics_chipset_brand, graphics_card_description,
            graphics_ram_type, graphics_card_ram_size, graphics_card_interface, connectivity_type, wireless_type,
            number_of_usb_2_ports, number_of_usb_3_ports, voltage, optical_drive_type, operating_system, average_battery_life,
            are_batteries_included, lithium_battery_energy_content, number_of_lithium_ion_cells, included_components, item_weight
        ) VALUES (
            :brand, :manufacturer, :series, :colour, :form_factor, :standing_screen_display_size, :screen_resolution, :resolution,
            :package_dimensions, :batteries, :item_model_number, :processor_brand, :processor_type, :processor_speed, :processor_count,
            :ram_size, :memory_technology, :computer_memory_type, :maximum_memory_supported, :memory_clock_speed, :hard_drive_size,
            :hard_disk_description, :audio_details, :graphics_coprocessor, :graphics_chipset_brand, :graphics_card_description,
            :graphics_ram_type, :graphics_card_ram_size, :graphics_card_interface, :connectivity_type, :wireless_type,
            :number_of_usb_2_ports, :number_of_usb_3_ports, :voltage, :optical_drive_type, :operating_system, :average_battery_life,
            :are_batteries_included, :lithium_battery_energy_content, :number_of_lithium_ion_cells, :included_components, :item_weight
        )
    """, data)

with open('output.txt', 'r') as file:
    for line in file.readlines():
        driver.get(line.strip())
        time.sleep(0)  # Allow the page to load

        data = {
            "brand": find_element_text("//*[contains(text(), 'Brand')]/following-sibling::td") or 'NULL',
            "manufacturer": find_element_text("//*[contains(text(), 'Manufacturer')]/following-sibling::td") or 'NULL',
            "series": find_element_text("//*[contains(text(), 'Series')]/following-sibling::td") or 'NULL',
            "colour": find_element_text("//*[contains(text(), 'Colour')]/following-sibling::td") or 'NULL',
            "form_factor": find_element_text("//*[contains(text(), 'Form Factor')]/following-sibling::td") or 'NULL',
            "standing_screen_display_size": find_element_text("//*[contains(text(), 'Standing screen display size')]/following-sibling::td") or 'NULL',
            "screen_resolution": find_element_text("//*[contains(text(), 'Screen Resolution')]/following-sibling::td") or 'NULL',
            "resolution": find_element_text("//*[contains(text(), 'Resolution')]/following-sibling::td") or 'NULL',
            "package_dimensions": find_element_text("//*[contains(text(), 'Package Dimensions')]/following-sibling::td") or 'NULL',
            "batteries": find_element_text("//*[contains(text(), 'Batteries')]/following-sibling::td") or 'NULL',
            "item_model_number": find_element_text("//*[contains(text(), 'Item model number')]/following-sibling::td") or 'NULL',
            "processor_brand": find_element_text("//*[contains(text(), 'Processor Brand')]/following-sibling::td") or 'NULL',
            "processor_type": find_element_text("//*[contains(text(), 'Processor Type')]/following-sibling::td") or 'NULL',
            "processor_speed": find_element_text("//*[contains(text(), 'Processor Speed')]/following-sibling::td") or 'NULL',
            "processor_count": find_element_text("//*[contains(text(), 'Processor Count')]/following-sibling::td") or 'NULL',
            "ram_size": find_element_text("//*[contains(text(), 'RAM Size')]/following-sibling::td") or 'NULL',
            "memory_technology": find_element_text("//*[contains(text(), 'Memory Technology')]/following-sibling::td") or 'NULL',
            "computer_memory_type": find_element_text("//*[contains(text(), 'Computer Memory Type')]/following-sibling::td") or 'NULL',
            "maximum_memory_supported": find_element_text("//*[contains(text(), 'Maximum Memory Supported')]/following-sibling::td") or 'NULL',
            "memory_clock_speed": find_element_text("//*[contains(text(), 'Memory Clock Speed')]/following-sibling::td") or 'NULL',
            "hard_drive_size": find_element_text("//*[contains(text(), 'Hard Drive Size')]/following-sibling::td") or 'NULL',
            "hard_disk_description": find_element_text("//*[contains(text(), 'Hard Disk Description')]/following-sibling::td") or 'NULL',
            "audio_details": find_element_text("//*[contains(text(), 'Audio Details')]/following-sibling::td") or 'NULL',
            "graphics_coprocessor": find_element_text("//*[contains(text(), 'Graphics Coprocessor')]/following-sibling::td") or 'NULL',
            "graphics_chipset_brand": find_element_text("//*[contains(text(), 'Graphics Chipset Brand')]/following-sibling::td") or 'NULL',
            "graphics_card_description": find_element_text("//*[contains(text(), 'Graphics Card Description')]/following-sibling::td") or 'NULL',
            "graphics_ram_type": find_element_text("//*[contains(text(), 'Graphics RAM Type')]/following-sibling::td") or 'NULL',
            "graphics_card_ram_size": find_element_text("//*[contains(text(), 'Graphics Card Ram Size')]/following-sibling::td") or 'NULL',
            "graphics_card_interface": find_element_text("//*[contains(text(), 'Graphics Card Interface')]/following-sibling::td") or 'NULL',
            "connectivity_type": find_element_text("//*[contains(text(), 'Connectivity Type')]/following-sibling::td") or 'NULL',
            "wireless_type": find_element_text("//*[contains(text(), 'Wireless Type')]/following-sibling::td") or 'NULL',
            "number_of_usb_2_ports": find_element_text("//*[contains(text(), 'Number of USB 2.0 Ports')]/following-sibling::td") or 'NULL',
            "number_of_usb_3_ports": find_element_text("//*[contains(text(), 'Number of USB 3.0 Ports')]/following-sibling::td") or 'NULL',
            "voltage": find_element_text("//*[contains(text(), 'Voltage')]/following-sibling::td") or 'NULL',
            "optical_drive_type": find_element_text("//*[contains(text(), 'Optical Drive Type')]/following-sibling::td") or 'NULL',
            "operating_system": find_element_text("//*[contains(text(), 'Operating System')]/following-sibling::td") or 'NULL',
            "average_battery_life": find_element_text("//*[contains(text(), 'Average Battery Life')]/following-sibling::td") or 'NULL',
            "are_batteries_included": find_element_text("//*[contains(text(), 'Are Batteries Included')]/following-sibling::td") or 'NULL',
            "lithium_battery_energy_content": find_element_text("//*[contains(text(), 'Lithium Battery Energy Content')]/following-sibling::td") or 'NULL',
            "number_of_lithium_ion_cells": find_element_text("//*[contains(text(), 'Number of Lithium Ion Cells')]/following-sibling::td") or 'NULL',
            "included_components": find_element_text("//*[contains(text(), 'Included Components')]/following-sibling::td") or 'NULL',
            "item_weight": find_element_text("//*[contains(text(), 'Item Weight')]/following-sibling::td") or 'NULL'
        }

        insert_data(data)
        conn.commit()

# Close the driver and the database connection
driver.quit()
cursor.close()
conn.close()
