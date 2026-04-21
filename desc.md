1️⃣ creation_analyse.md
Fonction

Spécifie l’écran n°1 de l’application.
Point d’entrée de toute analyse de risques EBIOS RM.
Décrit :

l’identification de l’analyse,
les responsabilités,
le cadre et le contexte de l’analyse,
les règles de gestion associées.


Sert de référence pour :

la cohérence méthodologique,
la traçabilité,
l’audit.



👉 Rôle dans l’application :
Initialisation d’un dossier d’analyse EBIOS RM (statut draft).

2️⃣ configuration_application.md
Fonction

Définit tous les référentiels configurables de l’application.
Alimente les listes déroulantes utilisées dans les écrans métier.
Couvre notamment :

analystes,
services,
cadres / contextes d’analyse,
cadres réglementaires.



👉 Rôle dans l’application :
Socle transverse garantissant cohérence, évolutivité et indépendance organisationnelle.

3️⃣ ecran_valeurs_metiers.md
Fonction

Spécifie l’écran n°2 : Valeurs métiers / Actifs essentiels (Atelier 1).
Décrit :

les champs métier nécessaires,
la granularité variable,
la justification de l’essentialité,
le lien avec un ou plusieurs périmètres.


Pose les bases pour les ateliers suivants sans calcul de risque.

👉 Rôle dans l’application :
Identifier ce qui a de la valeur et doit être protégé.

4️⃣ regles_coherence_atelier_1.md
Fonction

Document normatif listant les règles méthodologiques non négociables de l’Atelier 1.
Sert de :

garde-fou fonctionnel,
base de validation,
référence en audit.



👉 Rôle dans l’application :
Empêcher toute dérive (calculs prématurés, automatisme abusif, confusion menace/valeur).

5️⃣ initial_analysis.json
Fonction

Exemple de structure de données initiale pour une analyse.
Sert de :

données de démarrage,
test de cohérence,
base de migration future vers PostgreSQL.



👉 Rôle dans l’application :
Modèle de persistance minimal au lancement.
