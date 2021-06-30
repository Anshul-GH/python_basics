Hello and welcome to the section on Attributes and Methods. In the previous section you learn what are

Classes and Objects and you briefly looked at what are Attributes and Methods.

And in this section you will be learning about the different types of attributes which are class attributes and instance attributes.

And in this section you will be learning about the different types of attributes which are class attributes and instance attributes.

And then you will learn the different types of methods which are static methods and instance methods.

And then you will learn how to fully initialize an object by making use of the special method in Python

called the 'init' method. And you will also learn in detail about the self parameter which we had seen in the previous section.

called the 'init' method. And you will also learn in detail about the self parameter which we had seen in the previous section.

So let's start with the first lecture which is on class attributes and instance attributes.

Let's get started by opening Python's IDLE environment.








So what are class attributes and instance attributes ? Class attributes are attributes that are common to all the instances of your class.

Which means for every object of the class which you create the value of a class attribute will remain the same.

Now in the previous example in the section of classes and objects, we created an Employee class and created two objects for the class.

But both the objects had the same name of an employee.

That's because what we made use of in those examples was a class attribute.

Now what should go into a class attribute ? Your class attribute should contain data which is common to all the instances of your class and a name of an employee is definitely not something which should be

a class attribute. Your class attribute could be something like the number of working hours which could be common to all the employees in your company.


So let's create a class called Employee and then a class attribute called numberOfWorkingHours and assign it with the value 40.

So let's create a class called Employee and then a class attribute called numberOfWorkingHours and assign it with the value 40.

So now let's create two objects for this class. Let's say employeeOne and then another object called employeeTwo

So now let's create two objects for this class. Let's say employeeOne and then another object called employeeTwo

So now both your employeeOne and employeeTwo should have access to the class attribute numberOfWorkingHours and that should return the value of 40.

So now both your employeeOne and employeeTwo should have access to the class attribute numberOfWorkingHours and that should return the value of 40.

Let's see if it works as expected.

So employeeOne does have the value of 40 and similarly employeeTwo will have the value 40 as well.

Yes it does!

Now what if you wanted to change this class attribute ?

What if you wanted to change the numberOfWorkingHours to say 45 ?

In that case, you need to make use of the name of your class and then access the class attribute.

So the name of the class here is Employee and then use a dot operator and then the name of your class attribute which is numberOfWorkingHours and change the value to 45.

So the name of the class here is Employee and then use a dot operator and then the name of your class attribute which is numberOfWorkingHours and change the value to 45.

Now if you try to access employeeOne.numberOfWorkingHours, that should return the value of 45.

Yes it does.

And similarly, employeeTwo will return 45 as well.

So now that you have understood what is a class attribute, let's next take a look at what an instance attribute is. Now a class attribute is common to all the instances of your class while an instance attribute is specific to each instance of your class.

So now that you have understood what is a class attribute, let's next take a look at what an instance attribute is. Now a class attribute is common to all the instances of your class while an instance attribute is specific to each instance of your class.

So now that you have understood what is a class attribute, let's next take a look at what an instance attribute is. Now a class attribute is common to all the instances of your class while an instance attribute is specific to each instance of your class.

For example, the name of each employee could be different.

So let's see how to create an instance attribute. To create an instance attribute, you will make use of the name of your object.

So let's see how to create an instance attribute. To create an instance attribute, you will make use of the name of your object,

Let's say we're trying to create a name for our employeeOne and then give a name for your instance attribute

after a dot operator. Let's say the name of our instance attribute is 'name' and let's assign the name John to our first employee.

after a dot operator. Let's say the name of our instance attribute is 'name' and let's assign the name John to our first employee.

Now when you try to access employeeOne.name, that will return the value John.

Now let's see what happens if you try to access employeeTwo. name. Now on accessing employeeTwo.name, you have an attribute error,

Now let's see what happens if you try to access employeeTwo. name. Now on accessing employeeTwo.name, you have an attribute error,

That says Employee object has no attribute name.

That's because you created an attribute for your employeeOne, but not the name attribute for an employeeTwo

That's because you created an attribute for your employeeOne, but not the name attribute for an employeeTwo

So if you wanted to create a name attribute for employeeTwo, you should be doing it similar to how you

did for your employeeOne. So that would be employeeTwo.name = Mary

did for your employeeOne. So that would be employeeTwo.name = Mary

So now when you try to access employeeTwo.name, that should return Mary.

So now though both the name of the attribute is same, the value that is being held are different.

That's because both of these are instance attributes, which are specific to that particular object.

Now what if you tried to change the name of your class attribute by making use of the name of your object ?

Which means, instead of changing the value as Employee.numberOfWorkingHours, you'll try to do something like employeeOne.numberOfWorkingHours and modify the value

Which means, instead of changing the value as Employee.numberOfWorkingHours, you'll try to do something like employeeOne.numberOfWorkingHours and modify the value

Which means, instead of changing the value as Employee.numberOfWorkingHours, you'll try to do something like employeeOne.numberOfWorkingHours and modify the value

Let's see what would happen then.

So I'm trying to do employeeOne.numberOfWorkingHours.

Let's say I'm trying to reduce the numberOfWorkingHours to 40.

So now if I print employeeOne.numberOfWorkingHours, that does return 40.

So what you have done is reduce the number of working hours to 40.

No let's see if the same has been reflected on your employeeTwo as well since you want your class attribute to be reflected across all the instances of your class.

No let's see if the same has been reflected on your employeeTwo as well since you want your class attribute to be reflected across all the instances of your class.

No it did not.

The value is still 45 for your employeeTwo.

So what happened in this particular statement here was, you did not actually change the value of your

class attribute numberOfWorkingHours, when you used the name of your object along with the numberOfWorkingHours,

class attribute numberOfWorkingHours, when you used the name of your object along with the numberOfWorkingHours,

What you just did here was to create another instance attribute called numberOfWorkingHours with the value 40.

What you just did here was to create another instance attribute called numberOfWorkingHours with the value 40.

So how Python accesses the attributes is, now for an object when you provide the name of an attribute,

it first goes and checks if there is an instance attribute with that name.

Now in case of employeeOne, you created an instance attribute with the name numberOfWorkingHours and assigned it with the value 40

Now in case of employeeOne, you created an instance attribute with the name numberOfWorkingHours and assigned it with the value 40

So when you said employeeOne.numberOfWorkingHours, on checking for an instance attribute,

it found that attribute and printed the value 40. Now for employeeTwo, it first checked if there is an instance attribute with the name numberOfWorkingHours. Now on checking it did not find any instance attribute with

it found that attribute and printed the value 40. Now for employeeTwo, it first checked if there is an instance attribute with the name numberOfWorkingHours. Now on checking it did not find any instance attribute with

the name numberOfWorkingHours.

And then it goes and checks if there is any class attribute by name numberOfWorkingHours and on checking for it, it finds a class attribute with the name numberOfWorkingHours with the value 45 and it prints that value.

And then it goes and checks if there is any class attribute by name numberOfWorkingHours and on checking for it, it finds a class attribute with the name numberOfWorkingHours with the value 45 and it prints that value.

And then it goes and checks if there is any class attribute by name numberOfWorkingHours and on checking for it, it finds a class attribute with the name numberOfWorkingHours with the value 45 and it prints that value.

So if you try to access something like employeeOne.age, what will happen is, it first checks

if an instance attribute called age is present, which returns false and then it checks if a class attribute called age is present, which returns false

if an instance attribute called age is present, which returns false and then it checks if a class attribute called age is present, which returns false

And then it throws an error that says Employee object has no attribute age.

Now that you have an understanding of what are the class attributes and instance attributes,

Let's move on to our next lecture in which we will be talking about what is a self parameter.

I'll see you there.

