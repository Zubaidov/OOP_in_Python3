# OOP_in_Python3

## Introductuion
[+] Object Oriented Programming (OOP) allows programmers to create their own objects that have methods and attributes.
[+] Recall that after defining a string, list, dictionary, or other objects, you were able to call methods off of them with the .method_name() syntax.
[+] These methods act as functions that use information about the object, as well as the object itself to return results, or change the current object.

[+] For example this includes appending to a list, or counting the occurences of an element in a tuple

[+] For much larger scripts of the Python code, functions by themselves aren't enough for organization and repeatability.

[+] Commonly repeated tasks and objects can be defined with OOP to create code that is more usable.

## PyPi

[+] PupI is a repository is a repository for open-source third-party Python packages.
[+] It's similar to RubyGems in the Ruby world, PHP's Packagist, CPAN for Perl, and NPM for Node.js
[+] All important libraries mantioned in requirements.txt (pip list shaw > requirements.txt)

## Writing your own Modules and Packages

[+] Modules are any.py scripts that we call in another .py script.
[+] Packages are a collection of modules.

## __name__ & __main__

[+] An often confusing part of the Python is a mysterious line of code. [ if __name__ == "__main__"]
[+] Sometimes when you are importing from a module, you would like to know whether a modules function is being used as an import, or if you are using the original .py file of that module.


## Errors and Exceptions

[+] Errors are bound to happen in our code!
[+] Especially when someone else ends up using it in an unexpected way.
[+] We can use error handling to attempt to plan for possible errors.
[+] We use three keywords for the exceptions:
        [+] try: this is a block of code to be attempted(may lead to an error)
        [+] except: Block of code will execute in case there is an error in try block
        [+] finally: A final block of code to be executed, regardless of an error.

## Unit Testing

