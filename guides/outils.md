## [MITK Diffusion](https://github.com/MIC-DKFZ/MITK-Diffusion/)

C'est une suite d'outils.

Documentation : https://github.com/MIC-DKFZ/MITK-Diffusion/

Contient, entres autres, les outils suivant.


### [Fiberfox](https://docs.mitk.org/2016.11/org_mitk_views_fiberfoxview.html)

On l'utilise pour visualiser les fibres (`*.fib`) générées par la bibliothèque logicielle [Simulation Generator](#simulation-generator).

Le logiciel [Mi-Brain](https://scil-documentation.readthedocs.io/en/latest/tools/mi-brain.html) peut être utilisé à la place de Fiberfox, puisque ce premier est
conceptuellement une couche de visualisation par-dessus MITK-Diffusion.
Il est plus léger et plus simple à utiliser que MITK Diffusion.

Le réplicat généré du fantôme FiberCup se trouve au lien suivant : https://www.nitrc.org/projects/diffusion-data/.


#### Wrapper

Wrapper Python de Fiberfox : https://github.com/PennBBL/fiberfox-wrapper  
Wrapper Python de Fiberfox, mis à jour : https://github.com/dPys/fiberfox-wrapper  
Wrapper Python de Fiberfox, ma version (inachevée) : https://github.com/benoit-dubreuil/fiberfox-wrapper


#### Génération aléatoires de fantômes

Le script `MitkRandomFiberPhantom.(bat | sh)` qui se situe à la racine de l'installation de MITK Diffusion.  
Documentation https://docs.mitk.org/2016.11/org_mitk_views_fiberfoxview.html.


## [Simulation Generator](https://bitbucket.org/voxsim/simulation_generator)

Outil [Python](https://www.python.org/) de génération de fibre de matière blanche développé par [Alex Valcourt Caron](mailto:alex.valcourt.caron@usherbrooke.ca).
Cet outil est un wrapper Python de VoxSim.

Code source : https://bitbucket.org/voxsim/simulation_generator

Alex Valcourt Caron est un étudiant au doctorat à l'université de Sherbrooke (hiver 2022) sous la supervision du
professeur [Maxime Descoteaux](mailto:maxime.descoteaux@usherbrooke.ca) au laboratoire [SCIL](http://scil.dinf.usherbrooke.ca/).

L'extrant de l'outil est compatible avec Fiberfox (VTK).  
L'outil automatise la création manuelle de bundles de fibres de matières blanches de Fiberfox.

L'outil est supporté et utilisable.
Il a déjà été utilisé par différentes personnes / étudiants.
Il sera encore supporté.


### Prérequis

Voir la page du projet [Simulation Generator](https://bitbucket.org/voxsim/simulation_generator).


#### [Singularity](https://sylabs.io/)

[Singularity](https://sylabs.io/) est un exécuteur de conteneurs logiciels employé afin de simplifier l'accès à [VoxSim](https://bitbucket.org/voxsim/), le rouleur de
simulations de fibres de matière blanche qui est basé sur MITK Diffusion.
La simulation consiste en la génération de fibres de matière blanche jusqu'à la simulation de l'acquisition de signaux d'IRM.

Il faut l'installer sur une machine Linux.
Pour Windows, utiliser l'environnement WSL2.

Voici le [guide d'utilisation](https://sylabs.io/guides/latest/user-guide/quick_start.html).
Voici le [guide d'administration](https://sylabs.io/guides/latest/admin-guide/).


#### Python

Si Windows est utilisé, alors il faut que Python ≥ 3.7 soit installé dans l'environnement WSL2. Simulation Generator appelle la singularité à partir de scripts Python.


### Utilisation

Dans le but d'exploiter Simulation Generator aux fins du projet, je dois moi-même développer le ou les fichiers de configuration des paramètres de génération (ex:
base_anchors).


#### Exécution

Activez l'environnement Python dans lequel [Simulation Generator](#simulation-generator) a été installé.

```shell
source ./env/bin/activate
```

Lancez la simulation en prenant soin de ne fournir que des chemins absolus dépourvus de liens symboliques.
Dans le cas suivant, je suis connecté au sous-système Ubuntu (WSL2) de ma machine Windows 10.

```shell
python3 ./simulation_generator/scripts/simulation_runner.py --out /mnt/c/Users/Admin/Documents/Moi/Workspace/School/UQAM/inf6200-h2022/user/out
```

Allez dans dans le dossier `geometry_outputs`.

```shell
cd ./out/geometry_outputs/
```

Constatez les fichiers extrants.

```shell
ls -l
```

Constatez le fichier `*merged_bundles.fib` qui contient la fusion de tous bundles générés de fibres de matière blanche.

```shell
ls -l *merged_bundles.fib
```

#### Extrants

La simulation (VoxSim) génère, entre autres, des fichiers `*.fib` dans le dossier `geometry_outputs` de la sortie, en plus des fichiers `*.vspl` et `*geometry_base.json`
à la racine de la sortie.

Le fichier `*.vspl` est un fichier de configuration et de limites de fibres.
C’est en fait le monde des fibres ou des grappes (clusters) de fibres.
Penser à un monde local d’un modèle / objet en infographie vs `*geometry_base.json` qui est le monde racine.

Les fichiers `*.nii` sont des images 3D / 4D.

Les fichiers `*.vtk` contiennent les points sur les surfaces des sphères

Pour l'instant, seulement les fichiers `*.fib` nous intéressent.

#### Documentation

Afin d'avoir accès à la documentation dans un format ergonomique, il faut la construire à partir du script shell `build_documentation.sh` lorsque l'environnement Python
est activé.

Répertoires et fichiers intéressants :

- `scripts/` contient des exemples
- `simulator/` contient l'API
- `scripts/geometry_factory.py`


#### Glossaire

- **Centroïde de bundle** ([Simulation Generator](#simulation-generator)) : ligne directrice au centre du bundle, c'est-à-dire l'axe.
  Dans l'outil [Simulation Generator](#simulation-generator), un centroïde de bundle est définit par l'entremise d'une [spline](https://fr.wikipedia.org/wiki/Spline)
  composée d'ancres.
  Lors de la simulation, la spline génère des ellipses, tout comme [Fiberfox](#fiberfox).
- **Sphèrere** ([Simulation Generator](#simulation-generator)) : définit un compartiment qui n'est pas de la matière blanche, par exemple la matière grise ou de l'eau.


#### Remarques

Ce n'est pas grave si les ancres dépassent les limites. À cause de petits problèmes de clipping, on souhaite dépasser les ancres.


## [Phantomas](http://www.emmanuelcaruyer.com/phantomas.php)

Documentation : http://www.emmanuelcaruyer.com/phantomas.php  
Code source : https://github.com/ecaruyer/phantomas


## [Overleaf](https://www.overleaf.com)

Editeur de LaTeX pour l'écriture du rapport du cours INF6200.

Lien du document Overleaf du rapport : https://www.overleaf.com/project/6239d6dc52aac4c86b3c705e  
Lien d'un exemple PDF d'un rapport écrit avec Overleaf : https://github.com/linum-uqam/stage-2021-gael/blob/main/Rapport.pdf
