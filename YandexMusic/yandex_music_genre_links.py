def get_link(genre):
    try:
        link = all_links[genre]
        return link
    except:
        return None


all_links = {'гиперпоп': 'https://music.yandex.ru/users/music-blog/playlists/2709',
             'русский поп': 'https://music.yandex.ru/users/yamusic-new/playlists/1006',
             'русский рэп': 'https://music.yandex.ru/users/yamusic-top/playlists/1002',
             'иностранный рэп': 'https://music.yandex.ru/users/yamusic-top/playlists/1089',
             'иностранный хип-хоп': 'https://music.yandex.ru/users/music-blog/playlists/2103',
             'инди': 'https://music.yandex.ru/users/music-blog/playlists/2096',
             'кантри': 'https://music.yandex.ru/users/yamusic-top/playlists/1027',
             'иностранный поп': 'https://music.yandex.ru/users/yamusic-top/playlists/1084',
             'для детей': 'https://music.yandex.ru/users/yamusic-top/playlists/1075',
             'джаз': 'https://music.yandex.ru/users/yamusic-top/playlists/1024',
             'танцевальная': 'https://music.yandex.ru/users/yamusic-top/playlists/1015',
             'ретро': 'https://music.yandex.ru/users/yamusic-top/playlists/1018',
             'панк': 'https://music.yandex.ru/users/music-blog/playlists/2105',
             'блюз': 'https://music.yandex.ru/users/music-blog/playlists/1891',
             'электроника': 'https://music.yandex.ru/users/music-blog/playlists/1025',
             'метал': 'https://music.yandex.ru/users/music-blog/playlists/2063',
             'ска': 'https://music.yandex.ru/users/yandexmusic/playlists/1102',
             'классическая': 'https://music.yandex.ru/users/ya.playlist/playlists/1099',
             'лофи': 'https://music.yandex.ru/users/TheChilledCow/playlists/1000'
             }
