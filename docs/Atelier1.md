Atelier 1 : Cadrage et périmètre

1. Objet du document
Ce document décrit les exigences fonctionnelles et métier associées à l’Atelier 1 de la méthode EBIOS Risk Manager au sein de l’outil PreCogRM.
Il constitue :

la base de conception fonctionnelle de l’outil,
un référentiel de conformité méthodologique,
un support de dialogue entre experts cyber et développeurs.


2. Rappel méthodologique (non discutable)
L’Atelier 1 EBIOS RM a pour objectifs :

définir le périmètre de l’analyse de risques,
identifier les actifs essentiels,
identifier les biens supports,
caractériser les enjeux de sécurité et leurs impacts métier,
poser un cadre partagé et traçable.

👉 Aucune cotation de risque n’est réalisée à ce stade.

3. Acteurs concernés
Utilisateur cible

Expert cybersécurité
Analyste risques
Chef de projet sécurité

Rôles attendus (niveau Atelier 1)

Contributeur : saisie / modification
Lecteur : consultation


4. Périmètre fonctionnel de l’Atelier 1
Inclus

Gestion du contexte d’analyse
Définition du périmètre
Identification des actifs et biens supports
Qualification des enjeux et impacts
Justification textuelle

Exclu (volontairement)

Sources de risque
Scénarios
Cotation de vraisemblance
Calcul de niveaux de risque


5. Objets métier à gérer
5.1 Contexte d’analyse
Le système doit permettre de définir :

le contexte organisationnel
le contexte métier
le contexte réglementaire (optionnel au MVP)
les hypothèses de départ

Exigences :

champ texte structuré
historique des modifications
justification obligatoire


5.2 Périmètre de l’analyse
Fonctionnalités attendues :

description textuelle du périmètre
exclusion explicite de zones hors périmètre
lien explicite avec les actifs listés

Objectif :

éviter toute ambiguïté lors des ateliers suivants ou en audit.


5.3 Actifs essentiels
Définition :

Actif dont l’indisponibilité, l’altération ou la compromission a un impact significatif sur les missions de l’organisation.

Fonctionnalités :

création / modification / suppression
description métier
rattachement au périmètre
justification du caractère « essentiel »

Contraintes :

vocabulaire métier prioritaire
pas de langage technique imposé


5.4 Biens supports
Définition :

Élément technique, humain ou organisationnel supportant un ou plusieurs actifs essentiels.

Fonctionnalités :

rattachement à un ou plusieurs actifs essentiels
typologie (SI, humain, organisationnel, physique…)
description fonctionnelle

Prévision (non activée à ce stade) :

lien futur avec des indices de maturité cyber
lien futur avec des scénarios par défaut


5.5 Enjeux de sécurité
Le système doit permettre de caractériser :

les enjeux de confidentialité
les enjeux d’intégrité
les enjeux de disponibilité
tout autre enjeu métier spécifique

Fonctionnalités :

association enjeux ↔ actifs essentiels
justification textuelle obligatoire
absence de cotation chiffrée à ce stade


5.6 Impacts métier
Objectif :

qualifier les conséquences potentielles sans encore parler de risque.

Fonctionnalités :

description des impacts :

métier
financier
juridique
image / réputation


possibilité d’utiliser une échelle qualitative (faible / significatif / critique), configurable


6. Exigences de traçabilité
Pour chaque élément de l’Atelier 1, le système doit :

conserver l’auteur de la modification,
conserver la date,
conserver les versions successives,
permettre une consultation en audit.


7. Exigences d’ergonomie

navigation guidée par étapes (Atelier 1)
champs obligatoires clairement identifiés
aide contextuelle rappelant la logique EBIOS RM
absence de surcharge fonctionnelle


8. Exigences techniques (au niveau Atelier 1)

données stockées dans une structure lisible (JSON au départ)
séparation claire :

données métier
règles de gestion


facilité de migration vers une base relationnelle
documentation intégrée (README / commentaires métier)


9. Critères de complétude de l’Atelier 1
L’Atelier 1 est considéré comme complet lorsque :

le périmètre est clairement défini,
les actifs essentiels sont identifiés et justifiés,
les biens supports sont reliés aux actifs,
les enjeux et impacts sont décrits,
l’ensemble est compréhensible sans connaissance implicite.



