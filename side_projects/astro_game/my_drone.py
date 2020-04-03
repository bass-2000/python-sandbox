from collections import defaultdict

from astrobox.core import Drone


class MyDrone(Drone):
    mitrodrones = []
    dict_for_test = defaultdict()
    dict_for_test_2 = defaultdict()

    def on_born(self):
        self.mitrodrones.append(self)
        self.target = self.get_next_asteroid(reverse=True)
        self.move_at(self.target)

    def get_next_asteroid(self, reverse):
        distances = self.get_distances()
        if distances:
            name_asteroids = [k for k, v in
                              sorted(distances.items(), key=lambda para: para[1], reverse=reverse)]
            payload = sum([asteroid.payload for asteroid in name_asteroids])
            if payload >= 400:
                """чем больше ресурсов, тем больше дронов неоходимо"""
                if self.mitrodrones.index(self) < 2:
                    return name_asteroids[0]
                elif 2 <= self.mitrodrones.index(self) < 4:
                    return name_asteroids[1]
                elif 4 <= self.mitrodrones.index(self) < 6:
                    return name_asteroids[2]
            elif 300 < payload < 400:
                if self.mitrodrones.index(self) < 2:
                    return name_asteroids[0]
                elif 2 <= self.mitrodrones.index(self) < 4 and len(name_asteroids) > 1:
                    return name_asteroids[1]
                elif 4 <= self.mitrodrones.index(self) < 6 and len(name_asteroids) > 2:
                    return name_asteroids[2]
            elif 100 < payload <= 300:
                if self.mitrodrones.index(self) < 2:
                    return name_asteroids[0]
                elif self.mitrodrones.index(self) == 2 and payload > 150 and len(name_asteroids) > 1:
                    return name_asteroids[1]
                elif 4 <= self.mitrodrones.index(self) < 6:
                    return name_asteroids[len(name_asteroids) - 1]
            elif payload <= 100:
                if len(name_asteroids) > 1:
                    if self.mitrodrones.index(self) == 1:
                        return name_asteroids[0]
                    elif self.mitrodrones.index(self) == 2:
                        return name_asteroids[1]
                else:
                    if self.mitrodrones.index(self) == 1:
                        return name_asteroids[0]
        else:
            return None

    def get_distances(self):
        distances = defaultdict()
        for asteroid in self.asteroids:
            if asteroid.payload:
                distances[asteroid] = self.distance_to(asteroid)
        return distances

    def on_stop_at_asteroid(self, asteroid):
        self.load_from(asteroid)

    def on_load_complete(self):
        """После загрузки на объекте, дрон определяет самый ближайший астероид, и если он заполнено меньше, чем на 90,
         то он летит к астероиду, в противном случае - на базу"""
        self.target = self.get_next_asteroid(reverse=False)
        if self.payload <= 90 and self.target:
            self.move_at(target=self.target)
        else:
            self.move_at(self.my_mothership)

    def on_stop_at_mothership(self, mothership):
        self.unload_to(mothership)

    def on_unload_complete(self):
        self.target = self.get_next_asteroid(reverse=True)
        if self.target:
            self.move_at(target=self.target)
        else:
            self.stop()
