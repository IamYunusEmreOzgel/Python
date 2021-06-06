import random

f=open("AcademicProgram.txt","a")
print("Academic Program For 1st and 2nd Grade!! \n")
f.write("Academic Program For 1st and 2nd Grade!! \n\n")
print("There's lectures of 1st Grade : ")
f.write("There's lectures of 1st Grade : \n")
firstGrade = ["Computer Programming", "Teknik Resim", "Matematik", "Fizik", "Elektrik"]
secondGrade = ["Mekanik", "Elektronik", "Mühendislik Matematiği", "Kontrol", "Termodinamik" ]
print(firstGrade)
f.write("{} \n".format(firstGrade))
print("")
print("There's lectures of 2nd Grade :")
f.write("There's lectures of 2nd Grade : \n")
print(secondGrade)
f.write("{} \n".format(secondGrade))
print("")

class FirstClass():
    studentNumber=[100859132,100859133,100859134,100859135,100859136]    #Birinci sınıftaki tüm öğrenciler bu listenin içerisinde    
    
    def Students1(self):       
        for i in self.studentNumber :
            print(i)
        
class  Bilgisayarprogramlama(FirstClass):
    programmingStudent=[]

    def __init__(self): 
        f=open("AcademicProgram.txt","a")
        print("Programming Courses Student :")
        f.write("\nProgramming Courses Student : \n")
        self.studentNumber.append(159789456)
        self.studentNumber.append(159789453)        #Dersi alttan alan öğrencileri De bu sınıfa atıyorum
        for i in self.studentNumber:                #Tüm birinci Sınıf Öğrencilerini sınıfın içine atıyoruz.
            self.programmingStudent.append(i)   
        print(self.programmingStudent)
        f.write("{} \n".format(self.programmingStudent))
        f.close()
        self.studentNumber.remove(159789456)        #Alttan alan öğrenciler 1.sınıf öğrencileri arasında kalmaması için bu listeden çıkarıyoruz.
        self.studentNumber.remove(159789453)
        
class Teknikresim(FirstClass):
    trStudent=[]
    
    def __init__(self):
        f=open("AcademicProgram.txt","a")
        print("Teknik Resim Courses Student : ")
        f.write("Teknik Resim Courses Student : \n")
        self.studentNumber.append(159789453)
        for i in self.studentNumber:
            self.trStudent.append(i)
        print(self.trStudent)
        f.write("{} \n".format(self.trStudent))
        f.close()
        self.studentNumber.remove(159789453)

class Matematik(FirstClass):
    matStudent=[]
    
    def __init__(self):
        f=open("AcademicProgram.txt","a")
        f.write("Mat Courses Student : \n")
        print("Mat Courses Student :")
        self.studentNumber.append(159789452)
        for i in self.studentNumber:
            self.matStudent.append(i)
        print(self.matStudent)
        f.write("{} \n".format(self.matStudent))
        f.close()
        self.studentNumber.remove(159789452)
                     
class Fizik(FirstClass):
      fizStudent=[]
      
      def __init__(self):
        f=open("AcademicProgram.txt","a")
        print("Fizik Courses Student :")
        f.write("Fizik Courses Student : \n")
        self.studentNumber.append(159789452)
        self.studentNumber.append(159789456)
        for i in self.studentNumber:
            self.fizStudent.append(i)
        print(self.fizStudent)
        f.write("{} \n".format(self.fizStudent))
        f.close()
        self.studentNumber.remove(159789452)
        self.studentNumber.remove(159789456)
  
class Elektrigintemeldevreleri(FirstClass):
      etdStudent=[] 
      
      def __init__(self):
        f=open("AcademicProgram.txt","a")
        print("Elektrik Courses Student :")
        f.write("Elektrik Courses Student : \n")
        self.studentNumber.append(159789453)       
        for i in self.studentNumber:
            self.etdStudent.append(i)
        print(self.etdStudent)
        f.write("{} \n".format(self.etdStudent))
        f.close()
        self.studentNumber.remove(159789453)
        
    
class SecondClass():
        studentNumber2=[159789452,159789453,159789454,159789455,159789456]  #Tüm ikinci sınıf öğrencileri bu listenin içerisinde
        
        def Students2(self):               
            for i in self.studentNumber2 :
                print(i)               

class Mekanik(SecondClass):
      mekStudent=[]  
      
      def __init__(self):
        f=open("AcademicProgram.txt","a")
        print("Mekanik Courses Student :")
        f.write("Mekanik Courses Student : \n")
        self.studentNumber2.append(100859132)  #Dersi alttan alan öğrencileri ekliyoruz
        for i in self.studentNumber2:
            self.mekStudent.append(i)
        print(self.mekStudent)
        f.write("{} \n".format(self.mekStudent))
        f.close()
        self.studentNumber2.remove(100859132)  #Dersi alttan alan öğrencileri tekrar kaldırıyoruz ki ikinci sınıfların arasında yer almasın.
        
class Elektronik(SecondClass):
    eStudent=[] 
    
    def __init__(self):
        f=open("AcademicProgram.txt","a")
        print("Elektronik Courses Student :")
        f.write("Elektronik Courses Student : \n")
        self.studentNumber2.append(100859135)
        for i in self.studentNumber2:
            self.eStudent.append(i)
        print(self.eStudent)
        f.write("{} \n".format(self.eStudent))
        f.close()
        self.studentNumber2.remove(100859135)
        
class Mühmatematik(SecondClass):
      mmStudent=[]  
      
      def __init__(self):
        f=open("AcademicProgram.txt","a")
        print("Mühendislik Matematiği Courses Student :")
        f.write("Mühendislik Matematiği Courses Student: \n")        
        for i in self.studentNumber2:
            self.mmStudent.append(i)
        print(self.mmStudent)
        f.write("{} \n".format(self.mmStudent))
        f.close()
         
class Kontrol(SecondClass):
      kStudent=[]   
      
      def __init__(self):
        f=open("AcademicProgram.txt","a")
        print("Kontrol Courses Student :")
        f.write("Kontrol Courses Student : \n")
        self.studentNumber2.append(100859133)
        
        for i in self.studentNumber2:
            self.kStudent.append(i)
        print(self.kStudent)
        f.write("{} \n".format(self.kStudent))
        f.close()            
        self.studentNumber2.remove(100859133)
            
                       
class Termodinamik(SecondClass):
    tStudent=[]
    
    def __init__(self):
        f=open("AcademicProgram.txt","a")
        print("Termodinamik Courses Student :")
        f.write("Termodinamik Courses Student : \n")
        self.studentNumber2.append(100859132)
        self.studentNumber2.append(100859135)       
        for i in self.studentNumber2:
            self.tStudent.append(i)
        print(self.tStudent)
        f.write("{} \n".format(self.tStudent))
        f.close()        
        self.studentNumber2.remove(100859132)

        self.studentNumber2.remove(100859135)        

bp=Bilgisayarprogramlama()     #Her classtan bir adet Nesne Oluşturdum
tr=Teknikresim()
mat=Matematik()
etd=Elektrigintemeldevreleri()
fiz=Fizik()

mek=Mekanik()
el=Elektronik()
mühmat=Mühmatematik()
Kont=Kontrol()
ter=Termodinamik()
f=open("AcademicProgram.txt","a")
f.write("")
print("")
f.close()

firstClass=[bp.programmingStudent,tr.trStudent,mat.matStudent,etd.etdStudent,fiz.fizStudent]  #birinci ve ikinci sınıf derslerini atadım.
secondClass=[mek.mekStudent,el.eStudent,mühmat.mmStudent,Kont.kStudent,ter.tStudent]

days=["Monday","Tuesday","Wednesday","Thursday","Friday"]

flag = True #iki dersin öğrencileri tamamen aynı olduğu için kullandım .

for i in range(5):  #Dersleri ikişer ikişer ele aldığım için 5 tur döngüde kalıyoruz.
    temporary=True
    chosenFirstClass=[]  #Seçtiğimiz dersleri içine atacağımız listeler
    chosenSecondClass=[]
    chosenFirstClass =random.choice(firstClass)  #Dersler arasından rastgele seçim yapıyoruz
    chosenSecondClass =random.choice(secondClass)
    firstClass.remove(chosenFirstClass)  #Aynı dersi birden fazla kez  koymamak için  listeden siliyoruz
    secondClass.remove(chosenSecondClass)
    c=days[i]   #Günler lıstesısnde sırayla geziniyoruz ilgili günü seçmek için kullandık
    
    hours=[8,9,10,11,12,13,14,15]  #Derslerin olabileceği saat aralığıdır
    
    if chosenFirstClass==bp.programmingStudent:  #Random seçilen dersin hangisi oldupunu tespit etmekte kullandım.
        lectureName="Bilgisayar Programlama"
    elif chosenFirstClass==tr.trStudent and flag:
        lectureName="Teknik Resim"
        flag=False
    elif chosenFirstClass==mat.matStudent:
        lectureName="Matematik"
    elif chosenFirstClass==etd.etdStudent:
        lectureName="Elektriğin Temel Devreleri"
    elif chosenFirstClass==fiz.fizStudent:
        lectureName="Fizik"
    
    if chosenSecondClass==mek.mekStudent:
         lectureName2="Mekanik"
    elif chosenSecondClass==el.eStudent :
        lectureName2="Elektronik"
    elif chosenSecondClass==mühmat.mmStudent:
        lectureName2="Mühendisliğin Matematiği"
    elif chosenSecondClass==Kont.kStudent:
        lectureName2="Kontrol"
    elif chosenSecondClass==ter.tStudent:
        lectureName2="Termodinamik"
        
        
    for i in (chosenFirstClass):  #hangi öğrencilerin çakıştığını söyler.
        for j in (chosenSecondClass):
            if i==j:              
                print("Student number {} takes both {} and {} lessons.".format(i,lectureName,lectureName2))
                #Hangi öğrencinin çakıştığını görmek için yorum satırını kaldırın.
                temporary=False #Dersler arasında çakışma olduysa false yapar
    
    if temporary==False:   #Eğer dersler arasında çakışma olduysa bu kısma girilir
        f=open("AcademicProgram.txt","a")
        print("________________________________________________________________________________")
        print("|Lectures of {} : ".format(c))
        f.write("________________________________________________________________________________")
        f.write("\n|Lectures of {} : \n".format(c))
        print("|** Student Overlap That's why classes are being moved to different hours **")
        h=random.randint(10,13) #çakışma oldupu için yeniden saat seçilmesini sağlar.
        hours.remove(h)         #Seçilen saat dilimi tüm saatlerden çıkarılır böyleci diğer dersin aynı saatte olması önlenir
        h=h+1
        hours.remove(h)
        h=h+1
        hours.remove(h)
        h2=h-3
        hours.remove(h2)
        h2=h2-1
        hours.remove(h2)
        h3=random.choice(hours)
        print("|There is a {} class between {} and {} .".format(lectureName, h-2 , h+1)) 
        f.write("|There is a {} class between {} and {} .\n".format(lectureName, h-2 , h+1))
        print("|There is a {} class between {} and {} .".format(lectureName2,h3,h3+3))
        f.write("|There is a {} class between {} and {} . \n".format(lectureName2,h3,h3+3))
        print("|_______________________________________________________________________________")
        f.write("|_______________________________________________________________________________ \n")
        f.close()
    
    else:         #Eğer çaışma yoksa zaten saatler önemli değildir  ve rastgele bastırılır.
        print("**Student Dont Overlap**")
        h=random.randint(8,15)
        h3=random.randint(8,15)
        print("There is a {} class between {} and {} on {}".format(lectureName, h-2 , h+1,c)) 
        print("There is a {} class between {} and {} on {}".format(lectureName2,h3,h3+3,c))
