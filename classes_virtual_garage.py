print('welcome to your virtual garage')

#options = [mirrors,locks,seats1,seats2,remote,camera,bluetooth,cruise,keyless,assist,lojack,allwheel]
optionsdetail = ['power mirrors, ', 'power locks, ', 'power seats, ', 'heated seats, ', 'remote start, ', 'backup camera, ', 'bluetooth, ', 'cruise control, ', 'keyless start, ', 'driver assists, ', 'lojack, ', 'drivetrain(AWD,4WD,FWD,RWD)']
optionsdetailstring= ""
optionsdetailstring=optionsdetailstring.join(optionsdetail)
#(power mirrors, power locks, power seats, heated seats, remote start, backup camera, bluetooth, cruise control, keyless start, 
#driver assists, lojack, drivetrain) parent class list options attribute

class Vehicle():
	'''garage parent class'''
	def __init__(self,make,model,color,fueltype,options):
		self.make = make
		self.model = model
		self.color = color
		self.fueltype = fueltype

		self.options = options


	def getmake(self):
		return self.make

	def getmodel(self):
		return self.model

	def getcolor(self):
		return self.color

	def getfueltype(self):
		return self.fueltype

	def getoptions(self):
		return self.options

	






class Car(Vehicle):
	'''child class for cars'''
	def __init__(self,make,model,color,fueltype,options,enginesize,numdoors):
		Vehicle.__init__(make,model,color,fueltype,options)
		self.enginesize = enginesize
		self.numdoors = numdoors

	def getenginesize(self):
		return self.enginesize

	def getnumdoors(self):
		return self.numdoors


class Pickup(Vehicle):
	'''child class for pickups'''
	def __init__(self,make,model,color,fueltype,options,cabstyle,bedlength):
		Vehicle.__init__(make,model,color,fueltype,options)
		self.cabstyle = cabstyle
		self.bedlength = bedlength

	def getcabstyle(self):
		return self.cabstyle

	def getbedlength(self):
		return self.bedlength






#show the options list (print attributes/options)
print("Remark these are the options availabe in app\n" + optionsdetailstring)

#function for building car

def createcar():
	title= input('choose a title for your car\n')
	make= input("Let's begin with building your car. \nwhat is the make?\n")
	model = input("model?\n")
	color= input("color?\n")
	fuel= input("type of fuel?\n")
	eng= input("size of engine?\n")
	doors= input("how many doors?\n")
	opts= str(input("and any of the applicable options \nseparated by a comma then a space\n" + optionsdetailstring+"\n"))
	car= Car(make, model, color, fuel, opts, eng, doors)
	return car

#function for building truck
def createpickup():
	title= input('choose a title for your truck\n')
	make= input("Let's begin with building your pickup. \nwhat is the make?\n")
	model = input("model?\n")
	color= input("color?\n")
	fuel= input("type of fuel?\n")
	cab= input ("style of cabin?\n")
	bed= input ("how long is the bed?\n")
	opts = input("and any of the applicable options \nseparated by a comma then a space\n" + optionsdetailstring+"\n")
	pickup = Pickup(make,model,color,fuel,opts,cab,bed)
	return pickup










#prompt user to create object of a car for first choice
print('first we create your car')
createcar()

#prompt user to create object of a pickup for second choice
print('secondly we create your truck')
createpickup()

#prompt user to create more objects if they wish to make more choices (loop) (car, pickup, or finished)
choice = 3
while choice>0:
	choice =int(input('choose 1 for another car,choose 2 for another truck, choose 0 if finished\n'))
	if choice ==1:
		createcar()
	elif choice == 2:
		createpickup()
	pass

print('you have finished your garage')

#finish inputs


def showcase():
	pass
#display agarage
