# PyScript Playground  

This is a collection of simple scripts written using the recently released PyScript framework which allows Python code to be executed locally, entirely within the browser. I am only slightly more knowledgeable than a beginner, so nothing in here is particularly complex (compared with the work of experienced developers, this is rank amateurism on display). However, the entire point of PyScript is to bring programming to the 99%. I'm one of that group. 

These scripts are in various stages of development (translation: Some might work. Some might not). If you're interested, the repo containing these scripts (and more detritus) can be found <a href="https://github.com/mdlattimore/pyscript_playground">here</a> and the PyScript repository can be found <a href="https://github.com/pyscript/pyscript">here.</a>

A quick note on design. These pages don't necessarily use best design practices (in fact, some of these are visual trainwrecks and none are particularly polished). For example, the CSS is generally contained in the ```<head>``` or occassionally inline rather than an external CSS file. My goal with these scripts is to create single file interactive pages with no local dependencies. The same can be said of the Python code which is, in all cases, sandwiched between ```py-script``` tags at the end of the ```body``` rather than external files. I could, and probably will at some point, move the CSS and maybe some oft-used PyScript functions to files hosted at some web location and link them with the HTML via their URL.

### [Mortgage Calculator](https://mdlattimore.github.io/pyscript_playground/mortgage_calc)  
> Calculates monthly principal and interest payments on a fully amortized mortgage loan. You can optionally add annual property tax and insurance cost to calculate and total monthly payment. This is second PyScript page I ever wrote (after the temperature converter). Nothing flashy, but it does the job. I've actually used it once or twice in the real world.  
   
### [Dog Reference](https://mdlattimore.github.io/pyscript_playground/dogs)  
> Search for a dog breed to access basic information. Information is taken from api at <a href="https://thedogapi.com">The Dog API.</a> I wrote this in order to practice/figure out how to work with an external web content. Ordinarily, one would use something like the ```requests``` library to interact with internet content using Python. However, for security reasons, browsers don't support the connection protocols used by these Python libraries. PyScript does provide a wrapper for JavaScript's ```fetch``` function (called, predicably PyFetch) that does allow the program to access internet content. This page was my first attempt at using that wrapper. 
    
### [Simple Encryption](https://mdlattimore.github.io/pyscript_playground/encrypt)  
> Takes user text input then encrypts it using a Fernet cipher (It displays both the key and the encrypted text. DO NOT use for any real-world application). The encryption is handled by the third party 'cryptography' library, available at <a href="https://pypi.org">Pypi.org</a>. The code demonstrates PyScript's ability to use third party libraries using PyScript's ```<env>``` tag. NOTE: not all third party libraries work with PyScript. Generally speaking, compatible third party libraries are those that have been compiled to run with Pyodide. A list of compatible libraries can be found <a href="https://github.com/pyodide/pyodide/tree/main/packages">here.</a>  

### [Simple Hash Function](https://mdlattimore.github.io/pyscript_playground/hashing)  
> Uses Python's hashlib module (in the standard library) to generate a sha-256 hash for user-supplied input.  
  
### [Temperature Converter](https://mdlattimore.github.io/pyscript_playground/temp_converter)  
> Simple fahrenheit to celsius converter. The first PyScript page I ever wrote.

### [Ron Swanson Quotes](https://mdlattimore.github.io/pyscript_playground/swanson)
> For fans of Parks and Recreation, this is a page that accesses a searchable API containing quotes from that loveable Director of Parks and Recreation in Pawnee, Indiana, Ron Swanson. As with the Dog Reference, this uses the PyFetch wrapper to access API content.

### [Code Timer](https://mdlattimore.github.io/pyscript_playground/timing)
> This demo runs two essentially equivalent functions, one written in JavaScript, the other in Python (executed using the PyScript framework). The code times how long it takes each function to execute, allowing you to see the speed difference between a JS function and Python function run in a browser. Predictably, JavaScript executes (this function, anyway) much faster than Python.

### [Rock Paper Scissors](https://mdlattimore.github.io/pyscript_playground/rps)
> This is a version of the classic Rock Paper Scissors game that nearly every novice programmer writes at some point. You click 'Rock', 'Paper', or 'Scissors' and the game begins. The computer's choice is randomly selected using Python's ```random``` module. This one currently presents some challenges. First, the ```pys-onClick``` action doesn't behave in the same way as its counterpart in JavaScript. When passing arguments to the function called by the ```pys-onClick```, the function fires on page load rather than onClick (which is how JavaScript behaves). There is currently a PR on GitHub proposing to change the behavior of ```pys-onClick``` so that it mirrors JavaScript's ```onClick```. In the mean time, we can stop the function from firing on page load by passing the argument to the function prefixed with ```functools.partial```. Also, to get the "Rock...Paper...Scissors...SHOOT" message to come up on the page one word at a time, we've have to use ```await asyncio.sleep(n)```. Python's ```time.sleep(n)``` doesn't give us the execution delay we need for the effect.
 
