# Écran de création d’une analyse de risques

Ce document décrit les exigences fonctionnelles et les champs attendus pour l’écran de création d’une nouvelle analyse de risques dans PreCogRM.  
Il constitue la première étape obligatoire avant l’entrée dans les ateliers EBIOS RM.  
L’objectif est de garantir une identification claire, traçable et auditabile de chaque analyse.

---

## 1. Finalité de l’écran

L’écran de création d’analyse permet de :
- créer une nouvelle analyse de risques EBIOS RM,
- identifier le bénéficiaire, le contexte et les responsables,
- initialiser les métadonnées nécessaires au suivi de l’analyse.

Aucune donnée de fond liée aux ateliers n’est saisie à ce stade.

---

## 2. Champs fonctionnels attendus

### 2.1 Informations générales

- **Nom de l’analyse**
  - Champ technique : `analysis_name`
  - Type : chaîne de caractères
  - Obligatoire

- **Nom du bénéficiaire / client**
  - Champ technique : `beneficiary_name`
  - Type : chaîne de caractères
  - Obligatoire

- **Service réalisant l’analyse**
  - Champ technique : `analysis_service`
  - Type : valeur issue d’un référentiel
  - Sélection via liste déroulante

- **Analyste responsable**
  - Champ technique : `analyst_id`
  - Type : identifiant unique (UUID)
  - Sélection via liste déroulante
  - La liste est alimentée depuis la configuration de l’application

- **Date de démarrage**
  - Champ technique : `start_date`
  - Type : date
  - Valeur par défaut : date du jour

---

## 3. Règles de gestion

- Tous les champs obligatoires doivent être renseignés avant validation.
- Une analyse créée ne peut pas être supprimée, uniquement archivée.
- Chaque création génère un identifiant unique d’analyse (`analysis_id`).
- Le statut initial de l’analyse est positionné à `draft`.

---

## 4. Exigences de traçabilité

Les informations suivantes doivent être enregistrées automatiquement :
- date de création,
- identifiant de l’utilisateur créateur,
- version initiale de l’analyse.

---

## 5. Prompt de génération de code (pour LLM)

> Tu es un développeur logiciel expérimenté.  
> Code un écran de création d’analyse conforme à ce document.  
> Le code doit :
> - utiliser des noms de champs strictement identiques,
> - inclure des commentaires expliquant chaque champ et règle métier,
> - séparer clairement logique métier et interface utilisateur,
> - être lisible par un humain non développeur.
``
