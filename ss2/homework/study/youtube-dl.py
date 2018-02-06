from youtube_dl import YoutubeDL

# dl.download(['https://www.youtube.com/watch?v=WHK5p7JL7g4'])
# dl.download(['https://www.youtube.com/watch?v=wNVIn-QS4DE', 'https://www.youtube.com/watch?v=JZjRrg2rpic'])
# option = {
#     'format':'bestaudio/audio'
# }
# dl = YoutubeDL(option)
# dl.download(['https://www.youtube.com/watch?v=c3jHlYsnEe0'])
# options = {
#     'default_search':'ytsearch',
#     'max_downloads': 1,
#     'format':'bestaudio/audio'
# }
# dl = YoutubeDL(options)
# dl.download(['Nhớ mưa sài gòn Lam Trường'])
options ={
    'default_search' : 'ytsearch',
    'max_downloads' : 1,
}
dl = YoutubeDL(options)
dl.download(['con dien tam ka pkl'])
