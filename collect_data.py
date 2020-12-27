import time

from selenium import webdriver
from selenium.webdriver.support.select import Select


class Lottery:
    """
    Class that represents a Lottery scraper.

    It collects data for 6/49 Bulgarian Lottery History.

    Resources: https://bgtoto.com/6ot49_arhiv.php

    Tips & Tricks

    Edit executable_path with the location of chromedriver.exe on your system.

    Install the newest version of chromedriver.exe depending on your current version of Chrome.

    You can check your Chrome version here: https://www.whatismybrowser.com/detect/what-version-of-chrome-do-i-have

    You can download chromedriver.exe here: https://chromedriver.chromium.org/downloads

    Your current version of Chrome and chromedriver.exe must match for the script to run properly.

    You can edit start_year and end_year depending on the selection you want to make.

    """
    executable_path = "D://chromedriver.exe"
    toto_archive_page = "https://bgtoto.com/6ot49_arhiv.php"
    start_year = 1959
    end_year = 2020

    def __init__(self):
        """
        Initialize Selenium Chrome driver from executable path.
        """

        self.driver = webdriver.Chrome(executable_path=self.executable_path)

    def initialize_main_page(self):
        """
        Open lottery archive page.

        :return:
        """

        self.driver.get(self.toto_archive_page)

    def write_to_txt(self, year, week, winning_numbers):
        """
        Function to write the year, week and winning numbers to
        a txt file.

        :param year:
        :param week:
        :param winning_numbers:
        :return:
        """

        with open("toto_6x49.txt", "a") as f:
            to_write = f"{year},{week},{winning_numbers} \n"
            f.write(to_write)

    def collect_data_for_year(self, year):
        """
        Function that collects winning numbers for all weeks for
        the selected year.

        :param year:
        :return:
        """

        table = self.driver.find_element_by_xpath("//table[@bordercolor='#CCCCCC']")
        rows = table.find_elements_by_xpath(".//tr[@align='center']")

        for row in rows:
            columns = row.find_elements_by_xpath(".//td")
            week = columns[0].text
            winning_numbers = columns[1].text

            week = ''.join(i for i in week if i.isdigit())

            self.write_to_txt(year, week, winning_numbers)

    def get_data(self):
        """
        The function finds the select button for different years.
        It loops over all years between the start_year and end_year.
        It selects year, presses the submit button aand calls
        collect_data_for_year() to collect the updated table with
        weeks and winning numbers.

        :return:
        """

        self.driver.find_element_by_xpath("//select[@name='g']")

        for year in range(self.start_year, self.end_year + 1):
            select = Select(self.driver.find_element_by_xpath("//select[@name='g']"))
            # select by value
            select.select_by_value(str(year))
            # press submit
            self.driver.find_element_by_xpath("//input[@id='Submit']").click()
            time.sleep(1)
            self.collect_data_for_year(str(year))

    def run(self):
        """
        Function to that executes scrape logic.

        :return:
        """

        self.initialize_main_page()
        self.get_data()


if __name__ == '__main__':
    lottery = Lottery()
    lottery.run()
