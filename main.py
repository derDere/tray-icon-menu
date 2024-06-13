"""Contains the main function that runs the program.
"""


import os
from pathlib import Path
import pystray
from PIL import Image, ImageDraw
from config import CmdConfigBase, CmdEntryConfig, CmdMenuConfig, CmdTextConfig


class Config(CmdConfigBase):
  """The configuration class.
  """
  def __init__(self):
    super().__init__(self._get_conf_path())

  def _to_json_obj(self) -> list | str | dict | None:
    return super()._to_json_obj()

  def _from_json_obj(self, json_obj: list | str | dict | None) -> None:
    return super()._from_json_obj(json_obj)

  def _get_conf_path(self) -> str:
    """Returns the path to the configuration file.
    """
    path = "~/.config/cmdmenu/cmds.json"
    path = path.replace("~", str(Path.home()))
    return path



class App:
  """The main application class.
  """

  icon:pystray.Icon

  def __init__(self):
    self.config:Config = Config()
    self.exit_code:int = -1

  def run(self, *_) -> None:
    """Runs the application.
    """

    # Load the config
    jj = """
    {
      "T1": ["Line1", "Line2", {"date": "/t"}],
      "SubMenu": {
        "T3": ["Line3", "Line4"],
        "Cmd1": "echo lol1"
      },
      "Cmd2": "echo lol2&read"
    }
    """
    _ = """
    print(jj)
    self.config = loads_config(jj)

    for itm in self.config.items:
      print(type(itm).__name__, itm.key)

    print("#####################################################")

    # Print the config
    print(self.config.to_json_str())

    print("#####################################################")

    for itm in self.config.items:
      printobj(itm)
    """

    self.config.loads(jj)
    items = []

    for itm in self.config.root_menu.items:
      items += self._cmd_obj_to_menu_item(itm)

    items.append(pystray.MenuItem('─' * 20, None, enabled=False))
    items.append(pystray.MenuItem('Exit', self.stop))
    menu = pystray.Menu(*items)

    self.icon = pystray.Icon('test name', icon=create_image(), menu=menu)
    self.icon.run()

    self.exit_code = 0

  def _cmd_obj_to_menu_item(self, cmd_obj) -> list[pystray.MenuItem]:
    """Converts a command object to a menu item.
    """
    if isinstance(cmd_obj, CmdTextConfig):
      return list(map(lambda line: pystray.MenuItem(line, None, enabled=False), str(cmd_obj).split("\n")))

    if isinstance(cmd_obj, CmdMenuConfig):
      items = []
      for itm in cmd_obj.items:
        items += self._cmd_obj_to_menu_item(itm)
      return [pystray.MenuItem(cmd_obj.key, pystray.Menu(*items))]

    if isinstance(cmd_obj, CmdEntryConfig):
      return [pystray.MenuItem(cmd_obj.key, lambda: self._menuitem_clicked(cmd_obj))]

    return []

  def _menuitem_clicked(self, item) -> None:
    """Called when a menu item is clicked.
    """
    os.system(item.cmd)

  def stop(self) -> None:
    """Stops the application.
    """
    self.icon.stop()


def create_image():
  """Generate an image and draw a pattern
  """
  SIZE = 24
  MARGINX = 3
  MARGINY = 5
  HEIGHT = 3
  PADDING = 1
  image = Image.new('RGBA', (SIZE, SIZE), 'rgba(0,0,0,0)')
  dc = ImageDraw.Draw(image)
  for i in range(5):
    if i % 2 == 0:
      x0 = MARGINX
      x1 = SIZE - MARGINX
      y0 = MARGINY + (i * HEIGHT)
      y1 = MARGINY + ((i + 1) * HEIGHT)
      dc.rectangle([x0, y0, x1, y1], fill='rgba(0,0,0,128)')

      x0 = MARGINX + PADDING
      x1 = SIZE - MARGINX - PADDING
      y0 = MARGINY + (i * HEIGHT) + PADDING
      y1 = MARGINY + ((i + 1) * HEIGHT) - PADDING
      dc.rectangle([x0, y0, x1, y1], fill='white')
  return image


def main(*args) -> int:
  """Runs the program.
  """
  app:App = App()
  app.run(*args)
  return app.exit_code


if __name__ == "__main__":
  import sys
  sys.exit(main(*sys.argv[1:]))
