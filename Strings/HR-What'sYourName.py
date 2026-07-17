def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]


string = input("Enter a string: ")
position = int(input("Enter the position: "))
character = input("Enter the new character: ")

new_string = mutate_string(string, position, character)

print("Updated String:", new_string)