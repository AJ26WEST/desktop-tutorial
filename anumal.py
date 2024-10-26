def animal_sound(animal):
    sounds = {
        'dog': 'bark',
        'cat': 'meow',
        'cow': 'moo',
        'sheep': 'baa',
        'duck': 'quack',
        'lion': 'roar',
        'frog': 'ribbit',
        'bird': 'chirp',
    }
    
    return sounds.get(animal.lower(), "Unknown animal sound")

# Example usage:
print(animal_sound('dog'))  # Output: bark
print(animal_sound('cat'))  # Output: meow
print(animal_sound('lion'))  # Output: roar
print(animal_sound('elephant'))  # Output: Unknown animal sound
