class Talaba:
    def __init__(self,ism,yosh):
        self.ism=ism
        self.yosh=yosh
        self.fanlar=[]

    def fanga_yozil(self,fan):
        if isinstance(fan,Fan):
            self.fanlar.append(fan)
            print(f"{self.ism} {fan.nomi} faniga yozildi")
        else:
            print("Fan classiga tegishli obyekt")

    def remove_fan(self,fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
            print(f"{fan.nomi} royxatdan o`chirildi")
        else:
            print("Siz bu fanga yozilmagansz")

    def talaba_malumotlari(self):
        return {
            "Ism": self.ism,
            "Yosh": self.yosh,
            "Fanlar": [fan.nomi for fan in self.fanlar]  # Fanlar nomini ko'rsatish
        }

class Fan(Talaba):
    def __init__(self,nomi,oqituvchi):
        self.nomi=nomi
        self.ustoz=oqituvchi
        self.baholar=[]

    # def baho_qoyish(self,baho):
    #     self.baholar.append(baho)
    #
    #
    # def fan_malumotlari(self):
    #     return{
    #         "Fan": self.nomi,
    #         "O'qituvchi": self.ustoz,
    #         "Baholar": self.baholar,
    #     }
talaba1= Talaba("Jasur",20)
talaba2= Talaba("Moxina",21)


matem = Fan("Matematika","Madina Nigmatova")
ona_tili= Fan("Ona tili","Saida Mamajonova")
tarbiya= Fan("Tarbiya","Jamshid Nurmuxamedov")

talaba1.fanga_yozil(matem)
talaba1.fanga_yozil(tarbiya)
talaba2.fanga_yozil(ona_tili)
talaba2.fanga_yozil(tarbiya)

talaba2.remove_fan(tarbiya)
talaba1.remove_fan(ona_tili)
# matem.baho_qoyish(5)
# matem.baho_qoyish(5)
# matem.baho_qoyish(4)
# tarbiya.baho_qoyish(3)
# ona_tili.baho_qoyish(5)
# tarbiya.baho_qoyish(5)
# ona_tili.baho_qoyish(4)

print(talaba1.talaba_malumotlari())
print(talaba2.talaba_malumotlari())
# print(tarbiya.fan_malumotlari())
