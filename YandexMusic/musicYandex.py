import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pickle
import yandex_music_config
import yandex_music_genre_links
import config

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 OPR/91.0.4516.95'}

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options,
                          executable_path='C:\\Users\\Admin\\PycharmProjects\\newRobotModel\\chromedriver\\chromedriver.exe')


def get_data(link):
    req = requests.get(link, headers=headers)
    src = req.text
    with open('index.html', 'w', encoding='utf-8') as file:
        file.write(src)
    return src


def play_playlist(playlist_url):
    url = 'https://music.yandex.ru/' + playlist_url
    driver.get(url)
    for cookie in pickle.load(open('yandex_music_cookies', 'rb')):
        driver.add_cookie(cookie)
    time.sleep(2)
    driver.refresh()
    time.sleep(5)
    play_button = driver.find_element(By.XPATH, yandex_music_config.play_playlist_xpath)
    play_button.click()


def play_album(album_url):
    url = 'https://music.yandex.ru/' + album_url
    driver.get(url)
    for cookie in pickle.load(open('yandex_music_cookies', 'rb')):
        driver.add_cookie(cookie)
    time.sleep(5)
    driver.refresh()
    time.sleep(2)
    play_button = driver.find_element(By.XPATH, yandex_music_config.play_album_xpath)
    play_button.click()


def search(request):
    url = 'https://music.yandex.ru/search?text=' + request
    data = get_data(url)
    soup = BeautifulSoup(data, 'lxml')

    result = {}
    playlists_links = []
    artists_link = []
    albums_link = []
    tracks_links = []

    playlists = soup.find_all('div', class_="playlist playlist_selectable")
    artists = soup.find_all('div', class_="artist")
    albums = soup.find_all('div', class_="album album_selectable")
    tracks = soup.find_all('div', class_="d-track typo-track d-track_selectable d-track_with-cover")

    for playlist in playlists:
        link = playlist.find('div', class_='playlist__title deco-typo typo-main').find('a', class_='d-link deco-link playlist__title-cover').get('href')
        playlists_links.append(link)

    for artist in artists:
        link = artist.find('div', class_="artist__name deco-typo typo-main").find('span', class_="d-artists").find('a', class_='d-link deco-link').get('href')
        artists_link.append(link)

    for album in albums:
        link = album.find('div', class_="album__bottom").find('div', class_="album__bottom-right").find('a', class_='d-link deco-link album__caption').get('href')
        albums_link.append(link)

    for track in tracks:
        link = track.find('div', class_="d-track__overflowable-column").find('div', class_="d-track__overflowable-wrapper deco-typo-secondary")\
            .find('div', class_='d-track__name').find('a', class_='d-track__title deco-link deco-link_stronger').get('href')
        tracks_links.append(link)


    result = {'playlists': playlists_links, 'artists': artists_link, 'albums': albums_link, 'tracks': tracks_links}
    return result


def genre_playlist(genre):
    url = yandex_music_genre_links.get_link(genre)
    driver.get(url)
    for cookie in pickle.load(open('yandex_music_cookies', 'rb')):
        driver.add_cookie(cookie)
    time.sleep(3)
    driver.refresh()
    time.sleep(5)
    play_button = driver.find_element(By.XPATH, yandex_music_config.play_playlist_xpath)
    play_button.click()


def play_user():
    playlist = get_liked_tracks()
    play_playlist(playlist)


def play_author(artist):
    url = 'https://music.yandex.ru/' + artist
    driver.get(url)
    for cookie in pickle.load(open('yandex_music_cookies', 'rb')):
        driver.add_cookie(cookie)
    time.sleep(2)
    driver.refresh()
    time.sleep(5)
    play_button = driver.find_element(By.XPATH, yandex_music_config.play_artist_xpath)
    play_button.click()


def pause():
    play_button = driver.find_element(By.XPATH, yandex_music_config.play_track_xpath)
    play_button.click()


def loop():
    loop = yandex_music_config.loop_consist
    if loop == 0:
        play_button = driver.find_element(By.XPATH, yandex_music_config.loop_xpath)
        play_button.click()
        yandex_music_config.loop_consist = 1
    elif loop == 1:
        pass
    elif loop == 2:
        play_button = driver.find_element(By.XPATH, yandex_music_config.loop_xpath)
        play_button.click()
        time.sleep(0.1)
        play_button.click()
        yandex_music_config.loop_consist = 1


def loop_one():
    loop = yandex_music_config.loop_consist
    if loop == 0:
        play_button = driver.find_element(By.XPATH, yandex_music_config.loop_xpath)
        play_button.click()
        time.sleep(0.1)
        play_button.click()
        yandex_music_config.loop_consist = 2
    elif loop == 1:
        play_button = driver.find_element(By.XPATH, yandex_music_config.loop_xpath)
        play_button.click()
        yandex_music_config.loop_consist = 2
    elif loop == 2:
        pass


def unloop():
    loop = yandex_music_config.loop_consist
    if loop == 0:
        pass
    elif loop == 1:
        play_button = driver.find_element(By.XPATH, yandex_music_config.loop_xpath)
        play_button.click()
        time.sleep(0.1)
        play_button.click()
        yandex_music_config.loop_consist = 0
    elif loop == 2:
        play_button = driver.find_element(By.XPATH, yandex_music_config.loop_xpath)
        play_button.click()
        yandex_music_config.loop_consist = 0


def shuffle():
    play_button = driver.find_element(By.XPATH, yandex_music_config.shuffle_xpath)
    play_button.click()


def hq():
    play_button = driver.find_element(By.XPATH, yandex_music_config.hq_xpath)
    play_button.click()


def mute():
    play_button = driver.find_element(By.XPATH, yandex_music_config.volume_button_xpath)
    play_button.click()


def play_my_vibe():
    url = 'https://music.yandex.ru/home'
    driver.get(url)
    for cookie in pickle.load(open('yandex_music_cookies', 'rb')):
        driver.add_cookie(cookie)
    time.sleep(5)
    driver.refresh()
    time.sleep(2)
    play_button = driver.find_element(By.XPATH, yandex_music_config.my_vibe_xpath)
    play_button.click()


def next_track():
    play_button = driver.find_element(By.XPATH, yandex_music_config.next_xpath)
    play_button.click()


def previous_track():
    play_button = driver.find_element(By.XPATH, yandex_music_config.previous_xpath)
    play_button.click()


def like():
    play_button = driver.find_element(By.XPATH, yandex_music_config.like_xpath)
    play_button.click()


def play_track_in_album(track_url):
    url = 'https://music.yandex.ru/' + track_url
    driver.get(url)
    for cookie in pickle.load(open('yandex_music_cookies', 'rb')):
        driver.add_cookie(cookie)
    time.sleep(3)
    driver.refresh()
    time.sleep(4)
    play_button = driver.find_element(By.XPATH, yandex_music_config.play_open_track_xpath)
    play_button.click()


def get_liked_user_playlists():
    url = 'https://music.yandex.ru/users/' + config.yandex_music_login + '/playlists'
    data = get_data(url)
    result = []
    soup = BeautifulSoup(data, 'lxml')

    element = soup.p

    playlists = soup.find_all('span', class_="d-link deco-link playlist__title-link")
    for playlist in playlists:
        name = playlist.find('a').get('href')
        result.append(name)
    result = result[1:]
    return result


def play_liked_user_playlists(playlist_num=0):
    plsylists = get_liked_user_playlists()
    playlist = plsylists[playlist_num]

    play_playlist(playlist)


def get_liked_tracks():
    url = 'https://music.yandex.ru/users/' + config.yandex_music_login + '/playlists'
    data = get_data(url)
    result = []
    soup = BeautifulSoup(data, 'lxml')

    like_playlist = soup.find('span', class_="d-link deco-link playlist__title-link").find('a').get('href')
    return like_playlist


def get_new_releases():
    url = 'https://music.yandex.ru/new-releases'
    data = get_data(url)

def get_playing_song_text():
    pass


def get_name_and_artist():
    pass


def block_track():
    pass


def get_name_and_artist_playing_song():
    pass

