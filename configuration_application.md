# Configuration de l’application PreCogRM

Ce document définit les écrans et données nécessaires à la configuration fonctionnelle de PreCogRM.  
La configuration permet d’alimenter les listes de sélection utilisées dans les analyses de risques.  
Ces données sont administratives et transverses à toutes les analyses.

---

## 1. Objectifs de la configuration

La section configuration permet :
- de maintenir les référentiels nécessaires au fonctionnement de l’outil,
- d’assurer la cohérence des données saisies,
- de garantir la traçabilité et l’auditabilité.

---

## 2. Référentiel des analystes

### Champs attendus

- **Identifiant analyste**
  - `analyst_id` : UUID (clé technique)

- **Nom**
  - `last_name` : string

- **Prénom**
  - `first_name` : string

- **Service**
  - `service_name` : string

- **Statut**
  - `is_active` : boolean
  - Un analyste inactif ne peut plus être sélectionné mais reste référencé

---

## 3. Référentiel des services

### Champs attendus

- `service_id` : UUID
- `service_name` : string
- `service_description` : text
- `is_active` : boolean

---

## 4. Référentiel des cadres réglementaires

### Champs attendus

- **Identifiant**
  - `framework_id` : UUID

- **Nom de la réglementation**
  - `framework_name` : string

- **Type**
  - `framework_type` : enum (loi, norme, directive, référentiel)

- **Description**
  - `framework_description` : text

- **Statut**
  - `is_active` : boolean

---

## 5. Règles de gestion générales

- Les éléments de configuration ne doivent jamais être supprimés, uniquement désactivés.
- Les modifications doivent être historisées.
- Les changements de configuration n’impactent pas rétroactivement les analyses existantes.

---

## 6. Prompt de génération de code (pour LLM)

> Tu es un développeur chargé de coder la partie configuration d’une application web.  
> Implémente les écrans et modèles de données décrits ci‑dessus.  
> Le code doit :
> - être fortement commenté (logique métier, règles de gestion),
> - prévoir l’extensibilité des référentiels,
> - éviter toute suppression destructrice des données,
> - rester compatible avec une future base PostgreSQL.
