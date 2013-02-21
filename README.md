#Turing's Bicycle

This program attempts to model Alan Turing's bicycle as described in Neal Stephenson's [Cryptonomicon](https://en.wikipedia.org/wiki/Cryptonomicon). Turing's bicycle has a rear rim with a bent spoke and a chain with a weak link. When the bent spoke and weak link come in contact with each other the chain falls off. The user can input various information about the bicycle, which is then used to calculate how far the bicycle can travel before the chain falls off. Note the logic used, especially to detect states where the chain never falls off, may be faulty.

The program can be used through an interactive prompt or with command line arguments. 

###Interactive Prompt
When called without arguments the user will get an interactive prompt. Try it.

###Command Line Arguments
    python turings-bicycle.py [tire diameter][chain links][sprocket teeth][weak chain link location]
                              [optional - sprocket revolution limit - default 500]

For example 
`python turings-bicycle.py 650 101 20 1 1000`
would return
`The bike can be ridden 10.21 meters before the chain falls off.`

