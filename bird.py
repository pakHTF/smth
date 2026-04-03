class Bird:
    def __init__(self, bird_name):
        self.bird_name = bird_name

    def fly(self, destination=None):
        if destination!=None:
            print(f'{self.bird_name} летит в {destination}')
        else:
            print(f'{self.bird_name} летит в неизвестном направлении')
