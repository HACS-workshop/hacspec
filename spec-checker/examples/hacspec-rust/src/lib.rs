
mod chacha20;

#[cfg(test)]
mod tests {
    use chacha20::*;

    #[test]
    fn quarter_round_test() {
        // Quarter round test vectors from RFC 7539
        let a: u32 = 0x11111111;
        let b: u32 = 0x01020304;
        let c: u32 = 0x9b8d6f43;
        let d: u32 = 0x01234567;
        let mut my_state = state{v: [0; 16]};
        my_state.v[0] = a;
        my_state.v[1] = b;
        my_state.v[2] = c;
        my_state.v[3] = d;
        let my_state = quarter_round(0, 1, 2, 3, my_state);
        let exp_state = [0xea2a92f4 as u32, 0xcb1cf8ce as u32,
                         0x4581472e as u32, 0x5881c4bb as u32];
        println!("computed qround = {:?}", my_state);
        println!("expected qround = {:?}", exp_state);
        for i in 0..4 {
            assert_eq!(my_state.v[i], exp_state[i]);
        }
    }

    #[test]
    fn chacha20_block_test() {
        // Test vector from RFX 7539 section 2.3.2
        let key = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09,
                   0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f, 0x10, 0x11, 0x12, 0x13,
                   0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1a, 0x1b, 0x1c, 0x1d,
                   0x1e, 0x1f];
        let nonce = [0x00, 0x00, 0x00, 0x09, 0x00, 0x00, 0x00, 0x4a, 0x00, 0x00,
                     0x00, 0x00];
        let counter = 1;
        let result = chacha20(&key, counter, &nonce);
        let expected_state = state{ v: [
            0xe4e7f110, 0x15593bd1, 0x1fdd0f50, 0xc47120a3,
            0xc7f4d1c7, 0x0368c033, 0x9aaa2204, 0x4e6cd4c3,
            0x466482d2, 0x09aa9f07, 0x05d7c214, 0xa2028bd9,
            0xd19c12b5, 0xb94e16de, 0xe883d0cb, 0x4e3c50a2
        ]};
        println!("expected state = {:?}", expected_state);
        println!("computed state = {:?}", result);
        for i in 0..16 {
            assert_eq!(result.v[i], expected_state.v[i]);
        }
    }
}
