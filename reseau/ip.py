import socket
import requests
import whois
import sys
import subprocess
#-----------------------------
# Outil d'analyse d'IP
#   
# Crée par Iban Preuilh--Jauréguiberry  
# Petit projet pour analyser une IP : géolocalisation, reverse DNS, ping, WHOIS. Retourne des informations basiques
# Améliorations possibles :
# - Récupérer plus d'infos (ex: ASN, historique WHOIS)
# - Générer un rapport plus complet
# - Connecter à une base de données de vulnérabilités pour alerter sur les IPs suspectes
#
#-----------------------------


# -----------------------------
# GÉOLOCALISATION
# -----------------------------
def geolocaliser(ip):
    print("\n[+] Géolocalisation...")

    try:
        reponse = requests.get(f"http://ip-api.com/json/{ip}").json()

        print(f"Pays : {reponse.get('country')}")
        print(f"Ville : {reponse.get('city')}")
        print(f"ISP : {reponse.get('isp')}")
        print(f"Organisation : {reponse.get('org')}")

    except:
        print("Erreur géolocalisation")


# -----------------------------
# DNS Inverse
# -----------------------------
def dns_inverse(ip):
    print("\n[+] DNS Inverse...")

    try:
        hote = socket.gethostbyaddr(ip)
        print(f"Nom de domaine : {hote[0]}")
    except:
        print("Aucun reverse DNS")


# -----------------------------
# Ping
# -----------------------------
def ping(ip):
    print("\n[+] Ping...")

    try:
        resultat = subprocess.run(
            ["ping", "-n", "2", ip],
            capture_output=True,
            text=True
        )

        print(resultat.stdout)
    except:
        print("Erreur ping")


# -----------------------------
# WHOIS
# -----------------------------
def recherche_whois(ip):
    print("\n[+] WHOIS...")

    try:
        donnees = whois.whois(ip)
        print(f"Organisation : {donnees.org}")
        print(f"Pays : {donnees.country}")
    except:
        print("Erreur WHOIS")


# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":

    print("=== 🌍 Outil d'Intelligence IP ===")

    ip = input("Entrez une IP: ")

    geolocaliser(ip)
    dns_inverse(ip)
    ping(ip)
    recherche_whois(ip)

    input("\n=== Terminé ===\n\nAppuyez sur Entrée pour quitter...")