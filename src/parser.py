from sly import Parser
from lexer import YaailLexer
#from ._ast import Function, Assignement, Store, Ret, Alloca
import _ast as Ast

class YaailParser(Parser):
    tokens = YaailLexer.tokens

    #debugfile = 'parser.out'

    def __init__(self):
        self.variables = list()

    @_('declarations')
    def prog(self, p):
        return (p.declarations)
    
    @_('declaration declarations')
    def declarations(self, p):
        return (p.declaration, p.declarations)
    
    @_('declaration')
    def declarations(self, p):
        return p.declaration
    
    @_('expressions')
    def declaration(self, p):
        return p.expressions
    
    @_('expression expressions')
    def expressions(self, p):
        return (p.expression, p.expressions)
    
    @_('expression')
    def expressions(self, p):
        return p.expression
    
    @_('statements')
    def expression(self, p):
        return p.statements
    
    @_('statements statement')
    def statements(self, p):
        return (p.statements + p.statement)
    
    @_('statement')
    def statements(self, p):
        return p.statement
        

    @_('DEFINE type GLOBAL "(" arguments ")" "{" expressions "}"')
    def declaration(self, p):
        return Ast.Function(p.GLOBAL, p.type, p.arguments, p.expressions)
    
    @_('variable "=" statement')
    def expression(self, p):
        return Ast.Assignement(p.variable, p.statement)
    
    @_('STORE arguments')
    def expression(self, p):
        return Ast.Store(**p.arguments)
    
    @_('RET arguments')
    def expression(self, p):
        return (p.RET, p.arguments)
        

    @_('ALLOCA argument')
    def statement(self, p):
        return (p.ALLOCA, p.argument) 
    
    @_('LOAD arguments')
    def statement(self, p):
        return (p.LOAD, p.arguments)

    @_('CALL arguments')
    def statement(self, p):
        return (p.CALL, p.arguments)

    @_('GEP arguments')
    def statement(self, p):
        return (p.GEP, arguments)

    @_('ICMP arguments')
    def statement(self, p):
        return (p.ICMP, p.arguments)

    @_('EXTRACTVALUE arguments')
    def statement(self, p):
        return (p.EXTRACTVALUE, p.arguments)

    @_('INSERTVALUE arguments')
    def statement(self, p):
        return (p.INSERTVALUE, p.arguments)
        
    @_('argument "," arguments')
    def arguments(self, p):
        return (p.argument, p.arguments)
    
    @_('argument')
    def arguments(self, p):
        return p.argument
    
    @_('type variable')
    def argument(self, p):
        return (p.type, p.variable)
    
    @_('type literal')
    def argument(self, p):
        return (p.type, p.literal)

    @_('type')
    def argument(self, p):
        return (p.type)
    
    @_('')
    def argument(self, p):
        return None
        
    
    @_("VOID_TYPE")
    def type(self, p):
        return (p.VOID_TYPE)

    @_('LABEL_TYPE')
    def type(self, p):
        return (p.LABEL_TYPE)

    @_("INT_TYPE")
    def type(self, p):
        return (p.INT_TYPE)
    
    @_('INT_TYPE_PTR')
    def type(self, p):
        return (p.INT_TYPE_PTR)
    
    @_('TYPE')
    def type(self, p):
        return (p.TYPE)

    @_('ARRAY_TYPE')
    def type(self, p):
        return (p.TYPE)
        
    @_("LOCAL")
    def variable(self, p):
        self.variables.append(p.LOCAL)
        return (p.LOCAL)
    
    @_("GLOBAL")
    def variable(self, p):
        self.variables.append(p.GLOBAL)
        return (p.GLOBAL)
    
    @_('NUMBER')
    def literal(self, p):
        return (p.NUMBER)
    
    def error(self, p):
        raise ValueError(f"Parsing error at token {str(p)}")

