# RSA Algorithm Implementation

from math import gcd

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d
    return None

def rsa_demo(p, q, e, m):

    print("-" * 50)
    print(f"Input: p={p}, q={q}, e={e}, m={m}")

    if p == q:
        print("Error: p and q must be different prime numbers.")
        return

    if not is_prime(p) or not is_prime(q):
        print("Error: p and q must both be prime.")
        return

    n = p * q
    phi = (p - 1) * (q - 1)

    if not (1 < e < phi):
        print("Error: e must satisfy 1 < e < phi(n).")
        return

    if gcd(e, phi) != 1:
        print("Error: e is not coprime with phi(n).")
        return

    if not (0 <= m < n):
        print("Error: Message must satisfy 0 <= m < n.")
        return

    d = mod_inverse(e, phi)

    if d is None:
        print("Error: Private key could not be calculated.")
        return

    c = pow(m, e, n)
    recovered = pow(c, d, n)

    print(f"n = {n}")
    print(f"phi(n) = {phi}")
    print(f"Public Key (e) = {e}")
    print(f"Private Key (d) = {d}")
    print(f"Ciphertext = {c}")
    print(f"Recovered Message = {recovered}")


print("===== Test Case 1 =====")
rsa_demo(3, 11, 3, 4)

print("\n===== Test Case 2 =====")
rsa_demo(5, 17, 5, 8)
