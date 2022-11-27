from downloaders.SaikoAnimeDownloader import SaikoAnimeDownloader
from utils.constants import season_animes
from typing import Type
from interfaces.AnimeDownloaderInterface import AnimeDownloaderInterface
from utils.custom_errors import AlreadyExistsError, NotFoundError

class Dowloader():
    def download(self, anime_dowloader: Type[AnimeDownloaderInterface]):
        anime_dowloader.get_html_tree()
        anime_dowloader.get_title()
        anime_dowloader.get_season_urls()
        anime_dowloader.create_folder()
        anime_dowloader.download_cover()
        episodes_informations = anime_dowloader.get_episodes_informations()
        
        for episode_information in episodes_informations:
            try:
                anime_dowloader.download_episode_from_saiko_drive(episode_information)
            
            except AlreadyExistsError as ex:
                print("\033[1;32;40m {}".format(ex))
                
            except Exception as ex:
                print("\033[1;31;40m {}".format(ex))

for anime_url in season_animes:
    try:
        downloader = Dowloader()
        downloader.download(SaikoAnimeDownloader(anime_url))
    
    except NotFoundError as ex:
        print("\033[1;31;40m {} {}".format(anime_url, ex))
        
    except Exception as ex:
        print("\033[1;31;40m {}".format(ex))
