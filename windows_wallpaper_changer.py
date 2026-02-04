import win32api, win32con, win32gui

def set_wallpaper(image_path):
    # Définir le style du fond d'écran (0 = centered, 1 = tiled, 2 = stretched)
    style = '2'  # Exemple : '2' pour étirer l'image

    # Ouvrir la clé de registre où Windows stocke ses paramètres de fond d'écran
    key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)

    # Définir le style du fond d'écran
    win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, style)
    win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, '0')

    # Changer le fond d'écran
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, image_path, 1 + 2)

# Chemin vers l'image de fond d'écran que vous souhaitez définir
original_wallpaper_path = "C:/Users/YourUsername/Pictures/wallpaper.png"  # Adjust to your image path

# Appel de la fonction pour changer le fond d'écran
set_wallpaper(original_wallpaper_path)
