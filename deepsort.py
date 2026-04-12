def deep_sorted(x:any) -> str:
    if type(x) == list:
        return sorted([deep_sorted(i) for i in x], key=str)
    elif type(x) == dict:
        return {k: deep_sorted(v) for k, v in sorted(x.items())}
    elif type(x) == set:
        return {deep_sorted(i) for i in x}
    elif type(x) == tuple:
        return tuple(sorted([deep_sorted(i) for i in x], key=str))
    else:
        if type(x) == str and x.isdigit():
            return int(x)
        return x


if __name__ == '__main__':
    # x=eval(input()) 
    # print(deep_sorted(x))
    import doctest
    print (doctest.testmod())
