import socket
from os import system
#-----------------------------
# Scanner d'IP et de failles
#   
# Crée par Iban Preuilh--Jauréguiberry  
# Petit projet pour scanner les ports d'une IP et détecter des vulnérabilités basiques, plutôt orienté "simulation" que réel (pas de scan de vulnérabilités complexes, juste des messages d'alerte sur certains ports).
# Améliorations possibles : 
# - Multithreading
# - Scan de plages d'IP
# - Génération de rapports plus détaillés
#
#-----------------------------


# -----------------------------
# CONFIG
# -----------------------------
PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3389: "RDP"
}

# Vulnérabilités simples associées
VULN = {
    21: "FTP peut être mal sécurisé (anonymous login)",
    23: "Telnet non chiffré (dangereux)",
    445: "SMB vulnérable (ex: EternalBlue)",
    3389: "RDP exposé (bruteforce possible)"
}

# -----------------------------
# Scan IP
# -----------------------------
def scanner_ip(cible):
    print(f"\n[+] Scan de {cible}")
    ports_ouverts = []

    for port, service in PORTS.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        if sock.connect_ex((cible, port)) == 0:
            print(f"[OUVERT] {port} ({service})")
            ports_ouverts.append(port)

        sock.close()

    return ports_ouverts


# -----------------------------
# Analyse vulnérabilités
# -----------------------------
def analyser_vuln(ports_ouverts):
    print("\n[+] Analyse des vulnérabilités...")
    trouves = []

    for port in ports_ouverts:
        if port in VULN:
            print(f"[VULN] Port {port} : {VULN[port]}")
            trouves.append(port)

    return trouves


# -----------------------------
# Score
# -----------------------------
def calculer_score(ports_ouverts, vuln):
    score = 100

    score -= len(ports_ouverts) * 3
    score -= len(vuln) * 10

    return max(score, 0)


# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":
    print("=== Scanner d'IP et de failles ===")
    system("title Scanner d'IP et de failles")
    cible = input("Entrez une IP (laissez vide pour localhost): ") or "127.0.0.1"

    ports_ouverts = scanner_ip(cible)
    vuln = analyser_vuln(ports_ouverts)

    score = calculer_score(ports_ouverts, vuln)

    print("\n=== 📊 RÉSULTAT ===")
    print(f"Score de sécurité : {score}/100")

    if score > 80:
        print("🟢 Faible exposition")
    elif score > 50:
        print("🟠 Exposition modérée")
    else:
        print("🔴 Système exposé")

    input("\n=== Scan terminé ===\n\nAppuyez sur Entrée pour quitter...")