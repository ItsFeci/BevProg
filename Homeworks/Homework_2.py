def prog():
    print("Adja meg a haromszog harom oldalat cm-ben:")

    a_oldal = int(input("a oldal (cm): "))
    b_oldal = int(input("b oldal (cm): "))
    c_oldal = int(input("c oldal (cm): "))
    szerkesztheto = True

    if a_oldal >= b_oldal + c_oldal:
        szerkesztheto = False
    elif b_oldal >= a_oldal + c_oldal:
        szerkesztheto = False
    elif c_oldal >= a_oldal + b_oldal:
        szerkesztheto = False

    if szerkesztheto:
        print(f"A(z) {a_oldal}, {b_oldal} es {c_oldal} oldalu haromszog szerkesztheto")
    else:
        print(f"A(z) {a_oldal}, {b_oldal} es {c_oldal} oldalu haromszog NEM szerkesztheto")

if __name__ == "__main__":
    prog()