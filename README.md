# Python Aimaira OData

Wrapper Python pour les OData Aimaira d'Ipesup

## Installation de la librarie `python-odata`

La librairie `python-odata` est installable depuis PyPI via la commande

```bash
python -m pip install python-odata
```
La documentation est disponible sur [cette page](https://python-odata.readthedocs.io/en/latest/index.html).

## Installation du module

1) Télécharger ou cloner le repository. On suppose que le dossier téléchargé s'appelle `pyaimairapodata-master`.
2) Créer dans `pyaimairapodata-master/src/pyaimairaodata` un fichier `credentials.json` de la forme

```json
{
    "email": "",
    "password": ""
}
```

3) Installer le module : avec un terminal, se placer dans le dossier racine et exécuter la commande

```bash
python -m pip install .
```

## Utilisation du module

### Instancier un accès à l'odata d'Aimaira :
```python
from pyaimairaodata import AimairaOData

odata = AimairaOData()
```

### Récupérer toutes les entités de l'OData :
```python
odata.get_entities()
```

### Récupérer la liste des entités de l'OData provenant d'un univers donné :
```python
from pyaimairaodata.universe import Universe

# univers disponibles : ADMISSION, INSCRIPTION, PEDAGOGY, PLANIFICATION, ACADEMY, REFERENTIAL, FINANCE

odata.get_entities(universe=Universe.ADMISSION)
```
Il s'agit d'objets provenanant du module `python-odata`.

### Récupérer une entité
```python

odata[<entity_name>]
```

```python

odata.get(<entity_name>)
```

### Afficher les attributs d'une entité :
```python
entity.get_attributes()
```
`entity` est un objet de la classe `pyaimairaodata.Entity`

### Faire une requête sur une entité :
```python
odata.query(entity=<entity>)
```
Il faut ensuite compléter avec ce qu'on souhaite faire. Par exemple, pour obtenir tous les `EntitySet` de l'entité :
```python
odata.query(entity=<entity>).all()
```
Pour filtrer selon une condition :
```python
self.odata.query(self).filter(<condition>).all()
```
La condition est par exemple 
```python
<entity>._entity.InscriptionPeriode_Periode == "2024-2025"
```
Pour construire des conditions plus complexes, on utilisera les symboles `&` (et) et `|` (ou).
