Hello and welcome to this lecture. In the previous lecture you learnt what are class attributes and instance attributes,

Hello and welcome to this lecture. In the previous lecture you learnt what are class attributes and instance attributes,

And in this lecture you will be learning what is a self parameter and the reason why we use it.

And in this lecture you will be learning what is a self parameter and the reason why we use it.


And then what we will be doing in this program is to create a method for a class and initially without

the self parameter and then we will execute it and see what happens,

and then we will understand the reason why we need to go for the self parameter.

So let's create a class called Employee and then let's have a method to initialize the details of the employee.

So let's create a class called Employee and then let's have a method to initialize the details of the employee.

So let me create a method called employeeDetails() and initially I'm not going to pass the self parameter

Let's see what happens when we execute it

For now I'm not initializing anything.

Let me just give a pass statement which means to say that do nothing.

So no what we will do is to create an object for this class.

So let me just call my object as employee with the 'e' in lower case to differentiate it from that of my class.

So let me just call my object as employee with the 'e' in lower case to differentiate it from that of my class.

And next what I will do is use this object to call the method employeeDetails()

Now let's save this program and execute it to see what happens.

So let's save it and to execute it, if you're on Mac or Linux you could use Terminal and if you're on

Windows, you should be using command prompt. And enter Python 3 space

The path to your filename and if you are on Windows remember to use py instead of Python 3.

Now my file is in Desktop/self.py. Now on executing it,

We have an error that says TypeError employeeDetails(), which is the name of our method takes zero positional arguments but one was given.

We have an error that says TypeError employeeDetails(), which is the name of our method takes zero positional arguments but one was given.

Now here we might think that hey something is wrong with Python.

I never passed any parameters at the time of calling my function.

It's empty.

But then Python says that I have passed a parameter.

So what's wrong ?

In order to understand what's happening, you should know how this method call is being handled by Python.

Now though you are calling the method this way, the Python interpreter converts it into this -

It uses the name of your class which is Employee.employeeDetails()

and then it passes the name of your object, which os employee.

So that's the reason that Python was giving you an error stating that you had passed one argument whereas you have not received it in a function call.

So that's the reason that Python was giving you an error stating that you had passed one argument whereas you have not received it in a function call.

So this is the shorthand notation for this function call.

Now both are valid statements but this is a more commonly used style when it comes to a function call.

Now both are valid statements but this is a more commonly used style when it comes to a function call.

So now let's go back to our method and make few changes.

So now that we are passing a parameter, which is the object, let's receive it in the first place.

So the first parameter which we receive will be the object and by convention this parameter is called 'self'.

So the first parameter which we receive will be the object and by convention this parameter is called 'self'.

No it need not be self.

You are free to choose any name of your choice but by convention it happens to be self.

Because someone else if they're reading your code or if you're reading someone else's code when you

look at this parameter called self, you will understand that it is referring to the object itself.

Now in our method let's give a name for our employee.

So let's create an instance attribute called name.

And how do we create an instance attribute ? By using your objectName.attributeName.

And how do we create an instance attribute ? By using your objectName.attributeName.

So in this method the name of our object is self which is the object employee contained in the parameter self

and then enter a dot followed by the name of your instance attribute which is name and assign a value.

and then enter a dot followed by the name of your instance attribute which is name and assign a value.

Let me just call it Matthew.

You know let's print and find out if it works as expected.

So let me try.

If name is being printed as Matthew.

So let's save it now and go back to our terminal and execute it. Now on executing you see that

this time the program worked without any mistakes and you also see that it is being printed twice.

The reason is because both these calls are valid function calls and this is the more commonly used function call so let's just get rid of this.

The reason is because both these calls are valid function calls and this is the more commonly used function call so let's just get rid of this.

This was just to show you how internally Python makes this function call.

So now that you have understood the reason to go for the self you might want to try and find out what

happens if you try to create an attribute without using the self parameter.

So let's experiment that out.

So if you're creating a parameter, let's say you are creating the age for your employee and let's say he is 30 years old.

So if you're creating a parameter, let's say you are creating the age for your employee and let's say he is 30 years old.

Now let's print and check if it works as expected.

So, "Age= ",age

No let's save it and go back to our terminal and execute it to see what the output will be.

The output is 30 which means you did not have any error.

So now you might ask me.

I got the output without using the self parameter,

Then why should I be using a self parameter ?

No when you create an instance attribute your objective is for that particular attribute to be available throughout the lifespan of your object.

No when you create an instance attribute your objective is for that particular attribute to be available throughout the lifespan of your object.

Now what do I mean by the lifespan of an object ?

It is the time the object is being created until the time it is being destroyed. An object destruction can happen when the program terminates.

It is the time the object is being created until the time it is being destroyed. An object destruction can happen when the program terminates.

Or you manually choose to delete your object.

So now if you want to check if your age attribute is available as long as your object is alive,

it should be accessible in other methods of your object as well.

Let's see if it works as expected.

Now let's say we have another method, let's call it printEmployeeDetails()

And here what we will do is print name and age.

So let me first differentiate it from the other method.

Let's just give a plain statement that says printing in another method and now what we will do is,

print the name and age of the employee.

So when we print the name and remember that we use the self parameter for the name.

So that would be self.name

And then let's try printing the age of the employee.

So that would be just age since we created it without the self parameter.

And make a function call for it, which is employee.printEmployeeDetails()

Now let's save it and then go back to our terminal and execute it.

So now on execution you'll see that there is an error which is being thrown which means to say,

NameError: name 'age' is not defined in your function printEmployeeDetails()

So this means to say that this age attribute cannot be accessed within this printEmployeeDetails method.

That's because when you create an age attribute you never used the name of your object. In order to create an instance attribute,

That's because when you create an age attribute you never used the name of your object. In order to create an instance attribute,

You need to use the name of your object.

So since you did not use the name of an object the lifespan of this attribute is only within your method.

So once your method terminates this particular attribute cannot be used in any other methods.

So I hope you now have a strong understanding on how the self parameter works.

You might now have another confusion.

What if my method does not need a self parameter ?

What if I'm not using any of the instance attributes ?

What if I just want to give a print statement to the user ?

Well, the answer to that is to use a static method which will be dealt in the next lecture,

When we talk about instance methods and static methods.

So as a review for this class you have understood how to use the self parameter how the parameter is

actually being passed as the objectName.method call in which an object is being passed.

That's the reason that you use the self parameter and you also understood what would happen if you do

not use the self parameter along with the attribute, where the lifespan will be restricted within just that method.

not use the self parameter along with the attribute, where the lifespan will be restricted within just that method.

So I'll see you in the next lecture.

Thank you.