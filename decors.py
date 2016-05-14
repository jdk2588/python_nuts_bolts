def outside_method(fn):
    def _inside(name, amount, *args, **kwargs):
        print name
        amount += 100
        return fn(name, amount, amount=999, *args, **kwargs)
    return _inside

@outside_method
def func(name, salary, kw=None, amount=None):

    print amount, kw
    pass

func("Jaideep", 200000, kw='x')
