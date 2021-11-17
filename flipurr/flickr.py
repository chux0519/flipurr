import flickr_api
import datetime as dt

def init_flickr_client(api_key, api_secret):
    flickr_api.set_keys(api_key = api_key, api_secret = api_secret)

def fetch_interesting_photo(save_dir="/tmp"):
    photos = flickr_api.Photo.getInteresting()
    idx = dt.datetime.today().hour
    photo = photos[idx]
    size_label = photo._getLargestSizeLabel()
    photo_url = photo.getPhotoUrl()
    photo_info = photo.getInfo()
    print(photo_info)
    photo_file = photo.getPhotoFile(size_label)
    file_ext = ('.' + photo_file.split('.')[-1]) if photo.media == "photo" else ".mp4"
    file_name = "{}/input".format(save_dir)
    full_name = file_name + file_ext
    if photo:
        photo.save(file_name, size_label = size_label)
        print("saved {} to {}".format(photo_url, full_name))
        return full_name, photo
    return '', None
