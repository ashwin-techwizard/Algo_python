#closer
def decorFun(msg):
    message=msg

    def display():
        print("display ",message)
    return display   


hey =decorFun("hi")
heyji =decorFun("ji")
heyji()

# decorrator

def decor(functionx):
    def wraper():
        print("Extra fun before "+functionx.__name__)
        return functionx()

    return wraper

def display():
    print("Display fun")

display= decor(display)
#or @decor 

display()


