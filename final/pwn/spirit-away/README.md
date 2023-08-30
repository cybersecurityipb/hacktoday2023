# Spirit Away

## Desc

```
remember when zafin said : hacktoday{soalnya_dibikin_dadakan_karena_ada_probset_yang_buat_soal_tapi_gaada_solvernya_muehehehe___ZafiN}, well here's the chall now ENJOY!
```

## Bug

```
use-after-free leak         --> leak heap, leak libc (house of spirit)
use-after-free edit         --> reverse gray code and libc random
return-oriented-programming --> seccomp open read write
```

## Solver

```
- reverse gray code
- leak heap
- leak libc
- leak stack
- write rop payload to writteable addr
- stack pivot (pop rsp gadget)
```

## Service

`nc <ip> 17010`

## Flag
`hacktoday{If_I_die_tomorrow_I'd_be_all_right_Because_I_believe_That_after_we're_gone_The_SPIRIT_carries_LIBC_on_~Dr34m_Th3ATh3r}`