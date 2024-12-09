class Camera:
    def __init__(self,resolution):
        self.resolution=resolution
    def take_photo(self):
        print(f"Taking a photo with resolution:{self.resolution} MP")
class Phone:
    def __init__(self,phone_number):
        self.phone_number=phone_number
    def make_call(self):
        print(f"Making a call from {self.phone_number} number")
class SmartPhone(Camera,Phone):
    def __init__(self,brand,model,resolution,phone_number):
        Camera.__init__(self,resolution)
        Phone.__init__(self,phone_number)
        self.brand=brand
        self.model=model
    def display_device_info(self):
        print(f"Brand:{self.brand}\nModel:{self.model}\nResolution:{self.resolution}\nPhone Number:{self.phone_number}")
sp=SmartPhone("Samsung","F15",55,6387872189)
sp.display_device_info()

#2
class Student:
    def __init__(self,name,course):
        self.name=name
        self.course=course
    def student_info(self):
        print(f"Name:{self.name}\nCourse:{self.course}")
class StudentAthlete(Student):
    def __init__(self,name,course,sport):
        super().__init__(name,course)
        self.sport=sport
    def display_athlete_info(self):
        self.student_info()
        print(f"Sport:{self.sport}")
s=StudentAthlete("Dharshini","AI","Badminton")
s.display_athlete_info()

