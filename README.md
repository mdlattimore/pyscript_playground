# PyScript Playground  

This is a collection of scripts written using the recently released PyScript framework, which allows Python code to be executed locally, entirely within the browser. These scripts are in various stages of development (translation: Some might work. Some might not). If you're interested, the PyScript repository can be found <a href="https://github.com/pyscript">here</a>

### [Mortgage Calculator](https://mdlattimore.github.io/pyscript_playground/mortgage_calc)  
> Calculates monthly principal and interest payments on a fully amortized mortgage loan. You can optionally add annual property tax and insurance cost to calculate and total monthly payment  
   
### [Dog Reference](https://mdlattimore.github.io/pyscript_playground/dogs)  
> Search for a dog breed to access basic information. Information is taken from api at <a href="https://thedogapi.com">The Dog API</a>  
    
### [Simple Encryption](https://mdlattimore.github.io/pyscript_playground/encrypt)  
> Takes user text input then encrypts using a Fernet cipher (It displays both the key and the encrypted text. DO NOT use for any real-world application). The encryption is handled by the third part 'cryptography' library, available at <a href="https://pypi.org">Pypi.org</a>. The code demonstrates PyScript's ability to use third party libraries using PyScript's \<env\> tag. NOTE: not all third party libraries work with PyScript. Generally speaking, third party party libraries are those that have been compiled to run with Pyodide. A list of compatible libraries can be found <a href="https://github.com/pyodide/pyodide/tree/main/packages">here</a>  

### [Simple Hash Function](https://mdlattimore.github.io/pyscript_playground/hashing)  
> Uses Python's hashlib module (in the standard library) to generate a sha-256 hash for user-supplied input.  
  
### [Temperature Converter](https://mdlattimore.github.io/pyscript_playground/temp_converter)  
> Simple fahrenheit to celsius converter

### [Ron Swanson Quotes](https://mdlattimore.github.io/pyscript_playground/swanson)
> For fans of Parks and Recreation, this is a page that accesses an searchable API containing quotes from that loveable Director of Parks and Recreation in Pawnee, Indiana, Ron Swanson

### [Code Timer](https://mdlattimore.github.io/pyscript_playground/timing)
> This page runs two essentially equivalent functions, one written in JavaScript, the other in Python (and executed using the PyScript framework). The code times how long it takes each function to execute, allowing you to see the spped difference between a JS function and Python function run in a browser.
 
