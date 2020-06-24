import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--user_info_dir', type=str, default='userInfo', help='location of database for user information')
parser.add_argument('--user_info_db', type=str, default='userInfo.db', help='name of database for user information')
parser.add_argument('--ip_name', type=str, default='ip')
parser.add_argument('--user_id_name', type=str, default='user_id')
parser.add_argument('--respond_name', type=str, default='res')
parser.add_argument('--image_title_name', type=str, default='image_name')
parser.add_argument('--image_name', type=str, default='image')
parser.add_argument('--server_url', type=str, default='http://ec2-13-125-237-47.ap-northeast-2.compute.amazonaws.com')


def get_config():
    return parser.parse_args()
