PARSER_FIELDS = ['pose', 'feelings', 'depth_image', 'color_image']

USER = {
    'user_id': 1,
    'username': 'Dr Heinz Doofenshmirtz',
    'birthday': 1000,
    'gender': 0
}

POSE = {
    'rotation': {
        'x': 0.31, 'y': 0.315, 'z': 0.32, 'w': 0.325
    },
    'position': {
        'x': 0.21, 'y': 0.215, 'z': 0.22
    }
}

FEELINGS = {
    'hunger': 0.1, 'thirst': 0.15, 'exhaustion': 0.2, 'happiness': 0.25
}

COLOR_IMAGE = {
    'path': 'col_img'
}

DEPTH_IMAGE = {
    'path': 'dpt_img'
}

SNAPSHOT = {
    'user_id': 1,
    'snap_id': 2,
    'feelings': FEELINGS,
    'pose': POSE,
    'color_image': COLOR_IMAGE,
    'depth_image': DEPTH_IMAGE,
    'datetime': '1234'
}


RAW_SNAPSHOT = b'\x84\x00\x00\x00\x03data\x00L\x00\x00\x00\x01hunger\x00\x9a\x99\x99\x99\x99\x99\xb9?\x01thirst\x00333333\xc3?\x01exhaustion\x00\x9a\x99\x99\x99\x99\x99\xc9?\x01happiness\x00\x00\x00\x00\x00\x00\x00\xd0?\x00\x02datetime\x00\x05\x00\x00\x001234\x00\x10snap_id\x00\x02\x00\x00\x00\x10user_id\x00\x01\x00\x00\x00\x00'
