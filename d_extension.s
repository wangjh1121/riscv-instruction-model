.global _start
_start:
    addi sp, sp, -64
    sd ra, 56(sp)
    sd s0, 48(sp)
    la a0, data
    li a1, 10
    fld fa1, 0(a0)
    fld fa2, 8(a0)
    fld fa3, 16(a0)
    fld fa4, 24(a0)
    fld fa5, 32(a0)
    fld fa6, 40(a0)
    fld fa7, 48(a0)
    fcvt.d.wu f7, x2
    fmadd.d f2, f1, f5, f2
    fle.d x3, f1, f4
    fmv.x.d x7, f7
    fcvt.d.s f4, f5
    fmul.d f7, f1, f3
    fmin.d f6, f2, f6
    fcvt.s.d f1, f2
    fnmadd.d f6, f5, f3, f3
    fmv.x.d x6, f7
    fsub.d f6, f4, f7
    fclass.d x4, f5
    fnmadd.d f7, f1, f7, f6
    fsgnjn.d f7, f7, f5
    fmv.d.x f5, x7
    fsgnjn.d f5, f6, f5
    fsub.d f4, f4, f7
    fsgnj.d f1, f7, f5
    fsgnj.d f3, f1, f4
    fmv.x.d x1, f5
    fsd fa1, 0(a0)
    fsd fa2, 8(a0)
    fsd fa3, 16(a0)
    fsd fa4, 24(a0)
    fsd fa5, 32(a0)
    fsd fa6, 40(a0)
    fsd fa7, 48(a0)
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