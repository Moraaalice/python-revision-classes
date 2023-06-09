#You are a music composer known for creating music that adapts to the listener's emotions and surroundings. 
#You want to develop a software system that analyzes the listener's mood and environment to predict the type of music 
#that would best suit their current state. Think about the classes you'll need to model the music compositions and how 
#to predict the appropriate music based on mood and environment.
class Music:
    def __init__(self,emotions,surroundings):
        self.emotions = emotions
        self.surroundings = surroundings
        
        
    def predict_song(self):
        emotion = "Sad"
        surrounding = "Chilly"
        if self.emotions == emotion and self.surroundings==surrounding:
            return f"Compose sad songs in a {self.surroundings} environment"
        else:
            return f"Compose happy songs in {self.surroundings} environment"
        

