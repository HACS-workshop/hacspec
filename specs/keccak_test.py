from speclib import *
from keccak import shake128, shake256, sha3_224, sha3_256, sha3_384, sha3_512
from sys import exit

def test(msgLen, msg, expected224, expected256, expected384, expected512, num):
    d224 = bytes.to_hex(sha3_224(msgLen, msg))
    d256 = bytes.to_hex(sha3_256(msgLen, msg))
    d384 = bytes.to_hex(sha3_384(msgLen, msg))
    d512 = bytes.to_hex(sha3_512(msgLen, msg))
    if (expected224 == d224 and expected256 == d256 and expected384 == d384 and
        expected512 == d512):
        print("SHA-3 (224/256/384/512) Test "+str(num)+" successful!")
    else:
        print("Test failed!")
        print("Computed: "+d224)
        print("Expected: "+expected224)
        print("Computed: "+d256)
        print("Expected: "+expected256)
        print("Computed: "+d384)
        print("Expected: "+expected384)
        print("Computed: "+d512)
        print("Expected: "+expected512)
        exit(1)

def main(x: int) -> None:
    msg = bytes.from_ints([])
    expected224 = "6b4e03423667dbb73b6e15454f0eb1abd4597f9a1b078e3f5b5a6bc7"
    expected256 = "a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a"
    expected384 = "0c63a75b845e4f7d01107d852e4c2485c51a50aaaa94fc61995e71bbee983a2ac3713831264adb47fb6bd1e058d5f004"
    expected512 = "a69f73cca23a9ac5c8b567dc185a756e97c982164fe25859e0d1dcc1475c80a615b2123af1f5f94c11e3e9402c3ac558f500199d95b6d3e301758586281dcd26"
    test(0, msg, expected224, expected256, expected384, expected512, 0)

    msg = bytes.from_ints([0x61, 0x62, 0x63])
    expected224 = "e642824c3f8cf24ad09234ee7d3c766fc9a3a5168d0c94ad73b46fdf"
    expected256 = "3a985da74fe225b2045c172d6bd390bd855f086e3e9d525b46bfe24511431532"
    expected384 = "ec01498288516fc926459f58e2c6ad8df9b473cb0fc08c2596da7cf0e49be4b298d88cea927ac7f539f1edf228376d25"
    expected512 = "b751850b1a57168a5693cd924b6b096e08f621827444f70d884f5d0240d2712e10e116e9192af3c91a7ec57647e3934057340b4cf408d5a56592f8274eec53f0"
    test(3, msg, expected224, expected256, expected384, expected512, 1)

    msg = bytes.from_ints([
        0x61, 0x62, 0x63, 0x64, 0x62, 0x63, 0x64, 0x65, 0x63, 0x64, 0x65, 0x66, 0x64, 0x65, 0x66, 0x67,
        0x65, 0x66, 0x67, 0x68, 0x66, 0x67, 0x68, 0x69, 0x67, 0x68, 0x69, 0x6a, 0x68, 0x69, 0x6a, 0x6b,
        0x69, 0x6a, 0x6b, 0x6c, 0x6a, 0x6b, 0x6c, 0x6d, 0x6b, 0x6c, 0x6d, 0x6e, 0x6c, 0x6d, 0x6e, 0x6f,
        0x6d, 0x6e, 0x6f, 0x70, 0x6e, 0x6f, 0x70, 0x71])
    expected224 = "8a24108b154ada21c9fd5574494479ba5c7e7ab76ef264ead0fcce33"
    expected256 = "41c0dba2a9d6240849100376a8235e2c82e1b9998a999e21db32dd97496d3376"
    expected384 = "991c665755eb3a4b6bbdfb75c78a492e8c56a22c5c4d7e429bfdbc32b9d4ad5aa04a1f076e62fea19eef51acd0657c22"
    expected512 = "04a371e84ecfb5b8b77cb48610fca8182dd457ce6f326a0fd3d7ec2f1e91636dee691fbe0c985302ba1b0d8dc78c086346b533b49c030d99a27daf1139d6e75e"
    test(56, msg, expected224, expected256, expected384, expected512, 2)

    msg = bytes.from_ints([
        0x61, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69,
        0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x6a, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x6a, 0x6b,
        0x65, 0x66, 0x67, 0x68, 0x69, 0x6a, 0x6b, 0x6c, 0x66, 0x67, 0x68, 0x69, 0x6a, 0x6b, 0x6c, 0x6d,
        0x67, 0x68, 0x69, 0x6a, 0x6b, 0x6c, 0x6d, 0x6e, 0x68, 0x69, 0x6a, 0x6b, 0x6c, 0x6d, 0x6e, 0x6f,
        0x69, 0x6a, 0x6b, 0x6c, 0x6d, 0x6e, 0x6f, 0x70, 0x6a, 0x6b, 0x6c, 0x6d, 0x6e, 0x6f, 0x70, 0x71,
        0x6b, 0x6c, 0x6d, 0x6e, 0x6f, 0x70, 0x71, 0x72, 0x6c, 0x6d, 0x6e, 0x6f, 0x70, 0x71, 0x72, 0x73,
        0x6d, 0x6e, 0x6f, 0x70, 0x71, 0x72, 0x73, 0x74, 0x6e, 0x6f, 0x70, 0x71, 0x72, 0x73, 0x74, 0x75])
    expected224 = "543e6868e1666c1a643630df77367ae5a62a85070a51c14cbf665cbc"
    expected256 = "916f6061fe879741ca6469b43971dfdb28b1a32dc36cb3254e812be27aad1d18"
    expected384 = "79407d3b5916b59c3e30b09822974791c313fb9ecc849e406f23592d04f625dc8c709b98b43b3852b337216179aa7fc7"
    expected512 = "afebb2ef542e6579c50cad06d2e578f9f8dd6881d7dc824d26360feebf18a4fa73e3261122948efcfd492e74e82e2189ed0fb440d187f382270cb455f21dd185"
    test(112, msg, expected224, expected256, expected384, expected512, 3)

if __name__ == "__main__":
    main(0)
