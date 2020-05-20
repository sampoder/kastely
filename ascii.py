from pyfiglet import Figlet

def ascii(text):

  custom_fig = Figlet(font = "banner3")

  ascii_banner = custom_fig.renderText(text)

  print(ascii_banner)