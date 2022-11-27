import os
from lxml import html
import requests
import re
from tqdm import tqdm
from interfaces.AnimeDownloaderInterface import AnimeDownloaderInterface
from utils import constants
from utils.custom_errors import AlreadyExistsError, NotFoundError


class SaikoAnimeDownloader(AnimeDownloaderInterface):
    def __init__(self, anime_url: str) -> None:
        self.anime_url = anime_url
        self.html_tree = None
        self.anime_title = None
        self.season_urls = []
    
    def get_html_tree(self) -> None:
        anime_page = requests.get(self.anime_url)
        self.html_tree = html.fromstring(anime_page.content)

    def get_title(self):
        search_result = self.html_tree.xpath(constants.saiko_title_xpath)
        if search_result:
            title = search_result[0]
            title = re.sub(constants.regex_remove_last_space_and_tabulation, '', title)
            title = re.sub(constants.regex_remove_special_characters, '-', title)
            self.anime_title = title
        
        if not self.anime_title:
            raise NotFoundError("Title not found")
    
    def download_cover(self) -> None:
        search_result = self.html_tree.xpath(constants.saiko_cover_xpath)
        if search_result:
            response = requests.get(search_result[0].get('src'))
            with open("./animes/{}/{}".format(self.anime_title, "cover.jpg"), 'wb') as file:
                for data in response.iter_content(constants.block_size):
                    file.write(data)       
    
    def get_season_urls(self) -> str:
        for season in range(1, 10):
            result_search = self.html_tree.xpath(constants.saiko_episodes_url_xpath_3.format(season))
            if not result_search:
                result_search = self.html_tree.xpath(constants.saiko_episodes_url_xpath_4.format(season))
            
            if result_search:
                self.season_urls.append(result_search[0].get('href'))
        
        if not self.season_urls:
            raise NotFoundError("Episodes url not found")
    
    def create_folder(self):
        if not os.path.exists('./animes/{}'.format(self.anime_title)):
            os.mkdir('./animes/{}'.format(self.anime_title))
    
    def get_items_informations(self, hash, filters):
        return requests.get(constants.saiko_episodes_infos_new_url.format(hash, filters)).json()
    
    def map_episodes_informations(self, anime_id, item, maped_episodes_information, season):
        maped_episodes_information.append({
            "anime_id": anime_id,
            "episode_id": item.get('id'),
            "episode_name": item.get('name'),
            "hash": item.get('hash'),
            "season": "S{}".format(season)
        })
        
        return maped_episodes_information
        
    def get_episodes_informations(self) -> None:
        maped_episodes_information = []
        
        for season, episodes_url in enumerate(self.season_urls):
            season += 1
            anime_hash = episodes_url.split('/')
            anime_hash = anime_hash[len(anime_hash) - 1]
            
            if 'cloud' in episodes_url:
                self.download_episode_from_cloud_saiko(
                    anime_hash,
                    self.anime_title
                    )
            else:
                items_informations = self.get_items_informations(anime_hash, '')
                anime_id = items_informations.get('link').get('id')
                items = items_informations.get('folderChildren').get('data')
                for item in items:
                    if item.get('type') == 'folder' and '1080p' in item.get('name'):
                        page = 1
                        while page: 
                            episodes_informations = self.get_items_informations(
                                anime_hash + ':' + item.get('hash'),
                                '&page={}'.format(page)
                                )
                                                               
                            episodes = episodes_informations.get('folderChildren').get('data')
                            for episode in episodes:
                                maped_episodes_information = self.map_episodes_informations(
                                    anime_id,
                                    episode,
                                    maped_episodes_information,
                                    season
                                    )
                                
                            page = episodes_informations.get('folderChildren').get('next_page')  
                    else:
                        maped_episodes_information = self.map_episodes_informations(
                            anime_id,
                            item,
                            maped_episodes_information,
                            season
                            )
                    
        return maped_episodes_information
    
    def download_episode_from_saiko_drive(self, episode_information: str) -> None:
        headers = constants.saiko_headers
        headers['Referer'] = headers['Referer'].format(
            episode_information.get('episode_id'),
            episode_information.get('anime_id')
            )
        
        if not os.path.exists('./animes/{}/{}'.format(self.anime_title, episode_information.get('season'))):
            os.mkdir('./animes/{}/{}'.format(self.anime_title, episode_information.get('season')))
        
        if not os.path.exists("./animes/{}/{}/{}".format(
            self.anime_title,
            episode_information.get('season'),
            episode_information.get('episode_name')
            )):
            video_response = requests.get(constants.saiko_episode_download_new_url.format(
                episode_information.get('episode_id'),
                episode_information.get('anime_id')
            ), stream=True)
            
            print("\033[1;33;40m {}".format(episode_information.get('episode_name')))
            total_size_in_bytes= int(video_response.headers.get('content-length', 0))
            progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
            
            with open("./animes/{}/{}/{}".format(
                self.anime_title,
                episode_information.get('season'),
                episode_information.get('episode_name')
                ), 'wb') as file:
                for data in video_response.iter_content(constants.block_size):
                    progress_bar.update(len(data))
                    file.write(data)
                    
            progress_bar.close()
            
        else:
            raise AlreadyExistsError("{} already exists".format(episode_information.get('episode_name')))
        
    def download_episode_from_cloud_saiko(self, hash, anime_title):
        response = requests.get('https://cloud.saikoanimes.net/api/sharing/{}'.format(hash)).json()   
        item_id = response['data']['attributes']['item_id']
        response = requests.get('https://cloud.saikoanimes.net/api/sharing/folders/{}/{}?sort=created_at&direction=DESC&page=1'.format(item_id, hash)).json()
        for episode in response['data']:
            episode_name = episode['data']['attributes']['name']
            file_url = episode['data']['attributes']['file_url']

            if not os.path.exists("./animes/{}/{}".format(anime_title, episode_name)):
                video_response = requests.get(file_url, stream=True)
                print("\033[1;33;40m {}".format(episode_name))
                total_size_in_bytes= int(video_response.headers.get('content-length', 0))
                progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
                with open("./animes/{}/{}".format(anime_title, episode_name), 'wb') as file:
                    for data in video_response.iter_content(constants.block_size):
                        progress_bar.update(len(data))
                        file.write(data)

                progress_bar.close()
                
            else:
                raise AlreadyExistsError("{} already exists".format(episode_name))
