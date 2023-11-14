# Jeu de la Vie avec Tkinter

Ce script Python implémente le "Jeu de la Vie" de John Conway en utilisant la bibliothèque Tkinter pour créer une interface graphique simple. Le jeu se déroule sur une grille bidimensionnelle où chaque cellule peut être soit vivante (1) soit morte (0). Les règles du jeu déterminent l'évolution des cellules au fil du temps.

## Fonctionnalités

### Interface graphique Tkinter

La grille du jeu est affichée dans une fenêtre Tkinter avec des boutons pour contrôler le jeu.

### Boutons

- **Start :** Démarre le jeu en continu en appelant la méthode `start_game`.
- **Stop :** Arrête le jeu en mettant la variable `self.running` à `False`.
- **Restart :** Redémarre le jeu avec une nouvelle configuration aléatoire en appelant `restart_game`.
- **Quit :** Ferme l'application en appelant `self.root.destroy()`.

### Méthodes principales

- **count_neighbors(x, y) :** Compte le nombre de voisins vivants autour de la cellule à la position (x, y). Utilise les règles du jeu classiques du "Jeu de la Vie".
- **update_grid() :** Met à jour la grille en fonction des règles du jeu. Crée une nouvelle grille en appliquant les règles à chaque cellule.
- **draw_grid() :** Affiche la grille mise à jour dans la fenêtre Tkinter. Utilise le module Canvas de Tkinter pour dessiner les cellules vivantes et mortes.

## Utilisation

1. **Démarrage de l'application :** Exécutez le script Python.
2. **Interaction avec les boutons :**
   - Cliquez sur "Start" pour démarrer le jeu en continu.
   - Cliquez sur "Stop" pour arrêter le jeu.
   - Cliquez sur "Restart" pour redémarrer le jeu avec une nouvelle configuration aléatoire.
   - Cliquez sur "Quit" pour fermer l'application.

## Configuration

Vous pouvez ajuster la taille de la grille en modifiant les valeurs de `width` et `height` dans la création de l'objet `JeuDeLaVie`.

---
**Note :** Assurez-vous d'avoir Python installé sur votre machine pour exécuter ce script.
