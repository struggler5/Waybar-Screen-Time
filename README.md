# Waybar-Screen-Time
A simple screentime widget for waybar
<img width="884" height="66" alt="image" src="https://github.com/user-attachments/assets/ef75f81f-5cbf-4ca3-b885-f78d34065fbe" />

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
