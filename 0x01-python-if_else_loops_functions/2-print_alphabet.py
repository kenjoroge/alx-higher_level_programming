#!/usr/bin/python3
for Alphabet in range(ord('a'), ord('z') + 1):
    # the ord function here I am using it to get the
    # ascii code of the first and last lowercase
    # The chr is being used to convvert the ascii code back to characters
    print(chr(Alphabet), end=" ")
