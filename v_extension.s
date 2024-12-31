.global _start
_start:
    addi sp, sp, -64
    sd ra, 56(sp)
    sd s0, 48(sp)
    la a0, data
    li a1, 10
    vsetvli zero, a0, ta, ma, mf8
    vadd.d v1, v2, v6
    vadd.d v7, v1, v6
    vadd.d v3, v5, v7
    vadd.d v3, v2, v4
    vadd.d v5, v2, v1
    vadd.d v7, v2, v1
    vadd.d v6, v2, v6
    vadd.d v3, v7, v4
    vadd.d v6, v3, v5
    vadd.d v2, v2, v7
    vadd.d v7, v3, v7
    vadd.d v3, v4, v3
    vadd.d v1, v6, v3
    vadd.d v5, v3, v6
    vadd.d v4, v5, v1
    vadd.d v2, v5, v2
    vadd.d v1, v1, v6
    vadd.d v1, v5, v7
    vadd.d v3, v5, v4
    vadd.d v1, v6, v6
    ld ra, 56(sp)
    ld s0, 48(sp)
    addi sp, sp, 64
    li a7, 93
    li a0, 0
    ecall
.data
.align 8
data: .double 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0

.global main
main:
    j _start