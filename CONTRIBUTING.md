# How to contribute

Some helpful tips for getting pull requests merged:

* Have one logical change per pull request. For example, don't also
    change the meaning or content while correcting spelling.

    It is difficult to merge only part of a pull request, so if they do
    too much, they might not be merged.

* There are tests which run automatically when a pull request is
    created. These tests ensure that the documentation will build and that
    the parameters list is valid (against a schema).
    
    Pull requests which cause these tests to fail will not be merged
    until the breaking chnage is fixed.

* Have a meaningful commit message. 
* Ask for help if you need it.
* Do make issues.


## The parameters.json file

The file `meta/parameters.json` contains the master list of parameters
for the CCHDO. On the TODO list is documenting the format of this file,
there is a schema which is used to validate the `parameters.json` file:
`meta/parameters.schema.json`.

It is very important to note that the list of parameter names is
ordered. So when submitting pull requests for new parameters make sure
to put it in the array at a location that makes sense. For most new
parameters, this means occuring near the end of the list, or at least
after the carbon parameters.
