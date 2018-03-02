
# A quick cheatsheet of error handling techniques.

"""
Common exceptions:

AssertionError - one of your asserts failed
ZeroDivisionError - you divided by zero
NameError - ex. local or global name/variable not found
TypeError - ex. using an int as a str
IOError - ex. problem reading a file
KeyboardInterrupt - ex. you end the program prematurely with an interrupt key
ImportError - ex. unable to load a module or function from module
ModuleNotFoundError - tried to load a module which can't be found
IndexError - ex. index is out of range
KeyError - ex. dictionary key not found in set of keys
MemoryError - operation runs out of memory
ValueError - built-in operation recieves argument of correct type but inappropriate value

"""



# a simple error catch
while True:
    try:
        l = [1,2,3]
        x = int(input("enter a number: "))
        assert x >= 0
        print(l[i]) 
        break
    except ValueError:
        print("not a valid number")
    except TypeError:
        print("not a valid type")
    except AssertionError:
        print("your assertion raised an error.. number is not greater than zero")
        print("auto-converting this to a positive integer")
        x = abs(int(x))
    except:
        print("danger, this will catch ANY and EVERY other possible error... not just the ones you expect")
    else:
        print("thanks! this code is executed IF there is no error")
    finally:
        print("this code always gets executed REGARDLESS of any errors")
        
        

# raising an error to pre-emptively terminate your code
if anumber < 0:
    raise RuntimeError("You can't use a negative number")
 else:
    print(math.sqrt(anumber))

    
# creating raising an exception
class MyException(Exception)
    pass
raise MyException("foo")
# gives >> "MyException: foo"

