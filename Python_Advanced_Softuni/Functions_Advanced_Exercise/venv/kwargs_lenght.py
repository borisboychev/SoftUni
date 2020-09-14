def kwargs_lenght(**kwargs):
    ll = []
    for i in kwargs:
        ll.append(i)

    return len(ll)

dictionary = {'name' : 'Peter' , 'age' : 25}
print(kwargs_lenght(**dictionary))