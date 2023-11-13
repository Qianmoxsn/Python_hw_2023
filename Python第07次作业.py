'''
Description:
狼吃羊的游戏

假设游戏场景范围为（x,y），0≤x≤9,0≤y≤9。

游戏生成1只狼和10只羊；
它们的移动方向均随机；
狼的最大移动能力是2（可以随机移动1或2），羊的最大移动能力是1，移动随机沿x轴或y轴进行；
当移动到场景边界，则向反方向移动；
狼初始化体力为100；
狼每移动一次，体力消耗1；
当狼和羊坐标重叠，狼吃掉羊，狼体力增加20；
羊暂不计算体力；
当狼体力值为0或者羊的数量为0，游戏结束。

注意：无需图形界面展示，但要有中间过程输出。
'''
import random


class GameScene:
    def __init__(self, x, y):
        self.round = 1
        self.x = x
        self.y = y
        self.Wolves = []
        self.Sheep = []

    def generate_animals(self, num_wolves, num_sheep):
        for _ in range(num_wolves):
            wolf = Wolf(self)
            self.Wolves.append(wolf)
        for _ in range(num_sheep):
            sheep = Sheep(self)
            self.Sheep.append(sheep)

    def game_logic(self):
        while self.Wolves and self.Sheep:
            print(f"==== Round {self.round} ====")
            print(f"Wolves: {len(self.Wolves)} Sheep: {len(self.Sheep)}")
            for wolf in self.Wolves:
                wolf.move()
            for sheep in self.Sheep:
                sheep.move()
            self.display_map()
            self.check_collisions()
            self.round += 1
            print("")

    def check_collisions(self):
        for wolf in self.Wolves:
            print(f">> Wolf at {wolf.get_coordinates()}")
            for sheep in self.Sheep:
                print(f">> Sheep at {sheep.get_coordinates()}")
                if wolf.x == sheep.x and wolf.y == sheep.y:
                    wolf.eat()
                    sheep.die()

    def game_over(self):
        check = len(self.Wolves) == 0 or len(self.Sheep) == 0
        # print(f"Game Over:{check}")
        return check

    def display_map(self):
        print("+++" * (self.x + 2) + "+")
        # a matrix defualt 0
        map = [[0 for _ in range(self.x + 1)] for _ in range(self.y + 1)]
        for wolf in self.Wolves:
            x, y = wolf.get_coordinates()
            map[x][y] += 1
        for sheep in self.Sheep:
            x, y = sheep.get_coordinates()
            map[x][y] += 2
        # print(map),0-'· '，1-'W '，2-'S '
        for i in range(self.y + 1):
            print("|", end="  ")
            for j in range(self.x + 1):
                if map[i][j] == 0:
                    print("·", end="  ")
                elif map[i][j] == 1:
                    print("W", end="  ")
                elif map[i][j] == 2:
                    print("S", end="  ")
                elif map[i][j] == 3:
                    print("X", end="  ")
                # multiple sheep
                elif map[i][j] % 2 == 0 and map[i][j] > 3:
                    cnt = map[i][j] // 2
                    print("S" + str(cnt), end=" ")
            print("|")
        print("+++" * (self.x + 2) + "+")
        map.clear()


class Animal:
    def __init__(self, game_scene):
        self.game_scene = game_scene
        self.x = random.randint(0, game_scene.x)
        self.y = random.randint(0, game_scene.y)
        self.energy = 100

    def random_move(self):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        direction = random.choice(directions)
        max_move = self.max_move_ability()
        dx, dy = direction
        new_x = self.x + dx * random.randint(1, max_move)
        new_y = self.y + dy * random.randint(1, max_move)
        if 0 <= new_x <= self.game_scene.x:
            self.x = new_x
        if 0 <= new_y <= self.game_scene.y:
            self.y = new_y

    def is_at_edge(self):
        return self.x == 0 or self.x == self.game_scene.x or self.y == 0 or self.y == self.game_scene.y

    def max_move_ability(self):
        pass

    def get_coordinates(self):
        return (self.x, self.y)

    def die(self):
        pass


class Wolf(Animal):
    def __init__(self, game_scene):
        super().__init__(game_scene)
        self.max_energy = 100
        self.energy = self.max_energy
        self.max_move = 2

    def max_move_ability(self):
        return 2

    def move(self):
        self.energy -= 1
        self.random_move()
        if self.is_at_edge():
            self.random_move()

    def eat(self):
        self.energy += 20
        if self.energy > self.max_energy:
            self.energy = self.max_energy

    def die(self):
        if self.energy == 0:
            self.game_scene.Wolves.remove(self)


class Sheep(Animal):
    def max_move_ability(self):
        return 1

    def move(self):
        self.random_move()
        if self.is_at_edge():
            self.random_move()

    def die(self):
        print(f"Sheep at {self.get_coordinates()} died!")
        self.game_scene.Sheep.remove(self)


if __name__ == "__main__":
    # answer here
    # 创建游戏场景(0-9)
    scene = GameScene(4, 4)
    scene.generate_animals(1, 5)
    # 游戏逻辑
    while not scene.game_over():
        scene.game_logic()
    print("Game Over!")
