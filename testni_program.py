seznam_motorjev = [
    "Aprilia", "Benelli", "Beta", 
    "BMW", "Cagiva", "CF Moto", 
    "CPI", "Daelim", "Dnepr", 
    "Dream Pitbikes", "Ducati", "GasGas", 
    "Gilera", "Harley-Davidson", "Honda",
    "Husaberg", "Husqvarna", "Hyosung",
    "Indian", "Jawa", "Kawasaki",
    "KeeWay", "Kinroad", "KTM",
    "Kuberg", "Kymco", "Laverda",
    "LEM", "Loncin", "Malaguti",
    "Mash", "MOTO", "Moto Morini",
    "Motobi", "MotoGuzzi", "MV Agusta",
    "MZ", "NSU", "Oldtimer",
    "Pitbikes", "Puch", "Rieju",
    "Sachs", "Sherco", "Stomp",
    "Suzuki", "SWM", "Sym",
    "TM Racing", "TMS", "Tomos",
    "Triumph", "TRS", "Victory",
    "Xmotos", "Yamaha", "YCF",
    "Zongshen"]

import re
import json
import csv
import requests

# Nekateri avti nimajo podatka o prevoženih kilometrih. Te program izpusti, ker me niti ne zanimajo!

vzorec = re.compile(
    r'<img SRC=".+?" '
    r'alt="(?P<znamka>.+?)" '   # vzorec za znamko
    r'title=".+?"'
    r'[\s\S]+?1.registracija</td>\s+? <td class="w-75 pl-3">(?P<leto>\d\d\d\d)</td>' # leto 1. registracije 
    r'[\s\S]+?Prevoženih</td>\s+? <td class="pl-3">(?P<kilometri>.*? km)</td>' # prevoženi kilometri
    r'[\s\S]+?Menjalnik</td>\s+? <td class="pl-3 text-truncate">(?P<menjalnik>.*?)</td>' # vrsta menjalnika
    r'[\s\S]+?<div class="GO-Results-?T?o?p?-Price-TXT-Regular">(?P<cena>.*?)</div>'
)



# najdeni = re.findall(vzorec, vsebina)

# najdeni = re.search(vzorec, vsebina)


# zajem strani iz interneta, recimo da smo to naredili in jih imamo v testna_datoteka.html

motorji = []

with open('testna_datoteka.html', encoding='utf-8') as dat:
    vsebina = dat.read()
    najdeni = vzorec.finditer(vsebina)
    for i, ujemanje in enumerate(najdeni, 1):
        print(i, ujemanje.groupdict())
        motorji.append(ujemanje.groupdict())

# s tem bomo shranili v JSON datoteko
with open('motorji.json', 'w', encoding='utf-8') as dat:
    json.dump(motorji, dat, indent=4, ensure_ascii=False)


# newline="" naredi, da ni praznih vrstic v CSV datoteki!

with open("motorji.csv", "w", encoding="utf-8", newline="") as dat:
    writer = csv.DictWriter(dat, [
        "znamka",
        "leto",
        "kilometri",
        "menjalnik",
        "cena"
    ])
    for motor in motorji:
        writer.writerow(motor)

# mogoče je bolje če namesto celega zapisa imena za motor prevzame samo njegov znamko,
# da pogleda seznam znamk in poišče katera je, potem bom lahko primerjal statistiko po znamkah



# print(najdeni.group(1))