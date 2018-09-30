cena= float(input("Wprowadz cene samochodu: "))
podatek = cena*0.19
oplataRejestracyjna = float(cena*0.05)
prowizja = 30
dostawa = 50

print("cena samochodu po dodaniu wszystkich oplat", cena+podatek+oplataRejestracyjna+prowizja+dostawa)
