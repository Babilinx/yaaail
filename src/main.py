from lexer import YaailLexer
from parser import YaailParser

if __name__ == '__main__':
    data = '''
define void @main() {
    %0 = alloca i16
    store i16 10, i16* %0
    %1 = load i16, i16* %0
    ret i16 0
}

define void @store_test(i16* %0) {
    store i16 10, i16* %0
}
'''
    lexer = YaailLexer()
    parser = YaailParser()
    
    toks = lexer.tokenize(data)
    for tok in toks:
        print(tok)
    
    #parser.parse(lexer.tokenize(data))
    
    print(parser.parse(lexer.tokenize(data)))
