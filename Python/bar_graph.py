import matplotlib.pyplot as pyplot
labels = ("Java", "Python", "C", "Scala")
sizes = (2, 1, 4, 3)
index= [30, 45, 10, 15]

pyplot.bar(index, sizes, tick_label = labels)

pyplot.ylabel("Usage")
pyplot.xlabel("Programming language")

pyplot.show()
