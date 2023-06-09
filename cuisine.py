#You are a chef specializing in fusion cuisine, and you've discovered that certain ingredients react differently 
# when combined based on the temperature and cooking time. You want to create a software system that predicts the 
# taste and texture of a dish based on the combination of ingredients, cooking temperature, and time. Think about 
# the classes you'll need to model the ingredients, cooking process, and how to predict the final result.
class FusionCuisine:
    def __init__(self,ingridients,cooking_temprature,cooking_time):
        self.ingridients = ingridients
        self.cooking_temprature = cooking_temprature
        self.cooking_time = cooking_time
        
        
    def predict_taste_texture(self):
        cooking_ingridients = ["Onions","Tomatoes","Baking Powder","Flour","Capsicum"]
        temp = [21,22,23,24,25]
        time = [15,16,17,18,19]
        if self.cooking_temprature<temp[0] and self.cooking_time<time[0] and self.ingridients in cooking_ingridients:
            return f"The food is rough because it used less {self.cooking_time} and a very low temprature of {self.cooking_temprature}"
        elif self.cooking_temprature in temp and self.cooking_time in time and self.ingridients in cooking_ingridients:
            return f"The food is smooth because it used the required {self.cooking_time} of time and the required temprature of {self.cooking_temprature}"
        elif self.cooking_temprature>temp[4] and self.cooking_time>time[4] and self.ingridients in cooking_ingridients:
            return f"The food is overcooked because of high temprature of{self.cooking_temprature}"