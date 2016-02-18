def my_logger(*to_include):
    def outer(func):
        def inner(*args, **kwargs):
            module_name = func.__module__
            kwargs_values = {}
            args_values = list(args)
            if len(args) > 0 and str(args[0])[1:].startswith(func.__module__):
                module_name = str(args[0])[1:].split(" ")[0]
                args_values = list(args[1:])
            for kw in kwargs.keys():
                if len(to_include) > 0 and kw in to_include[0]:
                    kwargs_values[kw] = kwargs[kw]
            print "Executing: "+module_name+"."+func.__name__
            print "Arguments: %s, %s" % (args_values, kwargs_values)
            return func(*args, **kwargs)
        return inner
    return outer