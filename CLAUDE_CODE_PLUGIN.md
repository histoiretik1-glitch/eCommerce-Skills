# Plugin Claude Code : eCommerce Skills

Ce dépôt est aussi un **marketplace de plugins Claude Code**. Il contient un seul plugin, `ecommerce-skills`, qui regroupe les **162 skills** du dépôt. Une seule installation suffit pour les avoir tous, dans tous vos projets.

## Prérequis

- Claude Code avec la commande `/plugin`. Une version récente est conseillée : `claude update`.
- Python 3 pour les skills qui contiennent des scripts (calculateurs, détecteurs, rapports). Seule la bibliothèque standard est utilisée, aucun `pip install` n'est nécessaire.
- Un accès Git au dépôt GitHub : si le dépôt est privé, votre compte doit pouvoir le cloner.

## Installation

Dans Claude Code :

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
```

```
/plugin install ecommerce-skills@ecommerce-skills
```

Puis redémarrez Claude Code (ou lancez `/reload-plugins`).

Équivalent en ligne de commande, hors session :

```bash
claude plugin marketplace add histoiretik1-glitch/eCommerce-Skills
```

```bash
claude plugin install ecommerce-skills@ecommerce-skills
```

Par défaut l'installation se fait au niveau **utilisateur** : le plugin est actif dans tous vos projets. Pour le limiter à un projet partagé avec votre équipe, ajoutez `--scope project`.

### Installer depuis un clone local

Pratique pour tester des modifications avant de les publier :

```bash
git clone https://github.com/histoiretik1-glitch/eCommerce-Skills.git ~/eCommerce-Skills
```

```bash
claude plugin marketplace add ~/eCommerce-Skills
```

```bash
claude plugin install ecommerce-skills@ecommerce-skills
```

## Vérifier l'installation

```bash
claude plugin list
```

```bash
claude plugin details ecommerce-skills@ecommerce-skills
```

`details` doit afficher `Skills (162)`. Dans une session, la commande `/skills` liste aussi les skills chargés.

## Utilisation

- **Automatique** : décrivez votre besoin en langage naturel. Claude choisit le skill dont la description correspond, par exemple « Mon IPI Amazon est tombé à 450, que faire ? » déclenche `warehouse-optimization`.
- **Manuelle** : tapez `/` suivi du nom du skill, par exemple `/ecommerce-skills:profit-margin-calculator-amazon`. Les skills d'un plugin portent le préfixe `ecommerce-skills:`.

Les skills qui contiennent des scripts les lancent avec `python3 scripts/<fichier>.py`. Claude reçoit le dossier de base du skill au moment où il le charge et exécute les scripts depuis ce dossier.

## Mises à jour

### Côté utilisateur

```bash
claude plugin marketplace update ecommerce-skills
```

```bash
claude plugin update ecommerce-skills@ecommerce-skills
```

Puis redémarrez Claude Code. Vous pouvez aussi activer la mise à jour automatique du marketplace dans `/plugin` → onglet *Marketplaces*.

### Côté mainteneur : publier une nouvelle version

1. Ajoutez ou modifiez un skill. Chaque skill est un dossier contenant un `SKILL.md` qui commence par :
   ```yaml
   ---
   name: nom-du-dossier
   description: "Ce que fait le skill. Use when the user asks for help ..."
   ---
   ```
   `name` doit être **identique au nom du dossier** (minuscules, chiffres, tirets).
2. Si le skill a des voisins fonctionnels, déclarez son rôle dans `tools/skill_groups.json`, puis lancez `python3 tools/apply_skill_groups.py` pour régénérer les sections « Role and Scope ». Ne modifiez pas ces sections à la main.
3. Si vous modifiez un script partagé (familles `profit-margin-calculator`, `supply-chain-optimization`, `brand-protection`, `product-differentiation`, `review-checker`), modifiez une copie puis recopiez-la à l'identique dans chaque dossier de la famille : un test vérifie qu'elles restent identiques. La plateforme est déduite du nom du dossier.
4. Régénérez la liste des skills du manifeste, validez et lancez les tests :
   ```bash
   python3 tools/validate_plugin.py --write
   ```
   ```bash
   claude plugin validate .
   ```
   ```bash
   python3 -m unittest discover -s tests -v
   ```
5. **Augmentez le numéro `version`** du plugin dans `.claude-plugin/marketplace.json` (par exemple `1.0.0` → `1.1.0`). Claude Code se sert de ce numéro pour détecter une mise à jour : sans changement de version, `claude plugin update` considère le plugin à jour.
6. Faites un commit et un push sur la branche par défaut (`main`).

### Validation automatique (GitHub Actions)

Le workflow `.github/workflows/validate-plugin.yml` s'exécute à chaque Pull Request, à chaque push sur `main` et sur les branches `claude/**`, et à la demande (*Actions* → *Run workflow*). Il échoue, et bloque donc la validation, si :

- le nombre de `SKILL.md` diffère de `EXPECTED_SKILL_COUNT` (162) ;
- `marketplace.json` n'est pas un JSON valide ou ne contient pas de plugin ;
- `python3 tools/validate_plugin.py` détecte une erreur : YAML invalide, `name` ou `description` manquant ou vide, `name` différent du dossier, doublon, fichier référencé introuvable, skill absent du manifeste ou chemin du manifeste sans `SKILL.md` ;
- les tests de `tests/` échouent : modèles de frais par plateforme, sorties Amazon comparées aux fichiers de référence de `tests/golden/`, exécution de tous les exemples `python3 scripts/...` documentés, copies identiques des scripts partagés ;
- `claude plugin validate .` échoue. Cette étape est ignorée, avec un avertissement, uniquement si la CLI Claude Code ne peut pas être installée sur le runner.

**Quand vous ajoutez ou retirez des skills, mettez à jour `EXPECTED_SKILL_COUNT` dans le workflow.**

Sécurité du workflow :

- **Droits minimaux** : jeton en lecture seule (`contents: read`), et `persist-credentials: false` au checkout. Aucun secret n'est utilisé.
- **Actions figées** sur un commit précis (SHA complet, version en commentaire) : `actions/checkout` v7.0.1, `actions/setup-python` v7.1.0, `actions/setup-node` v7.1.0.
- **Outils figés et vérifiés** dans `tools/ci/` :
  - PyYAML 6.0.3 s'installe avec `--require-hashes` (`requirements.txt`) ;
  - Claude Code 2.1.319 s'installe avec `npm ci` depuis `package-lock.json` (empreintes d'intégrité), puis `npm audit signatures` vérifie les signatures du registre npm. Si cette vérification échoue, la CLI n'est pas exécutée.
- **Mises à jour** : `.github/dependabot.yml` propose chaque mois les nouvelles versions des actions, de la CLI et de PyYAML. Le délai de 14 jours (`cooldown`) écarte les versions trop récentes.

Pour changer de version de Claude Code à la main : modifiez `tools/ci/package.json`, puis lancez `npm install --package-lock-only` dans `tools/ci/` et commitez les deux fichiers.

Règles de rédaction vérifiées pour chaque `SKILL.md` : description d'au plus 1 024 caractères, sans `<` ni `>`, avec une phrase « Use when… » et le nom de la plateforme dans les 80 premiers caractères pour les skills `etsy-`, `shopify-`, `tiktok-`, `walmart-`, `ebay-`, `amazon-` et `woocommerce-` ; une seule section `## Installation` ; aucun renvoi vers un skill absent du plugin (sauf ceux de la liste `EXTERNAL_OR_NON_SKILL_NAMES`).

Pour rendre ce contrôle obligatoire avant toute fusion : *Settings* → *Branches* → règle de protection sur `main` → *Require status checks to pass*, puis cochez **Skills, manifest and plugin**.

## Organisation

```
.claude-plugin/marketplace.json   ← marketplace + plugin "ecommerce-skills" (liste des 162 skills)
<skill>/SKILL.md                   ← 142 skills à la racine
<catégorie>/<skill>/SKILL.md       ← 20 skills rangés par catégorie :
    brand-protection/, product-differentiation/, profit-margin-calculator/,
    review-checker/, supply-chain-optimization/
<skill>/scripts/*.py               ← scripts Python (bibliothèque standard uniquement)
tools/validate_plugin.py           ← validation du packaging
```

Le plugin est déclaré avec `"strict": false` et `"source": "./"`. Le manifeste liste explicitement chaque dossier de skill, ce qui permet de garder l'arborescence d'origine, sous-dossiers de catégorie compris, sans rien déplacer.

## Coût en contexte

Les descriptions des 162 skills sont chargées dans chaque session (environ 16 500 tokens d'après `claude plugin details`). Le contenu complet d'un skill n'est chargé qu'au moment où il est utilisé. Si vous ne voulez pas ce coût dans un projet, désactivez le plugin :

```bash
claude plugin disable ecommerce-skills@ecommerce-skills
```

## Historique des versions

### 1.3.0 — LOT 3 (doublons et rôles)

- **Aucun skill supprimé**, toujours 162. Les doublons sont traités par des rôles distincts, des renvois entre voisins et du contenu propre à chaque skill.
- **Registre des groupes** `tools/skill_groups.json` : 24 groupes de skills voisins (Etsy, TikTok Shop, vitesse Shopify, conversion, paiement, prix, avis, stocks, canaux, e-mail, abonnements…), 88 skills avec un rôle unique. `tools/apply_skill_groups.py` en génère une section « Role and Scope » dans chaque skill concerné ; `--check` vérifie qu'elle est à jour.
- **20 skills Etsy** et **20 skills Shopify** qui n'étaient que des gabarits identiques ont maintenant une méthode propre (informations à collecter, étapes, règles de la plateforme, format de livrable). `etsy-seller-guide` devient le point d'entrée Etsy et renvoie vers les 20 skills spécialisés.
- **TikTok Shop** : `tiktok-influencer-marketing` (stratégie et choix du modèle de collaboration) est distingué de `tiktok-creator-marketplace` (campagnes payées), `tiktok-shop-affiliate-program` (programme d'affiliation) et `tiktok-shop-creator-management` (gestion du vivier de créateurs).
- **Descriptions** : 22 descriptions réécrites pour que chaque skill se distingue de ses voisins (ressemblance inférieure à 50 % au sein d'un groupe).
- **Tests** (`tests/test_duplicates.py`) : registre cohérent, aucun nouveau gabarit, aucun doublon de contenu, descriptions distinctes, aucune ligne de contenu perdue depuis la 1.2.0, et sélection du bon skill face à ses voisins (50 demandes types).

### 1.2.0 — LOT 2 (installation et descriptions)

- **Installation** : chaque `SKILL.md` a une section `## Installation` unique, avec l'installation du plugin Claude Code et la commande Skills CLI de ce skill (`npx skills add histoiretik1-glitch/eCommerce-Skills --skill <nom> -g`). Les anciennes commandes (`clawhub install`, `npx skills add nexscope/<skill>`, dépôt d'origine) ont disparu.
- **Renvois entre skills** : les 12 blocs d'installation qui renvoyaient vers un autre skill du plugin sont remplacés par « Use the `<skill>` skill ». Les 4 renvois vers le dépôt externe Amazon-Skills sont signalés comme externes. Les 3 skills « coming soon » inexistants sont remplacés par les skills existants.
- **Descriptions** : les 162 descriptions disent ce que fait le skill, contiennent une phrase « Use when… » et, pour un skill propre à une plateforme, nomment la plateforme dès le début. 64 ont été complétées ou réécrites. Les skills qui se recouvrent indiquent vers quel skill voisin se tourner.
- **Validateur** : `tools/validate_plugin.py` vérifie aussi ces règles (description d'au plus 1 024 caractères sans chevrons, phrase « Use when », plateforme nommée, section d'installation unique et correcte, aucune commande héritée, aucun renvoi vers un skill inexistant).
- **Tests** : tests du validateur (un défaut injecté par catégorie) et test de déclenchement (44 demandes types doivent faire ressortir le bon skill parmi les 3 premiers).
- Testé avec le Skills CLI : les 162 skills sont détectés, et un skill rangé en sous-dossier s'installe avec ses scripts.

### 1.1.0 — LOT 1 (scripts multi-plateformes, TikTok Shop)

- Calculateurs de marge : un modèle de frais par plateforme. Amazon : commission par catégorie et FBA (inchangé). Shopify : frais Shopify Payments selon le plan, frais de passerelle tierce, aucune commission. TikTok Shop : commission par catégorie et commission des créateurs. Walmart : commission par catégorie avec paliers de prix et WFS. Les anciens noms de paramètres (`fba_fee`, `wfs_fee`, `creator_commission_rate`…) sont acceptés, et un paramètre inconnu produit une erreur explicite.
- Chaîne logistique : plateforme détectée selon le dossier, délai de paiement, libellés et conseils sur les stocks anciens propres à chaque plateforme, frais de commission et de créateurs optionnels.
- Protection de marque : canaux de signalement propres à chaque plateforme (eBay VeRO, Shopify et DMCA, IP Protection Center de TikTok Shop, Walmart Brand Portal). Les sous-commandes documentées fonctionnent désormais.
- Vérification des avis : identifiant du produit selon la plateforme, alias `wfs_verified` reconnu, et une erreur au lieu d'un retour silencieux aux données de démonstration.
- Frais TikTok Shop harmonisés (environ 6 à 8 % aux États-Unis, 5 % pour la bijouterie, à confirmer dans Seller Center) dans tous les skills.
- 13 skills TikTok Shop réécrits avec une méthode complète : compliance, conversion, creator-management, customer-service, fulfillment, inventory, pricing, product-research, promotions, returns, reviews, shipping, trending-products.
- Descriptions améliorées pour un meilleur déclenchement automatique.
- Tests automatisés dans `tests/`, exécutés par la CI.

Les sorties Amazon des scripts sont identiques à celles de la version 1.0.0, ce que vérifient les fichiers de référence de `tests/golden/`.

## Désinstallation

```bash
claude plugin uninstall ecommerce-skills@ecommerce-skills
```

```bash
claude plugin marketplace remove ecommerce-skills
```

## Dépannage

| Problème | Solution |
|---|---|
| `Skills (0)` ou skill introuvable | `python3 tools/validate_plugin.py` puis `claude plugin validate .` ; redémarrez Claude Code. |
| Mise à jour non détectée | Vérifiez que `version` a été augmentée dans `marketplace.json`, puis `claude plugin marketplace update ecommerce-skills`. |
| Échec du clonage du marketplace | Dépôt privé : vérifiez que `git clone https://github.com/histoiretik1-glitch/eCommerce-Skills.git` fonctionne avec vos identifiants. |
| Doublon avec un skill déjà installé (par exemple `ecommerce-growth-strategy` dans `~/.claude/skills/`) | Supprimez la copie isolée : la version du plugin, préfixée `ecommerce-skills:`, la remplace. |
