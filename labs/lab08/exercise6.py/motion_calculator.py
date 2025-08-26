import physics_constants

time = 2

position = (physics_constants.building_height + physics_constants.initial_velocity * time - (0.5 * physics_constants.standard_gravity * time**2))
print(f"Position after {time} seconds: {position} meters")

velocity = (physics_constants.initial_velocity - physics_constants.standard_gravity * time)
print(f"Velocity after {time} seconds: {velocity} m/s")

kinetic_energy = 0.5 * physics_constants.ball_mass * velocity**2
print(f"Kinetic Energy after {time} seconds: {kinetic_energy} Joules")

motion_status = "Moving up" if velocity > 0 else "Moving down" if velocity < 0 else "At Peak"
