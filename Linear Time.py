import time

def linear_time(n):
    print(f"\nO(n) with n = {n}")

    start = time.time()
    for i in range(n):
        pass # Simulate some linear operation
    end = time.time()

    print(f"Time taken: {end - start:.6f} seconds")

# Running for increasing sizes
linear_time(10000)
linear_time(20000)
linear_time(30000)
