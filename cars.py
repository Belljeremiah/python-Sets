showroom = {'mustang', 'lamborghini', 'ferrari', 'jaguar', 'camaro', 'ferrari'}

print(showroom)

showroom2 = {'grand prix', 'firebird'}

showroom.update(showroom2)

print(showroom)

showroom.discard('jaguar')

print(showroom)

junkyard = {'beater', 'cadillac', 'grand prix', 'camaro'}

showjunk = showroom.intersection(junkyard)

print(showjunk)

showroomplusjunkyard = showroom.union(junkyard)

print(showroomplusjunkyard)