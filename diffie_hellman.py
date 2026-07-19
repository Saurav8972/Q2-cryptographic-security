# Diffie-Hellman Key Exchange Implementation

def is_primitive_root(alpha, p):
    values = set()
    for i in range(1, p):
        values.add(pow(alpha, i, p))
    return len(values) == p - 1


def diffie_hellman(p, alpha, a, b):

    print("-" * 50)
    print(f"Input: p={p}, alpha={alpha}, a={a}, b={b}")

    if not is_primitive_root(alpha, p):
        print("Error: alpha is not a primitive root modulo p.")
        return

    if not (1 < a < p - 1):
        print("Error: Private key 'a' is invalid.")
        return

    if not (1 < b < p - 1):
        print("Error: Private key 'b' is invalid.")
        return

    A = pow(alpha, a, p)
    B = pow(alpha, b, p)

    key_alice = pow(B, a, p)
    key_bob = pow(A, b, p)

    print(f"Public Key of Alice (A) = {A}")
    print(f"Public Key of Bob (B) = {B}")

    print(f"Shared Key computed by Alice = {key_alice}")
    print(f"Shared Key computed by Bob   = {key_bob}")

    if key_alice == key_bob:
        print("Shared Secret Matched")
    else:
        print("Shared Secret Not Matched")


print("===== Test Case 1 =====")
diffie_hellman(29, 2, 5, 12)

print("\n===== Test Case 2 =====")
diffie_hellman(23, 5, 6, 15)
