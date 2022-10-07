class Team:
    def __init__(self, nev, projekt, szerepkor):
        self.nev = nev
        self.projekt = projekt
        self.szerepkor = szerepkor
        print("-- Developer letrehozva. --") 
        print(f"{nev} a {projekt}-en dolgozik {szerepkor} Szerepkorben")

    def __eq__(self, masik_dev):
        return self.projekt == masik_dev.projekt

def eggyutt_dolgoznak(dev_team):
    for index_i, item_i in enumerate(dev_team):
        for index_j, item_j in enumerate(dev_team):
            if item_i.projekt == item_j.projekt and index_i < index_j:
                print(f"{item_i.nev} es {item_j.nev} dolgoznak egy projekten")
        pass


def main():
    
    Developer1 = Team("Ricsi","SolArch","Frontend")
    Developer2 = Team("Angela","ZerTeng","Tesztelo")
    Developer3 = Team("Peti","KefERP","Backend")
    Developer4 = Team("Eva","KefERP","Frontend")
    print()

    ubisoft = [Developer1, Developer2, Developer3, Developer4]
    eggyutt_dolgoznak(ubisoft)
    

        

if __name__ == "__main__":
    main()