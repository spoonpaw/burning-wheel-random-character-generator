from webdriver_manager.chrome import ChromeDriverManager
import pyinputplus as pyip
import sys
from selenium import webdriver
import time
import random
import pyautogui
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.select import Select

continueRun = True

while continueRun:
    try:
        if raceChoice is not None:
            pass
        else:
            raceChoice = None
    except NameError:
        pass
    try:
        if lifePathNum is not None:
            pass
        else:
            lifePathNum = None
    except NameError:
        pass
    try:
        if genderNum is not None:
            pass
        else:
            genderNum = None
    except NameError:
        pass
    try:
        if lifePathNumber is not None:
            pass
        else:
            lifePathNumber = None
    except NameError:
        pass
    editMode = True
    while editMode:
        print('select a parameter to edit')
        print('1 - race')
        print('2 - number of lifepaths')
        print('3 - gender')
        print('4 - generate')
        print('5 - parameters so far')
        print('0 - exit')
        editChoiceInputNumber = pyip.inputNum()
        if editChoiceInputNumber < 0 or editChoiceInputNumber > 5:
            print('please enter a number between 1 and 5')
            continue
        elif editChoiceInputNumber == 0:
            sys.exit()
        elif editChoiceInputNumber == 1:
            raceEditMode = True
            while raceEditMode:
                print('select a race')
                print('1 - man')
                print('2 - dwarf')
                print('3 - elf')
                print('4 - orc')
                print('5 - roden')
                print('6 - great wolf')
                print('7 - troll')
                print('0 - exit')
                raceChoice = pyip.inputNum()
                if raceChoice < 0 or raceChoice > 7:
                    print('please enter a number between 1 and 7')
                    continue
                elif raceChoice == 0:
                    sys.exit()
                elif raceChoice == 1:
                    print('man chosen. would you like to make further adjustments? (y/n)')
                    raceName = 'man'
                    backToMenuAnswer = pyip.inputYesNo()
                    if backToMenuAnswer == 'yes':
                        raceEditMode = False
                    else:
                        raceEditMode = False
                        editMode = False
                elif raceChoice == 2:
                    print('dwarf chosen. would you like to make further adjustments? (y/n)')
                    raceName = 'dwarf'
                    backToMenuAnswer = pyip.inputYesNo()
                    if backToMenuAnswer == 'yes':
                        raceEditMode = False
                    else:
                        raceEditMode = False
                        editMode = False
                elif raceChoice == 3:
                    print('elf chosen. would you like to make further adjustments? (y/n)')
                    raceName = 'elf'
                    backToMenuAnswer = pyip.inputYesNo()
                    if backToMenuAnswer == 'yes':
                        raceEditMode = False
                    else:
                        raceEditMode = False
                        editMode = False
                elif raceChoice == 4:
                    print('orc chosen. would you like to make further adjustments? (y/n)')
                    raceName = 'orc'
                    backToMenuAnswer = pyip.inputYesNo()
                    if backToMenuAnswer == 'yes':
                        raceEditMode = False
                    else:
                        raceEditMode = False
                        editMode = False
                elif raceChoice == 5:
                    print('roden chosen. would you like to make further adjustments? (y/n)')
                    raceName = 'roden'
                    backToMenuAnswer = pyip.inputYesNo()
                    if backToMenuAnswer == 'yes':
                        raceEditMode = False
                    else:
                        raceEditMode = False
                        editMode = False
                elif raceChoice == 6:
                    print('great wolf chosen. would you like to make further adjustments? (y/n)')
                    raceName = 'great wolf'
                    backToMenuAnswer = pyip.inputYesNo()
                    if backToMenuAnswer == 'yes':
                        raceEditMode = False
                    else:
                        raceEditMode = False
                        editMode = False
                elif raceChoice == 7:
                    print('troll chosen. would you like to make further adjustments? (y/n)')
                    raceName = 'troll'
                    backToMenuAnswer = pyip.inputYesNo()
                    if backToMenuAnswer == 'yes':
                        raceEditMode = False
                    else:
                        raceEditMode = False
                        editMode = False

        elif editChoiceInputNumber == 2:
            lifePathEditMode = True
            while lifePathEditMode:
                print('please enter the number of lifepaths you wish for your character to have')
                lifePathNumber = pyip.inputNum()
                if lifePathNumber <= 0:
                    print('please enter a positive integer')
                    continue
                print(f'{lifePathNumber} lifepaths chosen. would you like to make further adjustments? (y/n)')
                backToMenuAnswer = pyip.inputYesNo()
                if backToMenuAnswer == 'yes':
                    lifePathEditMode = False
                else:
                    lifePathEditMode = False
                    editMode = False
        elif editChoiceInputNumber == 3:
            genderPathEditMode = True
            while genderPathEditMode:
                print('please pick a gender.')
                print('1 - female')
                print('2 - male')
                genderNum = pyip.inputNum()
                if genderNum < 1 or genderNum > 2:
                    print('please enter 1 or 2')
                    continue
                if genderNum == 1:
                    genderName = 'female'
                    print("you've chosen female. would you like to make further adjustments? (y/n)")
                    backToMenuAnswer = pyip.inputYesNo()
                    if backToMenuAnswer == 'yes':
                        genderPathEditMode = False
                    else:
                        genderPathEditMode = False
                        editMode = False
                if genderNum == 2:
                    genderName = 'male'
                    print("you've chosen male. would you like to make further adjustments? (y/n)")
                    backToMenuAnswer = pyip.inputYesNo()
                    if backToMenuAnswer == 'yes':
                        genderPathEditMode = False
                    else:
                        genderPathEditMode = False
                        editMode = False

        elif editChoiceInputNumber == 5:
            print(f'race = {raceName}')
            print(f'number of lifepaths = {lifePathNumber}')
            print(f'gender = {genderName}')
            print('press enter to continue')
            input()
        elif editChoiceInputNumber == 4:
            editMode = False
            break
    generateMode = True
    while generateMode is True:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(3)
        driver.get('http://charred-black.herokuapp.com/#/')
        raceSelector = driver.find_element_by_css_selector('#collapse_first > div > div > div > div:nth-child(5) > '
                                                           'select')
        try:
            if raceChoice is None:
                raceNumber = random.randint(1, 7)
            else:
                raceNumber = raceChoice
        except NameError:
            raceNumber = random.randint(1, 7)
        print(f'raceNumber = {raceNumber}')
        raceSelector2 = Select(driver.find_element_by_xpath('//*[@id="collapse_first"]/div/div/div/div[5]/select'))
        if raceNumber == 1:
            raceSelector2.select_by_value('man')
        elif raceNumber == 2:
            raceSelector2.select_by_value('dwarf')
        elif raceNumber == 3:
            raceSelector2.select_by_value('elf')
        elif raceNumber == 4:
            raceSelector2.select_by_value('orc')
        elif raceNumber == 5:
            raceSelector2.select_by_value('roden')
        elif raceNumber == 6:
            raceSelector2.select_by_value('wolf')
        elif raceNumber == 7:
            raceSelector2.select_by_value('troll')
        genderSelector = driver.find_element_by_css_selector('#collapse_first > div > div > div > div:nth-child(8) > '
                                                             'select')
        try:
            if genderNum is None:
                genderNumber = random.randint(1, 2)
            else:
                genderNumber = genderNum
        except NameError:
            genderNumber = random.randint(1, 2)
        print(f'genderNumber = {genderNumber}')
        if genderNumber > 1:
            genderSelector2 = Select(driver.find_element_by_xpath('//*[@id="collapse_first"]/div/div/div/div[8]/select'))
            genderSelector2.select_by_value('male')
        else:
            pass
        try:
            if lifePathNumber is None:
                lifePathQuantity = random.randint(4, 6)
            else:
                lifePathQuantity = lifePathNumber
        except NameError:
            lifePathQuantity = random.randint(4, 6)
        print(f'lifepath quantity = {lifePathQuantity}')
        for i in range(0, lifePathQuantity):
            settingSelector = driver.find_element_by_xpath('''//*[@id="collapse_lp"]/div/div[2]/div[1]/div[1]/select''')
            allSettings = settingSelector.find_elements_by_tag_name("option")
            print(f'number of settings available = {len(allSettings)}')
            settingNum = random.randint(1, len(allSettings))
            print(f'settingNum = {settingNum}')
            setting = Select(driver.find_element_by_xpath('''//*[@id="collapse_lp"]/div/div[2]/div[1]/div[1]/select'''))
            setting.select_by_value(str(settingNum - 1))
            lifePathSelector = driver.find_element_by_xpath(
                '''//*[@id="collapse_lp"]/div/div[2]/div[1]/div[2]/select''')
            allLifepaths = lifePathSelector.find_elements_by_tag_name("option")
            print(f'number of lifepaths available = {len(allLifepaths)}')
            lifePathNum = random.randint(1, len(allLifepaths))
            print(f'lifePathNum = {lifePathNum}')
            lifepath = Select(
                driver.find_element_by_xpath('''//*[@id="collapse_lp"]/div/div[2]/div[1]/div[2]/select'''))
            lifepath.select_by_value(str(lifePathNum - 1))
            addLifePathButton = driver.find_element_by_css_selector(
                '#collapse_lp > div > div.container > div:nth-child(1) > div.col-md-1 > a')
            try:
                addLifePathButton.click()
            except ElementClickInterceptedException:
                for m in range(0, 15):
                    pyautogui.press('tab')
                    pyautogui.press('enter')
                    addLifePathButton.click()
            # collapse_lp > div > div.container > div:nth-child(1) > div:nth-child(1) > select

            # count = len(Select(settingSelector).options)
            # print(count)
        driver.find_element_by_css_selector('#collapse_stats > div > div > div:nth-child(3) > div > button').click()
        characterFinished = True
        while characterFinished == True:
            print('character complete. do you want to make a new character?')
            print('1 - yes, use the same parameters')
            print('2 - no, please start over from the beginning')
            finishedCharacterInput = pyip.inputNum()
            if finishedCharacterInput < 1 or finishedCharacterInput > 2:
                print('please enter 1 or 2')
                continue
            elif finishedCharacterInput == 2:
                raceChoice = None
                lifePathNum = None
                genderNum = None
                lifePathNumber = None
                characterFinished = False
                generateMode = False
                break
            elif finishedCharacterInput == 1:
                characterFinished = False
                break
