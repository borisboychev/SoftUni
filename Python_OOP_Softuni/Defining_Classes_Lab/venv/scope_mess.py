
#before
# x = 'global'
#
# def outer():
#     x =  'local'
#
#     def inner():
#         x = 'nonlocal'
#         print('inner: ', x)
#
#     def chnage_global():
#         x = 'global: changed!'
#
#     print('outer: ', x)
#     inner()
#     print('outer: ', x)
#     chnage_global()
#
# print(x)
# outer()
# print(x)

#after
x = 'global'

def outer():
    x =  'local'

    def inner():
        nonlocal x
        x = 'nonlocal'
        print('inner:', x)

    def chnage_global():
        global x
        x = 'global: changed!'

    print('outer:', x)
    inner()
    print('outer:', x)
    chnage_global()

print(x)
outer()
print(x)