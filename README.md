[![forthebadge](http://forthebadge.com/images/badges/made-with-python.svg)](https://ecoris.com)
[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](https://ecoris.com)
[![forthebadge](https://forthebadge.com/images/badges/designed-in-ms-paint.svg)](https://forthebadge.com)


> **Note**
> Interface graphique disponible !


# EBP Installer 2022

L'exécutable "EBP2022.exe" vous permettra d'installer la suite de logiciel EBP en fonction de vos choix.<br>

> **Note**
> Logiciels disponibles :
- EBP Open Line 2022 Autonome Paie | V.13_14_0_13423
- EBP Open Line 2022 Classic BusinessPlan | V.14_0_0_2005
- EBP Open Line 2022 LigneOL CRM | V.14_0_0_1201
- EBP Open Line 2022 LigneOL_Immos | V.14_0_0_3619
- EBP 2022 Comptabilite ELITE | V.21_0_0_9593
- EBP 2022 Etats Financiers PRO | V.21_3_1_3765
- EBP 2022 Gestion ELITE | V.21_1_0_6632
***

Code source disponible dans l'archive.<br>
> **Note**
> Le code source ne comporte pas les licences.
Script compilé à l'aide du module : <a href='https://pypi.org/project/auto-py-to-exe/' target="_blank">AUTO-PY-TO-EXE</a>.

> pyinstaller --noconfirm --onefile --windowed --icon "<path_to_ico>/ebp.ico" --name "EBP2022" --version-file "<path_to_versionfile>/file_version_info.txt" --uac-admin --add-data "<path_to_packages>/site-packages/customtkinter;customtkinter/"  "<path_to_py>/EBP_tkinter.py"
## How To Use
> **Note**
> Vous pouvez simplement télécharger le répertoire et lancer l'exécutable.
> **Note**
> Installation avec téléchargement de l'archive.
```bash
# Cloner ce répertoire
$ git clone https://github.com/greverdy/EBPInstaller2022.git
# Aller dans le répertoire
$ cd EBPInstaller2022
# Lancer l'application
$ EBP2022.exe
```
## TroubleShooting

- Systèmes d'exploitation supportés : Windows [sans le mode S ⚠] ;
- Désactiver le mode S : <a href="https://support.microsoft.com/fr-fr/windows/sortie-du-mode-s-dans-windows-4f56d9be-99ec-6983-119f-031bfb28a307">Sortie du mode S dans Windows</a> ; 
- Vérifier que vous n'avez aucune mise à jour en attente ⚠ ;
- <a href="mailto:informatique@ecoris.fr?subject=Problème avec l'application : EBPInstaller&body= --- Merci de détailler au mieux votre demande pour que nous puissions vous aider au plus vite ---" target="_blank"> Signaler une erreur / Autres problèmes ➡ mail à : informatique@ecoris.fr ;</a>
