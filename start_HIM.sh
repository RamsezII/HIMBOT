#!/bin/bash

# Déplacer l'exécution dans le répertoire du script
cd "$(dirname "$0")"

# Lancer la commande avec nohup pour qu'elle continue à s'exécuter en arrière-plan
nohup python3.11 HIM.py > output_HIM.txt &