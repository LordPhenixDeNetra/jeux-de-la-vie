import tkinter as tk
import random
import time

TIME_SLEEP = 0.6


class JeuDeLaVie:
    def __init__(self, root, width, height, cell_size=20):
        # Initialisation de l'objet JeuDeLaVie avec la fenêtre principale (root), la taille de la grille,
        # et la taille des cellules.
        self.root = root
        self.root.title("Jeu de la Vie")
        self.width = width
        self.height = height
        self.cell_size = cell_size
        # Création d'un canvas pour afficher la grille.
        self.canvas = tk.Canvas(self.root, width=width * cell_size, height=height * cell_size, borderwidth=0,
                                highlightthickness=0)
        self.canvas.pack()

        # Initialisation de la grille à une matrice vide (toutes les cellules mortes).
        self.grid = [[0] * width for _ in range(height)]
        # Variable pour suivre l'état du jeu (en cours ou arrêté).
        self.running = False
        # Configuration des boutons dans l'interface.
        self.setup_buttons()

    def setup_buttons(self):
        # Création des boutons Start, Stop, Restart, et Quit dans l'interface.
        start_button = tk.Button(self.root, text="Start", command=self.start_game)
        start_button.pack(side=tk.LEFT)

        stop_button = tk.Button(self.root, text="Stop", command=self.stop_game)
        stop_button.pack(side=tk.LEFT)

        restart_button = tk.Button(self.root, text="Restart", command=self.restart_game)
        restart_button.pack(side=tk.LEFT)

        quit_button = tk.Button(self.root, text="Quit", command=self.root.destroy)
        quit_button.pack(side=tk.RIGHT)

    def start_game(self):
        # Méthode appelée lorsqu'on clique sur le bouton Start.
        # Elle initialise le jeu en continu en appelant run_game().
        self.running = True
        self.run_game()

    def stop_game(self):
        # Méthode appelée lorsqu'on clique sur le bouton Stop.
        # Elle arrête le jeu en mettant la variable self.running à False.
        self.running = False

    def restart_game(self):
        # Méthode appelée lorsqu'on clique sur le bouton Restart.
        # Elle arrête le jeu, initialise une nouvelle grille aléatoire, et dessine la nouvelle grille.
        self.running = False
        self.grid = [[random.choice([0, 1]) for _ in range(self.width)] for _ in range(self.height)]
        self.draw_grid()

    def run_game(self):
        # Méthode principale qui fait évoluer le jeu en continu tant que self.running est True.
        while self.running:
            self.update_grid()  # Met à jour la grille selon les règles du jeu.
            self.draw_grid()  # Dessine la grille mise à jour.
            self.root.update()  # Met à jour l'interface Tkinter.
            time.sleep(TIME_SLEEP)  # Pause pour rendre l'affichage plus lisible.

    def count_neighbors(self, x, y):
        # Méthode qui compte le nombre de voisins vivants autour d'une cellule à la position (x, y).
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                new_x = (x + i + self.width) % self.width
                new_y = (y + j + self.height) % self.height
                count += self.grid[new_y][new_x]
        return count

    def update_grid(self):
        # Méthode qui met à jour la grille selon les règles du "Jeu de la Vie".
        new_grid = [[0] * self.width for _ in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                neighbors = self.count_neighbors(x, y)
                if self.grid[y][x] == 1 and (neighbors < 2 or neighbors > 3):
                    new_grid[y][x] = 0
                elif self.grid[y][x] == 0 and neighbors == 3:
                    new_grid[y][x] = 1
                else:
                    new_grid[y][x] = self.grid[y][x]
        self.grid = new_grid

    def draw_grid(self):
        # Méthode qui dessine la grille sur le canvas Tkinter.
        self.canvas.delete("all")  # Efface le contenu actuel du canvas.
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == 1:
                    color = "black"
                else:
                    color = "white"
                # Dessine un rectangle pour représenter la cellule.
                self.canvas.create_rectangle(x * self.cell_size, y * self.cell_size,
                                             (x + 1) * self.cell_size, (y + 1) * self.cell_size,
                                             fill=color, outline="gray")


if __name__ == "__main__":
    # Code exécuté lorsque le script est lancé directement.
    root = tk.Tk()
    game = JeuDeLaVie(root, width=30, height=20, cell_size=20)
    root.mainloop()
