# Windows Wallpaper Changer

Simple Python script to programmatically change Windows desktop wallpaper.

## Description

This utility allows you to set a Windows desktop wallpaper using Python and the Windows API through the `pywin32` library.

## Prerequisites

- Windows OS
- Python 3.x
- pywin32 library

## Installation

```bash
# Install required package
pip install pywin32
```

## Usage

### Basic Usage

```python
from windows_wallpaper_changer import set_wallpaper

# Set wallpaper with full path
set_wallpaper("C:/Users/YourName/Pictures/wallpaper.png")
```

### Command Line

```bash
python windows_wallpaper_changer.py
```

Edit the script to change the `original_wallpaper_path` variable to your desired image path.

## Configuration

### Wallpaper Styles

The script supports different wallpaper styles:

| Style | Value | Description |
|-------|-------|-------------|
| Centered | 0 | Image centered on screen |
| Tiled | 1 | Image tiled across screen |
| Stretched | 2 | Image stretched to fit |

To change the style, modify the `style` variable in the script.

## Supported Formats

- PNG
- JPG/JPEG
- BMP
- GIF (static)

## Example

```python
import win32api, win32con, win32gui

def set_wallpaper(image_path, style='2'):
    """
    Set Windows desktop wallpaper.

    Args:
        image_path: Full path to the image file
        style: '0' = centered, '1' = tiled, '2' = stretched
    """
    key = win32api.RegOpenKeyEx(
        win32con.HKEY_CURRENT_USER,
        "Control Panel\\Desktop",
        0,
        win32con.KEY_SET_VALUE
    )
    win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, style)
    win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, '0')
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, image_path, 1 + 2)

# Usage
set_wallpaper("C:/path/to/your/image.png")
```

## Troubleshooting

### "Module not found" error
```bash
pip install pywin32
```

### Wallpaper not changing
- Ensure the image path is absolute (full path)
- Check that the image file exists
- Run the script with administrator privileges if needed

### Image format issues
Convert your image to PNG or BMP format for best compatibility.

## License

MIT License - See LICENSE file for details.

## Requirements

```
pywin32
```
