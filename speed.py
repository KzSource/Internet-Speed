# I am not risponsible of any acts you do with this tool.

import colorama
from colorama import Fore, Back, Style
import time
import speedtest

print(Fore.BLUE + "   |<>====> Kz's Tools <====<>|")
time.sleep(0.5)
print(Fore.RED + "          Created By Kz.")
print("=====> Network Scanner Tool <=====")
print("              >>V3<<             ")
print("")
print(Fore.LIGHTCYAN_EX + "Note: Si cet outil n'est plus valable ou ne marche plus, merci d'en informer le créateur [> Kz#1114] merci.")
print("")
time.sleep(1)
print(Fore.GREEN + "L'analyse se lancera dans quelques secondes.")
time.sleep(2)
print("")
test = speedtest.Speedtest()

print("Chargement de la liste des serveurs. . .")
test.get_servers()
print("Choix du meilleur serveur. . .")
best = test.get_best_server()
print(f"Trouvé: {best['host']} localisé dans {best['country']}")

print("Exécute le test d'installation. . .")
download_result = test.download()
print("Exécute le test d'envoi. . .")
upload_result = test.upload()
print("Exécute le test de la latence. . .")
ping_result = test.results.ping
time.sleep(1)

print(Fore.YELLOW + "")
print(f"Vitesse d'installation: {download_result / 1024 / 1024:.2f} Mbit/s")
print(f"Vitesse d'envoi: {upload_result / 1024 / 1024:.2f} Mbit/s")
print(f"Latence: {ping_result:.2f} ms")

print(Fore.RED + "")
time.sleep(1)

print("Created By Kz.")
print("Ⓒ Copyright Kz | Kz's Tools | Developper.")

#Created By Kz
