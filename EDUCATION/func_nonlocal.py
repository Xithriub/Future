def func_outer():
    x=2
    print('х равно',x)
    def func_inner():
        global x
        x=5
    func_inner()
    print('Локальное х сменилось на',x)
func_outer()

