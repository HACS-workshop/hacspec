from lib.speclib import *
from specs.kyber2 import Kyber #crypto_kem_keypair, crypto_kem_enc, crypto_kem_dec
import json
from tests.testlib import print_dot, exit

def main():
    file = open('tests/test_vectors/kyber2_test_vectors.json')
    kyber_test_vectors = json.load(file)
    print_dot()
    for i in range(len(kyber_test_vectors)):
        kyber_k = kyber_test_vectors[i]['kyber_k']
        kyber_du = kyber_test_vectors[i]['kyber_du']
        kyber_dv = kyber_test_vectors[i]['kyber_dv']
        kyber_sharedkeybytes = kyber_test_vectors[i]['kyber_sharedkeybytes']
        keypaircoins = bytes.from_hex(kyber_test_vectors[i]['keypaircoins'])
        coins = bytes.from_hex(kyber_test_vectors[i]['coins'])
        msgcoins = bytes.from_hex(kyber_test_vectors[i]['msgcoins'])
        pk_expected = bytes.from_hex(kyber_test_vectors[i]['pk_expected'])
        sk_expected = bytes.from_hex(kyber_test_vectors[i]['sk_expected'])
        ct_expected = bytes.from_hex(kyber_test_vectors[i]['ct_expected'])
        ss_expected = bytes.from_hex(kyber_test_vectors[i]['ss_expected'])

        (crypto_kem_keypair, crypto_kem_enc, crypto_kem_dec) = Kyber(kyber_k,kyber_du,kyber_dv,kyber_sharedkeybytes)
        pk, sk = crypto_kem_keypair(keypaircoins, coins)
        ct, ss1 = crypto_kem_enc(pk, msgcoins)
        ss2 = crypto_kem_dec(ct, sk)

        if (ss1 == ss2 and ss1 == ss_expected and ct == ct_expected and pk == pk_expected and sk == sk_expected):
            print("Kyber Test "+str(i)+" successful!")
        else:
            print("Kyber Test "+str(i)+" failed!")
            print("Computed shared secret 1: " + str(ss1))
            print("Computed shared secret 2: " + str(ss2))
            print("Expected shared secret: " + str(ss_expected))
            exit(1)
    exit(0)

main()
