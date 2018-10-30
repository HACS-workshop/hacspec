from lib.speclib import *

# Four variants of SHA-2

variant_t = refine_t(nat_t, lambda x: x == 224 or x == 256 or x == 384 or x == 512)
i_range_t = range_t(0, 4)
op_range_t = range_t(0, 1)

# Generic SHA-2 spec parameterized by variant_t

@typechecked
def sha2(v:variant_t) -> FunctionType:
    # Initializing types and constants for different variants
    if v == 224 or v == 256:
        blockSize : int = 64
        block_t = bytes_t(blockSize)
        lenSize : int = 8
        len_t = uint64_t
        to_len : FunctionType = ruint64
        len_to_bytes : FunctionType = bytes.from_uint64_be
        word_t = ruint32_t
        to_word : FunctionType = ruint32
        bytes_to_words : FunctionType = bytes.to_uint32s_be
        words_to_bytes : FunctionType = bytes.from_uint32s_be
        kSize : int = 64
        k_t = array_t(word_t,kSize)
        opTableType_t = array_t(int,12)
        opTable : opTableType_t = opTableType_t([
            2, 13, 22,
            6, 11, 25,
            7, 18, 3,
            17, 19, 10])
        kTable : k_t = k_t([
            ruint32(0x428a2f98), ruint32(0x71374491), ruint32(0xb5c0fbcf), ruint32(0xe9b5dba5),
            ruint32(0x3956c25b), ruint32(0x59f111f1), ruint32(0x923f82a4), ruint32(0xab1c5ed5),
            ruint32(0xd807aa98), ruint32(0x12835b01), ruint32(0x243185be), ruint32(0x550c7dc3),
            ruint32(0x72be5d74), ruint32(0x80deb1fe), ruint32(0x9bdc06a7), ruint32(0xc19bf174),
            ruint32(0xe49b69c1), ruint32(0xefbe4786), ruint32(0x0fc19dc6), ruint32(0x240ca1cc),
            ruint32(0x2de92c6f), ruint32(0x4a7484aa), ruint32(0x5cb0a9dc), ruint32(0x76f988da),
            ruint32(0x983e5152), ruint32(0xa831c66d), ruint32(0xb00327c8), ruint32(0xbf597fc7),
            ruint32(0xc6e00bf3), ruint32(0xd5a79147), ruint32(0x06ca6351), ruint32(0x14292967),
            ruint32(0x27b70a85), ruint32(0x2e1b2138), ruint32(0x4d2c6dfc), ruint32(0x53380d13),
            ruint32(0x650a7354), ruint32(0x766a0abb), ruint32(0x81c2c92e), ruint32(0x92722c85),
            ruint32(0xa2bfe8a1), ruint32(0xa81a664b), ruint32(0xc24b8b70), ruint32(0xc76c51a3),
            ruint32(0xd192e819), ruint32(0xd6990624), ruint32(0xf40e3585), ruint32(0x106aa070),
            ruint32(0x19a4c116), ruint32(0x1e376c08), ruint32(0x2748774c), ruint32(0x34b0bcb5),
            ruint32(0x391c0cb3), ruint32(0x4ed8aa4a), ruint32(0x5b9cca4f), ruint32(0x682e6ff3),
            ruint32(0x748f82ee), ruint32(0x78a5636f), ruint32(0x84c87814), ruint32(0x8cc70208),
            ruint32(0x90befffa), ruint32(0xa4506ceb), ruint32(0xbef9a3f7), ruint32(0xc67178f2)])
    else:
        blockSize = 128
        block_t = bytes_t(blockSize)
        lenSize = 16
        len_t = uint128_t
        to_len = uint128
        len_to_bytes = bytes.from_uint128_be
        word_t = uint64_t
        to_word = uint64
        bytes_to_words : FunctionType = bytes.to_uint64s_be
        words_to_bytes : FunctionType = bytes.from_uint64s_be
        kSize : int = 80
        k_t = array_t(word_t,kSize)
        opTableType_t = array_t(int,12)
        opTable = opTableType_t([
            28, 34, 39,
            14, 18, 41,
            1,   8,  7,
            19, 61,  6])
        kTable = k_t([
            uint64(0x428a2f98d728ae22), uint64(0x7137449123ef65cd), uint64(0xb5c0fbcfec4d3b2f), uint64(0xe9b5dba58189dbbc),
            uint64(0x3956c25bf348b538), uint64(0x59f111f1b605d019), uint64(0x923f82a4af194f9b), uint64(0xab1c5ed5da6d8118),
            uint64(0xd807aa98a3030242), uint64(0x12835b0145706fbe), uint64(0x243185be4ee4b28c), uint64(0x550c7dc3d5ffb4e2),
            uint64(0x72be5d74f27b896f), uint64(0x80deb1fe3b1696b1), uint64(0x9bdc06a725c71235), uint64(0xc19bf174cf692694),
            uint64(0xe49b69c19ef14ad2), uint64(0xefbe4786384f25e3), uint64(0x0fc19dc68b8cd5b5), uint64(0x240ca1cc77ac9c65),
            uint64(0x2de92c6f592b0275), uint64(0x4a7484aa6ea6e483), uint64(0x5cb0a9dcbd41fbd4), uint64(0x76f988da831153b5),
            uint64(0x983e5152ee66dfab), uint64(0xa831c66d2db43210), uint64(0xb00327c898fb213f), uint64(0xbf597fc7beef0ee4),
            uint64(0xc6e00bf33da88fc2), uint64(0xd5a79147930aa725), uint64(0x06ca6351e003826f), uint64(0x142929670a0e6e70),
            uint64(0x27b70a8546d22ffc), uint64(0x2e1b21385c26c926), uint64(0x4d2c6dfc5ac42aed), uint64(0x53380d139d95b3df),
            uint64(0x650a73548baf63de), uint64(0x766a0abb3c77b2a8), uint64(0x81c2c92e47edaee6), uint64(0x92722c851482353b),
            uint64(0xa2bfe8a14cf10364), uint64(0xa81a664bbc423001), uint64(0xc24b8b70d0f89791), uint64(0xc76c51a30654be30),
            uint64(0xd192e819d6ef5218), uint64(0xd69906245565a910), uint64(0xf40e35855771202a), uint64(0x106aa07032bbd1b8),
            uint64(0x19a4c116b8d2d0c8), uint64(0x1e376c085141ab53), uint64(0x2748774cdf8eeb99), uint64(0x34b0bcb5e19b48a8),
            uint64(0x391c0cb3c5c95a63), uint64(0x4ed8aa4ae3418acb), uint64(0x5b9cca4f7763e373), uint64(0x682e6ff3d6b2b8a3),
            uint64(0x748f82ee5defb2fc), uint64(0x78a5636f43172f60), uint64(0x84c87814a1f0ab72), uint64(0x8cc702081a6439ec),
            uint64(0x90befffa23631e28), uint64(0xa4506cebde82bde9), uint64(0xbef9a3f7b2c67915), uint64(0xc67178f2e372532b),
            uint64(0xca273eceea26619c), uint64(0xd186b8c721c0c207), uint64(0xeada7dd6cde0eb1e), uint64(0xf57d4f7fee6ed178),
            uint64(0x06f067aa72176fba), uint64(0x0a637dc5a2c898a6), uint64(0x113f9804bef90dae), uint64(0x1b710b35131c471b),
            uint64(0x28db77f523047d84), uint64(0x32caab7b40c72493), uint64(0x3c9ebe0a15c9bebc), uint64(0x431d67c49c100d4c),
            uint64(0x4cc5d4becb3e42b6), uint64(0x597f299cfc657e2a), uint64(0x5fcb6fab3ad6faec), uint64(0x6c44198c4a475817)])

    hashSize : int = v // 8
    hash_t = array_t(word_t,8)
    digest_t = bytes_t(hashSize)
    h0_t = bytes_t(8)
    h0: h0_t = array.create(8,to_word(0))
    if v == 224:
        h0 = hash_t([
            ruint32(0xc1059ed8), ruint32(0x367cd507), ruint32(0x3070dd17), ruint32(0xf70e5939),
            ruint32(0xffc00b31), ruint32(0x68581511), ruint32(0x64f98fa7), ruint32(0xbefa4fa4)])
    elif v == 256:
        h0 = hash_t([
            ruint32(0x6a09e667), ruint32(0xbb67ae85), ruint32(0x3c6ef372), ruint32(0xa54ff53a),
            ruint32(0x510e527f), ruint32(0x9b05688c), ruint32(0x1f83d9ab), ruint32(0x5be0cd19)])
    elif v == 384:
        h0 = hash_t([
            uint64(0xcbbb9d5dc1059ed8), uint64(0x629a292a367cd507), uint64(0x9159015a3070dd17), uint64(0x152fecd8f70e5939),
            uint64(0x67332667ffc00b31), uint64(0x8eb44a8768581511), uint64(0xdb0c2e0d64f98fa7), uint64(0x47b5481dbefa4fa4)])
    else:
        h0 = hash_t([
            uint64(0x6a09e667f3bcc908), uint64(0xbb67ae8584caa73b), uint64(0x3c6ef372fe94f82b), uint64(0xa54ff53a5f1d36f1),
            uint64(0x510e527fade682d1), uint64(0x9b05688c2b3e6c1f), uint64(0x1f83d9abfb41bd6b), uint64(0x5be0cd19137e2179)])

    # Initialization complete: SHA-2 spec begins

    @typechecked
    def ch(x:word_t,y:word_t,z:word_t) -> word_t:
        return (x & y) ^ ((~ x) & z)

    @typechecked
    def maj(x:word_t,y:word_t,z:word_t) -> word_t:
        return (x & y) ^ ((x & z) ^ (y & z))

    @typechecked
    def sigma(x:word_t,i:i_range_t,op:op_range_t) -> word_t:
        tmp : uintn_t
        if op == 0:
            tmp = x >> opTable[3*i+2]
        else:
            tmp = ruint32.rotate_right(x,opTable[3*i+2])
        return (ruint32.rotate_right(x,opTable[3*i]) ^
                ruint32.rotate_right(x,opTable[3*i+1]) ^
                tmp)

    @typechecked
    def schedule(block:block_t) -> k_t:
        b : bytes_t = bytes_to_words(block)
        s = array.create(kSize,to_word(0))
        for i in range(kSize):
            if i < 16:
                s[i] = b[i]
            else:
                t16 : word_t = s[i-16]
                t15 : word_t = s[i-15]
                t7  : word_t = s[i-7]
                t2  : word_t = s[i-2]
                s1  : word_t = sigma(t2,3,0)
                s0  : word_t = sigma(t15,2,0)
                s[i] = s1 + t7 + s0 + t16
        return s

    @typechecked
    def shuffle(ws:k_t,hashi:hash_t) -> hash_t:
        h = array.copy(hashi)
        for i in range(kSize):
            a0 : word_t = h[0]
            b0 : word_t = h[1]
            c0 : word_t = h[2]
            d0 : word_t = h[3]
            e0 : word_t = h[4]
            f0 : word_t = h[5]
            g0 : word_t = h[6]
            h0 : word_t = h[7]

            t1 : word_t = h0 + sigma(e0,1,1) + ch(e0,f0,g0) + kTable[i] + ws[i]
            t2 : word_t = sigma(a0,0,1) + maj(a0,b0,c0)

            h[0] = t1 + t2
            h[1] = a0
            h[2] = b0
            h[3] = c0
            h[4] = d0 + t1
            h[5] = e0
            h[6] = f0
            h[7] = g0
        return h

    @typechecked
    def compress(block:block_t,hIn:hash_t) -> hash_t:
        s : k_t = schedule(block)
        h : hash_t = shuffle(s,hIn)
        for i in range(8):
            h[i] += hIn[i]
        return h

    @typechecked
    def truncate(b:bytes_t(v)) -> digest_t:
        result = array.create(hashSize, ruint8(0))
        for i in range(hashSize):
            result[i] = b[i]
        return digest_t((result))

    @typechecked
    def hash(msg:vlbytes_t) -> digest_t:
        blocks : array(block_t)
        last : block_t
        blocks,last = array.split_blocks(msg, blockSize)
        nblocks : int = array.length(blocks)
        h:hash_t = h0
        for i in range(nblocks):
            h = compress(blocks[i],h)
        last_len : int = array.length(last)
        len_bits : int = array.length(msg) * 8
        pad = array.create(2*blockSize,ruint8(0))
        pad[0:last_len] = last
        pad[last_len] = ruint8(0x80)
        if last_len < blockSize - lenSize:
            pad[blockSize-lenSize:blockSize] = len_to_bytes(to_len(len_bits))
            h = compress(pad[0:blockSize],h)
        else:
            pad[(2*blockSize)-lenSize:2*blockSize] = len_to_bytes(to_len(len_bits))
            h = compress(pad[0:blockSize],h)
            h = compress(pad[blockSize:2*blockSize],h)
        result : bytes_t = words_to_bytes(h)
        return truncate(result)
    return hash

# Specific instances of SHA-2

sha224 : FunctionType = sha2(224)
sha256 : FunctionType = sha2(256)
# sha384 : FunctionType = sha2(384)
# sha512 : FunctionType = sha2(512)
