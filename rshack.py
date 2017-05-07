#!/usr/bin/python3
# -*- coding: utf-8 -*-

# RSHack
# Zweisamkeit
# 16/03/17
# GNU/GPL v3

import subprocess
from os import getcwd

def accueil(arg):

  if arg == "first":

    subprocess.call(["clear"], shell=True)

    print ("\n")
    print ("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("\t\t          RSHack         ")
    print ("\t\t       Zweisamkeit       ")
    print ("\t\t        GNU GPL v3       ")
    print ("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("\n\n")
    print("\tList of the available attacks:\n")
    print("\t\t1. Wiener Attack")
    print("\t\t2. Hastad Attack")
    print("\t\t3. Fermat Attack")
    print("\t\t4. Bleichenbacher Attack")
    print("\t\t5. Common Modulus Attack")
    print("\t\t6. Chosen Ciphertext Attack")
    print("\n\tList of the available tools:\n")
    print("\t\t7. RSA Public Key parameters extraction")
    print("\t\t8. RSA Private Key construction")
    return(input("\n\tWhat attack or tool do you want to carry out? "))

  elif arg == "again":

    return(input("\n\tPlease enter the number of the attack you want to carry out: "))

def choose(arg):

  attack=accueil(arg)

  if attack == "1":

    print("\n\t\t\t ***** Wiener Attack *****")

    try:

      args=input("\n\t\t Arguments ([-h] -n modulus -e exponent):\n\n\t\t\t").split()
      args=' '.join([str(i) for i in args])

    except:

      print("\n\t\t\tArgument Error: Please verify your inputs\n")
      exit()
    
    subprocess.call(["Attacks/Wiener/wiener.py "+args], shell=True)

  elif attack == "2":

    print("\n\t\t\t ***** Hastad Attack *****")

    try:

      args=input("\n\t\tArguments ([-h] -k0 path_to_key0 -k1 path_to_key1 -k2 path_to_key2 -c0 cipher1 -c1 cipher2 -c2 cipher3):\n\n\t\t\t").split()

      if (args[0] != '-h'):

        for i in range (1,6,2):

          if (args[i][0] != '/'):

            args[i] = getcwd() + '/' + args[i]

      args=' '.join([str(i) for i in args])

    except:

      print("\n\t\t\tArgument Error: Please verify your inputs\n")
      exit()

    subprocess.call(["Attacks/Hastad/hastad.py "+args], shell=True)

  elif attack == "3":

    print("\n\t\t\t ***** Fermat Attack *****")

    try:

      args=input("\n\t\t Arguments ([-h] -n modulus -e exponent):\n\n\t\t\t").split()
      args=' '.join([str(i) for i in args])

    except:

      print("\n\t\t\tArgument Error: Please verify your inputs\n")
      exit()

    subprocess.call(["Attacks/Fermat/fermat.py "+args], shell=True)

  elif attack == "4":

    print("\n\t\t\t ***** Bleichenbacher Attack *****")

    try:

      args=input("\n\t\t Arguments ([-h] -n modulus -e exponent -c ciphertext --host hostname -p port --error error padding message):\n\n\t\t\t").split()
      args=' '.join([str(i) for i in args])

    except:

      print("\n\t\t\tArgument Error: Please verify your inputs\n")
      exit()

    subprocess.call(["Attacks/Bleichenbacher/bleichenbacher.py "+args], shell=True)

  elif attack == "5":

    print("\n\t\t\t ***** Common Modulus Attack *****")

    try:

      args=input("\n\t\t Arguments [-h] -n common modulus -e1 first exponent -e2 second exponent -c1 first cipher -c2 second cipher:\n\n\t\t\t").split()
      args=' '.join([str(i) for i in args])

    except:

      print("\n\t\t\tArgument Error: Please verify your inputs\n")
      exit()

    subprocess.call(["Attacks/Common_Modulus/comod.py "+args], shell=True)

  elif attack == "6":

    print("\n\t\t\t ***** Chosen Ciphertext Attack *****")

    try:

      args=input("\n\t\tArguments ([-h] -n N -e E -c C):\n\n\t\t\t").split()

    except:

      print("\n\t\t\tArgument Error: Please verify your inputs\n")
      exit()

    args=' '.join([str(i) for i in args])

    subprocess.call(["Attacks/Chosen_Ciphertext/chocip.py "+args], shell=True)

  elif attack == "7":

    print("\n\t\t\t ***** Parameters extraction *****")

    try:

      args=input("\n\t\tArgument ([-h] -k K):\n\n\t\t\t").split()

    except:

      print("\n\t\t\tArgument Error: Please verify your inputs\n")
      exit()

    if (args[0] == '-k' and args[1]!='/'):

      args[1] = getcwd() + "/" + args [1]

    args=' '.join([str(i) for i in args])

    subprocess.call(["Attacks/Other/Extractor/extractor.py "+args], shell=True)

  elif attack== "8":

    print("\n\t\t\t ***** RSA Private Key constructor *****")

    try:

      args=input("\n\t\tArgument ([-h] -p first_factorization_element -q second_factorization_element -e public_exponent):\n\n\t\t\t").split()

    except:

      print("\n\t\t\tArgument Error: Please verify your inputs\n")
      exit()

    args=' '.join([str(i) for i in args])

    subprocess.call(["Attacks/Other/Private_Key/privkey.py "+args], shell=True)

  else:
 
    choose("again")

if __name__ == "__main__":

  choose("first")
