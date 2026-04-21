# Description des fichiers du projet PreCogRM

Ce fichier présente la liste des documents de conception fonctionnelle actuellement présents dans le dépôt PreCogRM.  
Chaque fichier a une responsabilité claire et non redondante.  
L’ensemble forme un socle cohérent permettant à un développeur ou à un LLM spécialisé de comprendre, concevoir et implémenter l’application dans le respect de la méthodologie EBIOS Risk Manager.

---

## 1. `DESC.md`

### Rôle
Document d’orientation du dépôt.

### Fonction
- Donner une vision d’ensemble des artefacts disponibles.
- Expliquer la fonction de chaque fichier.
- Servir de point d’entrée pour tout nouveau contributeur (humain ou LLM).

---

## 2. `creation_analyse.md`

### Rôle
Spécification fonctionnelle de l’écran n°1.

### Fonction
- Décrire l’écran de **création d’une analyse de risques**.
- Définir :
  - l’identification de l’analyse,
  - les responsabilités,
  - le cadre et le contexte de l’analyse,
  - l’existence ou non d’un DSIL.
- Poser les métadonnées initiales (statut, version, traçabilité).

➡️ **Correspond à l’initialisation d’un dossier d’analyse EBIOS RM.**

---

## 3. `configuration_application.md`

### Rôle
Spécification des éléments configurables de l’application.

### Fonction
- Définir les **référentiels transverses** utilisés dans les écrans métier.
- Inclut notamment :
  - analystes,
  - services,
  - cadres / contextes d’analyse,
  - cadres réglementaires.
- Garantir la cohérence et l’évolutivité des listes déroulantes.

➡️ **Socle administratif et organisationnel de l’application.**

---

## 4. `Atelier_1.md`

### Rôle
Document pivot de l’Atelier 1 EBIOS RM.

### Fonction
- Décrire **la logique métier complète** de l’Atelier 1, indépendamment de toute interface.
- Préciser :
  - les objectifs de l’Atelier 1,
  - les objets métiers manipulés,
  - l’enchaînement logique des étapes,
  - les frontières méthodologiques (ce qui est autorisé / interdit),
  - les conditions de complétude de l’atelier.

➡️ **Contrat méthodologique entre EBIOS RM, l’outil et l’implémentation logicielle.**

---

## 5. `ecran_valeurs_metiers.md`

### Rôle
Spécification fonctionnelle de l’écran n°2.

### Fonction
- Décrire l’écran permettant de gérer les **valeurs métiers / actifs essentiels**.
- Préciser :
  - les champs métier nécessaires,
  - la justification du caractère essentiel,
  - la granularité variable,
  - le lien avec un ou plusieurs périmètres.
- Préparer les ateliers suivants sans introduire de calcul de risque.

➡️ **Cœur métier de l’Atelier 1 : identifier ce qui a de la valeur.**

---

## 6. `regles_coherence_atelier_1.md`

### Rôle
Document normatif de contrôle méthodologique.

### Fonction
- Énoncer les **règles de cohérence non négociables** de l’Atelier 1.
- Empêcher toute dérive, notamment :
  - calcul de risque prématuré,
  - automatisation abusive,
  - confusion entre valeur, menace et scénario.
- Servir de base aux validations fonctionnelles et aux audits.

➡️ **Garde-fou méthodologique de l’application.**

---

## 7. `initial_analysis.json`

### Rôle
Modèle de données de démarrage.

### Fonction
- Fournir un exemple de **structure JSON** initiale pour une analyse.
- Servir de :
  - base de développement,
  - support de tests,
  - référence pour la migration future vers PostgreSQL.

➡️ **Support technique de persistance initiale.**

---

## 8. Cohérence d’ensemble

Pris ensemble, ces fichiers permettent :
- de comprendre la méthodologie implémentée,
- de développer l’application sans interprétation implicite,
- de confier le développement à un LLM spécialisé tout en maintenant :
  - lisibilité,
  - traçabilité,
  - conformité EBIOS RM,
  - éthique open source.

Tout ajout de fonctionnalité doit s’inscrire dans ce cadre documentaire.
