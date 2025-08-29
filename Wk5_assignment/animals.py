class carnivores:
    def feed(self):
        return ["lion", "tiger", "cheetah"]
class herbivores:
    def feed(self):
        return ["deer", "elephant", "giraffe"]
for animal in [carnivores(), herbivores()]:
    print(animal.feed())
    
    
