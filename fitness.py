#You are a fitness trainer creating personalized workout routines for your clients. You want to develop a software 
#system that analyzes the clients' fitness level, goals, and available equipment to predict and generate customized 
#workout plans. Think about the classes you'll need to model the clients, exercises, and how to predict the most effective 
#workout routines based on their goals and resources.
class WorkOutFitness:
    def __init__(self,fitness_level,goals,available_equipment):
        self.fitness_level = fitness_level
        self.goals = goals
        self.available_equipment = available_equipment
        
        
    def predict_workout_plan(self):
        weight = range(45,60)
        equipments = ["Tummy trimmer","Kettlebelle","Ankle writs","Tread Mill","Cable Machine"]
        if self.fitness_level > weight[0] and self.goals == "Reduce Weight" and self.available_equipment in equipments[0:]:
            return "Prcatise Strength training"
        elif self.fitness_level in weight and self.goals == "Maintain my weight" and self.available_equipment in equipments[0:]:
            return "Practise Cadiovascular exercise"
        if self.fitness_level < weight[0] and self.goals == "Increase Weight" and self.available_equipment in equipments[0:]:
            return "Practise full body work out"
        
        
           
            
            
