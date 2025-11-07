def new_text(text):
    while '(' in text:
        start = text.find('(')
        end = text.find(')', start)
        text = text[:start] + text[end+1:]
    return text

orig = "Падал (куда он там падал) прошлогодний (значит очень старый) снег (а почему не дождь)."
result = new_text(orig)

print(result)