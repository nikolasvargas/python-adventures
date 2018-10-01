#!/usr/bin/python3
# -*- coding: UTF-8 -*-

class Program:

    def __init__(self, name, year):
        self.__name = name
        self.__year = year
        self.__likes = 0

    def __repr__(self):
        return f'{self.name}'

    def __str__(self):
        return f'{self.name} - {self.year} - {self.likes}'

    @classmethod
    def test_classmethod(cls):
        return cls.__name

    @property
    def name(self):
        return self.__name.title()

    @property
    def year(self):
        return self.__year

    @property
    def likes(self):
        return self.__likes

    def like(self):
        self.__likes += 1
        print('hmmm, human music: I like it')
        return f'total likes: {self.likes}'

class Movie(Program):

    def __init__(self, name, year, time):
        super().__init__(name, year)
        self.__time = time

    # def __repr__(self):
    #     return f"name: {self.name} \
    #         year: {self.year} \
    #         time: {self.time} \
    #         likes: {self.likes}"

    def __str__(self):
        return f'name: {self.name} - year: {self.year} - time: {self.time}m - likes: {self.likes}'

    @property
    def time(self):
        return self.__time

class Series(Program):
    def __init__(self, name, year, season):
        super().__init__(name, year)
        self.season = season

    # def __repr__(self):
    #     return f"name: {self.naem} \
    #         year: {self.year} \
    #         season: {self.season} \
    #         likes: {self.likes}"

    def __str__(self):
        return f'name: {self.name} - year: {self.year} - season: {self.season}t - likes: {self.likes}'

class Playlist:
    def __init__(self, name, program):
        self.name = name
        self.__program = program

    def __getitem__(self, item): ########################################
        return self.__program[item]               ##### DUCK TYPING #####
                                                  ##### DUCK TYPING #####
    def __len__(self):                            ##### DUCK TYPING #####
        return len(self.__program) ######################################

if __name__ == '__main__':
    X = Movie('ringrong - the world of rings', 2020, 120)
    Y = Series('wow - world of wow', 2010, 4)
    Z = Series('man of man - nam fo nam', 2144, 2330)

    print(list([p.name, p.year, p.time if hasattr(p, 'time') else p.season] for p in [X, Y, Z]))
    print([p for p in Playlist('zupzup', [X, Y, Z])])
    print(len(Playlist('zipzip', [X, Y, Z])))

    for p in Playlist('zapzap', [X, Y, Z]):
        print(p)
