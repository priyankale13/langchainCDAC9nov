import random

actors=['Amitabh Bachan','Amir Khan','Nana Patekar','Priyanka Chopra','Mindy Kalling','Dev Patel','Tom Cruise']
themes=['Scifi','Action','Adventure','Comedy','Drama','Fantasy','Horror','Romantic']
locations=['mumbai','pune','new delhi','new york','london','Hanapepe Valley','Matamata','Istanbul']

def actor_choice():
    return random.choice(actors)
   
def theme_choice():
    return random.choice(themes)
   
def location_choice():
    return random.choice(locations)
    

