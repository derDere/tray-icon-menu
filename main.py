"""Contains the main function that runs the program.
"""


from config import CmdMenuConfig, ConfigObject, CmdEntryConfig, CmdTextConfig, loads_config


class App:
  """The main application class.
  """

  def __init__(self):
    self.config:CmdMenuConfig = None
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

    self.exit_code = 0


def printobj(obj:ConfigObject) -> None:
  """Prints the object.
  """
  print(str(obj))


def main(*args) -> int:
  """Runs the program.
  """
  app:App = App()
  app.run(*args)
  return app.exit_code


if __name__ == "__main__":
  import sys
  sys.exit(main(*sys.argv[1:]))
