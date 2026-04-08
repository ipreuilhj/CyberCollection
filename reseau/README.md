# 🌐 Scanner d'IP et de failles

## 📌 Description
Ce script permet de scanner une adresse IP afin de détecter les ports ouverts et d’identifier des vulnérabilités potentielles associées aux services exposés.

L’outil utilise du multithreading pour accélérer le scan et fournir des résultats rapides.

---

## ⚙️ Fonctionnalités
- Scan des ports les plus courants
- Détection des services (HTTP, SSH, FTP…)
- Identification de vulnérabilités connues (logique simplifiée)
- Scan rapide grâce au multithreading
- Calcul d’un score de sécurité

---

## 🚀 Utilisation

python scan.py <IP>

## 📊 Exemple de sortie

[OPEN] 80 (HTTP)
[OPEN] 445 (SMB)

[VULN] 445 : SMB vulnérable (EternalBlue)

Score : 75/100


---

# 🌍 Outil d'analyse d'IP

## 📌 Description
Cet outil permet de collecter des informations publiques sur une adresse IP.

Il s’inscrit dans une démarche OSINT (Open Source Intelligence) et permet d’obtenir des données utiles pour l’analyse réseau ou les enquêtes.

---

## ⚙️ Fonctionnalités
- Géolocalisation IP (pays, ville, ISP)
- Reverse DNS (nom de domaine associé)
- Test de connectivité (ping)
- Informations WHOIS

---

## 🚀 Utilisation

python ip.py

## 📊 Exemple de sortie

Pays : United States
Ville : Mountain View
ISP : Google LLC

Nom de domaine : dns.google
