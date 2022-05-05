## [MITK Diffusion](https://github.com/MIC-DKFZ/MITK-Diffusion/)

C'est une suite d'outils.

Documentation : https://github.com/MIC-DKFZ/MITK-Diffusion/

Contient, entres autres, les outils suivant.


### [Fiberfox](https://docs.mitk.org/2016.11/org_mitk_views_fiberfoxview.html)

Abandonné. On l'utilise par l'entremise du [Simulation Generator](#simulation-generator).

Le réplicat généré du fantôme FiberCup se trouve au lien suivant : https://www.nitrc.org/projects/diffusion-data/.


#### Wrapper

Wrapper Python de Fiberfox : https://github.com/PennBBL/fiberfox-wrapper  
Wrapper Python de Fiberfox, mis à jour : https://github.com/dPys/fiberfox-wrapper  
Wrapper Python de Fiberfox, ma version (inachevé) : https://github.com/benoit-dubreuil/fiberfox-wrapper


#### Génération aléatoires de fantômes

Le script `MitkRandomFiberPhantom.(bat | sh)` qui se situe à la racine de l'installation de MITK Diffusion.  
Documentation https://docs.mitk.org/2016.11/org_mitk_views_fiberfoxview.html.


## [Simulation Generator](https://bitbucket.org/voxsim/simulation_generator)

Outil [Python](https://www.python.org/) de génération de fibre de matière blanche d'[Alex Valcourt Caron](alex.valcourt.caron@usherbrooke.ca).

Code source : https://bitbucket.org/voxsim/simulation_generator

[Alex Valcourt Caron](alex.valcourt.caron@usherbrooke.ca) est (hiver 2022) un étudiant au doctorat à l'université de Sherbrooke sous la supervision du
professeur [Maxime Descoteaux](maxime.descoteaux@usherbrooke.ca) au laboratoire [SCIL](http://scil.dinf.usherbrooke.ca/).

L'extrant de l'outil est compatible avec Fiberfox (VTK).  
L'outil automatise la création manuelle de bundles de fibres de matières blanches de Fiberfox.

L'outil est supporté et utilisable. Il a déjà été utilisé par différentes personnes / étudiants. Il sera encore supporté.


### Prérequis

Voir la page du projet [Simulation Generator](https://bitbucket.org/voxsim/simulation_generator).


#### [Singularity](https://sylabs.io/)

Il faut utiliser [Singularity](https://sylabs.io/) qui est un exécuteur de conteneurs logiciels. Il faut l'installer sur une machine Linux. Pour Windows, utiliser l'environnement
WSL2.

Voici le [guide d'utilisation](https://sylabs.io/guides/latest/user-guide/quick_start.html).

Voici le [guide d'administration](https://sylabs.io/guides/latest/admin-guide/).


#### Python

Si Windows est utilisé, alors il faut que Python ≥ 3.7 soit installé dans l'environnement WSL2. Simulation Generator appelle la singularité à partir de scripts Python.


### Utilisation

Dans le but d'exploiter Simulation Generator aux fins du projet, je dois moi-même développer le ou les fichiers de configuration des paramètres de génération (ex: base_anchors).


#### Documentation

Afin d'avoir accès à la documentation dans un format ergonomique, il faut la construire à partir du script shell `build_documentation.sh` lorsque l'environnement Python est activé.

Répertoires et fichiers intéressants :

- `scripts/` contient des exemples
- `simulator/` contient l'API
- `scripts/geometry_factory.py`


#### Glossaire

- **Centroïde d'un bundle** : ligne directrice au centre du bundle, c'est-à-dire l'axe.


#### Remarques

Ce n'est pas grave si les ancres dépassent les limites. À cause de petits problèmes de clipping, on souhaite dépasser les ancres.


## [Phantomas](http://www.emmanuelcaruyer.com/phantomas.php)

Documentation : http://www.emmanuelcaruyer.com/phantomas.php  
Code source : https://github.com/ecaruyer/phantomas


## [Overleaf](https://www.overleaf.com)

Editeur de LaTeX pour l'écriture du rapport du cours INF6200.

Lien du document Overleaf du rapport : https://www.overleaf.com/project/6239d6dc52aac4c86b3c705e  
Lien d'un exemple PDF d'un rapport écrit avec Overleaf : https://github.com/linum-uqam/stage-2021-gael/blob/main/Rapport.pdf
