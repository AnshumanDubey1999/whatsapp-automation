import pyfiglet

class AsciiArt:

    def __init__(self, sender):
        self.fonts = pyfiglet.Figlet().getFonts()
        self.chosen_font = 'calgphy2'
        self.sender = sender

    def fontToCharacterArray(self, message):
        sentence = []
        for i in message:
            character = pyfiglet.figlet_format(i, font = self.chosen_font)
            character = character.split('\n')
            character[0]='```'+character[0]
            character[-1] = character[-1]+'```'
            sentence.append(character)
        return sentence

    def demonstrate(self, sentence):
        print("This will be sent :")
        for character in sentence:
            for line in character:
                if line != '```':
                    print(line)

    def changeFont(self):
        print("Enter font name (or 'help' to get list of fonts) : ", end='')
        chosen_font = input().lower()

        if chosen_font == 'help':
            for i in range(0, len(self.fonts)-len(self.fonts) % 5, 5):
                for j in range(5):
                    print(str(i+j+1).rjust(4) + '. ' + self.fonts[i+j].ljust(14), end = "")
                print()
            print("\nEnter the number of the font you want to use : ", end='')
            font_number = int(input())
            while font_number < 1 or font_number > len(self.fonts):
                print("\nIncorrect Input. Please try again.\nEnter the number of the font you want to use "
                    ": ", end='')
                font_number = int(input())
            chosen_font = self.fonts[font_number-1]
        if chosen_font in self.fonts:
            self.chosen_font = chosen_font
            return
        print("Incorrect font name. Try again.")
        self.changeFont()
        
    def character_art(self):
        while True:
            word = []
            print("Enter the message: ", end="")
            msg = input()

            # creating default print
            word = self.fontToCharacterArray(msg)
            # menu
            while True:
                print('1. Change Font\n2. Demo\n3. Continue\n4. Back\n5. Exit\nEnter your choice : ', end="")

                choice = int(input())

                if choice == 3:
                    break
                if choice == 4:
                    return 0
                if choice == 5:
                    return 1

                elif choice == 1:
                    self.changeFont()
                    word = self.fontToCharacterArray(msg)
                    self.demonstrate(word)
                        
                elif choice == 2:
                    self.demonstrate(word)

            self.sender.sendAdvancedMessage(word)
            return 0