from perlin_noise import PerlinNoise

# Initialize Perlin noise
noise = PerlinNoise(octaves=4)

def generate_obstacle_pattern(time, scale=10.0):
    obstacle_pattern = noise(time / scale)
    return int(obstacle_pattern * 700)  # Scale based on game size
