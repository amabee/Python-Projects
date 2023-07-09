class EnigmaMachine:
    def __init__(self, rotor1, rotor2, rotor3, reflector):
        self.rotor1 = rotor1
        self.rotor2 = rotor2
        self.rotor3 = rotor3
        self.reflector = reflector
        
        self.rotor1_position = 0
        self.rotor2_position = 0
        self.rotor3_position = 0

    def encrypt(self, message):
        eMessage = ""
        for char in message:
            #char = self.rotor1[ord(char) - ord('A') + self.rotor1_position % 26]
            index = (ord(char) - ord('A') + self.rotor1_position) % 26
            #index = (ord(char) - ord('A') + self.rotor2_position) % 26
            #index = (ord(char) - ord('A') + self.rotor3_position) % 26
            index = min(max(index, 0), 25)
            char = self.rotor1[index]
            char = self.rotor2[index]
            char = self.rotor3[index]
            #char = self.rotor2[ord(char) - ord('A') + self.rotor2_position % 26]
            #char = self.rotor3[ord(char) - ord('A') + self.rotor3_position % 26]  

            # Substitute the character back through rotors
            char = self.reflector[ord(char) - ord('A')]
            char = chr((self.rotor3.index(char) - self.rotor3_position + ord('A')) % 26 + ord('A'))
            char = chr((self.rotor2.index(char) - self.rotor2_position + ord('A')) % 26 + ord('A'))
            char = chr((self.rotor1.index(char) - self.rotor1_position + ord('A')) % 26 + ord('A'))

            # Add the character to the encrypted message
            eMessage += char

            # Rotating the Rotors
            self.rotor1_position = (self.rotor1_position + 1) % 26

            if self.rotor1_position == 0:
                self.rotor2_position = (self.rotor2_position + 1) % 26

                if self.rotor2_position == 0:
                    self.rotor3_position = (self.rotor3_position + 1) % 26

        return eMessage

    def decrypt(self, message):
        decrypted_message = ""
        for char in message:
            # Substitute character through rotors in reverse order
            index = (self.rotor1.index(char) - self.rotor1_position + ord('A')) % 26
            index = (self.rotor1.index(char) - self.rotor2_position + ord('A')) % 26
            index = (self.rotor1.index(char) - self.rotor3_position + ord('A')) % 26
            char = chr(index + ord('A'))
            index = min(max(index, 0),25)
            # char = chr((self.rotor1.index(char) - self.rotor1_position + ord('A')) % 26 + ord('A'))
            # char = chr((self.rotor2.index(char) - self.rotor2_position + ord('A')) % 26 + ord('A'))
            # char = chr((self.rotor3.index(char) - self.rotor3_position + ord('A')) % 26 + ord('A'))
            char = self.rotor1[index]
            char = self.rotor2[index]
            char = self.rotor3[index]

            # Reflect character
            char = self.reflector[ord(char) - ord('A')]

            # Substitute character back through rotors in reverse order
            char = self.rotor3[(ord(char) - ord('A') + self.rotor3_position) % 26]
            char = self.rotor2[(ord(char) - ord('A') + self.rotor2_position) % 26]
            char = self.rotor1[(ord(char) - ord('A') + self.rotor1_position) % 26]

            # Add character to decrypted message
            decrypted_message += char

            # Rotate rotors
            self.rotor1_position = (self.rotor1_position - 1) % 26
            if self.rotor1_position == 0:
                self.rotor2_position = (self.rotor2_position - 1) % 26
                if self.rotor2_position == 0:
                    self.rotor3_position = (self.rotor3_position - 1) % 26
        return decrypted_message

rotor1 = ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J']
rotor2 = ['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E']
rotor3 = ['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', 'N', 'Y', 'E', 'I', 'A', 'G', 'K', 'M', 'O', 'Q', 'S', 'U', 'W']
reflector = ['Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'D', 'P', 'X', 'N', 'G', 'O', 'K', 'M', 'I', 'E', 'B', 'F', 'Z', 'C', 'W', 'V', 'J', 'A', 'T']

unknown = EnigmaMachine(rotor1, rotor2, rotor3, reflector)

while True:
    print("Type Something: ")
    message = input()
    eMessage = unknown.encrypt(message)
    dMessage= unknown.decrypt(message)
    print(eMessage)
    print(dMessage)
