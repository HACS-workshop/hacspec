#!/usr/bin/env python3

from specs.xmss import *
from lib.speclib import *
from tests.testlib import print_dot, exit

# KAT case 1.
# Generated with https://github.com/joostrijneveld/xmss-reference/
auth_path: AUTH_PATH_t = array([bytes.from_hex("edd5c7ad52fb44742754c21e8df7930860987bcdd813a5ad92275f2a2bd0b9a0"), bytes.from_hex("89ea5855403b9fbfdf285c848735a51f50ef60c4377d1511c8eced1caa87f7bc"), bytes.from_hex("97498a7c5d81cbe645e6bf360782e044541ac6eb7823ab636e9ea1164516f5e6"), bytes.from_hex("4096857edb58de5ffe5852dd3ae76d2cb98ac2c8d586f32558309e56042af8f5"), bytes.from_hex("5aa6a2ee887a998f78f5ace7dfe42a013b448cd8b15f4c48d42960f4b0fc0a4b"), bytes.from_hex("46f0a3181399b0e8786513f7c824fd7ba71c205492ce8b957bc7e6e62b5b1748"), bytes.from_hex("cb91128e5590fa539e5b69549bc691f627bf54dfd7ef4abdc53ee3cf838c6aab"), bytes.from_hex("3cf2577b953c2af48f8c71ca5ecf7b79b00d98963ab591fe46c9c7b83d2ee21c"), bytes.from_hex("62bfea72f92438ed851b938ddd72a4d5cf571d80fdf8850b9deb3ba05a96d385"), bytes.from_hex("519f104e1af722d18da004f1c845136b0033194e488dff78ae4f4458910f58bc")])
r: key_t = bytes.from_hex("a16058381620addd3b95f7de26958482ed8614176ff2c28b8dbd67ccca6f2e8a")
sig_ots: sig_t = array([bytes.from_hex("eb47805fb82bbdd5657826e8a7990fa0539589648b92292e7e7b4f92b4e9d6d2"), bytes.from_hex("d4c84ca568a8b55811a84c775ec15c5689872093d91cde758e00fd89b0a2ed62"), bytes.from_hex("577efbde7268a344b2025e4a8d532caa849a344a0668a71a30a90f01e31dcddd"), bytes.from_hex("ae5bdb0765729489eeb85f9c54a25a3e6d4b3dfbf1bf8479fdf73c41d6abc0b8"), bytes.from_hex("10514fa30b35cef042e5c524fc827e5356b942f85ce72be1d728e37a6faf4d22"), bytes.from_hex("19ae122933840c5dd462a975be849658a9e9f6fb9ba53a171fabe4008e2f2032"), bytes.from_hex("70bf1c38d094dd0548690512458b7f93294d50aec2c1ae81af375ab3eaea86c8"), bytes.from_hex("b90c89910df38894fb34e85d141b2a560c3ef767d893a15a0bcc33335a5bb3a1"), bytes.from_hex("945825cf761d86327acd0c4fd37e5236692a107bde48cd81c332c0af015d0b32"), bytes.from_hex("d662625f40c1ef484846e4e4eec51c02e64ba548dba5e0e9379eaa1e330b12a4"), bytes.from_hex("e63820af1e94f4281bcce42158bf23b9c41e762b0b085371a7c29b733e632adb"), bytes.from_hex("63be3adbe1ef7b2f4cdbea690191cca8973d2b5deb397b7133ac1ac807e0f930"), bytes.from_hex("a06dcf567f39138d508893c53552cba93b34919e24631950d4e6b95caa5189b6"), bytes.from_hex("94b2c64387b397c0ff71a86ceda267c65472335a05ce390aa5b20609c0b1b6e3"), bytes.from_hex("6dfe2e69bccddba6ab95f4b2974569f9bbf1a07f5ce2e7e1400361e871923760"), bytes.from_hex("a3d5aa1ee0299ae19cc29d7a07b4b6b96338bb28ebf0854c9d95a73804612981"), bytes.from_hex("cee124c6931b6dd921b562c735e82f20d58a4f332c87dedf6056f918811ce3a7"), bytes.from_hex("f7bb53674b65654a081c3c0bd7f15bfcd1ca922a71f5af101283935643f96161"), bytes.from_hex("51aff5b795d6b1a917b85349526b0294e570351af4a5cc9d03e8d3dd01bfef5d"), bytes.from_hex("5feb1cfe125a49368a61c1ae56e56758bc2d3f636e7c65122b134e4a06eb2ce0"), bytes.from_hex("3b27ba802cbc7789279b3d1e7dc2a6f4f9dbbf1ae08704fbf7e995a1dc1ca325"), bytes.from_hex("d58348bbd71ab2fa25a9b25d64d60d187e685bf38b42448d4efdbe680d7ebe2d"), bytes.from_hex("651bfc002aa6f9732a9f29f2235eb8b7a58fa186952e5aae1fce31a4c21453b0"), bytes.from_hex("1c8d03b7e57bf36cef8c5f6513106ee642698ef041911375480abc5cb79bcc3d"), bytes.from_hex("7fbd69c3cdbf903640f4420ed61c6e5e853b6674e688cd12a99e56340d4ed3f0"), bytes.from_hex("5b34bcbc7975e0ee00b103818d151509348422cefc2d4a7bbbcbc4a550b665a2"), bytes.from_hex("aaefbb9f4fa2ad2d3f312f84f132bfea3bff06ab2b66ba2104a878d55655fc3e"), bytes.from_hex("fdfbb418916b88e9309b10d26f64119c92efe353f725862f53e43a1d58667d65"), bytes.from_hex("7946cf6179f6c7bd34e2b1fb23e2898cf9571c4282f3c9a724101abd69a64b3d"), bytes.from_hex("1ba98c182f17966f5639dc5587acd7e8dd3603609dfb7813072c9b8858e47b9f"), bytes.from_hex("0b4dd0abe725eba71cb575460c2b96b4e860f70d629bd749a0809feada36c57c"), bytes.from_hex("02b295a47ea929ea2fd33fd8e403c30ce172893dd0c5c3de8538d65feb124fba"), bytes.from_hex("69b14796c683bb6b1c0a441bc898313410e3a38b5e17304c82d59832bea9a0aa"), bytes.from_hex("9de7e0e15804a9721594ca535876dbb88f8dd113f4c56d0fdb09edea2c23dcc7"), bytes.from_hex("5ddea007221d5e2651e8c784088b650f539449d099bfc00474cdbadc9fcc5fa7"), bytes.from_hex("3a3c427d53bd97f85e8023bc09e563eca85c3bfc84a10154c6b06085bccf82f6"), bytes.from_hex("ee0a627b02f085835e101975cfd863e683512bbfd8987dce9d576b477920b446"), bytes.from_hex("99d8732e7d5ae334b2de8a1b76d16ab9546a745b21dd3c7af3141a7c3bcf6d3f"), bytes.from_hex("3aefe97ed3f5db0a7cfa46e7658ac43546d95f2f0e9774a5eb22b80081854245"), bytes.from_hex("f4533abbabc281bba194b1e753f5a7541f2c9a6adfeaf1b8efb11ab9ae51eb5d"), bytes.from_hex("c6bd09d2ea70e73e2d1ab5ce65f0636891b068119174923e1de5ba58a01b6416"), bytes.from_hex("17ddb7cecbb80bdfd93ce20aa61b125a17f67f0ff77af007c56f0db82cd23fbd"), bytes.from_hex("a009da414fe6e2fd7d41a1072a96a2e26b775670187b6c73d447c648db8e421b"), bytes.from_hex("d2b1ead6e119c146bc278b05ecb58d961df87c8e1732933ee7432e58552a0ac3"), bytes.from_hex("b87cbb75ff15361ffef9ec15205a49ca2f0e3d780250fda1116848bfa0524652"), bytes.from_hex("a21caadddcea6b11c9c86ff1ae772fa6a68bec58287264e47765a4f8dcd99a69"), bytes.from_hex("f49cfc6ea610635f6dbbe6f8409800c24e4802da2163c4c45ba3c55e02f32772"), bytes.from_hex("13ceba0cbeb2c57fda794b5de33d61ae03512fcbb4c60eefb33752ae816e2c94"), bytes.from_hex("164db9fa7359fedaf792261c4bc4f8fd434c59bc4d2ecbde13eceb85e8c822f7"), bytes.from_hex("b03c18e5acf8bd9da51c1ade9e5fbee3298f0411ff2743c291e75c29b9320635"), bytes.from_hex("f7a0f8827d49bd76ee4fff84313940f05616b03f77bbcd0aaf704d5bedb8a0ff"), bytes.from_hex("2e8abfab3a272b678f6c2eeab375666d5ef34808d23e31f0c05410bf5cc4dc22"), bytes.from_hex("1c9b6051336a89b2ddcda9ec4b0b16e01335347c7e9461386448c043086022be"), bytes.from_hex("6e6eb1542e01613fc9452526487a48106da51320c135682a8e3b6c893ed138b4"), bytes.from_hex("99fd0fdc1bb0711c0ce77bb45eb4e0be9ddc86171838cff31bd3969a7949e353"), bytes.from_hex("9e907f3c872317225cbd7f5251ca04c81d9aa7a4e5d0f9c0794f20f0c08458ce"), bytes.from_hex("ce6eb023288d9b4df0668257971dea659cc8798203f6d09842279e5b3beb3b64"), bytes.from_hex("26b200e38a707e68579fa0649efa4b149394f1b60e5a038857ad1c416a747cd0"), bytes.from_hex("53266d1336082d251846dc4388df2015e05995b69648dfe3c0890d637929fbe7"), bytes.from_hex("5f9a996e2050c21d88b658babfd080ea6bb3728e6096b30fe30500417352d892"), bytes.from_hex("50406057d38982b19d53259c060a2f2c0692db6c4bb6e26547d281c1636e5cea"), bytes.from_hex("eff0cb899a2132db334e3521e1d0af93af11dd85931fa47102abd3fdf27e6917"), bytes.from_hex("b3cd7c4060fcc742c48d79888e2c8a515ac1d7fb68d067a236df3cf9d8168c29"), bytes.from_hex("2aa7a138c7491c2e0600bc3cd1e0389071dc1016f9033b1ae9c6172c6835c74e"), bytes.from_hex("14bae4e67714b0867fcada2a9c5addb5aab117633103b374bc35c25df9b41130"), bytes.from_hex("9d8f4f519beefc8d12c73ff8ca743a87730932250762c82d32d44b1812c9a9cc"), bytes.from_hex("4ee6127833d002ad80d76249fb211249821c3d370d099f3bf0a2512c3419749d")])
idx_sig: uint32_t = uint32(0)

oid: uint32_t = uint32(1)
root_node: key_t = bytes.from_hex("9449c44f9fee6f58fff45bb79b78377e315be3ada2e2c36d444374bc71ecaff2")
seed: seed_t = bytes.from_hex("269deaacfefa1c3f46f21a216e579fec9e209700a79f9dcc225d62ca34e149d4")

m: vlbytes_t = bytes.from_hex("ed4d25c8771bd126b6282d63a4e5d8a181355d5efe2829c920e398a1cd275910")
pk: PK_t = (oid, root_node, seed)
sig: SIG_t = (idx_sig, r, sig_ots, auth_path)

def test_xmss_kat():
    if xmss_verify(sig, m, pk):
        print("KAT verified successfully")
    else:
        print("Error verifying KAT")
        exit(0)

# TODO: This is way too slow.
def test_xmss_self():
    adr = array.create_random(nat(8), uint32)
    seed = bytes.create_random_bytes(n)
    msg = bytes.from_ints([0xFF, 0xFF, 0xFF, 0xFF, 0xFF])
    msg_h = sha256(msg)

    xmss_sk : SK_t = key_gen_xmss()
    print("Generated key")

def main():
    print_dot()
    test_xmss_self()
    test_xmss_kat()
    exit(0)


if __name__ == "__main__":
    main()
