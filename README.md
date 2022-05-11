# Lab: Cryptography
## Overview
**Today we’ll be tackling a cryptographic classic - the Caesar Cipher.**

**Your job will be to devise a method to encrypt a message that can then be decrypted when supplied with the corresponding key.**

**Feature Tasks and Requirements**:

1. [ ] Create an encrypt function that takes in a plain text phrase and a numeric shift.
2. [ ] the phrase will then be shifted that many letters.
3. [ ] E.g. encrypt(‘abc’,1) would return ‘bcd’. = E.g. encrypt(‘abc’, 10) would return ‘klm’.
4. [ ] shifts that exceed 26 should wrap around.
5. [ ] E.g. encrypt(‘abc’,27) would return ‘bcd’.
6. [ ] shifts that push a letter out or range should wrap around.
7. [ ] E.g. encrypt(‘zzz’,1) would return ‘aaa’.
8. [ ] Create a decrypt function that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form when correct key is supplied.
9. [ ] create a crack function that will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.
10. [ ] Devise a method for the computer to determine if code was broken with minimal human guidance.

**Implementation Notes**

    In order to accomplish a certain task you’ll need access to a corpus of English words.
        A search on something like python list of english words should get you going.


## Resources

[]()