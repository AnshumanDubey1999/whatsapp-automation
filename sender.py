import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyperclip
import traceback

class Sender:

    def __init__(self):
        self.driver = webdriver.Chrome('./driver/chromedriver')
        self.driver.get('https://web.whatsapp.com/')
        self.wait = WebDriverWait(self.driver, 600)
        self.waitTime = 0.5
        self.msgBoxClassName = '_13NKt'
        self.plugin = 0
        self.counter = 0
        self.startTime = time.time()
        self.liveView = False

    def changeWaitTime(self):
        print('Wait Time is the time delay between sending 2 consecutive messages.')
        print("Current waiting time: " + str(self.waitTime))
        print("Enter new waiting time (0.5 - 60) : ", end='')
        new_time = float(input())
        if new_time < 0.5 or new_time > 60.0:
            print("Invalid input. Waiting time didn't change.")
        else:
            self.waitTime = new_time
            print("Waiting time successfully changed.")

    def toggleLiveView(self):
        print('Live View prints what is being sent in the console while sending it to whatsapp.')
        print("Live View:", 'On' if self.liveView else 'Off')
        c = input('Press Y/y to toggle Live View: ')
        if c in 'Yy':
            self.liveView = not self.liveView
            print("Live View (Changed):", 'On' if self.liveView else 'Off')
        else:
            print("Live View (Unchanged):", 'On' if self.liveView else 'Off')

    def testing(self):
        try:
            msg_box = self.driver.find_elements_by_class_name(self.msgBoxClassName)[-1]
            msg_box.send_keys('.' + Keys.ENTER)
            print("Check if the recepient has recieved a '.' as a message. If not enter N: ", end="")
            result = input()
            if result=='N' or result=='n' or result=='no':
                raise RuntimeError
        except:
            print('Unable to send Test message.\nChech for class name of inout field using inspect and update the field.\nCurrent class name:', self.msgBoxClassName)
            msgBoxClassName = input("Enter new class name: ")
            if msgBoxClassName=='EXIT':
                return
            self.testing()

    def changePlugin(self):
        print('''1. Add serial number.\n2. Add Time Stamp\n3. Add Microsecond Stamp\nEnter your choice : ''', end='')
        plugin = int(input())
        if plugin not in [1, 2, 3]:
            print("Invalid Input. Please try again")
            self.plugin_menu()
        else:
            self.plugin = plugin
            print("Plugin change Successful.")

    def getPluginString(self):
        if self.plugin == 1:
            return self.counter + 1
        if self.plugin == 2:
            return time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime())
        if self.plugin == 3:
            return str(round(time.time()-self.startTime, 3))
        return ''

    def sendMessage(self, array, infinite = False):
        try:
            self.startTime = time.time()
            self.counter = 0
            msg_box = self.driver.find_elements_by_class_name(self.msgBoxClassName)[-1]
            while True:
                for element in array:
                    if self.plugin == 0:
                        msg_box.send_keys(element + Keys.ENTER)
                    else:
                        msg_box.send_keys(self.getPluginString() + ' : ' + element + Keys.ENTER)
                    if self.liveView:
                        print(self.counter,'\t:',element)
                    self.counter += 1
                    time.sleep(self.waitTime)
                if not infinite:
                    print('Counter:',self.counter,'(Press ctrl+c to stop!)')
                    break
            print('Task was successfully completed in', time.time()-self.startTime,'seconds.')
        except KeyboardInterrupt:
            print('\nTask was stopped by user!\nTime taken:', time.time()-self.startTime,'seconds.')
        except:
            print('An error occured while trying to send the message.\nPlease try again!')
            traceback.print_exc()

    def sendAdvancedMessage(self, characters):
        try:
            self.startTime = time.time()
            self.counter = 0
            msg_box = self.driver.find_elements_by_class_name(self.msgBoxClassName)[-1]
            for character in characters:
                pyperclip.copy('\n'.join(character))
                msg_box.send_keys(Keys.CONTROL, 'v')
                time.sleep(self.waitTime/2)
                msg_box.send_keys(Keys.ENTER)
                msg_box.send_keys(Keys.ENTER)
                if self.liveView:
                        print(self.counter,'\n:','\n'.join(character))
                time.sleep(self.waitTime/2)
                self.counter += 1
            print('Task was successfully completed in', time.time()-self.startTime,'seconds.')
        except KeyboardInterrupt:
            print('\nTask was stopped by user!\nTime taken:', time.time()-self.startTime,'seconds.')
        except:
            print('An error occured while trying to send the message.\nPlease try again!')
            traceback.print_exc()
