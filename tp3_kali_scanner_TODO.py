#!/usr/bin/env python3
"""
TP3 - Mini Scanner Kali avec nmap
[VERSION DÉMO - ne pas distribuer]
"""

import time
import random
import sys
from datetime import datetime
from pathlib import Path


BANNER = r"""
 ███╗   ███╗██╗███╗   ██╗██╗    ███████╗ ██████╗ █████╗ ███╗   ██╗
 ████╗ ████║██║████╗  ██║██║    ██╔════╝██╔════╝██╔══██╗████╗  ██║
 ██╔████╔██║██║██╔██╗ ██║██║    ███████╗██║     ███████║██╔██╗ ██║
 ██║╚██╔╝██║██║██║╚██╗██║██║    ╚════██║██║     ██╔══██║██║╚██╗██║
 ██║ ╚═╝ ██║██║██║ ╚████║██║    ███████║╚██████╗██║  ██║██║ ╚████║
 ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
                     420-LAP-OS • Collège O'Sullivan
"""

CAUGHT = r"""
   ██████╗  ██████╗ ████████╗  ██╗   ██╗ █████╗ ██╗
  ██╔════╝ ██╔═══██╗╚══██╔══╝  ╚██╗ ██╔╝██╔══██╗██║
  ██║  ███╗██║   ██║   ██║      ╚████╔╝ ███████║██║
  ██║   ██║██║   ██║   ██║       ╚██╔╝  ██╔══██║╚═╝
  ╚██████╔╝╚██████╔╝   ██║        ██║   ██║  ██║██╗
   ╚═════╝  ╚═════╝    ╚═╝        ╚═╝   ╚═╝  ╚═╝╚═╝
"""

MESSAGES = [
    "[!] 404 — Solution Not Found",
    "[!] Nice try champion",
    "[!] Copier-coller detected — access denied",
    "[!] La démo c'est pour voir le comportement, pas la solution",
    "[!] Le vrai code, tu l'écris toi-même",
    "[!] C'est pas Stack Overflow ici",
    "[!] Faut coder, pas juste regarder",
    "[!] Debug ton cerveau, pas le mien",
]

HINTS = [
    "💡 Hint: subprocess.run() c'est ton ami",
    "💡 Hint: pathlib.Path pour créer les dossiers",
    "💡 Hint: datetime.now().strftime() pour les timestamps",
    "💡 Hint: try/except pour les erreurs de nmap",
    "💡 Hint: lis la doc de subprocess, tout est dedans",
]


def matrix_rain(duree=1.2):
    chars = "01█▓▒░@#$%&*+=?~"
    start = time.time()
    while time.time() - start < duree:
        line = "".join(random.choice(chars) for _ in range(70))
        print(f"\033[92m{line}\033[0m")
        time.sleep(0.04)


def typing(text, delay=0.025):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(delay)
    print()


def progress_bar(label, duree=1.8):
    print(f"\n[*] {label}")
    for i in range(0, 101, 5):
        bar = "█" * (i // 5) + "░" * (20 - i // 5)
        print(f"\r    [{bar}] {i}%", end="", flush=True)
        time.sleep(duree / 20)
    print()


def menu():
    print("\n" + "═" * 64)
    print("                    MINI SCANNER - TP3")
    print("═" * 64)
    print("  1) Scan rapide (top 100 ports)")
    print("  2) Détection de services (-sV)")
    print("  3) Scan personnalisé")
    print("  4) Quitter")
    print("═" * 64)


def fake_scan(nom_scan):
    print()
    progress_bar(f"Initialisation : {nom_scan}", 1.5)
    print("[*] Loading nmap modules...")
    time.sleep(0.4)
    print("[*] Resolving target 127.0.0.1...")
    time.sleep(0.4)
    print("[*] Sending packets...")
    time.sleep(0.6)

    print("\n\033[92m")
    matrix_rain(1.0)
    print("\033[0m")

    print("\033[91m")
    print(CAUGHT)
    print("\033[0m")

    print(f"\033[93m{random.choice(MESSAGES)}\033[0m")
    print(f"\033[96m{random.choice(HINTS)}\033[0m\n")
    print("─" * 64)
    print("  Le comportement attendu? Scanner 127.0.0.1 avec nmap,")
    print("  parser la sortie, sauvegarder dans reports/ avec timestamp.")
    print("  À vous de coder la logique derrière 👾")
    print("─" * 64)


def main():
    print("\033[91m")
    print(BANNER)
    print("\033[0m")

    time.sleep(0.3)

    print("\033[93m")
    typing("  [*] Loading framework...")
    typing("  [*] Modules loaded: scanner, reporter, logger")
    typing("  [*] Target scope: 127.0.0.1 only")
    typing("  [*] Ready.")
    print("\033[0m")

    time.sleep(0.3)

    print("\n⚠️  Scanner uniquement 127.0.0.1 — tout scan externe est illégal\n")

    while True:
        menu()
        choix = input("  > ").strip()

        if choix == "1":
            fake_scan("scan_rapide")
        elif choix == "2":
            fake_scan("scan_services")
        elif choix == "3":
            options = input("  Options nmap (ex: -p 1-1024 -sV) : ").strip()
            print(f"\n[*] Options: {options}")
            time.sleep(0.5)
            fake_scan("scan_perso")
        elif choix == "4":
            print("\n\033[92m  [*] Session closed.\033[0m\n")
            break
        else:
            print("\033[91m  [!] Choix invalide\033[0m")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n\033[91m  [!] Interrupted.\033[0m\n")
