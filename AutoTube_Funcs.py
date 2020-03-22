from time import sleep
from selenium import webdriver
from pytube import YouTube, Playlist
import os


# TODO: add the ability to specify a download path

def ui():
    print('*****************Welcome to AutoTube!*****************\n\n')
    print('Please choose an option from the list:')
    print(' 1- Google     | 2- Youtube\n')
    choice = input()

    if choice == '1':
        print('Please choose what do you want to do:\n')
        print(' 1- Search Google    | 2- Search only a specific site in Google\n')
        command = input()

        if command == '1':
            print('Please enter what do you want to search for:\n')
            search_term = input()
            search(search_term, 'google')

        elif command == '2':
            print('Please choose one of the available sites:')
            print(' 1- Reddit    | 2- StackOverFlow')
            site = input()

            if site == '1':
                print('Please enter what do you want to search for:\n')
                search_term = input() + ' site:reddit.com'
                search(search_term, 'google')

            elif site == '2':
                print('Please enter what do you want to search for:\n')
                search_term = input() + ' site:stackoverflow.com'
                search(search_term, 'google')

        else:
            print('PLease choose on of the available options')

    elif choice == '2':
        print('Please choose what do you want to do:\n')
        print(' 1- Search Youtube    | 2- Download a youtube video | 3- Download a playlist')
        command = input()

        if command == '1':
            print('Please enter what do you want to search for:\n')
            search_term = input()
            search(search_term, 'youtube')

        elif command == '2':
            print("Please enter the video's url here:\n")
            url = input()
            download('video', url)
        elif command == '3':
            print("Please enter the playlist's url here:\n")
            url = input()
            download('playlist', url)


def search(search_term, site):
    # sets firefox as the browser
    browser = webdriver.Firefox(executable_path='E:\\geckodriver\\geckodriver.exe')
    browser.maximize_window()

    # go to a webpage
    if site == 'youtube':
        browser.get('https://www.youtube.com')

        # get the search box element
        search_box = browser.find_elements_by_id('search')[2]
        search_box.click()

        # search for the entered term and submit it
        search_box.send_keys(search_term)
        search_box.submit()

    elif site == 'google':
        browser.get('https://www.google.com')
        sleep(6)

        # get the search box element
        search_box = browser.find_element_by_css_selector('.gLFyf')
        search_box.click()

        # search for the entered term and submit it
        search_box.send_keys(search_term)
        search_box.submit()


def download(what, url):
    if what == 'video':
        i = 0
        print('Getting the video...')
        yt = YouTube(url)
        print('Done!\n')

        print('Please choose one of the available streams:\n')
        while i < len(yt.streams):
            print(str(i + 1) + '- ' + str(yt.streams[i]))
            i = i + 1
        choice = input()

        print('Downloading...')
        yt.streams[int(choice) - 1].download()
        print('Download complete!')

    elif what == 'playlist':

        i = 0
        print('Getting the playlist...')
        playlist = Playlist(url)
        print('Done!\n')

        first_video = YouTube(playlist[0])
        print('Please choose one of the available streams:\n')
        while i < len(first_video.streams):
            print(str(i + 1) + '- ' + str(first_video.streams[i]))
            i = i + 1
        choice = input()

        print('Downloading...')
        for item in playlist:
            item.streams[int(choice) - 1].download()
