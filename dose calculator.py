import os,sys,subprocess,time
#ISSIK
#pédiatrie
#med amine
#calcul de dose
try:
    q=int(input("entrer la quantité de traitement indiqué sur l'ampoule en mg: "))
    d=int(input("entrer le volume de dissolution du produit en ml: "))
    dp=int(input("quelle est la dose prescrite en mg: "))
    s=int(input("1 ml de la seringue utilisée correspond a combien de graduation: "))
    print("  ********** résultat *********")
    y=dp*(s*d)/q
    if y % 1 == 0:
        print(f"dose prenable ,on prend {y } graduations")
    else:
        u=q//(s*d)
        q1=(y // 1) * u
        q2=dp-q1
        i=0
        while 1:
            if q2 * (1+i) % u == 0:
                break
            else:
                i+=1
        p=1+i - (q2 * (1+i) // u)
        t= y//1+ q2 * (1+i) // u
        y1=q2 * (1+i) // u
        print(f"on prend une graduation de ttt pure ,on l'ajoute {i} G  de sérum physiologique,on purge {p} G et on garde {y1} G du ttt rédilué")
        print(f"au total {t} G: {y//1} G de ttt pure et {y1} G ttt rédu.")
    print("***********************************************************************")
    time.sleep(10)
    subprocess.call([sys.executable, os.path.realpath(__file__)] +
sys.argv[1:])
except:
    print("**************************")
    print("VEUILLEZ VÉRIFIER  VOS ENTRÉE")
    print("**************************")
    subprocess.call([sys.executable, os.path.realpath(__file__)] +
sys.argv[1:])