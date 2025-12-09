import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random


ROWS = 50
COLS = 50
PROBABILITY = random.uniform(0.2, 0.5)  # вероятность, что клетка живая в начале



def create_random_grid(rows, cols):
    """Создаёт случайную матрицу 0/1 по заданной вероятности."""
    return np.random.choice(
        [0, 1],
        size=(rows, cols),
        p=[1 - PROBABILITY, PROBABILITY],
    )



def add_glider(grid, top, left):
    """Добавляет паттерн Glider на сетку начиная с позиции (top, left)."""
    glider = np.array(
        [
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 1],
        ]
    )
    grid[top : top + 3, left : left + 3] = glider


def add_blinker(grid, top, left):
    """Добавляет паттерн Blinker (вертикальный осциллятор)."""
    blinker = np.array(
        [
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0],
        ]
    )
    grid[top : top + 3, left : left + 3] = blinker


def update(frame_num, img, grid):
    """Один шаг игры Жизнь."""
    new_grid = grid.copy()
    for i in range(ROWS):
        for j in range(COLS):
        
            total = int(
                (
                    grid[i, (j - 1) % COLS]
                    + grid[i, (j + 1) % COLS]
                    + grid[(i - 1) % ROWS, j]
                    + grid[(i + 1) % ROWS, j]
                    + grid[(i - 1) % ROWS, (j - 1) % COLS]
                    + grid[(i - 1) % ROWS, (j + 1) % COLS]
                    + grid[(i + 1) % ROWS, (j - 1) % COLS]
                    + grid[(i + 1) % ROWS, (j + 1) % COLS]
                )
            )

           
            if grid[i, j] == 1:
                if total < 2 or total > 3:
                    new_grid[i, j] = 0
            else:
                if total == 3:
                    new_grid[i, j] = 1

    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return (img,)



grid = create_random_grid(ROWS, COLS)


add_glider(grid, top=1, left=1)
add_blinker(grid, top=20, left=30)


fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation="nearest", cmap="binary")
ax.set_title("Игра Жизнь: Glider и Blinker (50x50)")
ax.axis("off")

ani = animation.FuncAnimation(
    fig,
    update,
    fargs=(img, grid),
    frames=200,
    interval=150,
    blit=True,
)

plt.show()