# Lottery_6x49
Data Collection project to get historical data of all winning numbers in the Bulgarian Lottery 6/49.

The script collects data for 6/49 Bulgarian Lottery History.

Resources: https://bgtoto.com/6ot49_arhiv.php

Tips & Tricks

Edit executable_path with the location of chromedriver.exe on your system.

Install the newest version of chromedriver.exe depending on your current version of Chrome.

You can check your Chrome version here:
https://www.whatismybrowser.com/detect/what-version-of-chrome-do-i-have
    
You can download chromedriver.exe here:
https://chromedriver.chromium.org/downloads
    
Your current version of Chrome and chromedriver.exe must match for the script to run properly.
    
You can edit start_year and end_year depending on the selection you want to make.

The toto_6x49.txt file contains all records from 1959 to 2020. It saves each record on a new line in the following format:
< year >,< lottery drawing number >, <the 6 winning numbers>
