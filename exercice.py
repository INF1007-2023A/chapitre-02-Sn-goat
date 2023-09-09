#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    mot_majuscule = ""
    for letter in mot:
        mot_majuscule += chr(ord(letter) - 32)
    return mot_majuscule
print(majuscule("sergile"))


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
