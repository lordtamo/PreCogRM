# Écran n°1 – Création d’une analyse de risques

Ce document décrit les exigences fonctionnelles de l’écran de création d’une nouvelle analyse de risques dans PreCogRM.  
Cet écran constitue le point d’entrée de toute analyse EBIOS Risk Manager et permet de définir le cadre, le contexte et les responsabilités.  
Aucune donnée relevant des ateliers EBIOS RM n’est saisie à ce stade.

---

## 1. Objectif de l’écran

L’écran de création d’une analyse permet de :

- identifier l’analyse de risques,
- préciser le bénéficiaire et les responsables,
- définir le cadre et le contexte dans lequel l’analyse est menée,
- initialiser les métadonnées nécessaires au suivi et à l’audit.

---

## 2. Champs fonctionnels attendus

### 2.1 Identification générale

- **Nom de l’analyse**
  - Champ technique : `analysis_name`
  - Type : chaîne de caractères
  - Obligatoire

- **Nom du bénéficiaire / client**
  - Champ technique : `beneficiary_name`
  - Type : chaîne de caractères
  - Obligatoire

---

### 2.2 Organisation et responsabilités

- **Service réalisant l’analyse**
  - Champ technique : `analysis_service`
  - Type : enum
  - Mode de saisie : liste déroulante
  - Liste issue de la configuration de l’application
  - Obligatoire

- **Analyste responsable**
  - Champ technique : `analyst_id`
  - Type : UUID
  - Mode de saisie : liste déroulante
  - Liste issue de la configuration de l’application
  - Obligatoire

---

### 2.3 Cadre et contexte de l’analyse

- **Date de démarrage**
  - Champ technique : `start_date`
  - Type : date
  - Valeur par défaut : date du jour
  - Obligatoire

- **Existence d’un DSIL**
  - Champ technique : `dsil_exists`
  - Type : booléen
  - Mode de saisie : case à cocher
  - Valeur par défaut : false
  - Obligatoire (choix explicite requis)

- **Cadre de l’analyse**
  - Champ technique : `analysis_context_type_id`
  - Type : UUID
  - Mode de saisie : liste déroulante
  - Liste issue du référentiel configuré dans l’application
  - Obligatoire

> Le cadre de l’analyse caractérise le contexte dans lequel l’analyse est menée  
> (ex. nouvelle analyse, renouvellement d’homologation, analyse préventive, etc.).

---

## 3. Règles de gestion

- Tous les champs obligatoires doivent être renseignés pour créer l’analyse.
- Une analyse nouvellement créée est positionnée au statut `draft`.
- Le cadre de l’analyse :
  - est purement déclaratif à ce stade,
  - n’entraîne aucun calcul,
  - peut être modifié tant que l’analyse est en statut `draft`.
- L’indication de l’existence d’un DSIL n’a aucune incidence automatique sur les ateliers.

---

## 4. Traçabilité

Les informations suivantes doivent être enregistrées automatiquement :

- identifiant unique de l’analyse (`analysis_id`),
- date de création,
- auteur de la création,
- version initiale de l’analyse (`v1.0`).

Aucune suppression définitive d’analyse n’est autorisée.

---

## 5. Prompt de génération de code (pour LLM)

> Tu es un développeur chargé de coder l’écran de création d’une analyse de risques.  
> Implémente strictement les champs et règles décrits dans ce document.  
> Le code doit :
> - utiliser exactement les noms de champs définis,
> - récupérer les listes déroulantes depuis la configuration applicative,
> - être abondamment commenté (logique métier, conformité EBIOS RM),
> - séparer clairement interface utilisateur, validation et persistance.
``
