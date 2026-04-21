# Configuration de l’application PreCogRM

Ce document décrit les éléments configurables de l’application PreCogRM.  
La configuration fournit les référentiels utilisés dans les écrans fonctionnels, sans modifier rétroactivement les analyses existantes.  
Ces données sont administratives, transverses et auditables.

---

## 1. Objectifs de la configuration

La section configuration permet :

- d’alimenter les listes déroulantes utilisées dans l’application,
- d’assurer la cohérence des saisies,
- de garantir la traçabilité des choix organisationnels,
- de préparer l’automatisation future sans rigidifier la méthode.

---

## 2. Référentiel des analystes

### Champs attendus

- `analyst_id` : UUID (clé technique)
- `last_name` : string
- `first_name` : string
- `service_name` : string
- `is_active` : boolean

### Règles
- Un analyste ne peut pas être supprimé, uniquement désactivé.
- Les analyses existantes restent liées aux analystes désactivés.

---

## 3. Référentiel des services

### Champs attendus

- `service_id` : UUID
- `service_name` : string
- `service_description` : text
- `is_active` : boolean

---

## 4. Référentiel des cadres / contextes d’analyse

Ce référentiel permet de définir les **types de cadre d’analyse** proposés lors de la création d’une analyse de risques.

### Champs attendus

- **Identifiant**
  - `analysis_context_type_id` : UUID

- **Libellé**
  - `analysis_context_label` : string
  - Exemple : "Nouvelle analyse de risques"

- **Description**
  - `analysis_context_description` : text
  - Permet de préciser le cas d’usage

- **Code fonctionnel**
  - `analysis_context_code` : string
  - Exemple : `new_analysis`, `accreditation_renewal`
  - Utilisé pour la logique applicative

- **Statut**
  - `is_active` : boolean

---

## 5. Référentiel des cadres réglementaires

### Champs attendus

- `framework_id` : UUID
- `framework_name` : string
- `framework_type` : enum (loi, norme, directive, référentiel)
- `framework_description` : text
- `is_active` : boolean

---

## 6. Règles de gestion générales

- Aucun élément de configuration ne doit être supprimé physiquement.
- Toute modification est historisée.
- Les changements de configuration :
  - n’impactent pas les analyses existantes,
  - s’appliquent uniquement aux nouvelles saisies.
- Les référentiels doivent rester compréhensibles par un non-technicien.

---

## 7. Prompt de génération de code (pour LLM)

> Tu es un développeur chargé d’implémenter la configuration de PreCogRM.  
> Implémente les référentiels décrits ci-dessus avec un stockage persistant.  
> Le code doit :
> - être fortement commenté (règles métier et usages),
> - empêcher toute suppression destructive,
> - permettre l’activation / désactivation des valeurs,
> - rester compatible avec une migration vers PostgreSQL.
