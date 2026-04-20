#!/usr/bin/env python3
"""
TP3 - Mini Scanner

- Menu simple (top100, -sV, custom)
- Nmap requis (doit être installé)
- Cible limitée à 127.0.0.1 (localhost)
- Rapports horodatés dans ./reports/

À FAIRE (4 TODO) :
  1) timestamp()   → retourner AAAAMMJJ_HHMMSS
  2) check_nmap()  → True si nmap est trouvé, sinon False
  3) allowed_target(t) → autoriser seulement localhost/127.0.0.1/::1
  4) options custom → .split() la chaîne saisie
"""

import subprocess, os, datetime, shutil, sys

REPORTS_DIR = "reports"

# --- utilitaires déjà faits ---
def ensure_reports_dir():
    os.makedirs(REPORTS_DIR, exist_ok=True)

def save_report(content, prefix="scan"):
    ensure_reports_dir()
    name = f"{prefix}_{timestamp()}.txt"  # dépend de TODO-1
    path = os.path.join(REPORTS_DIR, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path

def run_nmap(args, target):
    cmd = ["nmap"] + args + [target]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return p.stdout
    except subprocess.CalledProcessError as e:
        return f"[ERREUR] nmap code {e.returncode}\n{e.stderr or ''}"

# --- TODOs à compléter ---

def timestamp():
    # TODO-1: retourner un horodatage AAAAMMJJ_HHMMSS (ex: 20251112_213000)
    raise NotImplementedError("TODO-1")

def check_nmap():
    # TODO-2: retourner True si nmap est dans le PATH, sinon False (shutil.which)
    raise NotImplementedError("TODO-2")

def allowed_target(t):
    # TODO-3: autoriser STRICTEMENT '127.0.0.1', 'localhost' ou '::1'
    raise NotImplementedError("TODO-3")

# --- menu déjà fait ---
def menu():
    print("\nMini-scanner — choisissez :")
    print("1) Scan rapide (top 100 ports)")
    print("2) Détection services (-sV)")
    print("3) Scan personnalisé (ex: -p 1-1024 -sV)")
    print("4) Quitter")
    return input("Choix (1-4) : ").strip()

def main():
    if not check_nmap():  # dépend de TODO-2
        print("nmap non trouvé. Installez nmap (ex: apt install nmap) et relancez.")
        sys.exit(1)

    while True:
        c = menu()
        if c == "4":
            print("Au revoir.")
            break

        target = input("Cible (seulement 127.0.0.1) : ").strip()
        if not allowed_target(target):  # dépend de TODO-3
            print("Cible non autorisée. Utilisez uniquement 127.0.0.1 / localhost.")
            continue

        if c == "1":
            out = run_nmap(["--top-ports", "100"], target)
            path = save_report(out, "top100")  # dépend de TODO-1
            print("Rapport créé :", path)

        elif c == "2":
            out = run_nmap(["-sV"], target)
            path = save_report(out, "sv")
            print("Rapport créé :", path)

        elif c == "3":
            # TODO-4: lire la ligne d'options et la transformer en liste avec .split()
            line = input("Options nmap (ex: -p 1-1024 -sV) : ").strip()
            if not line:
                print("Options vides — annulé.")
                continue
            # >>> remplacer la ligne suivante par la version TODO (.split())
            raise NotImplementedError("TODO-4")
            # out = run_nmap(options, target)
            # path = save_report(out, "custom")
            # print("Rapport créé :", path)

        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()
