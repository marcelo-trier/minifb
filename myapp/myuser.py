
from . import myimg

class User:
  def __init__(self, user, login, email, pwd, imgpath):
    self._user = user
    self._login = login
    self._email = email
    self._pwd = pwd

    if not isinstance(imgpath, str):
      imgpath = self.process_img(imgpath)

    self._imgpath = imgpath

  def process_img(self, imgobj):
    imgname = myimg.mysave(imgobj)
    return imgname
