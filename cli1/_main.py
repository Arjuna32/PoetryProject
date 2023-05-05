import click
import ctypes


@click.command(no_args_is_help=True, help = "if you want to change your background use the command cli1 --image [image path] or use -i in place of --image ")
@click.option("--image", "-i", help = "image_path")
def cli(image):
    SPI_SETDESKWALLPAPER = 20
    SPIF_UPDATEINIFILE = 0x01
    SPIF_SENDWININICHANGE = 0x02
    
    # Use the SystemParametersInfo function from ctypes to set the desktop wallpaper.
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image, SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE)
    click.echo("hello world!")
    
    #"C:\Users\amaan\OneDrive\Pictures\fgo shenanigans\mash wallpaper.jpg"
    #"C:\Users\amaan\OneDrive\Pictures\fgo shenanigans\junao wallpaper.png"
