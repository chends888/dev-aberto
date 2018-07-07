from jinja2 import Template
import json

if __name__ == "__main__":
    with open('players/player_list_template.html') as f:
        t = Template(f.read())
    
    with open('players/player_list.json') as pfp:
        players = json.load(pfp)
    
    with open('skills/skill_list.json') as pfp:
        skills = json.load(pfp)

    for plr in players:
        plr["raw_img"] = 'https://github.com/igordsm/dev-aberto/raw/master/players/avatar_data/' + plr["avatar_image"]
        plr["xp"] = 0
        plr["level_name"] = "Newbie"

        # parse skill list and achievements
        plr["skills"] = []
        for sk in skills:
            plr["skills"].append(sk.copy())
            plr["skills"][-1]["achieved"] = False

    out = t.render(players=players)

    with open('docs/players.html', 'w') as f:
        f.write(out) 