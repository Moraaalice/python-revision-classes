#You are an architect designing smart homes that adapt to the occupants' preferences and needs. 
#You want to develop a software system that analyzes the occupants' behavior, preferences, and environmental 
#factors to predict and automate the adjustments of lighting, temperature, and other home features. Think about the 
#classes you'll need to model the home features, occupants, and how to predict the optimal settings based on their 
#behavior and environment.
class ArchitectDesign:
    def __init__(self,behaviour,prefences,environmental_factors):
        self.behaviour = behaviour
        self.prefences = prefences
        self.environmental_factors = environmental_factors
        
        
    def predict_lighting_and_temprature(self):
        if self.behaviour == "sleepy" and self.prefences == "relaxing" and self.environmental_factors == "darkness":
            return "Dim lighting and cold temprature"
        elif self.behaviour == "Active" and self.prefences == "Reading" and self.environmental_factors == "Calm":
            return "Soft lighting and normal temprature"
        else:
            return "Brighting and warm temprature"
        
        
        
            
        

