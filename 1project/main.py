import sys
from PyQt5.QtWidgets import ( QApplication, QMainWindow, QPushButton, 
QListWidget, QVBoxLayout, QWidget, QFileDialog, QLabel, QHBoxLayout, 
QInputDialog, QMessageBox
)
from PyQt5 import QtCore
import pygame
from music_track import MusicTrack
from PlayList import Playlist


class PlaylistUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        pygame.mixer.init()

        # Плейлисты
        self.playlists = {}
        self.current_playlist = None
        

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

        play_btn = QPushButton("▶️")
        play_btn.clicked.connect(self.play_current_track)
        playback_buttons_layout.addWidget(play_btn)

        next_track_btn = QPushButton("⏩")
        next_track_btn.clicked.connect(self.next_track)
        playback_buttons_layout.addWidget(next_track_btn)

        prev_track_btn = QPushButton("⏪")
        prev_track_btn.clicked.connect(self.previous_track)
        playback_buttons_layout.addWidget(prev_track_btn)

        main_layout.addLayout(playback_buttons_layout)

        # Текущий трек
        self.current_track_label = QLabel("Текущий трек: None")
        main_layout.addWidget(self.current_track_label)
    
    def create_playlist(self):
        """Создание нового плейлиста."""
        name, ok = QInputDialog.getText(self, 'Создать плейлист', 'Введите название:')
        if ok and name:
            if name in self.playlists:
                self.show_error_message(f"Плейлист с именем '{name}' уже существует.")
            else:
                new_playlist = Playlist()  # Создание нового объекта плейлиста
                self.playlists[name] = new_playlist  # Добавляем в словарь плейлистов
                self.playlist_list.addItem(name)  # Обновляем список плейлистов в интерфейсе
                self.current_playlist = new_playlist  # Назначаем его текущим
                print(f"Плейлист '{name}' создан и выбран.")
        else:
            self.show_error_message("Введите корректное название плейлиста.")

    def select_playlist(self):
        """Выбор текущего плейлиста из списка и обновление списка треков."""
        selected_playlist_item = self.playlist_list.currentItem()
        
        if selected_playlist_item:
            selected_playlist_name = selected_playlist_item.text()
            # Назначаем текущий плейлист из словаря по его имени
            self.current_playlist = self.playlists.get(selected_playlist_name)
            print(f"Выбран плейлист: {selected_playlist_name}")

            # Обновляем список треков
            self.update_track_list()
        else:
            self.current_playlist = None
            print("Не удалось выбрать плейлист.")

    def update_track_list(self):
        """Обновление списка треков на основе текущего плейлиста."""
        self.track_list.clear()  # Очищаем предыдущий список треков
        if self.current_playlist:
            for track in self.current_playlist:  
                # Итерация по трекам в текущем плейлисте
                self.track_list.addItem(track.data.path)

    def delete_playlist(self):
        """Удаление выбранного плейлиста."""
        selected_playlist_name = self.playlist_list.currentItem()
        
        if selected_playlist_name:
            del self.playlists[selected_playlist_name.text()]  
            # Удаляем из словаря
            self.playlist_list.takeItem(self.playlist_list.currentRow())  
            # Удаляем из интерфейса
            self.current_playlist = None
            print(f"Плейлист '{selected_playlist_name.text()}' удалён.")
        else:
            print("Плейлист для удаления не выбран.")

    def add_track(self):
        """Добавление трека в текущий плейлист."""
        selected_playlist = self.playlist_list.currentItem()
        if selected_playlist:
            track_path, _ = QFileDialog.getOpenFileName(self, "Add Track", 
                                            "", "Music Files (*.mp3 *.wav, *.flac)")
            if track_path:
                track = MusicTrack(track_path)
                self.current_playlist.append(track)  
                self.track_list.addItem(track.path) 
                print(f"Трек '{track_path}' добавлен в плейлист.")
            else:
                self.show_error_message("Не удалось загрузить трек.")
        else:
            self.show_error_message("Выберите плейлист для добавления трека.")

    def remove_track(self):
        """Удаление трека из текущего плейлиста."""
        if not self.current_playlist:
            print("Плейлист не выбран.")
            return

        selected_track = self.track_list.currentItem()
        if selected_track:
            track_path = selected_track.text()  
            # Получаем текст выбранного трека
            track_found = False  # Флаг для отслеживания, найден ли трек

            # Ищем трек в текущем плейлисте
            for node in self.current_playlist:  # Итерация по узлам
                if node.data.path == track_path:  # Сравниваем с node.data.path
                    self.current_playlist.remove(node.data)  
                    # Удаляем трек из плейлиста
                    track_found = True
                    break

            if track_found:
                self.track_list.takeItem(self.track_list.currentRow())  
                # Удаляем трек из интерфейса
                print(f"Трек '{track_path}' удалён из плейлиста.")
            else:
                print(f"Трек '{track_path}' не найден в плейлисте.")
        else:
            print("Трек для удаления не выбран.")


    def move_track(self):
        """Перемещение трека на другую позицию в текущем плейлисте."""
        if not self.current_playlist:
            print("Плейлист не выбран.")
            return

        current_row = self.track_list.currentRow()  # Получаем текущую позицию трека
        if current_row < 0:
            self.show_error_message("Выберите композицию для смены позиции.")
            return

        if len(self.current_playlist) < 2:
            self.show_error_message(
                "В плейлисте должно быть минимум 2 композиции для перестановки"
            )
            return

        # Запрашиваем новую позицию
        response = QInputDialog.getInt(
            self,
            "Место композиции",
            f"Введите число от 0 до {len(self.current_playlist) - 1}",
            min=0,
            max=len(self.current_playlist) - 1,
        )

        if not response[1]:
            print("Ввод отменен")
            return  # Если ввод отменен

        new_position = response[0]

        # Проверяем, не совпадают ли текущая и новая позиции
        if current_row == new_position:
            print("позиции совпадают")
            return

        # Находим трек для перемещения
        track_to_move = self.find_song_by_id(current_row)
        
        # Удаляем трек из текущей позиции
        self.remove_track()

        if new_position == 0:
            # Если перемещаем трек в самое начало
            self.current_playlist.append_left(track_to_move.data)
        elif current_row == len(self.current_playlist):
            print("перенос последнего")
            prev_track = self.find_song_by_id(new_position - 1)
            self.current_playlist.insert(prev_track.data, track_to_move.data)
        else:
            # Вставляем трек на нужную позицию
            print(current_row, len(self.current_playlist) - 2)
            
            if current_row < new_position:
                print(current_row, new_position)
                prev_track = self.find_song_by_id(new_position - 1)
            else:
                print(current_row, new_position)
                prev_track = self.find_song_by_id(new_position)

            self.current_playlist.insert(prev_track.data, track_to_move.data)

        # Обновляем список треков в интерфейсе
        self.update_track_list()


        
    def find_song_by_id(self, sid):
        """Find song by id."""
        for idx, track in enumerate(self.current_playlist):
            if idx == sid:
                return track

        return None

    def play_song_by_id(self, sid):
        """Play song by id."""
        track = self.find_song_by_id(sid)
        self.current_playlist.play_all(track)

    def play_current_track(self):
        """Проигрывание текущего трека."""
        if not self.current_playlist:
            print("Плейлист не выбран или он пуст.")
            return

        selected_track = self.track_list.currentRow()
        if selected_track >= 0:
            self.play_song_by_id(selected_track)

        else:
            print(selected_track)
            self.current_playlist.play_all(
                self.find_song_by_id(0)
            )
        
        self.timer.start()
            

    def next_track(self):
        """Воспроизведение следующего трека."""
        if not self.current_playlist:
            print("Плейлист не выбран.")
            return

        self.current_playlist.next_track()  # Переход на следующий трек

    def previous_track(self):
        """Воспроизведение предыдущего трека."""
        if not self.current_playlist:
            print("Плейлист не выбран.")
            return

        self.current_playlist.previous_track()  # Переход на предыдущий трек
        
    def next_track_when_ended(self):
        """Play next track on current end."""
        if pygame.mixer.music.get_busy():
            return

        self.current_playlist.next_track()

    def loop_playlist(self):
        """Зацикливание плейлиста."""
        if not self.current_playlist:
            print("Плейлист не выбран.")
            return

        if not pygame.mixer.music.get_busy():
            self.next_track() # Перезапуск текущего плейлиста

        pygame.mixer.music.set_endevent(pygame.USEREVENT)  # Зацикливание
        
    def show_error_message(self, message):
        """Отображение сообщения об ошибке"""
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setText(message)
        msg_box.setWindowTitle("Ошибка")
        msg_box.exec_()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PlaylistUI()
    window.show()
    sys.exit(app.exec_())