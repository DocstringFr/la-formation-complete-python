# Les opérateurs mathématiques

Il existe 4 opérateurs mathématiques de base en Python :

- \+ (addition)
- \- (soustraction)
- / (division)
- \* (multiplication)

Pas besoin de beaucoup d'explications pour ces opérateurs. À savoir que vous pouvez utiliser certains de ces opérateurs sur des chaînes de caractères ! Par exemple :
```python
>>> "Hello" * 3
"HelloHelloHello"
```

Cela peut être pratique si par exemple vous souhaitez rapidement afficher une ligne de séparation :
```python
>>> "-" * 50
--------------------------------------------------
```

Il existe également 3 opérateurs un peu plus avancés :

- % (appelé 'modulo')
- // (division entière)
- ** (puissance)

L'opérateur modulo retourne le reste de la division, par exemple :
```python
>>> 10 % 5
0
>>> 11 % 5
1
```

Dans le cas de figure ci-dessus, la division de 10 par 5 est égale à 2 et il reste 0. L'opérateur modulo retourne donc 0.

Dans le deuxième cas de figure, la division de 11 par 5 donne un reste de 1, qui est donc retournée par le modulo.

La division entière permet d'effectuer une division qui nous retournera toujours un nombre entier. Par exemple :
```python
>>> 10 / 3
3.3333333333333
>>> 10 // 3
3
```

À noter qu'avec une division normale, même si le compte est rond, la division vous retournera un nombre décimal :
```python
>>> 10 / 5
2.0
```

Ainsi, si vous souhaitez toujours récupérer un nombre entier, passez par la division entière.

Pour finir, l'opérateur puissance permet tout simplement d'effectuer un calcul du type 'a puissance n' :
```python
>>> 2 ** 2
4
>>> 2 ** 4
16
```

## Pour résumer :

Il existe en tout 7 opérateurs mathématiques, 4 de base (+, -, /, *) et 3 opérateurs avancés (%, //, **). Ces opérateurs permettent d'effectuer différentes opérations mathématiques, la plupart du temps sur des nombres, mais aussi dans certain cas sur des chaînes de caractères.

⚠️ Ne vous trompez pas pour l'opérateur de la multiplication, il s'agit bien du symbole 'astérisque' (*) et non pas de la lettre 'x'. Si vous essayez de faire `5 x 10` avec Python, vous aurez une erreur de syntaxe.

## Le module math
Si vous avez besoin d'effectuer des calculs mathématiques plus complexes, vous devrez utiliser le module math car pour ne pas trop surcharger les fonctions disponibles par défaut, Python ne charge pas toutes ces fonctions de base quand vous lancez un interpréteur.

Pour utiliser le module math, il faut l'importer comme ceci :
```python
import math
```

Une fois le module importé, vous pouvez utiliser toutes les fonctions contenues à l'intérieur du module, en préfixant la fonction du nom du module. Par exemple pour calculer une racine carrée :
```python
>>> racine = math.sqrt(16)
>>> print(racine)
4.0
```

Ci-dessous, vous trouverez une liste non-exhaustive des fonctions les plus utilisés et disponibles dans le module math :

- math.ceil(-4.7) : entier immédiatement supérieur, donne ici -4.
- math.exp(2) : exponentielle.
- math.factorial(5) : factorielle 5, donc 120 ici (fonctionne uniquement pour les entiers positifs).
- math.floor(-4.7) : partie entière, donne ici -5.
- math.isinf(x) : teste si x est infini (inf) et renvoie True si c'est le cas.
- math.log(2) : logarithme en base naturelle.
- math.log(8, 2) : log de 8 en base 2.
- math.log10(2) : logarithme en base 10.
- math.pow(2, 3) : 2 puissance 3 (peut aussi s'écrire 2 ** 3).
- math.sqrt(16) : racine carrée, donne ici 4.
- fonctions trigonométriques : math.sin, math.cos, math.tan, math.asin, math.acos, math.atan (argument en radians).
- fonctions hyperboliques : math.sinh, math.cosh, math.tanh, math.asinh, math.acosh, math.tanh.
- math.degrees(x) : convertit de radians en degrés.
- math.radians(x) : convertit de degrés en radians.

### Les constantes :
- math.pi (3.14159...)
- math.e (2.71828...)
