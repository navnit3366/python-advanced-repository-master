from pyfiglet import figlet_format


def draw_figure(txt):
    print(figlet_format(txt))


draw_figure(txt=input())
