import disnake

def party_button(invite):
    item = disnake.ui.Button(
        style = disnake.ButtonStyle.url, 
        label = "Click me!", 
        url = f"{invite}"
    )
    return item