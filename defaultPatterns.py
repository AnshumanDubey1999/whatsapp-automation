class DefaultPatterns:

    def __init__(self, sender):
        self.sender = sender

    def takeInput(self):
        msg = input("Enter the message: ").replace(' ', '_')
        infinite = input("Press Y/y to repeat the message infinite times: ") in 'Yy'
        return (msg, infinite)

    def left_triangle(self):
        msg, infinite = self.takeInput()
        msgArray = []
        for i in range(len(msg)):
            msgArray.append(msg[:i+1])
        self.sender.sendMessage(msgArray, infinite)


    def right_triangle(self):
        msg, infinite = self.takeInput()
        msgArray = []
        for i in range(len(msg)):
            msgArray.append(msg[len(msg)-i-1:])
        self.sender.sendMessage(msgArray, infinite)
       


    def repeater(self):
        msg, infinite = self.takeInput()
        n = 1
        if not infinite:
            while True:
                n = int(input("Enter the number of times you want the message to be repeated(1-100): "))
                if n>=1 and n<=100:
                    break
                print('Invalid Input. Please try again!')
        msgArray = [msg]*n
        self.sender.sendMessage(msgArray, infinite)

    def per_character(self):
        msg, infinite = self.takeInput()
        n = 1
        self.sender.sendMessage(list(msg), infinite)
