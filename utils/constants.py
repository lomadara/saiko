
block_size = 1024 * 1024

saiko_headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36', 
    'accept': '*/*', 
    'Referer': 'https://download.saikoanimes.net/secure/uploads/{}?shareable_link={}', 
    'cookie': 'theme=light; _gid=GA1.2.1558720664.1641603094; SaikÃ´ Direct_cookie_notice=1; XSRF-TOKEN=eyJpdiI6IjdaNXNGbUlEclg0TDVHcDB6VU9wZmc9PSIsInZhbHVlIjoiMFRYaEtaZkVqV09abE5vSnVCWGlDandheWF6S2g4TjRQVW5TbmNtT3UyY296L1czUHJ2V0JNK3JiemgyaDUwU1h3Mm1QQ0o1UWpiT0Z0eE5WNWhieVpkSG15Q0NabzhyL3VRN2xXWGVPQ1FCdWxHa1dHb2NCOVA4MDk0RGZDN3QiLCJtYWMiOiIwODMyN2E2ZWY3ZGU3YWUzNjYwZDUyNGZiMTMxNDZhMDkzNjgwOGFmY2MxM2RjNTNjMDk0NDQxNDhmYTdmNzM2IiwidGFnIjoiIn0%3D; saiko_direct_session=eyJpdiI6IldZTkNpVlpOWTFBWVpHY3ZPY0xNTEE9PSIsInZhbHVlIjoiSGd2SlhiVlpkNXBnaW51RnhDYW16T3ViZ0o4UHJDblkyWTRGamErRkpyZWN4eWRzeUxocmZIS1JEY2JOTUIvU25hV3lQMmFUdTliaEtZOVZPV0lmanp5c1drM21KSDd2MFpkWjcwdjZwTWx5ckt4VkViSEk5VkNCTDMvUkJTaW0iLCJtYWMiOiIwZjMwODk2NGFhN2NhMDAyYjVhODQ5ZmY5YTkyYjBhYzJjYzkwNjM2MGNiMjQxZjNiZTU3NGNiY2RmNTMzYjJmIiwidGFnIjoiIn0%3D; _ga_SGJM7RJB0N=GS1.1.1641693412.138.0.1641693412.0; _ga=GA1.2.457857542.1503198075; crisp-client%2Fsession%2F81f2f730-82ea-42ac-ac28-6061d2d4eca1=session_bd7d2e65-5026-4412-bace-0cbb32f7812e'
}

saiko_episodes_infos_url = 'https://download.saikoanimes.net/secure/drive/shareable-links/{}?withEntries=true'

saiko_episodes_infos_new_url = 'https://download.saikoanimes.net/api/v1/shareable-links/{}?withEntries=true{}'

saiko_episode_download_url = 'https://download.saikoanimes.net/secure/uploads/{}?shareable_link={}'

saiko_episode_download_new_url = 'https://download.saikoanimes.net/api/v1/file-entries/{}?shareable_link={}&password=null&thumbnail='

saiko_title_xpath = '/html/body/div[3]/div/div[2]/div/div[2]/text()'

saiko_cover_xpath = '/html/body/div[4]/div/div[2]/div[1]/a/div/img'

saiko_sonopse_xpath_1 = '//*[@id="box"]/text()'

saiko_sonopse_xpath_2 = '//*[@id="main"]/section/div/div[1]/div[2]/div[4]/div/div[2]/div[2]/text()'

saiko_tags_xpath = '//*[@id="main"]/section/div/div[1]/div[2]/div[4]/div/div[1]/div/div/text()'

saiko_episodes_url_xpath = '//*[@id="50"]/div/a'

saiko_episodes_url_xpath_2 = '//*[@id="5"]/div/a'

saiko_episodes_url_xpath_3 = '/html/body/div[4]/div/div[2]/div[{}]/a'

saiko_episodes_url_xpath_4 = '/html/body/div[4]/div/div[3]/div[{}]/a'

regex_remove_special_characters = '[^A-Za-z0-9]'

regex_remove_last_space_and_tabulation = '[ \t]+$'

season_animes = [
    "https://saikoanimes.net/anime/kancolle-kantai-collection/",
    'https://saikoanimes.net/anime/fumetsu-no-anata-e/',
    'https://saikoanimes.net/anime/arknights-reimei-zensou/',
    'https://saikoanimes.net/anime/urusei-yatsura-2022/',
    'https://saikoanimes.net/anime/seiken-densetsu-legend-of-mana-the-teardrop-crystal/',
    'https://saikoanimes.net/anime/blue-lock/',
    'https://saikoanimes.net/anime/chainsaw-man/',
    'https://saikoanimes.net/anime/peter-grill-to-kenja-no-jikan/',
    'https://saikoanimes.net/anime/noumin-kanren-no-skill-bakka-agetetara-nazeka-tsuyoku-natta/',
    'https://saikoanimes.net/anime/mairimashita-iruma-kun/',
    'https://saikoanimes.net/anime/yuusha-party-wo-tsuihou-sareta-beast-tamer-saikyoushu-no-nekomimi-shoujo-to-deau/',
    'https://saikoanimes.net/anime/spy-x-family/',
    'https://saikoanimes.net/anime/uzaki-chan-wa-asobitai/',
    'https://saikoanimes.net/anime/akiba-maid-sensou/',
    'https://saikoanimes.net/anime/kage-no-jitsuryokusha-ni-naritakute/',
    'https://saikoanimes.net/anime/do-it-yourself/',
    'https://saikoanimes.net/anime/futoku-no-guild/',
    'https://saikoanimes.net/anime/human-bug-daigaku/',
    'https://saikoanimes.net/anime/mob-psycho-100/',
    'https://saikoanimes.net/anime/yama-no-susume/',
    'https://saikoanimes.net/anime/shinobi-no-ittoki/',
    'https://saikoanimes.net/anime/golden-kamuy/',
    'https://saikoanimes.net/anime/c-danchi-housing-complex-c/',
    'https://saikoanimes.net/anime/shinmai-renkinjutsushi-no-tenpo-keiei-management-of-a-novice-alchemist/',
    'https://saikoanimes.net/anime/dragon-quest-dai-no-daibouken/',
    'https://saikoanimes.net/anime/boku-no-hero-academia/',
    'https://saikoanimes.net/anime/berserk-ougon-jidai-hen-memorial-edition/',
    'https://saikoanimes.net/anime/yuusha-party-wo-tsuihou-sareta-beast-tamer-saikyoushu-no-nekomimi-shoujo-to-deau/',
    #'https://saikoanimes.net/anime/pop-team-epic/',
    'https://saikoanimes.net/anime/uchi-no-shishou-wa-shippo-ga-nai-meu-mestre-nao-tem-cauda/',
    'https://saikoanimes.net/anime/tensei-shitara-ken-deshita/',
    'https://saikoanimes.net/anime/prima-doll/',
    'https://saikoanimes.net/anime/fuuto-tantei/',
    'https://saikoanimes.net/anime/bucchigire/',
    'https://saikoanimes.net/anime/saikin-yatotta-maid-ga-ayashii/',
    'https://saikoanimes.net/anime/digimon-ghost-game/',
    'https://saikoanimes.net/anime/yurei-deco/',
    'https://saikoanimes.net/anime/orient/',
    'https://saikoanimes.net/anime/kinsou-no-vermeil-gakeppuchi-majutsushi-wa-saikyou-no-yakusai-to-mahou-sekai-wo-tsukisusumu/',
    'https://saikoanimes.net/anime/dungeon-ni-deai-wo-motomeru-no-wa-machigatteiru-darou-ka-4/',
    'https://saikoanimes.net/anime/utawarerumono/',
    'https://saikoanimes.net/anime/engage-kiss/',
    'https://saikoanimes.net/anime/tensei-kenja-no-isekai-life-daini-no-shokugyo-wo-ete-sekai-saikyou-ni-narimashita/',
    'https://saikoanimes.net/anime/rwby-hyousetsu-teikoku/',
    'https://saikoanimes.net/anime/isekai-meikyuu-de-harem-wo/',
    'https://saikoanimes.net/anime/isekai-ojisan/',
    'https://saikoanimes.net/anime/yofukashi-no-uta/',
    'https://saikoanimes.net/anime/warau-arsnotoria-sun/',
    'https://saikoanimes.net/anime/hataraku-maou-sama-2/',
    'https://saikoanimes.net/anime/hoshi-no-samidare/',
    'https://saikoanimes.net/anime/summer-time-render/',
    'https://saikoanimes.net/anime/mobile-suit-gundam-the-witch-from-mercury/',
    'https://saikoanimes.net/anime/bleach/',
]
