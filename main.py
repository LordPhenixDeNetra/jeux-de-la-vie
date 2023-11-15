import tkinter as tk
from tkinter import ttk
import random
import time

TIME_SLEEP = 0.4
COLOR_LIFE = "yellow"
COLOR_DEAD = "black"
GRID_LINE_COLOR = "grey"


class JeuDeLaVie:
    def __init__(self, root, width, height, cell_size=20):
        # Initialisation de l'objet JeuDeLaVie avec la fenêtre principale (root), la taille de la grille,
        # et la taille des cellules.
        self.root = root
        self.root.title("Jeu de la Vie")
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Création d'un conteneur Frame pour organiser la grille, les boutons, et les explications.
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        # Création d'un canvas pour afficher la grille.
        self.canvas = tk.Canvas(self.frame, width=width * cell_size, height=height * cell_size, borderwidth=0,
                                highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=4)

        # Initialisation de la grille à une matrice vide (toutes les cellules mortes).
        self.grid = [[0] * width for _ in range(height)]
        # Variable pour suivre l'état du jeu (en cours ou arrêté).
        self.running = False
        # Configuration des boutons dans l'interface.
        self.setup_buttons()
        # Configuration de l'événement de clic de la souris.
        self.canvas.bind("<Button-1>", self.add_cell)

        # Configuration de la zone d'explication.
        self.setup_explanation()

    def setup_buttons(self):
        # Création des boutons Start, Stop, Restart, et Quit dans l'interface.

        # Utilisation de la police et de la taille de police personnalisées.
        button_font = ("Helvetica", 12)

        # Utilisez ttk.Button pour des styles améliorés.
        style = ttk.Style()
        style.configure('TButton', font=button_font, padding=5, borderwidth=2, foreground='black', background='#4CAF50')

        start_button = ttk.Button(self.frame, text="Start", command=self.start_game, style='TButton')
        start_button.grid(row=1, column=0, padx=5, pady=5)

        stop_button = ttk.Button(self.frame, text="Stop", command=self.stop_game, style='TButton')
        stop_button.grid(row=1, column=1, padx=5, pady=5)

        restart_button = ttk.Button(self.frame, text="Restart", command=self.restart_game, style='TButton')
        restart_button.grid(row=1, column=2, padx=5, pady=5)

        quit_button = ttk.Button(self.frame, text="Quit", command=self.root.destroy, style='TButton')
        quit_button.grid(row=1, column=3, padx=5, pady=5)

    def setup_explanation(self):
        # Création d'une zone d'explication du jeu avec un design moderne.
        explanation_text = """
        Règles :
        1. Une cellule morte avec exactement 3 voisins vivants devient vivante.
        2. Une cellule vivante avec moins de 2 ou plus de 3 voisins vivants devient morte.

        Cliquez sur la grille pour ajouter des cellules.
        Utilisez les boutons pour contrôler le jeu.
        """

        explanation_frame = tk.Frame(self.frame, bg='#f0f0f0', pady=10)
        explanation_frame.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky='ew')

        explanation_label = tk.Label(explanation_frame, text=explanation_text, justify=tk.LEFT, bg='#f0f0f0', fg='#333')
        explanation_label.pack()

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
                    color = COLOR_LIFE
                else:
                    color = COLOR_DEAD
                # Dessine un rectangle pour représenter la cellule.
                self.canvas.create_rectangle(x * self.cell_size, y * self.cell_size,
                                             (x + 1) * self.cell_size, (y + 1) * self.cell_size,
                                             fill=color, outline=GRID_LINE_COLOR)

    def add_cell(self, event):
        # Méthode appelée lorsqu'on clique sur le canvas pour ajouter une cellule à la position du clic.
        x = event.x // self.cell_size
        y = event.y // self.cell_size
        self.grid[y][x] = 1
        self.draw_grid()


if __name__ == "__main__":
    # Code exécuté lorsque le script est lancé directement.
    root = tk.Tk()
    game = JeuDeLaVie(root, width=30, height=20, cell_size=20)
    root.mainloop()
