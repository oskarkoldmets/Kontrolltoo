class Calculator():
    def __init__(self, a, b):
        #Lisab kalkulaatorisse kaks sisendnumbrit
        self.a = a
        self.b = b

    def addition(self):
        #Liidab kaks arvu kokku
        return self.a + self.b
    
    def subtraction(self):
        #Lahutab teise arvu esimesest
        return self.a - self.b
    
    def multiplication(self):
        #Korrutab kaks arvu omavahel
        return self.a * self.b
    
    def division(self):
        #Jagab esimese arvu teisega
        if self.b != 0:  
            return self.a / self.b
        else:
            return "Viga: nulliga jagamine!"
    
    def modulus(self):
        # eiab esimese arvu jäägi teisega jagamisel
        return self.a % self.b
    
    def square_root(self):
        # eiab esimese arvu ruutjuure
        return self.a ** 0.5
    
    def exponentiation(self):
        #Astendab esimese arvu teise arvu võrra
        return self.a ** self.b

#Küsib kasutajalt kaks arvu
a = int(input("Sisesta esimene number: "))          
b = int(input("Sisesta teine number: "))

calculator = Calculator(a, b)  #Loob kalkulaatori eksemplari

while True:
    #Menüü väljastamine
    print("Valikud:")
    print("1. Liitmine")
    print("2. Lahutamine")
    print("3. Korrutamine")
    print("4. Jagamine")
    print("5. Jäägi leidmine")
    print("6. Ruutjuure leidmine")
    print("7. Astendamine")

    valik = int(input('Sisesta üks valikutest: '))  #Küsib kasutajalt valikut

    #Kontrollib kasutaja valikut ja väljastab vastuse vastavalt
    if valik in range(1, 8):
        #Kui valik on sobiv, siis teostatakse vastav tehe
        operations = [calculator.addition, calculator.subtraction, calculator.multiplication,
                      calculator.division, calculator.modulus, calculator.square_root, calculator.exponentiation]
        result = operations[valik - 1]()
        print("Vastus:", result)
        break
    else:
        print("Vale valik, proovi uuesti")
