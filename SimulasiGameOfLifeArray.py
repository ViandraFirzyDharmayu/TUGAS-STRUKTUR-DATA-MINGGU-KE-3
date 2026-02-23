import time
import os
import copy

# Fungsi untuk menampilkan grid
def tampilkan(grid):
    for row in grid:
        print(" ".join("█" if cell == 1 else "." for cell in row))
    print()

# Fungsi menghitung tetangga hidup
def hitung_tetangga(grid, x, y):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            nx, ny = x + i, y + j
            if 0 <= nx < rows and 0 <= ny < cols:
                count += grid[nx][ny]
    
    return count

# Fungsi update satu generasi
def update(grid):
    rows = len(grid)
    cols = len(grid[0])
    new_grid = copy.deepcopy(grid)
    
    for i in range(rows):
        for j in range(cols):
            tetangga = hitung_tetangga(grid, i, j)
            
            if grid[i][j] == 1:
                if tetangga < 2 or tetangga > 3:
                    new_grid[i][j] = 0
            else:
                if tetangga == 3:
                    new_grid[i][j] = 1
    
    return new_grid

# Inisialisasi grid (contoh pola Glider)
grid = [
    [0,1,0,0,0],
    [0,0,1,0,0],
    [1,1,1,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
]

# Simulasi
generasi = 10
for _ in range(generasi):
    os.system("cls" if os.name == "nt" else "clear")
    tampilkan(grid)
    grid = update(grid)
    time.sleep(1)