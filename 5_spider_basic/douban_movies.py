# -*- coding: utf-8 -*-
import urllib2

def nowplaying_movies(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)\
                   AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73\
                   Safari/537.36'}
    req = urllib2.Request(url, headers=headers)
    s = urllib2.urlopen(req)
    parser = MovieParser() # 这是另外准备好的电影解析器
    parser.feed(s.read)  # 给解析器喂数据
    s.close()
    return parser.movies  # 解析器解析后返回解析好的电影


if __name__ == '__main__':
    url = 'https://movie.douban.com/nowplaying/xiamen/'
    movies = nowplaying_movies(url)

    import json
    print('%s' % json.dumps(
        movies, sort_keys=True, indent=4, separators=(',', ': ')))
