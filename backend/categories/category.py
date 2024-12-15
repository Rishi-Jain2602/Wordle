import random

species = {
    "animal": ["Dog", "Cat", "Elephant", "Lion", "Tiger", "Cow", "Monkey", "Rabbit", "Horse"],

    "bird": ["Sparrow", "Pigeon", "Parrot", "Crow", "Peacock", "Duck", "Owl", "Eagle", "Penguin"],

    "flower": ["Rose", "Sunflower", "Lily", "Lotus", "Daisy", "Marigold", "Hibiscus", "Tulip"],

    "vehicle" : ["Car", "Bus", "Bicycle", "Train", "Aeroplane", "Boat", "Motorcycle", "Truck"],

    "fruit": ["Apple", "Banana", "Mango", "Orange", "Grapes", "Pineapple", "Watermelon", "Strawberry"],

    "vegetable": ["Potato", "Tomato", "Carrot", "Onion", "Spinach", "Cucumber", "Peas", "Broccoli"]
}

def random_species(category):
    category = category.lower()
    sp = species[category]
    return random.sample(sp,1)[0]
