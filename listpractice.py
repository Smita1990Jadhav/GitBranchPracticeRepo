class food():


# init method or constructor
    def __init__(me, fruit, color):
       me.fruit = fruit
       me.color = color


    def show(me):
        print("fruit is", me.fruit)


        print("color is", me.color)

apple = food("apple", "red")
grapes = food("grapes", "green")

apple.show()
grapes.show()
