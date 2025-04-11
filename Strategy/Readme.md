# Design Pattern : Strategy

Le design pattern Strategy (ou patron de conception Stratégie) est **un modèle comportemental** en programmation orientée objet qui permet de définir une famille d’algorithmes, de les encapsuler dans des classes distinctes et de rendre leurs objets interchangeables. Ce modèle est particulièrement utile pour modifier dynamiquement le comportement d’un objet sans changer son code source.

---- 

![alt text](../Img/Strategy_Pattern_in_UML.png)

## Principes du design pattern Strategy
Encapsulation des algorithmes : Les différentes variantes d’un comportement ou d’un algorithme sont isolées dans des classes séparées, ce qui permet de les gérer indépendamment.

- Interchangeabilité : Les objets représentant ces algorithmes peuvent être substitués à tout moment, permettant ainsi une flexibilité au moment de l’exécution.

- Composition plutôt qu’héritage : Contrairement à l’héritage, qui peut rendre le code rigide, la stratégie utilise la composition pour déléguer les comportements à des objets spécifiques. Cela respecte le principe Open/Closed (ouvert à l'extension, fermé à la modification).

--- 

### Utilisation typique
Le design pattern Strategy est utile dans les cas suivants :

Lorsque plusieurs algorithmes ou comportements doivent être disponibles pour un objet, et que vous souhaitez pouvoir en changer dynamiquement.

Lorsque vous avez beaucoup de classes qui diffèrent uniquement par leur manière d’exécuter un comportement spécifique.

Pour éviter la duplication de code en regroupant les variantes dans une hiérarchie de classes distinctes.

### Exemple concret
Un exemple classique est celui d’une boutique en ligne proposant plusieurs méthodes de paiement (PayPal, carte bancaire). Chaque méthode de paiement est implémentée comme une classe distincte (stratégie concrète), et le système peut facilement passer d’une méthode à une autre selon le choix du client.
#### Diagramme UML simplifié
Context : L'objet principal qui utilise une stratégie.

Strategy : Interface commune pour toutes les stratégies.

ConcreteStrategy : Implémentation spécifique d’un algorithme.

---------- 

Avantages
Flexibilité accrue grâce à la possibilité de changer les algorithmes au moment de l’exécution.

Réduction du couplage entre les classes.

Respect des principes de conception comme le Open/Closed Principle.

Inconvénients
Peut entraîner une augmentation du nombre de classes dans le projet, rendant la gestion plus complexe.

Cas	Exemple de Stratégie
|  Cas                     |  Exemple de Stratégie                            |
|---------------------------|----------------------------------------------------|
| Prétraitement             | Normalisation : `StandardScaler`, `MinMaxScaler`, `RobustScaler` |
| Sélection de features     | `SelectKBest`, `PCA`, `RFE`                        |
| Optimiseur                | `SGD`, `Adam`, `RMSProp`                           |
| Métrique d’évaluation     | `Accuracy`, `F1`, `AUC`                            |
