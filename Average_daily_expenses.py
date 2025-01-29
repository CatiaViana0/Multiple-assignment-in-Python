# -*- coding: utf-8 -*
#calculating average daily expense for 4 days, knowing that each day spent 20% more

if __name__ == '__main__':
    Increase=20
    D1=float(input("Enter the first day's expense: "))
    D2=D1*(1+Increase/100)
    D3=D2*(1+Increase/100)
    D4=D3*(1+Increase/100)
    Dmed=(D1+D2+D3+D4)/4
    print(f"Average daily expense {Dmed:3.2f} euros")
