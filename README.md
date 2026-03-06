# playfair cipher
Playfair Cipher Implementation in Python


This project implements the classical Playfair cipher, a manual symmetric encryption technique based on digraph substitution. The program generates a 5×5 key matrix from a user-provided key (with the standard I/J merging rule) and performs encryption and decryption of plaintext using Playfair rules: same row, same column, and rectangle substitution.

The script processes plaintext by removing spaces, converting letters to uppercase, handling repeated letters in pairs with filler characters, and ensuring even-length digraphs. It then applies the Playfair cipher algorithm to produce the encrypted or decrypted text. The program runs through a simple command-line interface where the user selects encryption or decryption and provides the key and message.

This project demonstrates the implementation of classical cryptographic algorithms, matrix manipulation, and string processing in Python.
