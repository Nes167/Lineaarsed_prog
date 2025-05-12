import json
import os

faili_nimi="kontaktid.json"

def loe_failist():
    if not os.path.exists(faili_nimi):
        return[]
    with open(faili_nimi,'r',encoding="utf-8-sig") as f:
        return json.load(f)

def salvesta_kontaktid(kontaktid):
    with open(faili_nimi,'r',encoding="utf-8-sig") as f:
        json.dump(kontaktid, f, ensure_ascii=False, indent=4)

def lisa_kontakt(kontaktid, nimi, telefon,email):
    kontaktid.append({'nimi':nimi, "telefon": telefon,"email":email})

def otsi_kontakt(kontaktid , nimi):
    return [k for k in kontaktid if nimi.lower() in k['nimi'].lower()]

