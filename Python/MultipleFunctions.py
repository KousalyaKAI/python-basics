class MultipleFunctions():
    def Subfields():
        SubFieldsAI = ['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing']
        print('Sub-fields in AI are:')
        for Subfield in SubFieldsAI:
            print(Subfield)
    def OddEven():
        num = int(input("Enter a number:"))
        if((num%2) == 0):
            print(num,"is Even Number")
        else:
            print(num,"is Odd Number")
    def ElegiblityForMarriage():
        Gender = (input("Your Gender:"))
        Age = int(input("Your Age:"))
        if ((Gender == 'Male' and Age >= 21) or (Gender == 'Female' and Age >= 18)):
            print('ELIGIBLE')
        else:
            print('NOT ELIGIBLE')
    def FindPercent():
        Subject1 = int(input("Subject1="))
        Subject2 = int(input("Subject2="))
        Subject3 = int(input("Subject3="))
        Subject4 = int(input("Subject4="))
        Subject5 = int(input("Subject5="))
        Total = Subject1+Subject2+Subject3+Subject4+Subject5
        print('Total : ',Total)
        percentage = (Total/500)*100;
        print('Percentage : ',percentage)
    def triangle():
        Height = int(input('Height:'))
        Breadth = int(input('Breadth:'))
        AreaTriangle = (Height*Breadth)/2
        print('Area formula: (Height*Breadth)/2')
        print('Area of Triangle:',AreaTriangle)
        Height1 = int(input('Height1:'))
        Height2 = int(input('Height2:'))
        Breadth = int(input('Breadth:'))
        PerimeterTriangle = Height1+Height2+Breadth
        print('Perimeter formula: Height1+Height2+Breadth')
        print('Perimeter of Triangle:',PerimeterTriangle)