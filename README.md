# python-sep-2022
Python exercises on topics covered in Sanjay Vyas's Deep python course in Sep-2022
 Attended Deep python workshop by Sanjay Vyas Sir, here are my notes from the session :

----------- Day 1 -------------------

Python: 

Memory MAnagement 

Interpreter

JIT Compiler 

Garbage collector 

Variable declared are not global or local they are both 

Each Function call creates its own Stack frame 

Each stack frame has its own dictionary 

Checking the type (static programming ) and not checking in Type (dynamic programming)

Better comments configuration: 

"better-comments.tags": [ 

        {

            "tag": "!",

            "color": "#FF2020",

        },

        {

            "tag": "~!",

            "color": "#FFFFFF",

            "backgroundColor": "#FF2020",

        },

        {

            "tag": "_",

            "color": "#FF2020",

            "underline": true

        },

        {

            "tag": "-",

            "color": "#FF2D00",

            "strikethrough": true,

        },

        {

            "tag": "^",

            "color": "#CD607E",

        },

        {

            "tag": "~^",

            "color": "#FFFFFF",

            "backgroundColor": "#CD607E",

        },

        {

            "tag": "?",

            "color": "#0096FF",

        },

        {

            "tag": "~?",

            "color": "#FFFFFF",

            "backgroundColor": "#0096FF",

        },

        {

            "color": "#75757",

            "tag": "//",

        },

        {

            "color": "#FF8C00",

            "tag": "%",

        },

        {

            "tag": "~%",

            "color": "#FFFFFF",

            "backgroundColor": "#FF8C00",

        },

        {

            "tag": "*",

            "color": "#66FF66",

        },

        {

            "tag": "~*",

            "color": "#FFFFFF",

            "backgroundColor": "#29AB87",

        },

        {

            "tag": "#",

            "color": "#FFFF00",

        },

        {

            "tag": "~#",

            "color": "#000000",

            "backgroundColor": "#FFFF00",

        },

        {

            "tag": ">",

            "color": "#00FFFF",

        },

        {

            "tag": "~>",

            "color": "#000000",

            "backgroundColor": "#00FFFF",

        }

----------- Day 2 -------------------

Language have a pattern 

	- Type System -- Static or Dynamic both of them have type system 

	- Operators -- + = >

	- Control Flow -- Conditional, Loops, Switch 

	- Function -- Abiliti to write a function

	- Object Oriented -- Class

	- Functional -- f(x)-> x * x

Principles of Object Oriented 

There are no native types in pure OOP language, even Integer is a class 

Native data types are single unit 

Objects are supposed to be opaque 

SmallTalk has classes but no public private 

pharo.org for building classes in SmallTalk 

Communication happens through messages 

Objects are supposed to be composite 

C++, Java, C# are hybrid OOP language 

One can define classes but there are also Native types, so one can creat object and can create variables 

Public, Private and Protected 

Even in Python everything is an object 

Communication happens through message passing AT RUNTIME 

Objects are not OPAQUE in case of Python 

Types in Python 

- bool

- int 

- float

- complex

- string 

- list 

- tuple 

Python has no native types but instead we call them as Basic Datatypes as they are classes 

Control Flow 

Alter the sequence of program 

No code blocks but indentation which defines the scope of the code 

For python the control flow is mainly : 

- if, 

- for, 

- while 

: does the job of establishing code block 

; is a python separator which is used to write multiple lines of code in same line 

id() can be used to determine the equivalence of the objects in terms of both being the same object 

----------- Day 3 -------------------

Expressions are assigned and consumed, also they emit a value which can be consumed by someone  

1

a=1 

b = a = 1

Statements are actions and not values 

if a == 1: 

	pass 

for a in range(0, 11):

	pass 

if you one tries to asign statement to expression the there is an error

which says  "Expresssion expected to the right of ="

Pascal Case : first letter of english word is capitalized 

Camel Case: first charater of english word is lower case 

Snake Case: english word followed bu underscore  - def day_of_week (Used by Python)

Kebab Case: english word followd by the hyphen (-) --> webkit-toolkit- (Used in HTML classes and in CSS)

while can be paired with else to identify if the loop completed 

while a < b: 

	# conditions 

	if a == b : break # If break happens then the else part does not kick in, 

					  #	while having continue still executes the else part and contiues the loop too. 

else: 

	# this is done only if the loop was not broken 

----------- Day 4 -------------------

__init__ is called once the object is created 

first parameter of __init__ is self which points to current object, it can be named as anything self is just a variable name. 

Same class can be written as part of the class 

Monkey patching --> Insert a function inside an obejct at run time, 

def hello():

	print("hello")

p.hello = hello

p.hello()

q = Person()

q.bye()

q.hello()

Every thing in a class is a dictionary, assigning a function to a variable 

is nothing but assigning a funtion body to the key. 

Key can be a name while value can be function body or anything 

Can Monkey patching be done at Class Level ? 

Answer is yes the it can be done using the setattr(ClassName, "Method_name", method_definition)

print(locals()) --> This print locals 

----------- Day 5 -------------------

mypy is a tool which is used to check the types statically in Python 

mypy will flag the monkey patching as errors but the code will still run 

python3 -m pip install mypy

mypy filename --> is the command which can run a static type checking 

When we create a class python creates a PyClass object 

When deriving a class the first parameter of class definition is super which is base class : 

class SavingsAccount(Account)

Class which is the owner of the field should initiaize the field 

super() is a function in python which refers to the base class, it can be used refer the constructor of base class :

super().__init__(self, base class init params )

----------- Day 6 -------------------

simple array in python is not a contiguous location of memory 

Internally its a type of linked list, with one node pointing to another 

in the latest version of python there is a Array class which has contiguous memory 

Different methods attached to the list

Python can create mixed type list like [1, "Guido", True, 1], but python is strongly typed because it will not 

allow to add 2 different types but C can do it by implicitly conerting the data. 

import array from array # creates a contiguous memory array 

Lists are less performant than array, hence new version explicitly introduced array 

Map operations --> Hash Tables --> Dictionary 



----------- Day 7 -------------------

Constructor chaining 

The logic to update a field should be present in the class which owns the class 

super().withdraw() --> to call the base class method

Memory management in Python 

C, Pascal, C++ --> Manual Memory Management 

Python uses --> Reference Counting, when one adds reference to an object the refCount += 1 

Every time a new reference is pointed to same object the ref count is incremented by 1 

Also known as Automatic Reference Counting (ARC)

For every object Python holds its own reference hence the ref count starts at 1 

Python has RefCount GC and Generational GC 

Mark-Sweep-Compact GC used by Java, C#, 



----------- Day 8 -------------------

string.format library: https://docs.python.org/3/library/string.html

print("name [{0:^20s}] {1:o}").format(name, 14) --> first positional parameter center it in 20 charaacter and print it as a string

specifying f in front of a string in python makes it as a format string which we specified above 

__str__ is the same as toString in C# 

implementing __str__ for a class will help in printing the method 

there is another method repr(object) --> Representation of the object

which also calls the __repr__ which should present the representation of the object 

repr shows how the object was created --> Something similar to reflection 

Operators are te reak workhorses of programming

+, ==, > , < are the examples of operators 

to overload the operator == use the dunder method __eq__ 

operator overloading 

> maps to __gt__

< maps to __lt__

!= maps to __ne__

>= maps to __ge__

<= maps to __le__

Defining the __eq__ and __gt__ will also cater to implementing the __lt__

it will do a not of the greater than 

+ maps to __add__ (Add)

+= maps to __iadd__ (Plus equal to)

- maps to __sub__ (Subtract)

-= maps to __isub__ (Minus equal to)



----------- Day 9 -------------------

built-in data structures in python 

list - modification (insert, remove)

set (unique)

dictionary key:value pairs, unique keys 

tuple - readonly quick record, tuple requires a comma to be considered as a tuple 

otherwise with single it will be considered as the type of the element, read only quick record

ternary operator --> Condition ? when-true: when-false 

                 --> when-true Condition else when-false

return label if label is not None else "Unknown" 

Python dictionaries are always ordered since Python 3.8 

Default params have to be the last params the and can be followed by default params only 

Variadic parameter (var-args or rest arguments) use * represents that there can be any number of arguments, 

the name args can be changed, it's a convention 



----------- Day 10 -------------------

Decorator is an function which will call your function, it takes the function as a param to which it is applied

It must return a function to which it is called 

When you pass a parameter to decorator it becomes decorator factory and the decorator function is indented one level more 

Inbuilt decorators like 

	@staticmethod to mark methods as static method 

	@property 

		 @balance.setter --> Property setter 

 Generators yield out the transactions 
