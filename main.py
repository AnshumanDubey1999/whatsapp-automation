import sender
import asciiArt
import defaultPatterns


def main():
    mySender = sender.Sender()
    myAsciiArt = asciiArt.AsciiArt(mySender)
    myDefaultPatterns = defaultPatterns.DefaultPatterns(mySender)
    functions = [
        myDefaultPatterns.left_triangle, 
        myDefaultPatterns.right_triangle, 
        myDefaultPatterns.per_character, 
        myDefaultPatterns.repeater, 
        myAsciiArt.character_art,
        mySender.changePlugin,
        mySender.changeWaitTime,
        mySender.toggleLiveView
    ]

    print("Login to WhatsApp Web using your mobile and go to the chat you want to send your message to.")
    input("Press Enter to continue...")
    
    mySender.testing()
    while True:
        print('''
        1. T           2. g           3. T           4. Testing
           Te             ng             e              Testing
           Tes            ing            s              Testing
           Test           ting           t              Testing
           Testi          sting          i              Testing
           Testin         esting         n              Testing
           Testing        Testing        g              Testing
        
        5. Words in ASCII Art(buggy)
        6. Modify Plugin (Not for ASCII Art)
        7. Change Waiting time
        8. Toggle Live View
        9. Exit
        ''')
        choice = int(input('Enter your choice : '))
        if choice in range(1, 9):
            functions[choice-1]()
        elif choice == 9:
            credits()
            mySender.driver.quit()
            exit()
        else:
            print("Invalid input.\nPlease try again")

main()
