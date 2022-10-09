import matplotlib.pyplot as pyplot
labels = ("Java", "Python", "C", "Scala")
sizes= (30, 45, 10, 15)
pyplot.pie(sizes, labels=labels, autopct = "%1.f%%", counterclock=False, startangle=105)
pyplot.show()