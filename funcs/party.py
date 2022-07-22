import disnake

def party_activity(activity):
    match activity:
        case 'watch_together':
            return disnake.PartyType.watch_together
        case 'poker':
            return disnake.PartyType.poker
        case 'word_snack':
            return disnake.PartyType.word_snack
        case 'spellcast':
            return disnake.PartyType.spellcast
        case 'sketch_heads':
            return disnake.PartyType.sketch_heads
        case 'ocho':
            return disnake.PartyType.ocho
        case 'chess':
            return disnake.PartyType.chess
        case 'fishing':
            return disnake.PartyType.fishing
        case 'betrayal':
            return disnake.PartyType.betrayal
        case 'letter_tile':
            return disnake.PartyType.letter_tile
        case 'checkers':
            return disnake.PartyType.checkers

async def party_invite(voice, activity):
    invite = await voice.create_invite(
        target_type = disnake.InviteTarget.embedded_application, 
        target_application = activity,
        max_age = 300
    )
    return invite

def party_button(invite):
    item = disnake.ui.Button(
        style = disnake.ButtonStyle.url, 
        label = "Click me!", 
        url = f"{invite}"
    )
    return item