import random
import sys
from enum import Enum

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget


class Race(Enum):
    ROAD = 1
    DIRT = 2
    CROSS_COUNTRY = 3
    STREET = 4


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi(r'forza.ui', self)
        self.button.clicked.connect(self.click)
        self.setWindowTitle('Forza Horizon 5 Randomizer')

    def click(self):
        # upgrade
        div = random.randrange(self.slider.value(), 7)
        if div == 1:
            upgrade = "D CLASS"
        elif div == 2:
            upgrade = "C CLASS"
        elif div == 3:
            upgrade = "B CLASS"
        elif div == 4:
            upgrade = "A CLASS"
        elif div == 5:
            upgrade = "S1 CLASS"
        else:
            upgrade = "S2 CLASS OR MAX PI"
        self.result.setText(upgrade)
        # race
        a = ['ROAD', 'DIRT', 'CROSS COUNTRY', 'STREET']

        season = random.choice(['Hot season', 'Wet season', 'Dry season', 'Storm season'])

        if season == 'Hot season':
            hotweather = open('weather').readlines()
            hotweather.append('Dust storm\n')
            weather = random.choice(hotweather)
        elif season == 'Storm season':
            stormweather = open('weather').readlines()
            stormweather.append('Tropical Storm\n')
            weather = random.choice(stormweather)
        else:
            weather = random.choice(open('weather').readlines())

        time = random.choice(open('time').readlines())
        category = random.choice(a)
        if category == 'ROAD':
            race = random.choice(open('road').readlines())
        elif category == 'DIRT':
            race = random.choice(open('dirt').readlines())
        elif category == 'CROSS COUNTRY':
            race = random.choice(open('cross').readlines())
        elif category == 'STREET':
            race = random.choice(open('street').readlines())
        self.settings.setText('<br>'.join([category, race, season, time, weather]))


if __name__ == '__main__':
    app = QApplication([])
    window = MyApp()
    window.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing window...')
