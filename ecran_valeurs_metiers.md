# Écran n°2 – Valeurs métiers / Actifs essentiels

Ce document décrit les exigences fonctionnelles de l’écran permettant de gérer les valeurs métiers (actifs essentiels) dans le cadre de l’Atelier 1 EBIOS RM.  
Cet écran vise à identifier ce qui doit être protégé, indépendamment des menaces ou scénarios.  
Il constitue un socle méthodologique fondamental pour les ateliers suivants.

---

## 1. Objectif de l’écran

L’écran “Valeurs métiers / Actifs essentiels” permet à l’analyste de :

- identifier les valeurs métiers essentielles,
- expliciter pourquoi elles sont essentielles,
- rattacher une valeur à un ou plusieurs périmètres,
- structurer des analyses contenant un grand nombre de valeurs,
- préparer les ateliers suivants sans introduire de calcul de risque.

---

## 2. Principe méthodologique

Une valeur métier représente **ce qui a de la valeur pour l’organisation**.  
Elle n’est :
- ni un équipement,
- ni une menace,
- ni un scénario,
- ni un risque.

Aucune cotation chiffrée de risque n’est autorisée à ce stade.

---

## 3. Champs fonctionnels – Valeur métier

### 3.1 Identification

- **Nom de la valeur métier**
  - Champ : `business_value_name`
  - Type : chaîne de caractères
  - Obligatoire
  - Doit être compréhensible par un décideur métier

- **Nature de la valeur métier**
  - Champ : `business_value_nature`
  - Type : liste déroulante configurable
  - Obligatoire
  - Exemples : Mission, Processus métier, Donnée critique, Service rendu, Image, Obligation réglementaire

- **Description**
  - Champ : `business_value_description`
  - Type : texte libre
  - Optionnel

---

### 3.2 Caractère essentiel (obligatoire)

- **Justification du caractère essentiel**
  - Champ : `essentiality_justification`
  - Type : texte libre
  - Obligatoire
  - Répond à la question :  
    “Pourquoi cette valeur est-elle essentielle pour l’organisation ?”

Ce champ est indispensable pour la conformité EBIOS RM.

---

### 3.3 Structuration et granularité

- **Niveau de granularité**
  - Champ : `granularity_level`
  - Type : enum (macro / intermédiaire / fin)
  - Optionnel
  - Aucune incidence de calcul

- **Catégorie métier**
  - Champ : `business_value_category`
  - Type : enum configurable
  - Optionnel
  - Utilisé ultérieurement pour l’automatisation assistée

---

### 3.4 Responsabilité et contexte

- **Propriétaire métier**
  - Champ : `business_owner`
  - Type : texte ou référence utilisateur
  - Optionnel

- **Notes de contexte**
  - Champ : `context_notes`
  - Type : texte libre
  - Optionnel

---

### 3.5 Enjeux et impacts (qualitatif uniquement)

- **Enjeux de sécurité concernés**
  - Champ : `security_stakes`
  - Type : liste multiple (Confidentialité, Intégrité, Disponibilité, etc.)
  - Aucun calcul associé

- **Impacts métier pressentis**
  - Champ : `business_impacts`
  - Type : texte libre
  - Optionnel

---

## 4. Association aux périmètres

### 4.1 Principe

- Une valeur métier peut être associée à **plusieurs périmètres**.
- L’association n’est pas exclusive.
- Le lien valeur ↔ périmètre porte du sens métier.

---

### 4.2 Fonctionnalités attendues

- sélection d’un ou plusieurs périmètres existants,
- ajout d’un commentaire optionnel par périmètre,
- modification possible sans perte d’historique.

---

## 5. Traçabilité

Pour chaque valeur métier :
- date de création,
- auteur,
- date de modification,
- statut actif / inactif.

Aucune suppression définitive n’est autorisée.

---

## 6. Prompt de génération de code (pour LLM)

> Tu es un développeur expérimenté chargé de coder l’écran “Valeurs métiers / Actifs essentiels”.  
> Implémente exactement les champs et règles décrits dans ce document.  
> Le code doit :
> - utiliser les noms de champs tels que définis,
> - être abondamment commenté (logique métier, justification EBIOS),
> - empêcher toute cotation de risque à ce stade,
> - séparer clairement interface, règles de gestion et données.
``
