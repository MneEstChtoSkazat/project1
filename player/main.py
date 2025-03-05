import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QListWidget,
    QVBoxLayout,
    QWidget,
    QFileDialog,
    QLabel,
    QHBoxLayout,
    QInputDialog,
    QMessageBox,
)
from PyQt5 import QtCore
import pygame

from player.PlayList import Playlist


class PlaylistUI(QMainWindow):
    def __init__(self):
        super().__init__()
        pygame.mixer.init()
        # Плейлист
        self.playlist = {}
        self.curent_playlist = None
        self.initUI()
        self.setWindowTitle("Music Playlist Manager")
        self.setGeometry(700, 600, 500, 500)

    def initUI(self):
        self.setWindowTitle("Music Playlist Manager")
        self.setGeometry(100, 100, 800, 600)

        # Основной виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layouts
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # Плейлист
        self.playlist_list = QListWidget()
        self.playlist_list.currentItemChanged.connect(self.select_playlist)
        main_layout.addWidget(self.playlist_list)

        # Кнопки управления плейлистом
        playlist_buttons_layout = QHBoxLayout()

        add_playlist_btn = QPushButton("Add Playlist")
        add_playlist_btn.clicked.connect(self.create_playlist)
        playlist_buttons_layout.addWidget(add_playlist_btn)

        remove_playlist_btn = QPushButton("Remove Playlist")
        remove_playlist_btn.clicked.connect(self.delete_playlist)
        playlist_buttons_layout.addWidget(remove_playlist_btn)

        main_layout.addLayout(playlist_buttons_layout)

        # Список композиций
        self.track_list = QListWidget()
        self.track_list.setSelectionMode(QListWidget.SingleSelection)
        main_layout.addWidget(self.track_list)

        # Кнопки управления композициями
        track_buttons_layout = QHBoxLayout()

        add_track_btn = QPushButton("Add Track")
        add_track_btn.clicked.connect(self.add_track)
        track_buttons_layout.addWidget(add_track_btn)

        remove_track_btn = QPushButton("Remove Track")
        remove_track_btn.clicked.connect(self.remove_track)
        track_buttons_layout.addWidget(remove_track_btn)

        move_btn = QPushButton("Move track to")
        move_btn.clicked.connect(self.move_track)
        track_buttons_layout.addWidget(move_btn)

        main_layout.addLayout(track_buttons_layout)

        # Панель управления проигрыванием
        playback_buttons_layout = QHBoxLayout()

        play_btn = QPushButton("Play")
        play_btn.clicked.connect(self.play_current_track)
        playback_buttons_layout.addWidget(play_btn)

        next_track_btn = QPushButton("Next")
        next_track_btn.clicked.connect(self.next_track)
        playback_buttons_layout.addWidget(next_track_btn)

        prev_track_btn = QPushButton("Previous")
        prev_track_btn.clicked.connect(self.previous_track)
        playback_buttons_layout.addWidget(prev_track_btn)

        main_layout.addLayout(playback_buttons_layout)

        # Текущий трек
        self.current_track_label = QLabel("Current Track: None")
        main_layout.addWidget(self.current_track_label)

        def create_playlist(self):
            """Создание нового плейлиста."""
            name, ok = QInputDialog.getText(self, 'Создать плейлист', 'Введите название:')
            if ok and name:
                new_playlist = Playlist()
                self.playlist[name] = new_playlist
                print(f"Плейлист '{name}' создан и выбран.")

        def select_playlist(self):
            """Выбор текущего плейлиста из списка и обновление списка треков."""

        def delete_playlist(self):
            """Удаление выбранного плейлиста."""

        def add_track(self):
            """Добавление трека в текущий плейлист."""

        def remove_track(self):
            """Удаление трека из текущего плейлиста."""

        def move_track(self):
            """Перемещение трека на другую позицию в текущем плейлисте."""

        def play_current_track(self):
            """Проигрывание текущего трека."""
            

        def next_track(self):
            """Воспроизведение следующего трека."""
            self.current_playlist.next_track()
            self.pl
        def previous_track(self):
            """Воспроизведение предыдущего трека."""
            self.current_playlist.previous_track()

        def loop_playlist(self):
            """Зацикливание плейлиста."""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PlaylistUI()
    window.show()
    sys.exit(app.exec_())
