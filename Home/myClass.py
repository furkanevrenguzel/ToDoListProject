class Counter():
    count=0

    durum=True

    def arttir(self):
        self.count+=1
        return self.count

    def azalt(self):
        self.count-=1
        return self.count

    def sifirla(self):
        self.count=0
        return self.count


    def deger(self):
        return self.count


    def FalseYap(self):
        self.durum=False

    def TrueYap(self):
        self.durum=True
    
    def Durum(self):
        return self.durum