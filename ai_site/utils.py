import os
import secrets
import urllib.request

from PIL import Image
from bs4 import BeautifulSoup

from ai_site import app


def save_picture(form_picture, folder):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/', folder, picture_fn)

    output_size = (1280, 720)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


def delete_picture(folder, filename):
    os.remove(os.path.join(app.root_path, 'static/', folder, filename))


@app.template_filter('scholar_h_index')
def get_scholar_h_index(user_id):
    url = "https://scholar.google.ca/citations?user=" + user_id + "&hl=en"
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    indexes = soup.find_all("td", "gsc_rsb_std")
    h_index = indexes[2].string
    # i10_index = indexes[4].string
    # citations = indexes[0].string
    return h_index


@app.template_filter('scopus_h_index')
def get_scopus_h_index():
    url = "https://nulp.ovh/"
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    print(soup)
    # resp = requests.get("http://api.elsevier.com/content/author?author_id=7004212771&view=metrics",
    #                     headers={'Accept': 'application/json',
    #                              'X-ELS-APIKey': MY_API_KEY})
    #
    # print(json.dumps(resp.json(), sort_keys=True, indent=4, separators=(',', ': ')))
