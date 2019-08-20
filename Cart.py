from string import Template

class MyTemplate(Template):
    delimiter = "#"
    
def Main():
    cart = []
    cart.append(dict(item="Coke", price=8, qty=2))
    cart.append(dict(item="Cake", price=16, qty=1))
    cart.append(dict(item="Fish", price=32, qty=4))

    t= MyTemplate("#qty * #item = #price")
    total=0
    print("cart : ")

    for data in cart:
        print(t.substitute(data))
        total+= data["price"]
    print("Total : "+ str(total))

if __name__=='__main__':
    Main()
