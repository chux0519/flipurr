from mastodon import Mastodon

def new_toot_app(app_name, secret_file = 'toot_clientcred.secret', api_base_url='https://mastodon.social'):
    Mastodon.create_app(
         app_name,
         api_base_url = api_base_url,
         to_file = secret_file
    )

def new_toot_client(user_name, password, user_secret_file='toot_usercred.secret', secret_file = 'purrbot_clientcred.secret', api_base_url='https://mastodon.social'):
    toot = Mastodon(
        client_id = secret_file,
        api_base_url = api_base_url
    )
    toot.log_in(
        user_name,
        password,
        to_file = user_secret_file
    )
    return toot

def new_purr_toot(toot, input_img, output_img, msg):
    try:
        origin_media = toot.media_post(media_file=input_img, mime_type="image/jpeg")
        after_media = toot.media_post(media_file=output_img, mime_type="image/jpeg")
        # create the post with the media id
        toot.status_post(msg, media_ids=[origin_media['id'], after_media['id']])
    except Exception as inst:
        print("Mastodon ERR {}".format(inst))

