# Yaaal

Yet Another Above Assembly Language

Yaaal is used both as a primitive programming language and an intermediate
representation for compiled languages. It is hardly inspired by LLVM's IR.

# Syntax
## Types
```
```

## Variables
### Types
```
void : void
label : label to branch to
i<n> : signed/unsigned integer of n bits
i<n>* : pointer to a signed/unsigned integer of n bits
ptr : pointer
[y x t] : array of y elements of the type t
type { <t0>, <t1> } : struct of elements of the type t0 and t1
```

### Global
```
@name = <type> (<value>)
```

Exemple:
```
@counter = i16 0
@hello = [13 x i8] "\0DHello, world"
```

### Local
```
%name = <type> (<value>)
%name2 = <return_value>
```

## Functions
```
define <ret_type> @name(<t0> %<arg>, <t1> %<arg2>) { ... }
```

### Return
```
define <ret_type> @name(<t0> %<arg>, <t1> %<arg2>) {
    ret <ret_type> <ret_val>
}
```

### Call
```
call <ret_type> @name(<t0> %<arg>, <t1> %<arg2>)
%ret_val = call <ret_type> @name(<t0> %<arg>, <t1> %<arg2>)
```

## Memory
### Alloca
Allocate space on the stack. Return a pointer to the reserved space
```
<result> = alloca <type>[, <ty> <NumElements>][, align <alignment>]
```

### Load
```
<result> = load <type>, ptr <pointer>[, align <alignment>]
```

### Store
```
store <type> <value>, ptr <pointer>[, align <alignment>]
```

### Extractvalue
https://llvm.org/docs/LangRef.html#extractvalue-instruction
```
<result> = extractvalue <aggregate type> <val>, <idx>{, <idx>}*
```

### Insertvalue
https://llvm.org/docs/LangRef.html#insertvalue-instruction
```
<result> = insertvalue <aggregate type> <val>, <ty> <elt>, <idx>{, <idx>}*
```

### Getelementptr
Get the pointer to an element starting from its base pointer and its index.
```
<result> = getelementptr <type>, ptr <pointer>{, <ty> <idx>}*
```

Example :
```
%struct = type { i16, i16 }
%struct_ptr = alloca [2 x %struct]  ; allocate space for 2 structs
; Get the second element of the first struct
%struct1_e2 = getelementptr %struct, ptr %struct_ptr, i8 0, i8 1
; [{ i16, i16 }, { i16, i16 }]
;          ^
```

Note that even when there is no array of struct, the index '0' is needed.

For more : https://llvm.org/docs/GetElementPtr.html

## Arithmetic
```
<result> = add <ty> <op1>, <op2>
<result> = sub <ty> <op1>, <op2>
<result> = mul <ty> <op1>, <op2>
<result> = udiv <ty> <op1>, <op2>
<result> = sdiv <ty> <op1>, <op2>
<result> = urem <ty> <op1>, <op2>
<result> = srem <ty> <op1>, <op2>
<result> = shl <ty> <op1>, <op2>
<result> = lshr <ty> <op1>, <op2>
<result> = ashr <ty> <op1>, <op2>
<result> = and <ty> <op1>, <op2>
<result> = or <ty> <op1>, <op2>
<result> = xor <ty> <op1>, <op2>
<result> = not <ty> <op1>, <op2>
<result> = neg <ty> <op>
```

## Control flow
### Comparison
Integer comparison. Return an i1 value.
```
<result> = icmp <cond> <type> <op1>, <op2>
```

#### Conditions
```
eq: equal
ne: not equal
ugt: unsigned greater than
uge: unsigned greater or equal
ult: unsigned less than
ule: unsigned less or equal
sgt: signed greater than
sge: signed greater or equal
slt: signed less than
sle: signed less or equal
```

### Branch
```
br i1 <cond>, label <iftrue>, label <iffalse>
br label <dest>
```

### Switch
```
switch <int_type> <value>, label <defaultdest> [ <int_ty> <val>, label <dest> ... ]
```


