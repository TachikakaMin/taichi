import operator as ops

import numpy as np
import pytest

import taichi as ti
from tests import test_utils


@test_utils.test()
def test_bit_shl():
    @ti.kernel
    def shl(a: ti.i32, b: ti.i32) -> ti.i32:
        return a << b

    @ti.kernel
    def shl_assign(a: ti.i32, b: ti.i32) -> ti.i32:
        c = a
        c <<= b
        return c

    for i in range(8):
        assert shl(3, i) == shl_assign(3, i) == 3 * 2**i


@test_utils.test()
def test_bit_sar():
    @ti.kernel
    def sar(a: ti.i32, b: ti.i32) -> ti.i32:
        return a >> b

    @ti.kernel
    def sar_assign(a: ti.i32, b: ti.i32) -> ti.i32:
        c = a
        c >>= b
        return c

    n = 8
    test_num = 2**n
    neg_test_num = -test_num
    for i in range(n):
        assert sar(test_num, i) == sar_assign(test_num, i) == 2**(n - i)
    # for negative number
    for i in range(n):
        assert sar(neg_test_num, i) == sar_assign(neg_test_num,
                                                  i) == -2**(n - i)


@test_utils.test()
def test_bit_shr():
    @ti.kernel
    def shr(a: ti.i32, b: ti.i32) -> ti.i32:
        return ti.bit_shr(a, b)

    n = 8
    test_num = 2**n
    neg_test_num = -test_num
    for i in range(n):
        assert shr(test_num, i) == 2**(n - i)
    for i in range(n):
        offset = 0x100000000 if i > 0 else 0
        assert shr(neg_test_num, i) == (neg_test_num + offset) >> i


@test_utils.test()
def test_bit_shr_uint():
    @ti.kernel
    def func(x: ti.u32, y: ti.i32) -> ti.u32:
        return ti.bit_shr(x, y)

    assert (func(5, 2) == 1)
