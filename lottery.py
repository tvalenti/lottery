"""
Program: lottery.py
Author: Tom

Random number generator to look like lottery numbers in a GUI using a GUI helper script
"""
# Imports the random package and EasyFrame from the breezypythongui script
import random
from breezypythongui import EasyFrame

class Lottery(EasyFrame):

    def __init__(self):
        EasyFrame.__init__(self, title="Counter demo")
        self.setSize(300, 75)

        # Instance variable to track the count
        self.count = 0

        # Labels to display the random numbers in the first row
        self.label0 = self.addLabel(text="0", row=0, column=0, sticky="NSEW")
        self.label1 = self.addLabel(text="0", row=0, column=1, sticky="NSEW")
        self.label2 = self.addLabel(text="0", row=0, column=2, sticky="NSEW")
        self.label3 = self.addLabel(text="0", row=0, column=3, sticky="NSEW")
        self.label4 = self.addLabel(text="0", row=0, column=4, sticky="NSEW")
        self.label5 = self.addLabel(text="0", row=0, column=5, sticky="NSEW")

        # One command button
        self.addButton(text="Generate lotto numbers", row=1, column=0, columnspan=5, command=self.randomNumber)


    # Method to handle use events
    def randomNumber(self):
        """ Generates random numbers into an list then checks if they are already created """
        
        # Creates the list
        results = []
        # Loop that runs 6 times and appends the random number generated into the rsults
        for eachPass in range(6):
            results.append(random.randint(0,59))
        
        # The looping method to check the list for duplicates and runs the randint on y if found
        for x in range(len(results)-1):
            for y in range(len(results)-1):
                if results[x] == results[y + 1]:
                    if x == y + 1:
                        continue
                    else:
                        results[y + 1] = random.randint(0,59)

        # Assigns the index numbers in the corrosponding labels
        self.label0["text"] = results[0]
        self.label1["text"] = results[1]
        self.label2["text"] = results[2]
        self.label3["text"] = results[3]
        self.label4["text"] = results[4]
        self.label5["text"] = results[5]

def main():
    Lottery().mainloop()

if __name__ == "__main__":
    main()
