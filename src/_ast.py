import re

class Variable():
    def __init__(self, name, type, scope, array = None):
        self.name = name
        self.type = type
        self.scope = scope
        self.array = array

    def __lenght__(self):
        match self.type:
            case r'i[0-9]*' | r'i[0-9]*\*':
                return int(re.find('[0-9]*', self.type))
            case "void":
                return 0
            case "label":
                return 16
            case self.array:
                repeat = len(self.array)

class Local(Variable):
    def eval(self):
        pass

class Global(Variable):
    def eval(self):
        pass

class Function():
    def __init__(self, name, type, arguments = None, expressions):
        self.name = name
        self.type = type
        self.arguments = arguments
        self.expressions = expressions
    
    def eval(self):
        print(f'Function {self.name} of type {self.type} with\
        {len(self.arguments)} arguments.')
        self.expressions.eval()

class Assignement():
    def __init__(self, variable, statement):
        self.variable = variable
        self.statement = statement
    
    def eval(self):
        print(f'Variable {self.variable} ', end='')
        self.statement.eval()

class Store():
    def __init__(self, type, value, dest_type, dest_value):
        self.type = type
        self.value = value
        self.dest_type = dest_type
        self.dest_value = dest_value
    
    def eval(self):
        print(f'Storing {self.value} of type {self.type} in {self.dest_value} of type {self.dest_type}')

class Ret():
    def __init__(self, type, value):
        self.type = type
        self.value = value

class Alloca():
    def __init__(self, type):
        self.type = type

class Load():
    def __init__(self, type, value, ptr):
        self.type = type
        self.value = value
        self.ptr = ptr


class IntType():
    def __init__(self, type):
        self.size = get_size(type)

class IntPtrType():
    def __init__(self, type):
        self.size = get_size(type)

class VoidType():
    def __init__(self):
        self.size = 0

class Number():
    def __init__(self, value):
        self.value = value
    
    def eval(self):
        return int(value)
