import physics

# Použití funkcí z modulu physics
mass = 10
earth_weight = physics.weight_on_earth(mass)
moon_weight = physics.weight_on_moon(mass)


distance = 1000
speed_of_light_time = physics.speed_of_light(distance)
speed_of_sound_time = physics.speed_of_sound(distance)

print(f'Váha na Zemi: {earth_weight} N')
print(f'Váha na Měsíci: {moon_weight} N')

print(f'Čas cestování světlem na vzdálenost {distance} m: {speed_of_light_time} s')
print(f'Čas cestování zvukem na vzdálenost {distance} m: {speed_of_sound_time} s')