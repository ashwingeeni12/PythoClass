def grader(name, grade):
    if grade >= 89.5:
      print(name + " got an A!")
    elif 89.5 > grade >= 79.5:
      print(name + " got an B!")
    elif 79.5 > grade >= 69.5:
      print(name + " got an C!")
    else:
      print(name + " failed :(")


#don't change anything below this
grader("Jack", 79.6)
grader("Bob", 88.3)
grader("Alice", 97.6)
grader("Mysha", 89.4)
grader("Arjeet", 95.8)
grader("Billy", 2.1)