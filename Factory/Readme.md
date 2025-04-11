# Design Pattern : Factory

Le **Design Pattern Factory** est un modèle de création puissant en programmation orientée objet. Il permet de créer des objets sans avoir à spécifier la classe exacte de l'objet à instancier. La logique de création est déléguée à une classe dédiée appelée **"usine" (factory)**.

---

##  Pourquoi utiliser le Factory Pattern ?

-  **Délégation de la création d’objets**  
  Au lieu de créer directement des instances de classes, on utilise une *factory* pour produire les objets souhaités.

-  **Flexibilité accrue**  
  Les usines peuvent retourner différents types d'objets selon les paramètres d'entrée, ce qui offre une grande adaptabilité au contexte d'exécution.

-  **Réduction du couplage**  
  Le client n’a pas besoin de connaître la classe exacte des objets qu’il utilise. Cela améliore la modularité et facilite la maintenance du code.

---

## 📚 En résumé

Le **Factory Pattern** permet :
- De déléguer la création d'objets.
- De rendre la création plus flexible et dynamique.
- De réduire le couplage entre les composants du système.

---

## 📝 Référence

> https://en.wikipedia.org/wiki/Factory_method_pattern#:~:text=Room%20is%20the%20base%20class,in%20the%20event%20of%20change.

>https://dagster.io/blog/python-factory-patterns
---

##  Exemple d'utilisation


###  Problème
Dans de nombreux projets logiciels, on doit créer des objets dont le type peut varier selon les besoins, les entrées utilisateur ou les conditions d'exécution. Supposons que tu développes une application de dessin, de simulation géométrique ou même de calcul de propriétés physiques sur différentes formes.

Si tu crées manuellement chaque objet avec Cercle(...), Rectangle(...), etc., ton code devient rigide, difficile à maintenir, et fortement couplé aux classes concrètes. Cela rend :

- les changements futurs plus risqués,

- le code plus difficile à tester ou à étendre (par exemple, ajouter une nouvelle forme),

- l'utilisation dynamique impossible sans connaître d’avance les types exacts.

### Solution 
Tu veux une solution où **le type de forme n’est pas connu à l’avance**. Par exemple :

L’utilisateur saisit "cercle" dans une interface ou un fichier de config.

Un script lit des formes depuis un fichier JSON ({ "type": "cercle", "rayon": 5 }).

Tu veux réutiliser la logique de création dans plusieurs modules sans répéter le code.

### Le Factory Pattern
**L’idée est de déléguer la logique de création à une classe `FormeFactory`, qui décidera quel type de forme instancier. Le client (ton application principale) n’a pas besoin de connaître la classe exacte (`Cercle`, `Rectangle`, etc.).** 

Cela apporte :

* Flexibilité : on peut facilement créer de nouvelles formes.

* Modularité : le code est plus propre, mieux séparé.

* Testabilité : on peut tester la factory séparément.

* Extensibilité : on peut ajouter de nouvelles formes sans toucher au code existant.

## Cas d'utilisation

- Création dynamique de modèles ML (Model Factory)
- Loader de dataset selon la source (local, S3, HuggingFace, etc.)
- Déploiement ou inférence dynamique
