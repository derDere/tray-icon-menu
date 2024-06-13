"""Contains the main function that runs the program.
"""


#from config import CmdMenuConfig, ConfigObject, CmdEntryConfig, CmdTextConfig, loads_config

import pystray

from PIL import Image, ImageDraw


class App:
  """The main application class.
  """

  def __init__(self):
    #self.config:CmdMenuConfig = None
    self.exit_code:int = -1

  def run(self, *_) -> None:
    """Runs the application.
    """

    _ = """
    # Load the config
    jj = ""
    {
      "T1": ["Line1", "Line2", {"date": "/t"}],
      "SubMenu": {
        "T3": ["Line3", "Line4"],
        "Cmd1": "echo lol1"
      },
      "Cmd2": "echo lol2&read"
    }
    ""
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

    menu = pystray.Menu(
      pystray.MenuItem('Exit', lambda: icon.stop()),
    )

    icon = pystray.Icon('test name', icon=create_image(), menu=menu)
    icon.run()
    icon.stop()

    self.exit_code = 0


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
