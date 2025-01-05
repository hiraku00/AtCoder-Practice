import random

def estimate_pi(n):
    inside_circle = 0
    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1

    pi_estimate = (inside_circle / n) * 4
    return pi_estimate


if __name__ == '__main__':
    num_traials = [100, 1000, 10000, 100000, 1000000]
    for n in num_traials:
        estimated_pi = estimate_pi(n)
        print(f"Estimated value of pi for {n} trials is {estimated_pi}")
