from astrobox.space_field import SpaceField

from side_projects.astro_game.my_drone import MyDrone

if __name__ == '__main__':
    my_space = SpaceField(
        field=(1200, 900),
        speed=2,
        asteroids_count=7
    )

    my_drones = [MyDrone() for _ in range(5)]

    my_space.go()
