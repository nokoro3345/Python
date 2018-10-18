#Everything should work.
import math

print("Enter 'Y' or 'y' for Yes and 'N' or 'n' for No.")

Wel = input("Welcome to Good Burger Home of the Good Burger may I take your order: ")

print("")


while Wel == "Y" or Wel == "y":
  CN = 0.45
  GB = 2.50
  MMS = 5.00
  D = 2.00
  if Wel == "Y" or Wel == "y":
      print("Place Order:")
      print("========================================")
      print("1. Chicken Nuggets - $0.45")
      print("2. Good Burger - $2.50")
      print("3. Mystery Meal Special - $5.00 ")
      print("4. Drinks - $4.00")
      print("")
      print("Choice")
      print("========================================")
      Opt = input("Enter Option: ")
      Opt = float(Opt)
      print("")
      print("Quantity")
      print("========================================")

  if Opt == 1:
       HM = input("How Many?: ")
       HM = float(HM)
       print("")
       CWT = HM*CN
       CT = CWT*0.08
       FP = CT+CWT
       print("Receipt")
       print("========================================")
       print("Tax: ",CT)
       print("Amount Purchased: ",HM)
       print("Sub Total: ",CWT)
       print("Total: ",FP)
       print("")
       print("Have a great day!!")
       break
  if Opt == 2:
        HM = input("How Many?: ")
        HM = float(HM)
        print("")
        CWT = HM*GB
        CT = CWT*0.08
        FP = CT+CWT
        print("Receipt")
        print("========================================")
        print("Tax: ",CT)
        print("Amount Purchased: ",HM)
        print("Sub Total: ",CWT)
        print("Total: ",FP)
        print("")
        print("Have a great day!!")
        break
  if Opt == 3:
        HM = input("How Many?: ")
        HM = float(HM)
        print("")
        CWT = HM*MMS
        CT = CWT*0.08
        FP = CT+CWT
        print("Receipt")
        print("========================================")
        print("Tax: ",CT)
        print("Amount Purchased: ",HM)
        print("Sub Total: ",CWT)
        print("Total: ",FP)
        print("")
        print("Have a great day!!")
        break
  if Opt == 4:
        HM = input("How Many?: ")
        HM = float(HM)
        print("")
        CWT = HM*D
        CT = CWT*0.08
        FP = CT+CWT
        print("Receipt")
        print("========================================")
        print("Tax: ",CT)
        print("Amount Purchased: ",HM)
        print("Sub Total: ",CWT)
        print("Total: ",FP)
        print("")
        print("Have a great day!!")
        break
if Wel == "N" or Wel == "n":
    print("Please Exit Good Burger.")