import os
import base64
import uuid
import requests
 
def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

LIMIT = 200 * 1024
def new_purr_post(api_base_url, jwt, group_id, msg, input_img, output_img):
    s = os.path.getsize(output_img)
    ret = None
    headers = {'authorization': "Bearer {}".format(jwt)}
    if s >= 200*1024:
        # TODO: compress before send it
        print("too big, skip")
    else:
        # send it directly
        json = {
                'type': 'Add', 
                'object': {
                    'type': 'Note',
                    'content': msg, 
                    'name': '', 
                    'image':[
                        {
                            'content': get_base64_encoded_image(output_img),
                            'mediaType': 'image/jpeg',
                            'name': str(uuid.uuid4()),
                        }
                    ]
                },
                'target': {
                    'id': group_id,
                    'type': 'Group'
                }
        }
        ret = requests.post("{}/api/v1/group/content".format(api_base_url), json=json, headers=headers, verify=False).json()

    return ret
