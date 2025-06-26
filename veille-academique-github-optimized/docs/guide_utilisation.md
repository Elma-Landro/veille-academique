# 📖 Guide d'Utilisation - Système de Veille Académique
*Guide détaillé pour débutants complets*

## 🎯 Introduction

Ce guide vous accompagne **étape par étape** pour utiliser votre système de veille académique. Chaque instruction est détaillée et expliquée pour que vous puissiez utiliser l'outil même sans expérience technique.

## 🚀 Première Utilisation

### Étape 1 : Accéder à l'Interface

1. **Ouvrez votre navigateur web** (Chrome, Firefox, Safari, Edge)
2. **Tapez l'adresse** : `http://localhost:5173`
3. **Appuyez sur Entrée**

**Que se passe-t-il ?** Votre navigateur se connecte au serveur local qui fait tourner l'interface de votre système de veille.

### Étape 2 : Découvrir l'Interface

Vous arrivez sur une page avec :

#### 🏠 En-tête (partie haute)
- **Logo bleu-violet** avec icône de recherche
- **Titre** : "Veille Académique - STS & Cryptomonnaies"
- **Boutons verts** : "Alertes" et "Configuration"

#### 📊 Tableau de Bord (4 cartes colorées)
- **Carte bleue** : "Total Scrapé" - nombre total d'offres trouvées
- **Carte verte** : "Pertinentes" - offres qui correspondent à vos critères
- **Carte violette** : "Sources" - nombre de sites web surveillés
- **Carte grise** : "Dernière MAJ" - quand le système a cherché pour la dernière fois

#### 🔍 Barre de Recherche
- **Champ de texte** avec texte grisé : "Rechercher par titre, institution ou mots-clés..."
- **Bouton violet** : "Lancer Scraping" (pour chercher de nouvelles offres)
- **Bouton bleu** : "Exporter" (pour télécharger les résultats)

#### 📑 Onglets (3 sections)
- **"Offres"** : Liste des postes trouvés
- **"Sources"** : Sites web surveillés
- **"Configuration"** : Paramètres du système

## 🔍 Utiliser la Recherche

### Rechercher dans les Offres Existantes

1. **Cliquez** dans la barre de recherche (le curseur clignote)
2. **Tapez** un mot-clé, par exemple : "crypto"
3. **Regardez** : la liste se filtre automatiquement en temps réel

**Exemples de recherches utiles :**
- `crypto` → trouve toutes les offres mentionnant les cryptomonnaies
- `blockchain` → offres sur la blockchain
- `gouvernance` → postes en gouvernance algorithmique
- `Sciences Po` → offres à Sciences Po
- `Paris` → postes à Paris

**Astuce :** Vous n'avez pas besoin d'appuyer sur Entrée, le filtrage est instantané !

### Comprendre les Résultats

Chaque offre apparaît dans une **carte blanche** avec :

#### 📋 Informations Principales
- **Titre en gros** : nom du poste
- **Institution** : université ou laboratoire
- **Localisation** : ville et pays
- **Date limite** : quand candidater avant

#### 🏷️ Badges Colorés
- **Mots-clés trouvés** : termes qui correspondent à votre recherche
- Plus il y en a, plus l'offre est pertinente

#### ⭐ Score de Pertinence (coin droit)
- **Étoile jaune** + chiffre (ex: 0.85)
- **Point coloré** :
  - 🟢 Vert : très pertinent (score ≥ 0.8)
  - 🟡 Jaune : pertinent (score 0.6-0.8)
  - 🟠 Orange : peu pertinent (score < 0.6)

#### 📊 Détails Supplémentaires
- **Source** : site web où l'offre a été trouvée
- **Enseignement** : si le poste inclut des cours
- **Langue** : langue de travail attendue
- **Trouvé le** : quand le système a découvert cette offre

#### 🔗 Bouton "Voir l'offre"
- **Cliquez** pour ouvrir l'annonce complète sur le site original
- S'ouvre dans un nouvel onglet pour ne pas perdre votre place

## 🔄 Lancer une Nouvelle Recherche

### Quand Utiliser le Scraping

**Lancez une nouvelle recherche quand :**
- Vous n'avez pas utilisé le système depuis plusieurs jours
- Vous voulez les toutes dernières offres
- Le tableau de bord indique une ancienne "Dernière MAJ"

### Comment Lancer le Scraping

1. **Cliquez** sur le bouton violet "Lancer Scraping"
2. **Observez** : le bouton change pour "Scraping..." avec une animation qui tourne
3. **Attendez** : le processus prend 2-5 minutes
4. **Résultat** : nouvelles offres apparaissent, statistiques mises à jour

**Que fait le système pendant ce temps ?**
- Visite automatiquement 40+ sites web académiques
- Cherche les nouvelles offres d'emploi
- Filtre selon vos mots-clés spécialisés
- Calcule les scores de pertinence
- Met à jour votre base de données

## 📑 Explorer les Onglets

### Onglet "Sources"

**Cliquez** sur "Sources" pour voir :
- **Liste des 8 plateformes principales** surveillées
- **Badge vert "Actif"** : le site est surveillé
- **Exemples** : Galaxie/Antares, Academic Positions EU, Euraxess...

**Utilité :** Comprendre d'où viennent vos résultats

### Onglet "Configuration"

**Cliquez** sur "Configuration" pour voir :

#### 🏷️ Mots-clés Surveillés
- **Badges gris** : crypto, blockchain, gouvernance, STS, économie politique
- Ces termes sont recherchés dans toutes les offres

#### ⏰ Fréquence de Scraping
- **"Quotidien à 9h00"** : le système cherche automatiquement chaque matin
- Vous pouvez aussi lancer manuellement quand vous voulez

#### 📧 Alertes Email
- **"Activées pour les offres avec score > 0.7"**
- Vous recevrez un email pour les offres très pertinentes

## 💾 Exporter les Résultats

### Pourquoi Exporter ?

- **Sauvegarder** vos résultats
- **Partager** avec des collègues
- **Analyser** dans Excel ou Google Sheets
- **Archiver** pour référence future

### Comment Exporter

1. **Cliquez** sur le bouton bleu "Exporter"
2. **Choisissez** le format :
   - **JSON** : pour les développeurs
   - **CSV** : pour Excel/Google Sheets
   - **Excel** : fichier .xlsx direct

3. **Téléchargez** : le fichier arrive dans votre dossier Téléchargements

## 🔍 Conseils d'Utilisation Avancée

### Optimiser vos Recherches

#### Recherches Spécifiques
- `"maître de conférences"` → postes MCF uniquement
- `postdoc` → postes post-doctoraux
- `Sciences Po` → offres à Sciences Po spécifiquement

#### Recherches Larges
- `digital` → tout ce qui touche au numérique
- `governance` → gouvernance sous toutes ses formes
- `technology` → études technologiques

### Interpréter les Scores

#### Score 0.85+ (🟢)
- **Très pertinent** : correspond exactement à votre profil
- **Action** : candidater en priorité
- **Exemple** : "Maître de Conférences en Sociologie des Cryptomonnaies"

#### Score 0.60-0.84 (🟡)
- **Pertinent** : intéressant mais moins spécialisé
- **Action** : examiner attentivement
- **Exemple** : "Assistant Professor in Digital Political Economy"

#### Score < 0.60 (🟠)
- **Peu pertinent** : éloigné de votre spécialité
- **Action** : regarder si vous avez le temps
- **Exemple** : "Lecturer in General Sociology"

### Gérer les Résultats

#### Trop de Résultats ?
- **Utilisez la recherche** pour filtrer
- **Concentrez-vous** sur les scores élevés
- **Exportez** pour trier dans Excel

#### Pas assez de Résultats ?
- **Lancez un nouveau scraping** (peut-être de nouvelles offres)
- **Élargissez** vos termes de recherche
- **Vérifiez** la date de dernière mise à jour

## 🆘 Résolution de Problèmes

### L'Interface ne se Charge Pas

**Problème :** Page blanche ou erreur de connexion

**Solutions :**
1. **Vérifiez l'adresse** : doit être exactement `http://localhost:5173`
2. **Actualisez** la page (F5 ou Ctrl+R)
3. **Redémarrez** votre navigateur
4. **Contactez** le support technique

### Le Scraping ne Fonctionne Pas

**Problème :** Bouton reste sur "Scraping..." indéfiniment

**Solutions :**
1. **Attendez** 5-10 minutes (certains sites sont lents)
2. **Actualisez** la page
3. **Relancez** le scraping
4. **Vérifiez** votre connexion internet

### Aucun Résultat Trouvé

**Problème :** "Aucune offre trouvée" après scraping

**Causes possibles :**
- **Sites temporairement indisponibles**
- **Pas de nouvelles offres** correspondant aux critères
- **Problème technique** temporaire

**Solutions :**
1. **Réessayez** dans quelques heures
2. **Élargissez** vos critères de recherche
3. **Vérifiez** les sources dans l'onglet "Sources"

## 📞 Support et Assistance

### Contacts Utiles
- **Documentation technique** : voir fichier `documentation_complete.md`
- **Rapport de tests** : voir fichier `rapport_tests.md`
- **Code source** : dossiers `veille_academique/` et `veille-academique-*/`

### Informations Système
- **Version** : 1.0.0
- **Dernière mise à jour** : Juin 2025
- **Compatibilité** : Tous navigateurs modernes

---

**🎉 Félicitations !** Vous maîtrisez maintenant votre système de veille académique. Utilisez-le régulièrement pour ne manquer aucune opportunité dans votre domaine de spécialisation !

