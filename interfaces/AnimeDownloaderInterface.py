from abc import ABC, abstractmethod


class AnimeDownloaderInterface(ABC):
    @abstractmethod
    def get_html_tree(self) -> None:
        pass
    
    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def get_season_urls(self) -> str:
        pass
    
    @abstractmethod
    def create_folder(self):
        pass
    
    @abstractmethod
    def download_cover(self) -> None:
        pass
    
    abstractmethod
    def get_episodes_informations(self) -> dict:
        pass
    
    @abstractmethod
    def download_episode_from_saiko_drive(self, episode_information: str) -> None:
        pass