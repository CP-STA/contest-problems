use std::fmt::Display;
use std::io;
use std::iter::{repeat, zip};
use std::{error::Error, vec::Vec};

use std::convert::TryInto;
use std::fmt;
use std::ops::{Add, Mul, Neg, Sub};
pub trait Modular {
    fn to_modulo(self, modulus: u32) -> Modulo;
    fn is_congruent(self, with: impl Into<i32>, modulus: u32) -> bool;
}
#[derive(Copy, Clone, Debug, PartialEq)]
pub struct Modulo {
    remainder: i32,
    modulus: u32,
}

impl Modulo {
    pub fn zero(modulus: u32) -> Modulo {
        Modulo {
            remainder: 0,
            modulus,
        }
    }

    pub fn one(modulus: u32) -> Modulo {
        Modulo {
            remainder: 1,
            modulus,
        }
    }

    pub fn remainder(self) -> i32 {
        self.remainder
    }

    pub fn modulus(self) -> u32 {
        self.modulus
    }
}

impl Modular for i32 {
    fn to_modulo(self, modulus: u32) -> Modulo {
        Modulo {
            remainder: self % modulus as i32,
            modulus,
        }
    }

    fn is_congruent(self, with: impl Into<i32>, modulus: u32) -> bool {
        (self - with.into()) % modulus as i32 == 0
    }
}

impl Add for Modulo {
    type Output = Self;

    fn add(self, rhs: Self) -> Self {
        if self.modulus() != rhs.modulus() {
            panic!("Addition is only valid for modulo numbers with the same dividend")
        }

        (self.remainder() + rhs.remainder()).to_modulo(self.modulus())
    }
}

impl Sub for Modulo {
    type Output = Self;

    fn sub(self, rhs: Self) -> Self {
        if self.modulus() != rhs.modulus() {
            panic!("Subtraction is only valid for modulo numbers with the same dividend")
        }

        if self.remainder() >= rhs.remainder() {
            modulo!(self.remainder() - rhs.remainder(), self.modulus())
        } else {
            modulo!(
                self.remainder() - rhs.remainder() + self.modulus() as i32,
                self.modulus()
            )
        }
    }
}

impl Mul for Modulo {
    type Output = Self;

    fn mul(self, rhs: Self) -> Self {
        if self.modulus() != rhs.modulus() {
            panic!("Multiplication is only valid for modulo numbers with the same dividend")
        }

        match self.remainder().checked_mul(rhs.remainder()) {
            Some(i) => i.to_modulo(self.modulus()),
            None => <i64 as TryInto<i32>>::try_into(
                self.remainder() as i64 * rhs.remainder() as i64
                    % <u32 as TryInto<i64>>::try_into(self.modulus()).unwrap(),
            )
            .unwrap()
            .to_modulo(self.modulus()),
        }
    }
}

impl Neg for Modulo {
    type Output = Self;

    fn neg(self) -> Self {
        Self {
            remainder: self.modulus as i32 - self.remainder,
            modulus: self.modulus,
        }
    }
}

/// Represents residue systems for an integer modulo n
pub struct Residue {
    residue: i32,
    modulus: u32,
}

impl From<Modulo> for Residue {
    fn from(modulo: Modulo) -> Self {
        Self {
            residue: modulo.remainder(),
            modulus: modulo.modulus(),
        }
    }
}

impl Iterator for Residue {
    type Item = i32;

    fn next(&mut self) -> Option<Self::Item> {
        self.residue += self.modulus as i32;

        Some(self.residue)
    }
}

impl fmt::Display for Modulo {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{:?} mod {:?}", self.remainder, self.modulus)
    }
}

#[macro_export]
macro_rules! modulo {
    ($rem:expr, $div:expr) => {
        $rem.to_modulo($div)
    };
}

#[cfg(test)]
mod axioms {
    use super::*;

    mod associative {
        use super::*;

        #[test]
        fn addition() {
            let mod_num_1 = modulo!(23, 45);
            let mod_num_2 = modulo!(12, 45);
            let mod_num_3 = modulo!(2, 45);

            assert_eq!(
                mod_num_1 + (mod_num_2 + mod_num_3),
                (mod_num_1 + mod_num_2) + mod_num_3,
            )
        }

        #[test]
        fn multiplication() {
            let mod_num_1 = modulo!(9, 128);
            let mod_num_2 = modulo!(14, 128);
            let mod_num_3 = modulo!(72, 128);

            assert_eq!(
                mod_num_1 * (mod_num_2 * mod_num_3),
                (mod_num_1 * mod_num_2) * mod_num_3,
            )
        }
    }

    mod commutative {
        use super::*;

        #[test]
        fn addition() {
            let mod_num_1 = modulo!(23, 45);
            let mod_num_2 = modulo!(12, 45);

            assert_eq!(mod_num_1 + mod_num_2, mod_num_2 + mod_num_1)
        }

        #[test]
        fn multiplication() {
            let mod_num_1 = modulo!(9, 77);
            let mod_num_2 = modulo!(14, 77);

            assert_eq!(mod_num_1 * mod_num_2, mod_num_2 * mod_num_1)
        }
    }

    mod identity {
        use super::*;

        #[test]
        fn additive() {
            assert_eq!(modulo!(23, 77) + Modulo::zero(77), modulo!(23, 77));
        }

        #[test]
        fn multiplicative() {
            assert_eq!(modulo!(128, 143) * Modulo::one(143), modulo!(128, 143));
        }
    }

    mod inverse {
        use super::*;

        #[test]
        fn additive() {
            let mod_num = 5.to_modulo(12);
            assert_eq!(mod_num + -mod_num, Modulo::zero(12));
        }
    }

    mod distributive {
        use super::*;

        #[test]
        fn multiplication_distributive_over_addition() {
            let mod_3 = 3.to_modulo(12);
            let mod_4 = 4.to_modulo(12);
            let mod_5 = 5.to_modulo(12);

            assert_eq!(mod_3 * (mod_4 + mod_5), (mod_3 * mod_4) + (mod_3 * mod_5))
        }
    }

    #[test]
    fn add_successfully() {
        assert!(modulo!(23, 4) + modulo!(11, 4) == modulo!(2, 4));
    }

    #[test]
    #[should_panic]
    fn add_panics_with_different_moduli() {
        assert!(modulo!(23, 5) + modulo!(11, 6) == modulo!(2, 5));
    }

    #[test]
    fn subtract_successfully() {
        assert!(modulo!(22, 4) - modulo!(13, 4) == modulo!(1, 4));
    }

    #[test]
    #[should_panic]
    fn subtract_panics_with_different_moduli() {
        assert!(modulo!(47, 43) - modulo!(5, 27) == modulo!(12, 13));
    }

    #[test]
    fn multiply_successfully() {
        assert!(modulo!(2, 4) * modulo!(19, 4) == modulo!(2, 4));
    }

    #[test]
    #[should_panic]
    fn multiply_panics_with_different_moduli() {
        assert!(modulo!(91, 92) - modulo!(8, 9) == modulo!(12, 47));
    }

    #[test]
    fn string_representation() {
        let mod_new = modulo!(6, 7u32);
        assert_eq!(format!("{}", mod_new), "6 mod 7");
    }

    #[test]
    fn no_overflow_positive() {
        let a = (i32::MAX - 1).to_modulo(i32::MAX.try_into().unwrap());
        let b = (i32::MAX - 2).to_modulo(i32::MAX.try_into().unwrap());
        assert_eq!((a * b).remainder(), 2);
    }

    #[test]
    fn no_overflow_negative() {
        let a = (-((1 << 30) + 1)).to_modulo(1 << 30);
        let b = ((1 << 30) + 2).to_modulo(1 << 30);
        assert_eq!((a * b).remainder(), -2);
    }
}

pub fn ispow2(a: u32) -> bool {
    return a != 0 && (a & (a - 1)) == 0;
}

pub fn ceilpow2(a: u32) -> u32 {
    return 1 << if ispow2(a) { 31 } else { 32 } - a.leading_zeros();
}

pub fn egcd(a: i32, b: i32) -> (i32, i32, i32) {
    if a == 0 {
        (b, 0, 0)
    } else {
        let (g, x, y) = egcd(b % a, a);
        (g, y - (b / a) * x, x)
    }
}

pub fn modinverse(a: i32, m: i32) -> Option<i32> {
    let (g, x, _) = egcd(a, m);
    if g != 1 {
        None
    } else {
        Some((x % m + m) % m)
    }
}

pub struct NFFT {
    pub r#mod: u32,
    pub root: u32,
    pub root_1: u32,
    pub root_pw: u32,
    pub i_2: u32,
}

#[derive(Debug)]
pub struct InvalidArgumentError(String);
impl Display for InvalidArgumentError {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "Argument is invalid, the reason is: {}", self.0)
    }
}

impl Error for InvalidArgumentError {}

impl NFFT {
    pub fn new(r#mod: u32, root: u32, root_1: u32, root_pw: u32) -> Self {
        NFFT {
            r#mod,
            root,
            root_1,
            root_pw,
            i_2: modinverse(2i32, TryInto::<i32>::try_into(r#mod).unwrap())
                .unwrap()
                .try_into()
                .unwrap(),
        }
    }
    pub fn nfft(
        &self,
        mut a: Vec<Modulo>,
        invert: bool,
    ) -> Result<Vec<Modulo>, InvalidArgumentError> {
        let i_2: i32 = self.i_2.try_into().unwrap();
        let i_2 = i_2.to_modulo(self.r#mod);
        let n = a.len();
        if !ispow2(n.try_into().unwrap()) {
            return Err(InvalidArgumentError(
                "The length of a has to be a power of 2".to_string(),
            ));
        }
        if n == 1 {
            return Ok(a);
        }

        let mut a0: Vec<Modulo> = Vec::new();
        let mut a1: Vec<Modulo> = Vec::new();
        a0.reserve_exact(n / 2);
        a1.reserve_exact(n / 2);
        for i in 0..n / 2 {
            a0.push(a[i * 2]);
            a1.push(a[i * 2 + 1]);
        }

        let y0 = self.nfft(a0, invert)?;
        let y1 = self.nfft(a1, invert)?;
        let wlen: i32 = (if invert { self.root_1 } else { self.root })
            .try_into()
            .unwrap();
        let mut wlen = wlen.to_modulo(self.r#mod);
        let mut i: u32 = n.try_into().unwrap();
        while i < self.root_pw {
            wlen = wlen * wlen;
            i <<= 1;
        }

        let mut w = 1i32.to_modulo(self.r#mod);
        for i in 0..n / 2 {
            a[i] = y0[i] + w * y1[i];
            a[n / 2 + i] = y0[i] - w * y1[i];
            if invert {
                a[i] = a[i] * i_2;
                a[n / 2 + i] = a[n / 2 + i] * i_2;
            }
            w = w * wlen;
        }
        let y = a;
        Ok(y)
    }

    pub fn make_polynomial_from_i32(&self, v: Vec<i32>) -> Vec<Modulo> {
        v.into_iter().map(|x| x.to_modulo(self.r#mod)).collect()
    }

    pub fn export_polynomial_to_i32(&self, v: Vec<Modulo>) -> Vec<i32> {
        v.into_iter().map(|x| x.remainder()).collect()
    }

    pub fn multiply_polynomials(
        &self,
        mut a: Vec<Modulo>,
        mut b: Vec<Modulo>,
    ) -> Result<Vec<Modulo>, InvalidArgumentError> {
        let n: usize = ceilpow2((a.len() + b.len()) as u32).try_into().unwrap();
        a.extend(repeat(0.to_modulo(self.r#mod)).take(n - a.len()));
        b.extend(repeat(0.to_modulo(self.r#mod)).take(n - b.len()));
        let a1 = self.nfft(a, false)?;
        let b1 = self.nfft(b, false)?;
        let p1: Vec<Modulo> = zip(a1.into_iter(), b1.into_iter())
            .map(|(x, y)| x * y)
            .collect();
        let p = self.nfft(p1, true)?;
        Ok(p)
    }

    pub fn pow2_polynomial(&self, mut a: Vec<Modulo>) -> Result<Vec<Modulo>, InvalidArgumentError> {
        let n: usize = ceilpow2((a.len() * 2) as u32).try_into().unwrap();
        a.extend(repeat(0.to_modulo(self.r#mod)).take(n - a.len()));
        let a1 = self.nfft(a, false)?;
        let p1: Vec<Modulo> = a1.into_iter().map(|x| x * x).collect();
        let p = self.nfft(p1, true)?;
        Ok(p)
    }

    pub fn pow_polynomial(
        &self,
        mut a: Vec<Modulo>,
        n: u32,
        k: usize,
    ) -> Result<Vec<Modulo>, InvalidArgumentError> {
        if n == 1 {
            a.resize(k, 0.to_modulo(self.r#mod));
            return Ok(a);
        }
        if n % 2 != 0 {
            let mut ans =
                self.multiply_polynomials(a.clone(), self.pow_polynomial(a, n - 1, k)?)?;
            ans.resize(k, 0.to_modulo(self.r#mod));
            Ok(ans)
        } else {
            let p = self.pow_polynomial(a, n / 2, k)?;
            let mut ans = self.pow2_polynomial(p)?;
            ans.resize(k, 0.to_modulo(self.r#mod));
            Ok(ans)
        }
    }
}

pub static DEFAULT_NFFT: NFFT = NFFT {
    r#mod: 7340033,
    root: 5,
    root_1: 4404020,
    root_pw: 1 << 20,
    i_2: 3670017,
};

pub fn nfft(a: Vec<Modulo>, invert: bool) -> Result<Vec<Modulo>, InvalidArgumentError> {
    DEFAULT_NFFT.nfft(a, invert)
}

pub fn make_polynomial_from_i32(v: Vec<i32>) -> Vec<Modulo> {
    DEFAULT_NFFT.make_polynomial_from_i32(v)
}

pub fn export_polynomial_to_i32(v: Vec<Modulo>) -> Vec<i32> {
    DEFAULT_NFFT.export_polynomial_to_i32(v)
}

pub fn multiply_polynomials(
    a: Vec<Modulo>,
    b: Vec<Modulo>,
) -> Result<Vec<Modulo>, InvalidArgumentError> {
    DEFAULT_NFFT.multiply_polynomials(a, b)
}

pub fn pow_polynomial(
    a: Vec<Modulo>,
    n: u32,
    k: usize,
) -> Result<Vec<Modulo>, InvalidArgumentError> {
    DEFAULT_NFFT.pow_polynomial(a, n, k)
}

fn main() {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer).unwrap();
    let argv: Vec<u32> = buffer
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    // let argv: Vec<u32> = args().skip(1).map(|x| x.parse().unwrap()).collect();
    let n = argv[0];
    let k = argv[1];
    let ans = pow_polynomial(make_polynomial_from_i32(vec![1; 6]), n, k as usize).unwrap();
    let ans = export_polynomial_to_i32(ans);
    let ans = ans.into_iter().map(|x| x.to_string()).into_iter();
    let ans: Vec<String> = ans.collect();
    let ans = ans.join(" ");
    println!("{}", ans);
}
