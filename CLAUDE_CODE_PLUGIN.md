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
2. Régénérez la liste des skills du manifeste et validez :
   ```bash
   python3 tools/validate_plugin.py --write
   ```
   ```bash
   claude plugin validate .
   ```
3. **Augmentez le numéro `version`** du plugin dans `.claude-plugin/marketplace.json` (par exemple `1.0.0` → `1.1.0`). Claude Code se sert de ce numéro pour détecter une mise à jour : sans changement de version, `claude plugin update` considère le plugin à jour.
4. Faites un commit et un push sur la branche par défaut (`main`).

### Validation automatique (GitHub Actions)

Le workflow `.github/workflows/validate-plugin.yml` s'exécute à chaque Pull Request, à chaque push sur `main` et sur les branches `claude/**`, et à la demande (*Actions* → *Run workflow*). Il échoue, et bloque donc la validation, si :

- le nombre de `SKILL.md` diffère de `EXPECTED_SKILL_COUNT` (162) ;
- `marketplace.json` n'est pas un JSON valide ou ne contient pas de plugin ;
- `python3 tools/validate_plugin.py` détecte une erreur : YAML invalide, `name` ou `description` manquant ou vide, `name` différent du dossier, doublon, fichier référencé introuvable, skill absent du manifeste ou chemin du manifeste sans `SKILL.md` ;
- `claude plugin validate .` échoue. Cette étape est ignorée, avec un avertissement, uniquement si la CLI Claude Code ne peut pas être installée sur le runner.

**Quand vous ajoutez ou retirez des skills, mettez à jour `EXPECTED_SKILL_COUNT` dans le workflow.**

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
