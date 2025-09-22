#### Fonction secondaire
def ispalindrome(p):
    p=p.lower()
    translator=str.maketrans("éêèëçàô-!?:',","eeeecao      ")
    p=p.translate(translator)
    p=p.replace(" ","")
    return p==p[::-1]
#### Fonction principale
def main():
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))
if __name__ == "__main__":
    main()
