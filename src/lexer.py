from sly import Lexer


class YaailLexer(Lexer):
    tokens = {
        ID, NUMBER, STR,
        LABEL, GLOBAL, LOCAL,
        DEFINE, RET, STORE, BR, SWITCH,
        ALLOCA, LOAD, CALL, GEP, ICMP, EXTRACTVALUE, INSERTVALUE,
        VOID_TYPE, LABEL_TYPE, INT_TYPE, INT_TYPE_PTR, TYPE, ARRAY_TYPE,
        ADD, SUB, MUL, UDIV, SDIV, UREM, SREM, SHL, LSHR, ASHR, AND, OR, XOR, NEG,
        EQ, NE, UGT, UGE, ULT, ULE, SGT, SGE, SLT, SLE
    }
    
    literals = { '(', ')', '{', '}', ',', '=' }
    
    LABEL = r'[a-zA-Z0-9_]:'
    GLOBAL = r'@[-a-zA-Z$._0-9]*'
    LOCAL = r'%[-a-zA-Z$._0-9]*'
    
    
    INT_TYPE_PTR = r'i[0-9]*\*'
    INT_TYPE = r'i[0-9]*'
    ARRAY_TYPE = r'\[[0-9]* x [%[-a-zA-Z$._0-9]*@[-a-zA-Z$._0-9]*i[0-9]*i[0-9]*]\*\]'
    
    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t
    
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    
    ID['define'] = DEFINE
    ID['ret'] = RET
    ID['store'] = STORE
    ID['br'] = BR
    ID['switch'] = SWITCH

    ID['alloca'] = ALLOCA
    ID['load'] = LOAD
    ID['call'] = CALL
    ID['getelementptr'] = GEP
    ID['icmp'] = ICMP
    ID['extractvalue'] = EXTRACTVALUE
    ID['insertvalue'] = INSERTVALUE

    ID['void'] = VOID_TYPE
    ID['type'] = TYPE
    
    ID['add'] = ADD
    ID['sub'] = SUB
    ID['mul'] = MUL
    ID['udiv'] = UDIV
    ID['sdiv'] = SDIV
    
    ignore = ' \t'
    ignore_comment = r';.*'
    
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')
    
    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1

