
def main(): #marks the start of the main block
    Dia=float(input("Enter the dia of Anemometer in centimeter : "))
    R=int(input("Enter the number of revolutions per minute : "))
    s=(Dia*R*0.0011712)
    s1=(Dia*R*0.00188495)
    s2=(Dia*R*0.00052338)
    P=(0.00256*s*s)
    print(" ")
    print(" speed of air is: ",s,"miles/hr")
    print(" speed of air is: ",s1,"km/hr")
    print(" speed of air is: ",s2,"m/s")
    print(" Air Pressure is: ",P,"Pascal (Pa)")
    restart=input("Do you want to rerun the program y/n: ").lower()
    if restart == "y":
        main()
    else:
        print("End of program")
        exit()
main() #marks the closure of the main block # new addition

    
        

