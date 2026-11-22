# Rapport d'audit final — bibliothèque `ecommerce-skills` (version 1.5.0)

Date : 22 novembre 2026 · Périmètre : les 162 skills, le manifeste, les 48 scripts, l'installation et le déclenchement réel dans Claude Code.

## Synthèse

| Indicateur | Résultat |
|---|---|
| Skills présents | **162** (aucun supprimé) |
| Skills validés (critères complets) | **118** |
| Skills à améliorer | **44** (listes de sujets sans méthode en étapes, suivies par un test) |
| Tests automatisés | **75 sur 75** réussis (12 fichiers) |
| Exemples de commandes documentés exécutés | **61 commandes** dans 28 skills, toutes réussies |
| Déclenchement réel (`claude plugin eval`, 52 demandes) | **39 sur 52** (75 %) ; **0 mauvais skill choisi** ; 13 cas sans skill appelé |
| Installation, mise à jour, désinstallation | Réussies, avec et sans authentification (vérifiées aussi en CI) |
| Coût permanent en contexte | **≈ 23 500 tokens par session** (estimation de Claude Code), contre ≈ 24 400 avant ce lot |

Un skill est « validé » quand il remplit tous ces critères :
- un en-tête valide ;
- au moins 8 lignes de contenu propre, c'est-à-dire absentes de 5 autres skills ou plus ;
- une méthode : au moins 5 étapes, ou plus de 800 mots structurés ;
- un format de livrable ;
- des exemples d'utilisation ;
- le cas échéant, des scripts qui n'utilisent que la bibliothèque standard Python.

L'outil `tools/audit_library.py` applique ces critères et peut être relancé à tout moment.

## 1. Fichiers SKILL.md

- **162 fichiers valides** : en-tête YAML, `name` identique au dossier, description de 500 caractères au plus contenant « Use when » et la plateforme, une seule section d'installation correcte, aucun renvoi vers un skill inexistant. Tout est vérifié par `tools/validate_plugin.py`.
- **118 validés** sur l'ensemble des critères. Les **44 autres** n'ont qu'un manque, la méthode en étapes :
  - eBay (5) : advertising, product-research, seller-guide, seller-tools, seo ;
  - Walmart (4) : advertising-strategy, listing-optimization, seller-guide, seller-tools ;
  - Shopify (5) : ab-testing, analytics-guide, conversion-optimization, seo, store-setup ;
  - TikTok (1) : live-selling ;
  - génériques (29), dont les 12 skills `ecommerce-*` comme ab-testing ou branding, ainsi qu'affiliate-marketing-strategy, competitor-price-tracker, conversion-rate-optimization, dropshipping-product-research, google-shopping-optimization, influencer-outreach, market-gap-analysis, multichannel et omnichannel-ecommerce, product-launch-strategy, product-page-seo, product-title-optimization, review-monitoring, sales-tracking-tool, shoppable-video, social-media-monitor et woocommerce-seo.
- **Corrigés dans ce lot** : méthode, exemples ou format de livrable ajoutés à 29 skills, dont 12 skills TikTok, les skills à scripts (protection de marque, calculateurs, vérification d'avis) et la chaîne logistique.

## 2. Manifeste et métadonnées

- `marketplace.json` : 162 entrées, identiques aux dossiers ; version 1.5.0, la même pour le marketplace et pour le plugin. `claude plugin validate .` réussit.
- **Anomalie mineure, non corrigée** : 21 skills gardent dans leur en-tête une clé `version: 1.0.0` héritée du dépôt d'origine. D'autres clés sont également inconnues de Claude Code : `nexscope` (16), `author` (9), `lang` (1), `platform` (1).
  - **Impact** : aucun, car Claude Code ignore ces clés ; mais la `version` peut induire un lecteur en erreur.
  - **Proposition** : les supprimer ou les déplacer sous `metadata` dans un prochain lot, ce qui modifie des métadonnées d'origine.

## 3. Déclenchement automatique (test réel)

Méthode : 52 demandes rédigées comme un vendeur les écrirait, couvrant Amazon (5), Shopify (10), Etsy (10), TikTok Shop (9), Walmart (2), eBay (2), les skills génériques (13) et un cas témoin hors sujet. Chaque demande est envoyée à Claude avec le plugin chargé. Le cas réussit si Claude appelle l'un des skills attendus. Les définitions sont dans `evals/trigger_cases.json`.

| Passage | Résultat | Coût | Remarque |
|---|---|---|---|
| Avant optimisation (état du LOT 4) | 39/52 | 4,28 $ | 13 échecs, tous « aucun skill appelé » |
| Après optimisation | 39/52 | 4,23 $ | 2 cas corrigés, 2 cas qui varient alors que leur description n'a pas changé |

Constats :
- **Aucune confusion entre voisins** : aucun cas n'a déclenché un autre skill que celui attendu. Le travail des LOT 2 et 3 sur les rôles et les descriptions tient en conditions réelles.
- **Le cas témoin** (une question de programmation) ne déclenche aucun skill, comme attendu.
- **Les échecs sont du sous-déclenchement** : Claude répond lui-même aux questions qui lui paraissent simples, comme un calcul de marge à partir de trois chiffres ou la signification d'un score de vitesse. Les cas restants concernent les calculateurs Amazon, TikTok et Walmart, le suivi des prix Walmart, les stocks, les Core Web Vitals, les thèmes et les e-mails Shopify, la stratégie créateurs TikTok, la réputation et le point d'entrée Etsy.
- **Les descriptions renforcées** (« même pour une question rapide ») n'ont pas eu d'effet mesurable sur ces cas.
- **Limite de la mesure** : une seule exécution par cas. Une différence de 1 ou 2 cas entre deux passages reste dans le bruit.

## 4. Doublons et conflits

- Le registre `tools/skill_groups.json` définit 26 groupes et 99 skills, chacun avec un rôle unique, et une section « Role and Scope » générée dans chaque skill.
- Au sein de chaque groupe, aucune paire de descriptions ne dépasse 50 % de ressemblance.
- Aucune paire de skills ne partage plus de la moitié de son contenu spécifique, en dehors des variantes de plateforme voulues.
- Plus aucun skill-gabarit : il y en avait 56 avant le LOT 3.
- Ces règles sont vérifiées par `tests/test_duplicates.py`.

## 5. Scripts et calculs

- **48 scripts** dans 28 skills, tous compilables et n'utilisant que la bibliothèque standard Python (vérifié par test).
- **Calculs testés sur des valeurs vérifiées à la main** : frais par plateforme, point de commande, indice de prix, budget d'erreur, clé de contrôle GTIN, part de linéaire, violations du prix minimum annoncé.
- **Les sorties Amazon sont identiques à la version 1.0.0**, ce que vérifient des fichiers de référence.

**Anomalies graves trouvées et corrigées dans ce lot :**

| Script | Problème | Impact | Correction | Test |
|---|---|---|---|---|
| `brand-monitoring/scripts/monitor.py` | Rapport produit à partir de **mentions inventées** pour n'importe quelle marque, alerte de crise comprise ; la collecte en ligne n'est pas branchée | Un vendeur peut croire à de vrais avis ou à une vraie crise : contenu fictif présenté comme réel | Lit les mentions réelles fournies en JSON ; sans données, affiche « DEMO DATA » ; SKILL.md et description indiquent que le script ne collecte rien | `test_brand_monitoring_analyzes_given_mentions`, `test_demo_is_labelled` |
| `etsy-seo/scripts/analyzer.py` | Ignorait l'annonce fournie et analysait toujours un bracelet de démonstration | Score et conseils faux pour l'annonce du vendeur | Lit l'annonce en JSON, rejette les champs inconnus, signale la démonstration | `test_etsy_seo_analyzes_given_listing` |
| `product-differentiation/*/scripts/analyzer.py` (4 skills) | Ignorait les données fournies ; les exemples documentés utilisaient des champs inexistants | Analyse concurrentielle fausse | Lit le JSON réel ; exemples réécrits au bon format | `test_product_differentiation_analyzes_given_reviews`, `test_examples_run` |

Corrections des lots précédents, toujours vérifiées : scripts Amazon appliqués à d'autres plateformes (LOT 1), retour silencieux aux données de démonstration dans la vérification des avis (LOT 1), sous-commandes inopérantes de la protection de marque (LOT 1).

## 6. Fonctionnalités par plateforme

| Plateforme | Vérifié par test |
|---|---|
| Amazon | Calculateur (commissions par catégorie, FBA), chaîne logistique, protection de marque (Brand Registry), avis, différenciation ; sorties identiques à la 1.0.0 |
| Shopify | Frais Shopify Payments selon le plan, frais de passerelle tierce, coût d'acquisition maximal, chaîne logistique 3PL, protection de marque (DMCA) |
| Etsy | Analyse SEO sur l'annonce fournie (limite de 140 caractères, 13 tags), 20 skills Etsy avec méthode propre |
| TikTok Shop | Commission (8 % par défaut aux États-Unis, 5 % pour la bijouterie, taux réel modifiable), commission des créateurs, IP Protection Center, réseau FBT |
| Walmart, eBay | Commissions avec paliers de prix, WFS, indice de prix, VeRO, Brand Portal |

Les frais restent des estimations datées de novembre 2026 : les pages officielles de TikTok, Walmart et Shopify n'étaient pas accessibles depuis l'environnement de travail. Chaque skill et chaque script demande de confirmer le taux réel.

## 7. Installations et mises à jour

`tools/check_install.py` joue le parcours complet dans une configuration isolée : ajout du marketplace, installation (162 skills), publication simulée d'une version, mise à jour, désinstallation. Toutes les étapes réussissent, avec la version courante de la CLI comme avec la version figée de la CI (2.1.319), sans authentification. Le Skills CLI trouve aussi les 162 skills et installe correctement un skill rangé en sous-dossier.

## 8. Références et dépendances

- **Aucun renvoi vers un skill inexistant** (validateur). Les renvois vers le dépôt externe Amazon-Skills sont explicitement signalés comme externes.
- **369 liens externes vers 18 domaines**, surtout nexscope.ai et github.com. Leur disponibilité n'a pas pu être testée : le réseau de l'environnement est restreint.
- **Dépendances de CI figées** (PyYAML et Claude Code CLI avec empreintes et signatures), mises à jour par Dependabot.

## 9. Descriptions et coût en tokens

- Toutes les descriptions font 500 caractères au plus (59 600 caractères au total, contre 62 200 avant).
- Le coût permanent passe de 24 400 à **23 500 tokens par session** selon `claude plugin details`, soit environ 145 tokens par skill. Il s'ajoute à chaque session où le plugin est actif, même si aucun skill n'est utilisé. Le contenu complet d'un skill n'est chargé qu'à son utilisation.
- L'estimation interne de `tools/audit_library.py` (4 caractères par token) donne environ 16 500 tokens pour les seules descriptions. L'écart vient de la mise en forme ajoutée par Claude Code.

## 10. Régression

- La CI exécute à chaque modification : validateur, cohérence du registre, 75 tests, `claude plugin validate` et le parcours d'installation.
- Les tests de chaque lot ont été rejoués sur l'état précédent pour confirmer qu'ils détectent bien les défauts corrigés.
- Le test de déclenchement réel reste **manuel**, car il consomme le quota du compte (environ 4 $ par passage).

## Problèmes restants

1. **44 skills sans méthode en étapes.** Ils sont listés dans `tests/test_lot5_audit.py`, et la liste ne peut que diminuer. Ils sont utilisables, mais reposent surtout sur les connaissances générales du modèle.
2. **Sous-déclenchement sur les questions simples** (environ 25 % des demandes testées). La rédaction des descriptions ne l'a pas réduit.
3. **Frais non vérifiés auprès des sources officielles** : TikTok Shop US (6 % ou 8 % selon les sources), grille Walmart.
4. **Métadonnées héritées** dans 21 en-têtes (`version: 1.0.0`) et autres clés non standard.
5. **Coût permanent élevé** (≈ 23 500 tokens) dû au nombre de skills.
6. **Liens externes non vérifiés** (réseau restreint).
7. **La « fusion » des voisins est faite par rôles et renvois, sans suppression de contenu.** `tiktok-influencer-marketing` garde un contenu générique proche de `tiktok-creator-marketplace` ; retirer ce contenu attend ta décision.

## Recommandations finales

1. **Fusionner les PR dans l'ordre** #1, #2, #3, #4, #5, puis celle du LOT 5, après relecture. Chaque PR contient la précédente.
2. **LOT 6 : enrichir les 44 skills restants** avec la même structure que le LOT 4, en commençant par eBay et Walmart (9 skills sans méthode).
3. **Sous-déclenchement** :
   - documenter l'appel explicite (`/ecommerce-skills:profit-margin-calculator-amazon`) pour les calculs ;
   - mesurer avec 3 exécutions par cas avant toute nouvelle retouche des descriptions (environ 13 $) ;
   - envisager d'ajouter, sur décision de ta part, une consigne projet indiquant à Claude de privilégier ces skills.
4. **Coût en tokens** : proposer des plugins thématiques facultatifs (Amazon, Shopify, Etsy, TikTok Shop) dans le même marketplace, pour qu'un vendeur mono-plateforme charge 30 à 50 skills au lieu de 162. C'est un changement d'organisation qui demande ta validation.
5. **Vérifier les frais** auprès des pages officielles (Seller Center TikTok, Walmart, Shopify) depuis un réseau sans restriction, puis mettre à jour les valeurs par défaut datées.
6. **Nettoyer les métadonnées** héritées des en-têtes.
7. **Relancer la suite de déclenchement** (`claude plugin eval`) avant chaque version majeure, et consigner le résultat dans ce rapport.
