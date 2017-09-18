import argparse
import os
import time
from selenium import webdriver


if __name__=="__main__":

    # Get and parese the given words
    parser = argparse.ArgumentParser(description="Gather google trends csv for given word")
    parser.add_argument("word",type=str,help="Word to search google trends with, and to name the file")
    args = parser.parse_args()

    # Base google trends url
    base_url = "https://trends.google.com/trends/explore?date=now%201-d&q="

    # Gather the words to be search
    search_word = args.word.replace(" ","%20")

    # Put the whole url together
    url = base_url+search_word

    # Create an instance of the browser and gat the page
    driver = webdriver.Chrome()
    driver.get(url)

    # Stop and let load
    time.sleep(1)

    # Scroll down some to make sure the tool bar loads
    driver.execute_script("window.scrollTo(0,175);")

    # Stop and let the things load
    time.sleep(2)

    # Try to click the drop down menu then the download button
    try:
        driver.find_element_by_class_name("widget-action-menu").click()
        driver.find_element_by_class_name("csv-image").click()
    except:
        time.sleep(1)

    # Try to click the downlad button directly on the top of the chart
    try:
        driver.find_element_by_class_name("widget-actions-item").click()
    except:
        time.sleep(1)

    # Shut down browser
    driver.close()

    # Put together what the file will be named
    filename = args.word.replace(" ","_")+".csv"

    # Try to rename file, if there is no file print out no data pulled
    try:
        os.rename("multiTimeline.csv",filename)
    except:
        print("No data was pulled!")
        



