
# % Default params 
# % Default params have to be the last params the and can be followed by default params only 

def open_acct(an, hn, bal = 10000):
    print(an, hn, bal)
    
## Variadic parameter (var-args or rest arguments)
## * represents that there can be any number of arguments, the name args can be changed, it's a convention 
def add(*args):
    sum = 0
    for value in args:
        sum+=value
    return sum

print(add(7,8,9))

#^ Named parameters 
def drawClirlce(start_x, start_y, width, height, pixel_width, rgb_color):
    print(f"start_x {start_x}, start_y {start_y}, width {width}, height {height}, pixel_width {pixel_width}, rgb_color {rgb_color}")

#^ It would be nice to have named parameters 
drawClirlce(rgb_color=0b111111, start_x=10, start_y=10, width =40, height=40, pixel_width=2)

def args_kwdsFn(*args, **kwargs):
    print(args, kwargs)

def kwdsFn(**kwds):
    for param in kwds.keys():
        print(param)

kwdsFn(start_x=1, height=2, start_y=3, width=4)