# Les variables

## Différents types

Avec Python, vous pouvez utiliser différents types de variables, tels que les nombres entiers, les nombres décimaux ou encore les chaînes de caractères.

## Créer une variable

Pour créer une variable, c'est très simple, il suffit de lui donner un nom et une valeur, comme ceci :
```python
a = 5
```

☝️ Ci-dessus, on créé une variable que l'on appelle `a` et qui contient le **nombre entier** `5`.

### Quelques règles à suivre

Pour nommer une variable, il y a quelques règles que vous devez suivre, au risque de vous retrouver avec une erreur :

- Le nom d'une variabe doit commencer par **une lettre** ou un **tiret du bas.**
- Le nom d'une variable ne peut contenir que des **lettres**, des **nombres** et des **tirets du bas**.

Vous pouvez donc inclure des nombres dans le nom des variables, tant qu'il ne sont **pas au début** du nom. Vous ne pouvez par contre inclure **aucun symbole** (pas de @$%* etc). 

Également, le nom des variables est sensible à la casse. Ainsi, `ville`, `Ville` et `VILLE` sont considérés par Python comme trois variables différentes.

### Convention PEP-8

Selon les conventions de la PEP-8, il est conseillé de nommer vos variables uniquement avec des lettres minuscules en séparant les différents mots par un tiret du bas.

Les trois noms de variabe suivant sont tous valides, mais on préférera utiliser le premier :

    ✅ nom_de_famille
    ⚠️ NomDeFamille
    ⚠️ nomdefamille

Pour vous donner quelques exemples, voici une liste de noms de variables qui sont valides (✅), valides mais qui ne suivent pas la convention PEP-8 (⚠️) et invalides (🛑) :

    ✅ site_web
    ⚠️ NomDeLaVille
    🛑 5_employes
    ✅ adresse_email
    ⚠️ Salaire
    🛑 @dresseEmail
    ✅ taux_horaire

## Les mots réservés

Python utilise des noms qui sont réservés par le langage pour décrire certains comportements. Vous ne pouvez donc pas utiliser ces mots réservés comme nom de variable. Voici la liste des mots réservés par Python :
```python
False
class
finally
is
return
None
continue
for
lambda
try
True
def
from
nonlocal
while
and
del
global
not
with
as
elif
if
or
yield
assert
else
import
pass
break
except
in
raise
```