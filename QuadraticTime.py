
import time

def quadratic_time(n):
    print(f"\nO(n^2) with n = {n}")
    start = time.time()
    for i in range(n):
        for j in range(n):
            pass  # simulate O(n^2) operation
    end = time.time()
    print(f"Time taken: {end - start:.6f} seconds")

quadratic_time(100)
quadratic_time(400)
quadratic_time(800)
