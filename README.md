# Waybar-Screen-Time
A simple screentime widget for waybar
<img width="1360" height="60" alt="image" src="https://github.com/user-attachments/assets/9dd41f57-d612-474f-b2df-513768105ef0" />

## Dependencies
### scrntime
[https://pypi.org/project/scrntime/](https://github.com/sahaj-b/scrntime/tree/main)

# 1 Add the way_tim.py file to your waybar directory

# 2 Add this to the config file

```
"custom/screen_time":{
        "exec":"$HOME/.config/waybar/way_tim.py",
        "interval":30

    }
```

# 3 Add  "custom/screen_time" to wichever module you want

*restart might be necessary*
