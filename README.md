# Cryptographic Protocol Implementation

## Programming Language

Python 3

---

# RSA Implementation

The RSA program generates public and private keys using two prime numbers. It encrypts a numeric message using the public key and decrypts it using the private key. The program prints all important intermediate values, including n, φ(n), e, d, the ciphertext, and the recovered message.

### Test Case 1

- p = 3
- q = 11
- e = 3
- m = 4

### Test Case 2

- p = 5
- q = 17
- e = 5
- m = 8

---

# Diffie-Hellman Implementation

The Diffie-Hellman program performs secure key exchange between two users. It generates the public values, computes the shared secret independently for Alice and Bob, and verifies that both users obtain the same secret key.

### Test Case 1

- p = 29
- α = 2
- a = 5
- b = 12

### Test Case 2

- p = 23
- α = 5
- a = 6
- b = 15

---

# Security Principle Mapping

## RSA

RSA provides confidentiality by encrypting data with the public key so that only the private key can decrypt it. It can also provide authentication and non-repudiation when used for digital signatures.

## Diffie-Hellman

Diffie-Hellman is a key exchange protocol because it securely establishes a shared secret between two users. It does not encrypt or decrypt messages by itself.

---

# Threat Model Write-up

## (a) Firewall

A network firewall should be placed between the internet and the CampusConnect server. It should allow HTTPS traffic (TCP port 443) while blocking unnecessary incoming connections.

## (b) Intrusion Detection System

Both a Host-based IDS and a Network-based IDS should be deployed. A Host-based IDS monitors activities on the server, while a Network-based IDS monitors suspicious traffic across the network.

## (c) HTTP vs HTTPS

CampusConnect should use HTTPS instead of HTTP. HTTPS encrypts communication and helps prevent credential sniffing and session hijacking.

## (d) Authentication Design

The system should use Multi-Factor Authentication with two factors:

1. Password
2. One-Time Password (OTP)

Students should access only their own records, instructors should manage course-related information, and administrators should have full system privileges.

## (e) Attack Classification

Credential sniffing is a passive attack because an attacker secretly captures network traffic to obtain usernames and passwords without modifying the transmitted data.

---

# Running the Programs

Run the following files:

1. rsa.py
2. diffie_hellman.py
