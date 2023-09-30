def make_great(magicians):
    return ['The great ' + magician for magician in magicians]

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

magicians = ['Houdini', 'Dynamo', 'Penn Jillette']
magicians = make_great(magicians)
show_magicians(magicians)
