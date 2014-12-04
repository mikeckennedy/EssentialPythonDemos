[![Alt text](https://raw.githubusercontent.com/mikeckennedy/EssentialPythonDemos/master/supporting_files/dmlog.png)](https://develop.com)

Essential Python Demos
===========

Hi, I'm Michael Kennedy. Welcome to my demos repository for my 
[Essential Python Training Course](http://www.develop.com/training-course/essential-python-with-pyramid-sqlalchemy-nosql-and-core-language-features) 
from [DevelopMentor](https://develop.com). 

If you are in one of my courses *right now*, **start by selecting your course's branch** and then just click 'Download ZIP' or clone this repo to your system. On the other hand, if you took my course awhile ago and want access to the demos, your course has probably been **moved to another branch**. Use the branches dropdown to find it just contact me (email address is listed in my github profile).

If you are **not** in one of our courses, enjoy the samples and please consider DevelopMentor for your [Python Training](http://www.develop.com/training-courses/python)!

Cheers
[@mkennedy](https://twitter.com/mkennedy) - 
[http://blog.michaelckennedy.net/](http://blog.michaelckennedy.net/)

Course Outline
----------------------

The Python language has been emerging as a very powerful, flexible, and simple programming tool for building all manner of applications. Maybe you're one of the many developers looking get started with Python. If so, then this hands-on language course is just the thing for you.

You will start by installing Python and writing basic scripts. From there you'll move on to many of the language features needed in all applications. You will even dig into some of the advanced functionality such as OO Python, the Pyramid web framework, MongoDB, Data API, and more.

We round out the course by looking at unit testing, debugging, and multi-threaded parallel code in Python.

Module Outline
------------

**Day 1**

**Introduction to Python**

In this lesson, we will explore the history of Python and how it has changed over time (occasionally breaking backwards compatibility). We will see that Python is a platform that allows you to build all sorts of applications including web apps, GUI apps, and more. You will learn how to install and configure Python on both Windows and OS X. You will see some tips and tricks to using the interpreter as well as directly executing Python applications and scripts. We will discuss a variety of tools for working with Python from basic text editors to full blown IDEs including PyCharm, Visual Studio, Eclipse, Sublime Text and how to configure them. In short, you'll be ready to dig into specific Python topics after this lesson.

**Language basics**

Python is a unique language which values readability and productivity over terseness. In this lesson, you will get a quick introduction to the major language features. We start by examining the 'shape' of a Python application. Unlike many languages, whitespace is not just significant, but it defines blocks (or suites) of code. We will see how to define variables and understand Python's variable scope. Next up is a variety of flow control constructs (if, while, etc.). We will pay special attention to loops in Python, which unlike many languages omits any form of index-based loops (e.g. for loops in C). Finally we discuss how to import external modules and packages to extend our capabilities.

**Working with basic types and collections**

Python has a rich type system. This lesson explores some of the fundamental types and tips for working with them (numbers, strings, dates, etc.). Next we move on to the collection classes (lists, sets, dictionaries, etc.). These types have very powerful features and only some of them are covered in this lesson (saving the best for deeper examination later). You will learn to splice, combine, and generally manipulate these collections here.

**Functions**

Functions, along with classes, are key building blocks of any self-respecting language. Python's support for functions is very sophisticated. We start by defining basic functions and discussing parameters, return values, and related concepts. Unlike many languages, you will see that Python functions naturally support returning multiple return values and assigning them all in one step. You will see how to define functions with varying numbers of parameters. Finally we look at some of the best features of functions enabling modern, concise programming techniques: closures and lambdas in Python.

**Day 2**

**Classes**

Python is a first class object-oriented language. Many of the APIs are implemented as objects and all classes have a common base class just like languages such as Java and C#. You will see how to define your own classes and how to add methods and fields to them. We will discuss Python's special methods which are essentially Python's way to implement operator overloading and more. There are techniques to add data-hiding and encapsulation to your classes as well as single and multiple inheritance. We discuss how polymorphism is done in Python and it's clever use of duck-typing.

**Error handling**

Python has a solid try / catch error handling system. This lesson will explore catching and handling errors via exceptions. Throwing and signaling errors to calls when errors occur in our code. You will learn how to define your own exception types. Finally, we will use the with language keyword to ensure that we properly clean up resource intensive code blocks (e.g. file streams or open database connections)

**File I/O**

Working with files is fundamental to any programming language. Python has rich support for working with files including simple utility methods to load all data as well as more efficient streaming APIs. Beyond reading and writing text or bytes, we will explore intrinsic support for common file formats (JSON and XML) as well as object serialization via pickle. Finally, we look at two classes which provide access to files, directories, and more: os and sys.

**Iterator Zen**

Python has rich support for treating collections as data as well as using iterators as efficient data generators. The iterator zen lesson looks at all of these and more. We will begin by taking for in loops and class iterators apart. We will see there is a hard, manual way to support iteration. But Python also has generator methods, a very easy and efficient way to build iterators. After working with iterators, we will look at the more concise generator expressions and list comprehensions. Finally, we will take everything we've learned and use it to basically treat collections as in-memory databases.

**Day 3**

**Pythonic /Idiomatic Python**

To say that code is Pythonic is to say that it uses Python idioms well, that it is natural or shows fluency in the language, that it conforms with Python's minimalist philosophy and emphasis on readability. There are both tools and techniques which help you write more Pythonic code and we will cover them in this lesson. We start by looking at the recommended code styles and conventions. We will also cover the code analysis tool PyLint.

**Web applications in Python (Pyramid)**

There are several very popular and successful web frameworks in Python including Pyramid, Flask and Django. This course covers Pyramid for building web applications and services as we believe it offers greater flexibility to choose your building blocks (NoSQL vs. SQL databases, services, views, etc.) relative to Django. Pyramid is what is known as a micro web framework. It comes with "batteries included" but doesn't make any assumptions about the components of your site. Popular sites created with Pyramid include Dropbox, reddit, and digg.

**Database access via SQLAlchemy (ORM model)**

SQLAlchemy provides a world-class ORM (Object-Relational Mapper) which builds upon its general Core programming model. In this session we will see how to map objects and classes to tables. How to customize the tables with things like uniqueness constrains, default values, and relationships between classes. You will see how to express queries in terms of Python objects and classes as well as map classes to and from tables with ease using SQLAlchemy’s ORM.

**Day 4**

**Database access (NoSQL / MongoDB)**

Almost all applications depend on data in databases (either RDBMSes or NoSQL DBs). This lesson on accessing NoSQL databases from Python will show you not only how but why you want to work with NoSQL databases in Python. Because we want to have hands-on demonstrations of all techniques in this course, we will choose a specific NoSQL database to work with: MongoDB, the most popular NoSQL database. We start by giving you a brief introduction to NoSQL and MongoDB before quickly moving on to the MongoDB Python API: PyMongo. We will discuss object serialization, reading existing data, writing and updating data among other topics you will need to be successful with MongoDB from Python.

**Building redistributables (modules and packages)**

Python has several mechanisms of redistributing reusable libraries and classes and building and working with these is what this lesson is all about. You will learn the difference between modules and packages. We will be creating packages and export types from them using __init__.py. We will discuss when and how you can convert large modules into packages for maintainability. There are some simple steps to take to make your script both directly executable and usable via a module. Finally, we will cover deploying applications including topics such as py2exe, pre-compiled python .pyc files, and pyinstaller.

**Debugging and unit testing Python**

This lesson is all about building reliable code and tracking down any errors that may slip through. We start off discussing unit testing in Python using PyUnit and py.test. You will learn to assert conditional statements to verify correct behaviors as well as test for errors and exceptions. Then we will move on to debugging. First we will cover basic debugging with pdb, IDLE, and pudb. Then we will move on to debugging in the IDEs (PyCharm, Eclipse, Visual Studio).

