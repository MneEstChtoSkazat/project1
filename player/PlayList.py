"""Playlist"""

import pygame
from linked_list import LinkedList
from music_track import MusicTrack


class Playlist(LinkedList):
    def __init__(self, data=None):
        super().__init__(data)
        self.current_playlist = None
        self.playlists = {}

    def play_all(self, track):
        self._current = track
        pygame.mixer.music.load(self.current.path)
        pygame.mixer.music.play()

    def next_track(self):
        if self._current:
            self.play_all(self._current.next)

    def previous_track(self):
        if self._current:
            self.play_all(self._current.prev)

    @property
    def current(self):
        if not self._current:
            return None
        return self._current.data

    @current.setter
    def current(self, current):
        self._current = current
