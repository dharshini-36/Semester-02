cosmetic_brands = {
    "Lakme": ["foundation", "Lipstick", "eyeliner"],
    "Maybelline": ["Fitme", "Compact", "Mascara"],
    "Insight": ["Eyeshadow", "Kajal", "Primer"],
    "Nykaa": ["Eyeliner", "Highlighter", "concealer"],
    "Facescanada": ["Lipstick", "Highlighter", "Compact"]
}
     
give=input()
if give in cosmetic_brands:
    print(f"{give}")
    for i in cosmetic_brands[give]:
        print("->",i)
    
else:
    print("brand not found")

    

n1=int(input())
n2=int(input())
operation=int(input())
match operation:
    case 1:
        print(f"sum={n1+n2}")
    case 2:
        print(f"sub={n1-n2}")
    case 3:
        print(f"multiply={n1*n2}")
    case 4:
        print(f"division={n1/n2}")
    case 5:
        print(f"exponent={n1**n2}")
    case _:
        print("something went wrong)
              

