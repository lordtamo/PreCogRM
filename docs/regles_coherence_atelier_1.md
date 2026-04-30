# Règles de cohérence — Atelier 1 EBIOS RM

Ce document énonce les règles de cohérence fonctionnelles et méthodologiques applicables à l’Atelier 1 dans PreCogRM.  
Ces règles sont non négociables afin de garantir la conformité à EBIOS Risk Manager.  
Elles servent de référence pour le développement, la validation et l’audit.

---

## 1. Règles générales de l’Atelier 1

1. L’Atelier 1 ne produit **aucun calcul de risque**.
2. Aucun lien avec :
   - une source de risque,
   - un scénario,
   - une vraisemblance,
   n’est autorisé.
3. Tous les éléments produits doivent être compréhensibles sans connaissance implicite.

---

## 2. Règles liées aux valeurs métiers

### 2.1 Existence et complétude

- Une valeur métier :
  - doit avoir un nom,
  - doit avoir une nature,
  - doit impérativement contenir une justification de son caractère essentiel.

➡️ Une valeur sans justification est **invalide**.

---

### 2.2 Granularité

- Plusieurs niveaux de granularité peuvent coexister.
- Aucune hiérarchie technique n’est imposée.
- L’outil ne doit jamais déduire automatiquement qu’une valeur est plus importante qu’une autre.

---

### 2.3 Relation aux périmètres

- Une valeur métier peut être liée à :
  - zéro périmètre (cas transitoire),
  - un périmètre,
  - plusieurs périmètres.
- La suppression d’un lien ne supprime ni la valeur, ni le périmètre.

---

## 3. Enjeux et impacts

- Les enjeux (C/I/D/…) sont :
  - descriptifs uniquement,
  - non chiffrés,
  - non comparables automatiquement.
- Les impacts :
  - sont exprimés en langage métier,
  - ne constituent pas une gravité EBIOS.

---

## 4. Traçabilité et audit

1. Toute modification doit être historisée.
2. Aucun objet de l’Atelier 1 ne peut être supprimé physiquement.
3. Les données doivent rester lisibles en extraction (audit, homologation).

---

## 5. Interdictions explicites

L’outil ne doit en aucun cas :

- calculer un score,
- classer automatiquement les valeurs métiers,
- inférer une gravité,
- proposer des mesures de sécurité,
- générer des scénarios à ce stade.

---

## 6. Critère de complétude de l’Atelier 1

L’Atelier 1 est considéré comme conforme lorsque :

- le périmètre est clairement défini,
- les valeurs métiers sont identifiées et justifiées,
- les liens valeur ↔ périmètre sont explicites,
- aucun raisonnement de menace ou de risque n’est introduit.

---

## 7. Prompt de génération de code (pour LLM)

> Tu es un développeur chargé d’implémenter les règles de validation de l’Atelier 1 EBIOS RM.  
> Implémente ces règles comme des contrôles explicites et commentés.  
> Le code doit :
> - bloquer toute incohérence méthodologique,
> - expliquer chaque règle dans des commentaires lisibles,
> - être maintenable et extensible pour les ateliers suivants.
``
