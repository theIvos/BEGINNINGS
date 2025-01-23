import random
from soul_eater_attacks import *

# SYMBOLS  

# NATURAL  ≡
# SUICIDE  ¤
# VIOLENT  ×
# CHAOTIC  ▒


# EXP LEVEL POINTS
experience_levels = {1: 100, 2:300, 3:700 , 4:1300, 5: 2100, 6:3100, 7:4300, 8:5700, 9:7400,10:9400,11:11600,12:14000, 13:16600,14:19600,15:22800,16:26200,17:29800,18:33600,19:37600,20:41800,21:46200,22:50800,23:55600,24:60600,25:65800,26:99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999}

# CHARACTERS
no_form_levels = {4:light_storm,5:toxic_spit, 6:hypnosis, 12: regenerate}
no_form = {"name": "NO FORM","OG_NAME":"NO FORM","type":"none","status":" OK","speed":3,"OG_speed":3, "atk":2,"OG_atk":2,"dfk":2,"OG_dfk":2, "hp": 50,"base_hp": 50,"current_hp": 50,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0,"level":5, "attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [punch, bodycheck],
"level_list":no_form_levels}

no_form_hellking_levels = {4:light_storm,5:toxic_spit, 6:hypnosis, 12: regenerate,20:hell_power}
no_form_hellking = {"name": "NO FORM","OG_NAME":"HELLKING","type":"hellking","status":" OK","speed":3,"OG_speed":3, "atk":2,"OG_atk":2,"dfk":2,"OG_dfk":2, "hp": 50,"base_hp": 50,"current_hp": 50,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0,"level":22, "attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [],
"level_list":no_form_hellking_levels}

no_form_natural_master = {"name": "NO FORM","OG_NAME":"HELLMASTER","type":"natural","status":" OK","speed":3,"OG_speed":3, "atk":2,"OG_atk":2,"dfk":2,"OG_dfk":2, "hp": 50,"base_hp": 50,"current_hp": 50,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0,"level":18, "attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [punch, bodycheck],
"level_list":no_form_levels}

no_form_violent_master = {"name": "NO FORM","OG_NAME":"HELLMASTER","type":"violent","status":" OK","speed":3,"OG_speed":3, "atk":2,"OG_atk":2,"dfk":2,"OG_dfk":2, "hp": 50,"base_hp": 50,"current_hp": 50,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0,"level":18, "attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [punch, bodycheck],
"level_list":no_form_levels}

no_form_chaotic_master = {"name": "NO FORM","OG_NAME":"HELLMASTER","type":"chaotic","status":" OK","speed":3,"OG_speed":3, "atk":2,"OG_atk":2,"dfk":2,"OG_dfk":2, "hp": 50,"base_hp": 50,"current_hp": 50,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0,"level":18, "attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [punch, bodycheck],
"level_list":no_form_levels}

no_form_suicide_master = {"name": "NO FORM","OG_NAME":"HELLMASTER","type":"suicide","status":" OK","speed":3,"OG_speed":3, "atk":2,"OG_atk":2,"dfk":2,"OG_dfk":2, "hp": 50,"base_hp": 50,"current_hp": 50,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0,"level":18, "attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [punch, bodycheck],
"level_list":no_form_levels}


# POLAR BEAR
polar_bear_natural_levels = {2:roar,3:paw_slap,4:bodycheck,5:claws_sharpening,7:headbutt,11:dust_twister,14:massive_bite}
polar_bear_natural = {"name": "≡ POLAR BEAR","OG_NAME":"POLAR BEAR","type":"natural","status":" OK","speed":1,"OG_speed":1, "atk":4,"OG_atk":4,"dfk":5,"OG_dfk":5, "hp": 70,"base_hp": 70,"current_hp": 70,"hp_coef": 1.5, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0,"level":5,"attack_coef": 1.5,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bite],
"level_list":polar_bear_natural_levels}

polar_bear_violent_levels = {2:roar,3:paw_slap,4:bodycheck,5:slash,7: massive_bite,9: rage, 10: claws_sharpening, 15: deathjump}
polar_bear_violent = {"name": "× POLAR BEAR","OG_NAME":"POLAR BEAR","type":"violent","status":" OK","speed":1,"OG_speed":1, "atk":5,"OG_atk":5,"dfk":4,"OG_dfk":4, "hp": 70,"base_hp": 70,"current_hp": 70,"hp_coef": 1.5, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0,"level":5,"attack_coef": 1.5,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bite],
"level_list":polar_bear_violent_levels}

polar_bear_chaotic_levels = {2:ground_eating,3:claws_sharpening,4:paw_slap,5:fur_armor,7:dust_twister,9: rage, 12:deathjump,15:roar}
polar_bear_chaotic = {"name": "▒ POLAR BEAR","OG_NAME":"POLAR BEAR","type":"chaotic","status":" OK","speed":1,"OG_speed":1, "atk":4,"OG_atk":4,"dfk":5,"OG_dfk":5, "hp": 60,"base_hp": 60,"current_hp": 60,"hp_coef": 1.5, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0,"level":5,"attack_coef": 1.5,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bite],
"level_list":polar_bear_chaotic_levels}

polar_bear_suicide_levels = {2:claws_sharpening,3:paw_slap,4:headbutt,5:dust_twister,6:furball,8:ground_eating,10: deathjump,11:massive_bite,}
polar_bear_suicide = {"name": "¤ POLAR BEAR","OG_NAME":"POLAR BEAR","type":"suicide","status":" OK","speed":1,"OG_speed":1, "atk":3,"OG_atk":3,"dfk":5,"OG_dfk":5, "hp": 70,"base_hp": 70,"current_hp": 70,"hp_coef": 1.5, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0,"level":5,"attack_coef": 1.5,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bite],
"level_list":polar_bear_suicide_levels}


# FOX
fox_natural_levels = {2:bite,3:claws_sharpening,4:ground_eating, 6:dust_twister,8: slash, 11:tail_strangler, 15: massive_bite}
fox_natural = {"name": "≡ FOX","OG_NAME":"FOX","type":"natural","status":" OK","speed":4,"OG_speed":4,"atk":2,"OG_atk":2,"dfk":2,"OG_dfk":2, "hp": 30,"base_hp": 30,"current_hp": 30,"hp_coef": 1.2, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":4,"attack_coef": 1.2,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [scratch],
"level_list":fox_natural_levels}

fox_violent_levels = {2:bite,3:claws_sharpening,4:slash,6:accelerate,8:tail_strangler, 12: massive_bite, 17: clawstorm}
fox_violent = {"name": "× FOX","OG_NAME":"FOX","type":"violent","status":" OK","speed":3,"OG_speed":3,"atk":3,"OG_atk":3,"dfk":1,"OG_dfk":1, "hp": 30,"base_hp": 30,"current_hp": 30,"hp_coef": 1.2, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":4,"attack_coef": 1.2,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [scratch],
"level_list":fox_violent_levels}

fox_chaotic_levels = {2:accelerate,3:rage,4:ground_eating,6:furball, 7:dust_twister, 10:tail_strangler, 13: hypnosis, 16:light_storm, 21: clawstorm }
fox_chaotic = {"name": "▒ FOX","OG_NAME":"FOX","type":"chaotic","status":" OK","speed":4,"OG_speed":4,"atk":2,"OG_atk":2,"dfk":2,"OG_dfk":2, "hp": 25,"base_hp": 25,"current_hp": 25,"hp_coef": 1.2, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":4,"attack_coef": 1.2,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [scratch],
"level_list":fox_chaotic_levels}

fox_suicide_levels = {2:ground_eating,3:dust_twister, 4:tail_strangler, 5:bite,7:fur_armor,9:slash, 11:rage, 15: clawstorm}
fox_suicide = {"name": "¤ FOX","OG_NAME":"FOX","type":"suicide","status":" OK","speed":3,"OG_speed":3,"atk":1,"OG_atk":1,"dfk":3,"OG_dfk":3, "hp": 30,"base_hp": 30,"current_hp": 30,"hp_coef": 1.2, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":4,"attack_coef": 1.2,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [scratch],
"level_list":fox_suicide_levels}


# WOLF
wolf_natural_levels = {2:scratch,3:claws_sharpening,4:bodycheck,6:ground_eating,8:accelerate,10:massive_bite,14:rage}
wolf_natural = {"name": "≡ WOLF","OG_NAME":"WOLF","type":"natural","status":" OK","speed":3,"OG_speed":3,"atk":4,"OG_atk":4,"dfk":2,"OG_dfk":2, "hp": 45,"base_hp": 45,"current_hp": 45,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":4,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bite],
"level_list":wolf_natural_levels}

wolf_violent_levels = {2:paw_slap,3:claws_sharpening,4:bodycheck,5:slash,7:clawstorm,11:massive_bite,16:rage}
wolf_violent = {"name": "× WOLF","OG_NAME":"WOLF","type":"violent","status":" OK","speed":2,"OG_speed":2,"atk":5,"OG_atk":5,"dfk":1,"OG_dfk":1, "hp": 45,"base_hp": 45,"current_hp": 45,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":4,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bite],
"level_list":wolf_violent_levels}

wolf_chaotic_levels = {2:scratch,3:ground_eating,5:rage,6:accelerate,7:fur_armor,9:furball,13:massive_bite,14:clawstorm}
wolf_chaotic = {"name": "▒ WOLF","OG_NAME":"WOLF","type":"chaotic","status":" OK","speed":3,"OG_speed":3,"atk":4,"OG_atk":4,"dfk":2,"OG_dfk":2, "hp": 40,"base_hp": 40,"current_hp": 40,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":4,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bite],
"level_list":wolf_chaotic_levels}

wolf_suicide_levels = {2:fur_armor,3:furball,4:dust_twister,6:paw_slap,8:headbutt,10:clawstorm,15:tail_strangler}
wolf_suicide = {"name": "¤ WOLF","OG_NAME":"WOLF","type":"suicide","status":" OK","speed":2,"OG_speed":2,"atk":3,"OG_atk":3,"dfk":3,"OG_dfk":3, "hp": 45,"base_hp": 45,"current_hp": 45,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":4,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bite, ground_eating],
"level_list":wolf_suicide_levels}


# VIPER
viper_natural_levels = {3:whip,4:snake_dance,5:harding_scales,6:tail_strangler,9:toxic_spit,11: tail_strike}
viper_natural = {"name": "≡ VIPER","OG_NAME":"VIPER","type":"natural","status":" OK","speed":5,"OG_speed":5,"atk":3,"OG_atk":3,"dfk":1,"OG_dfk":1, "hp": 20,"base_hp": 20,"current_hp": 20,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":15,"attack_coef": 1.4,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [poison_bite,detox],
"level_list":viper_natural_levels}

viper_violent_levels = {3:whip,4:toxic_spit,5:tail_strangler,6:tail_strike,8:massive_bite,15: rain_of_poison}
viper_violent = {"name": "× VIPER","OG_NAME":"VIPER","type":"violent","status":" OK","speed":4,"OG_speed":4,"atk":4,"OG_atk":4,"dfk":1,"OG_dfk":1, "hp": 20,"base_hp": 20,"current_hp": 20,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.4,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [poison_bite,detox],
"level_list":viper_violent_levels}

viper_chaotic_levels = {3:snake_dance,4:hypnosis,5:tail_strangler,6:venom_fusion, 7:toxic_spit,9:tail_strike, 11:headbutt, 14: bloodshot, 20: rain_of_poison}
viper_chaotic = {"name": "▒ VIPER","OG_NAME":"VIPER","type":"chaotic","status":" OK","speed":5,"OG_speed":5,"atk":3,"OG_atk":3,"dfk":1,"OG_dfk":1, "hp": 17,"base_hp": 17,"current_hp": 17,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.4,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [poison_bite,detox],
"level_list":viper_chaotic_levels}

viper_suicide_levels = {3:toxic_spit,4:whip,5:tail_strike,6:bloodshot,7:snake_dance,9:tail_strangler}
viper_suicide = {"name": "¤ VIPER","OG_NAME":"VIPER","type":"suicide","status":" OK","speed":4,"OG_speed":4,"atk":2,"OG_atk":2,"dfk":2,"OG_dfk":2, "hp": 20,"base_hp": 20,"current_hp": 20,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.4,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [poison_bite,detox],
"level_list":viper_suicide_levels}


# EAGLE
eagle_natural_levels = {2:beak_drill,3:accelerate,4:feather_tornado,6:spur_blade,7:air_bomb,10:eye_of_ra,12: clawstorm}
eagle_natural = {"name": "≡ EAGLE","OG_NAME":"EAGLE","type":"natural","status":" OK","speed":5,"OG_speed":5,"atk":3,"OG_atk":3,"dfk":1,"OG_dfk":1, "hp": 30,"base_hp": 30,"current_hp": 30,"hp_coef": 1.2, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [peck,wing_slap],
"level_list":eagle_natural_levels}

eagle_violent_levels = {2:peck,3:air_bomb,4:slash,5:spur_blade,7:clawstorm,10:kick,11:tail_strike,14: rage}
eagle_violent = {"name": "× EAGLE","OG_NAME":"EAGLE","type":"violent","status":" OK","speed":4,"OG_speed":4,"atk":4,"OG_atk":4,"dfk":1,"OG_dfk":1, "hp": 30,"base_hp": 30,"current_hp": 30,"hp_coef": 1.2, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":16,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [beak_drill,wing_slap],
"level_list":eagle_violent_levels}

eagle_chaotic_levels = {2:accelerate,3:headbutt,4:spur_blade,6:feather_tornado,7:bodycheck,9:air_bomb,11:eye_of_ra,15: clawstorm}
eagle_chaotic = {"name": "▒ EAGLE","OG_NAME":"EAGLE","type":"chaotic","status":" OK","speed":5,"OG_speed":5,"atk":3,"OG_atk":3,"dfk":1,"OG_dfk":1, "hp": 26,"base_hp": 26,"current_hp": 26,"hp_coef": 1.2, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":16,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [peck,kick],
"level_list":eagle_chaotic_levels}

eagle_suicide_levels = {2:feather_tornado,3:spur_blade,4:cold_wind,5:air_bomb,8:headbutt,9:eye_of_ra,12: clawstorm}
eagle_suicide = {"name": "¤ EAGLE","OG_NAME":"EAGLE","type":"suicide","status":" OK","speed":5,"OG_speed":5,"atk":3,"OG_atk":3,"dfk":1,"OG_dfk":1, "hp": 30,"base_hp": 30,"current_hp": 30,"hp_coef": 1.2, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [peck,wing_slap],
"level_list":eagle_suicide_levels}


# BOAR
boar_natural_levels = {2:bite,3:tusk_attack,5:grounddigger,7:foulbreath,9:accelerate,10:rage,16: headbutt}
boar_natural = {"name": "≡ WILD BOAR","OG_NAME":"WILD BOAR","type":"natural","status":" OK","speed":1,"OG_speed":1,"atk":5,"OG_atk":5,"dfk":4,"OG_dfk":4, "hp": 66,"base_hp": 66,"current_hp": 66,"hp_coef": 1.5, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.5,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bodycheck],
"level_list":boar_natural_levels}

boar_violent_levels = {2:tusk_attack,3:rage,4:bite,5:headbutt,7:kick,10:headbutt,13: massive_bite}
boar_violent = {"name": "× WILD BOAR","OG_NAME":"WILD BOAR","type":"violent","status":" OK","speed":1,"OG_speed":1,"atk":5,"OG_atk":5,"dfk":3,"OG_dfk":3, "hp": 66,"base_hp": 66,"current_hp": 66,"hp_coef": 1.5, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.5,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bodycheck],
"level_list":boar_violent_levels}

boar_chaotic_levels = {2:bite,3:foulbreath,5:bodycheck,6:grounddigger,7:furball,9:accelerate,10:headbutt,11: tusk_attack}
boar_chaotic = {"name": "▒ WILD BOAR","OG_NAME":"WILD BOAR","type":"chaotic","status":" OK","speed":1,"OG_speed":1,"atk":5,"OG_atk":5,"dfk":4,"OG_dfk":4, "hp": 61,"base_hp": 61,"current_hp": 61,"hp_coef": 1.5, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.5,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bite],
"level_list":boar_chaotic_levels}

boar_suicide_levels = {2:fur_armor,3:headbutt,4:foulbreath,5:grounddigger,7:dust_blast,12:furball,13: massive_bite}
boar_suicide = {"name": "¤ WILD BOAR","OG_NAME":"WILD BOAR","type":"suicide","status":" OK","speed":1,"OG_speed":1,"atk":4,"OG_atk":4,"dfk":5,"OG_dfk":5, "hp": 66,"base_hp": 66,"current_hp": 66,"hp_coef": 1.5, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":12,"attack_coef": 1.5,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [tusk_attack],
"level_list":boar_suicide_levels}


# STAG
stag_natural_levels = {2:bite,3:stomp,5:triumphant_bellow,6:dust_blast,8:bodycheck,11:foulbreath,15: massive_bite}
stag_natural = {"name": "≡ STAG","OG_NAME":"STAG","type":"natural","status":" OK","speed":2,"OG_speed":2,"atk":4,"OG_atk":4,"dfk":4,"OG_dfk":4, "hp": 67,"base_hp": 67,"current_hp": 67,"hp_coef": 1.5, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.4,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [antlers_strike],
"level_list":stag_natural_levels}

stag_violent_levels = {2:rage,3:stomp,4:kick,5:bodycheck,7:bite,9:mudshot,10:triumphant_bellow,16: massive_bite}
stag_violent = {"name": "× STAG","OG_NAME":"STAG","type":"violent","status":" OK","speed":1,"OG_speed":1,"atk":5,"OG_atk":5,"dfk":3,"OG_dfk":3, "hp": 67,"base_hp": 67,"current_hp": 67,"hp_coef": 1.5, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":16,"attack_coef": 1.4,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [antlers_strike],
"level_list":stag_violent_levels}

stag_chaotic_levels = {2:triumphant_bellow,3:dust_blast,4:rage,5:antlers_strike,6:stomp,8:bodycheck,11:accelerate,15: kick}
stag_chaotic = {"name": "▒ STAG","OG_NAME":"STAG","type":"chaotic","status":" OK","speed":2,"OG_speed":2,"atk":4,"OG_atk":4,"dfk":4,"OG_dfk":4, "hp": 61,"base_hp": 61,"current_hp": 61,"hp_coef": 1.5, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":16,"attack_coef": 1.4,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bite],
"level_list":stag_chaotic_levels}

stag_suicide_levels = {2:dust_blast,4:bite,5:bodycheck,7:foulbreath,9:kick,12: stomp,16: rage}
stag_suicide = {"name": "¤ STAG","OG_NAME":"STAG","type":"suicide","status":" OK","speed":1,"OG_speed":1,"atk":3,"OG_atk":3,"dfk":5,"OG_dfk":5, "hp": 67,"base_hp": 67,"current_hp": 67,"hp_coef": 1.5, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.4,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [antlers_strike],
"level_list":stag_suicide_levels}


# RAT
rat_natural_levels = {2:tail_strangler,3:rage,4:squeak,5:dust_blast,6:paw_slap,7:foulbreath,8: massive_bite,9:accelerate,10:clawstorm}
rat_natural = {"name": "≡ RAT","OG_NAME":"RAT","type":"natural","status":" OK","speed":4,"OG_speed":4,"atk":3,"OG_atk":3,"dfk":1,"OG_dfk":1, "hp": 18,"base_hp": 18,"current_hp": 18,"hp_coef": 1.5, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bite, scratch],
"level_list":rat_natural_levels}

rat_violent_levels = {2:tail_strangler,3:slash,4:tail_strike,5:paw_slap,6:rage,7:clawstorm,8: massive_bite,9:accelerate,10:foulbreath}
rat_violent = {"name": "× RAT","OG_NAME":"RAT","type":"violent","status":" OK","speed":3,"OG_speed":3,"atk":4,"OG_atk":4,"dfk":1,"OG_dfk":1, "hp": 18,"base_hp": 18,"current_hp": 18,"hp_coef": 1.5, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":13,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bite, scratch],
"level_list":rat_violent_levels}

rat_chaotic_levels = {2:bite,3:furball,4:dust_blast,5:fur_armor,6:headbutt,7:foulbreath,8: accelerate,9:clawstorm,10:claws_sharpening,11:massive_bite,12:slash}
rat_chaotic = {"name": "▒ RAT","OG_NAME":"RAT","type":"chaotic","status":" OK","speed":4,"OG_speed":4,"atk":3,"OG_atk":3,"dfk":1,"OG_dfk":1, "hp": 15,"base_hp": 15,"current_hp": 15,"hp_coef": 1.5, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bite, tail_strangler],
"level_list":rat_chaotic_levels}

rat_suicide_levels = {2:squeak,3:dust_blast,4:fur_armor,5:tail_strangler,6:paw_slap,7:tail_strike,8: massive_bite,9:claws_sharpening,10:clawstorm}
rat_suicide = {"name": "¤ RAT","OG_NAME":"RAT","type":"suicide","status":" OK","speed":3,"OG_speed":3,"atk":2,"OG_atk":2,"dfk":2,"OG_dfk":2, "hp": 18,"base_hp": 18,"current_hp": 18,"hp_coef": 1.5, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":17,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bite, scratch],
"level_list":rat_suicide_levels}


# HARE
hare_natural_levels = {4:dust_blast,5:massive_bite,7:squeak,8:kick,9:listener,12:furball,15:rage}
hare_natural = {"name": "≡ HARE","OG_NAME":"HARE","type":"natural","status":" OK","speed":5,"OG_speed":5,"atk":2,"OG_atk":2,"dfk":1,"OG_dfk":1, "hp": 19,"base_hp": 19,"current_hp": 19,"hp_coef": 1.2, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.2,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bite, accelerate],
"level_list":hare_natural_levels}

hare_violent_levels = {3:kick,4:massive_bite,5:listener,7:bodycheck,9:headbutt,10:rage,13:paw_slap}
hare_violent = {"name": "× HARE","OG_NAME":"HARE","type":"violent","status":" OK","speed":4,"OG_speed":4,"atk":3,"OG_atk":3,"dfk":1,"OG_dfk":1, "hp": 19,"base_hp": 19,"current_hp": 19,"hp_coef": 1.2, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.2,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bite, accelerate],
"level_list":hare_violent_levels}

hare_chaotic_levels = {3:dust_blast,4:squeak,5:accelerate,7:listener,8:kick,9:furball,12:massive_bite,15:bodycheck}
hare_chaotic = {"name": "▒ HARE","OG_NAME":"HARE","type":"chaotic","status":" OK","speed":5,"OG_speed":5,"atk":2,"OG_atk":2,"dfk":1,"OG_dfk":1, "hp": 16,"base_hp": 16,"current_hp": 16,"hp_coef": 1.2, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.2,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bite, scratch],
"level_list":hare_chaotic_levels}

hare_suicide_levels = {3:listener,4:kick,6:squeak,8:fur_armor,9:massive_bite,12:furball,15:paw_slap}
hare_suicide = {"name": "¤ HARE","OG_NAME":"HARE","type":"natural","status":" OK","speed":4,"OG_speed":4,"atk":1,"OG_atk":1,"dfk":2,"OG_dfk":2, "hp": 19,"base_hp": 19,"current_hp": 19,"hp_coef": 1.2, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.2,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bite, dust_blast],
"level_list":hare_suicide_levels}


# GIRAFFE
giraffe_natural_levels = {2:stomp,4:headhammer,6:dust_blast,8:bite,10:air_bomb,12:rage,14:earthquake}
giraffe_natural = {"name": "≡ GIRAFFE","OG_NAME":"GIRAFFE","type":"natural","status":" OK","speed":1,"OG_speed":1,"atk":4,"OG_atk":4,"dfk":3,"OG_dfk":3, "hp": 69,"base_hp": 69,"current_hp": 69,"hp_coef": 1.5, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":16,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [kick],
"level_list":giraffe_natural_levels}

giraffe_violent_levels = {2:kick,4:headhammer,6:stomp,8:air_bomb,10:massive_bite,12:rage,14:earthquake}
giraffe_violent = {"name": "× GIRAFFE","OG_NAME":"GIRAFFE","type":"violent","status":" OK","speed":1,"OG_speed":1,"atk":5,"OG_atk":5,"dfk":2,"OG_dfk":2, "hp": 69,"base_hp": 69,"current_hp": 69,"hp_coef": 1.5, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [headhammer],
"level_list":giraffe_violent_levels}

giraffe_chaotic_levels = {2:light_storm,4:headhammer,6:accelerate,7:stomp,8:air_bomb,10:ground_eating,12:rage,14:foulbreath}
giraffe_chaotic = {"name": "▒ GIRAFFE","OG_NAME":"GIRAFFE","type":"chaotic","status":" OK","speed":1,"OG_speed":1,"atk":4,"OG_atk":4,"dfk":3,"OG_dfk":3, "hp": 62,"base_hp": 62,"current_hp": 62,"hp_coef": 1.5, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [kick],
"level_list":giraffe_chaotic_levels}

giraffe_suicide_levels = {2:earthquake,4:dust_blast,6:air_bomb,8:bite,10:foulbreath,12:ground_eating,14:deathjump}
giraffe_suicide = {"name": "¤ GIRAFFE","OG_NAME":"GIRAFFE","type":"suicide","status":" OK","speed":1,"OG_speed":1,"atk":3,"OG_atk":3,"dfk":4,"OG_dfk":4, "hp": 69,"base_hp": 69,"current_hp": 69,"hp_coef": 1.5, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [headhammer],
"level_list":giraffe_suicide_levels}


# BULLFROG
bullfrog_natural_levels = {2:tongue_whip,3:venom_fusion,4:regenerate,6:moon_song,7:detox,10:toxic_spit,11:environmentize,13:rain_of_poison}
bullfrog_natural = {"name": "≡ BULLFROG","OG_NAME":"BULLFROG","type":"natural","status":" OK","speed":3,"OG_speed":3,"atk":2,"OG_atk":2,"dfk":2,"OG_dfk":2, "hp": 15,"base_hp": 15,"current_hp": 15,"hp_coef": 1.5, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [kick],
"level_list":bullfrog_natural_levels}

bullfrog_violent_levels = {2:bodycheck,3:regenerate,4:toxic_spit,6:moon_song,7:kick,10:rain_of_poison,11:inflate,13:environmentize}
bullfrog_violent = {"name": "× BULLFROG","OG_NAME":"BULLFROG","type":"violent","status":" OK","speed":2,"OG_speed":2,"atk":3,"OG_atk":3,"dfk":1,"OG_dfk":1, "hp": 15,"base_hp": 15,"current_hp": 15,"hp_coef": 1.5, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [tongue_whip],
"level_list":bullfrog_violent_levels}

bullfrog_chaotic_levels = {2:regenerate,3:detox,4:kick,5:bite,6:moon_song,7:venom_fusion,10:cold_wind,11:environmentize,13:rain_of_poison}
bullfrog_chaotic = {"name": "▒ BULLFROG","OG_NAME":"BULLFROG","type":"chaotic","status":" OK","speed":3,"OG_speed":3,"atk":2,"OG_atk":2,"dfk":2,"OG_dfk":2, "hp": 12,"base_hp": 12,"current_hp": 12,"hp_coef": 1.5, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [kick],
"level_list":bullfrog_chaotic_levels}

bullfrog_suicide_levels = {2:moon_song,3:rain_of_poison,4:toxic_spit,6:kick,7:cold_wind,10:bloodshot,11:inflate,13:environmentize}
bullfrog_suicide = {"name": "¤ BULLFROG","OG_NAME":"BULLFROG","type":"suicide","status":" OK","speed":3,"OG_speed":3,"atk":2,"OG_atk":2,"dfk":2,"OG_dfk":2, "hp": 15,"base_hp": 15,"current_hp": 15,"hp_coef": 1.5, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":14,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [headbutt],
"level_list":bullfrog_suicide_levels}


# TORTOISE
tortoise_natural_levels = {4:regenerate,6:hypnosis,7:detox,8:dust_blast,10:massive_bite,14:earthquake,}
tortoise_natural = {"name": "≡ TORTOISE","OG_NAME":"TORTOISE","type":"natural","status":" OK","speed":1,"OG_speed":1,"atk":1,"OG_atk":1,"dfk":5,"OG_dfk":5, "hp": 90,"base_hp": 90,"current_hp": 90,"hp_coef": 1.6, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bite, shell_fortress],
"level_list":tortoise_natural_levels}

tortoise_violent_levels = {4:regenerate,6:hypnosis,7:detox,8:dust_blast,10:massive_bite,14:earthquake,}
tortoise_violent = {"name": "× TORTOISE","OG_NAME":"TORTOISE","type":"violent","status":" OK","speed":1,"OG_speed":1,"atk":2,"OG_atk":2,"dfk":4,"OG_dfk":4, "hp": 90,"base_hp": 90,"current_hp": 90,"hp_coef": 1.6, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bite, shell_fortress],
"level_list":tortoise_violent_levels}

tortoise_chaotic_levels = {4:regenerate,6:hypnosis,7:detox,8:dust_blast,10:massive_bite,14:earthquake,}
tortoise_chaotic = {"name": "▒ TORTOISE","OG_NAME":"TORTOISE","type":"chaotic","status":" OK","speed":1,"OG_speed":1,"atk":1,"OG_atk":1,"dfk":5,"OG_dfk":5, "hp": 95,"base_hp": 95,"current_hp": 95,"hp_coef": 1.6, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bite, shell_fortress],
"level_list":tortoise_chaotic_levels}

tortoise_suicide_levels = {4:regenerate,6:hypnosis,7:detox,8:dust_blast,10:massive_bite,14:earthquake,17: rain_of_poison}
tortoise_suicide = {"name": "¤ TORTOISE","OG_NAME":"TORTOISE","type":"suicide","status":" OK","speed":1,"OG_speed":1,"atk":1,"OG_atk":1,"dfk":5,"OG_dfk":5, "hp": 90,"base_hp": 90,"current_hp": 90,"hp_coef": 1.6, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bite, shell_fortress],
"level_list":tortoise_suicide_levels}


# RHINO
rhino_natural_levels = {2:horn_attack,4:dust_blast,6:earthquake,7:resting,10:earthquake,14:rage}
rhino_natural = {"name": "≡ RHINO","OG_NAME":"RHINO","type":"natural","status":" OK","speed":2,"OG_speed":2,"atk":5,"OG_atk":5,"dfk":5,"OG_dfk":5, "hp": 80,"base_hp": 80,"current_hp": 80,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.4,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bodycheck],
"level_list":rhino_natural_levels}

rhino_violent_levels = {2:bodycheck,4:earthquake,5:rage,7:stomp,13:resting,15:dust_blast}
rhino_violent = {"name": "× RHINO","OG_NAME":"RHINO","type":"violent","status":" OK","speed":1,"OG_speed":1,"atk":5,"OG_atk":5,"dfk":4,"OG_dfk":4, "hp": 80,"base_hp": 80,"current_hp": 80,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.4,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [horn_attack],
"level_list":rhino_violent_levels}

rhino_chaotic_levels = {2:horn_attack,4:accelerate,6:kick,7:light_storm,10:earthquake,14:rage}
rhino_chaotic = {"name": "▒ RHINO","OG_NAME":"RHINO","type":"chaotic","status":" OK","speed":2,"OG_speed":2,"atk":5,"OG_atk":5,"dfk":5,"OG_dfk":5, "hp": 73,"base_hp": 73,"current_hp": 73,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.4,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bodycheck],
"level_list":rhino_chaotic_levels}

rhino_suicide_levels = {2:bodycheck,3:horn_attack,4:resting,6:stomp,10:light_storm,14:rage}
rhino_suicide = {"name": "¤ RHINO","OG_NAME":"RHINO","type":"suicide","status":" OK","speed":1,"OG_speed":1,"atk":1,"OG_atk":1,"dfk":5,"OG_dfk":5, "hp": 80,"base_hp": 80,"current_hp": 80,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.4,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [earthquake],
"level_list":rhino_suicide_levels}


# ELEPHANT
elephant_natural_levels = {3:trunksmash,4:tusk_attack,6:dust_twister,9:mudshot,12:resting,15:roar}
elephant_natural = {"name": "≡ ELEPHANT","OG_NAME":"ELEPHANT","type":"natural","status":" OK","speed":1,"OG_speed":1,"atk":4,"OG_atk":4,"dfk":5,"OG_dfk":5, "hp": 120,"base_hp": 120,"current_hp": 120,"hp_coef": 1.4, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [earthquake],
"level_list":elephant_natural_levels}

elephant_violent_levels = {3:trunksmash,4:tusk_attack,6:mudshot,9:stonethrow,12:roar,15:stomp}
elephant_violent = {"name": "× ELEPHANT","OG_NAME":"ELEPHANT","type":"violent","status":" OK","speed":1,"OG_speed":1,"atk":5,"OG_atk":5,"dfk":4,"OG_dfk":4, "hp": 120,"base_hp": 120,"current_hp": 120,"hp_coef": 1.4, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":13,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [earthquake],
"level_list":elephant_violent_levels}

elephant_chaotic_levels = {3:tusk_attack,4:dust_blast,6:roar,9:earthquake,12:kick,15:trunksmash}
elephant_chaotic = {"name": "▒ ELEPHANT","OG_NAME":"ELEPHANT","type":"chaotic","status":" OK","speed":1,"OG_speed":1,"atk":4,"OG_atk":4,"dfk":5,"OG_dfk":5, "hp": 112,"base_hp": 112,"current_hp": 112,"hp_coef": 1.4, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [mudshot],
"level_list":elephant_chaotic_levels}

elephant_suicide_levels = {3:tusk_attack,4:dust_blast,6:trunksmash,9:mudshot,12:stonethrow,15:stomp}
elephant_suicide = {"name": "¤ ELEPHANT","OG_NAME":"ELEPHANT","type":"suicide","status":" OK","speed":1,"OG_speed":1,"atk":3,"OG_atk":3,"dfk":5,"OG_dfk":5, "hp": 120,"base_hp": 120,"current_hp": 120,"hp_coef": 1.4, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":13,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [earthquake],
"level_list":elephant_suicide_levels}


# LION
lion_natural_levels = {2:paw_slap,4:claws_sharpening,6:ground_eating,8:roar,9:accelerate,10:resting,14:massive_bite}
lion_natural = {"name": "≡ LION","OG_NAME":"LION","type":"natural","status":" OK","speed":3,"OG_speed":3,"atk":5,"OG_atk":5,"dfk":3,"OG_dfk":3, "hp": 60,"base_hp": 60,"current_hp": 60,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.4,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bite],
"level_list":lion_natural_levels}

lion_violent_levels = {2:paw_slap,3:slash,5:rage,8:bodycheck,9:clawstorm,12:massive_bite,15:resting}
lion_violent = {"name": "× LION","OG_NAME":"LION","type":"violent","status":" OK","speed":2,"OG_speed":2,"atk":5,"OG_atk":5,"dfk":2,"OG_dfk":2, "hp": 60,"base_hp": 60,"current_hp": 60,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.4,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bite],
"level_list":lion_violent_levels}

lion_chaotic_levels = {2:claws_sharpening,3:bite,5:accelerate,6:tail_strike,8:resting,10:roar,14:massive_bite,17:massive_bite}
lion_chaotic = {"name": "▒ LION","OG_NAME":"LION","type":"chaotic","status":" OK","speed":3,"OG_speed":3,"atk":5,"OG_atk":5,"dfk":3,"OG_dfk":3, "hp": 54,"base_hp": 54,"current_hp": 54,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.4,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [headbutt],
"level_list":lion_chaotic_levels}

lion_suicide_levels = {2:ground_eating,4:claws_sharpening,6:paw_slap,8:dust_blast,9:listener,10:headbutt,14:massive_bite}
lion_suicide = {"name": "¤ LION","OG_NAME":"LION","type":"suicide","status":" OK","speed":2,"OG_speed":2,"atk":4,"OG_atk":4,"dfk":4,"OG_dfk":4, "hp": 60,"base_hp": 60,"current_hp": 60,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":14,"attack_coef": 1.4,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bite],
"level_list":lion_suicide_levels}


# OSTRICH
ostrich_natural_levels = {3:dust_blast,5:accelerate,7:beak_drill,8:peck,11:headhammer,12:clawstorm,16:stomp}
ostrich_natural = {"name": "≡ OSTRICH","OG_NAME":"OSTRICH","type":"natural","status":" OK","speed":3,"OG_speed":3,"atk":3,"OG_atk":3,"dfk":3,"OG_dfk":3, "hp": 50,"base_hp": 50,"current_hp": 50,"hp_coef": 1.4, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [kick, ground_energy],
"level_list":ostrich_natural_levels}

ostrich_violent_levels = {3:peck,5:beak_drill,7:bodycheck,9:headhammer,10:clawstorm,14:stomp,15:hypnosis}
ostrich_violent = {"name": "× OSTRICH","OG_NAME":"OSTRICH","type":"violent","status":" OK","speed":2,"OG_speed":2,"atk":4,"OG_atk":4,"dfk":2,"OG_dfk":2, "hp": 50,"base_hp": 50,"current_hp": 50,"hp_coef": 1.4, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":13,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [kick, ground_energy],
"level_list":ostrich_violent_levels}

ostrich_chaotic_levels = {2:beak_drill,4:ground_energy,7:earthquake,9:rage,12:dust_blast,13:headhammer,14:clawstorm}
ostrich_chaotic = {"name": "▒ OSTRICH","OG_NAME":"OSTRICH","type":"chaotic","status":" OK","speed":3,"OG_speed":3,"atk":3,"OG_atk":3,"dfk":3,"OG_dfk":3, "hp": 45,"base_hp": 45,"current_hp": 45,"hp_coef": 1.4, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [kick, accelerate],
"level_list":ostrich_chaotic_levels}

ostrich_suicide_levels = {3:dust_blast,5:bloodshot,7:peck,8:beak_drill,11:headhammer,12:clawstorm,16:deathjump}
ostrich_suicide = {"name": "¤ OSTRICH","OG_NAME":"OSTRICH","type":"suicide","status":" OK","speed":2,"OG_speed":2,"atk":2,"OG_atk":2,"dfk":4,"OG_dfk":4, "hp": 50,"base_hp": 50,"current_hp": 50,"hp_coef": 1.4, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [kick],
"level_list":ostrich_suicide_levels}


# PHEASANT
pheasant_natural_levels = {3:wing_slap,4:grounddigger,5:kick,6:dust_twister,7:air_bomb,9:claws_sharpening,12:beak_drill,16:clawstorm}
pheasant_natural = {"name": "≡ PHEASANT","OG_NAME":"PHEASANT","type":"natural","status":" OK","speed":2,"OG_speed":2,"atk":2,"OG_atk":2,"dfk":2,"OG_dfk":2, "hp": 32,"base_hp": 32,"current_hp": 32,"hp_coef": 1.4, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.2,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [peck],
"level_list":pheasant_natural_levels}

pheasant_violent_levels = {2:spur_blade,3:beak_drill,4:air_bomb,6:clawstorm,7:wing_slap,8:feather_tornado,10:dust_twister,13:scratch}
pheasant_violent = {"name": "× PHEASANT","OG_NAME":"PHEASANT","type":"violent","status":" OK","speed":1,"OG_speed":1,"atk":3,"OG_atk":3,"dfk":1,"OG_dfk":1, "hp": 32,"base_hp": 32,"current_hp": 32,"hp_coef": 1.4, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.2,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [peck],
"level_list":pheasant_violent_levels}

pheasant_chaotic_levels = {3:headbutt,5:cold_wind,6:kick,7:dust_blast,8:claws_sharpening,9:air_bomb,10:ground_eating,17:eye_of_ra}
pheasant_chaotic = {"name": "▒ PHEASANT","OG_NAME":"PHEASANT","type":"chaotic","status":" OK","speed":2,"OG_speed":2,"atk":2,"OG_atk":2,"dfk":2,"OG_dfk":2, "hp": 28,"base_hp": 28,"current_hp": 28,"hp_coef": 1.4, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.2,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [peck],
"level_list":pheasant_chaotic_levels}

pheasant_suicide_levels = {2:beak_drill,3:cold_wind,4:dust_blast,5:claws_sharpening,6:air_bomb,8:wing_slap,13:clawstorm,14:feather_tornado}
pheasant_suicide = {"name": "¤ PHEASANT","OG_NAME":"PHEASANT","type":"natural","status":" OK","speed":1,"OG_speed":1,"atk":1,"OG_atk":1,"dfk":3,"OG_dfk":3, "hp": 32,"base_hp": 32,"current_hp": 32,"hp_coef": 1.4, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.2,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [peck],
"level_list":pheasant_suicide_levels}


# HOUND
hound_natural_levels = {2:scratch,3:foulbreath,4:claws_sharpening,5:accelerate,7:dust_blast,10:listener,15:resting}
hound_natural = {"name": "≡ HOUND","OG_NAME":"HOUND","type":"natural","status":" OK","speed":3,"OG_speed":3,"atk":3,"OG_atk":3,"dfk":2,"OG_dfk":2, "hp": 43,"base_hp": 43,"current_hp": 43,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":14,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bite],
"level_list":hound_natural_levels}

hound_violent_levels = {2:scratch,4:rage,6:paw_slap,7:bodycheck,8:dust_blast,11:massive_bite,14:headbutt}
hound_violent = {"name": "× HOUND","OG_NAME":"HOUND","type":"violent","status":" OK","speed":2,"OG_speed":2,"atk":4,"OG_atk":4,"dfk":1,"OG_dfk":1, "hp": 43,"base_hp": 43,"current_hp": 43,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":4,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bite],
"level_list":hound_violent_levels}

hound_chaotic_levels = {3:bite,4:accelerate,5:claws_sharpening,6:paw_slap,7:dust_blast,9:listener,17:resting}
hound_chaotic = {"name": "▒ HOUND","OG_NAME":"HOUND","type":"chaotic","status":" OK","speed":3,"OG_speed":3,"atk":3,"OG_atk":3,"dfk":2,"OG_dfk":2, "hp": 40,"base_hp": 40,"current_hp": 40,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":4,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [scratch],
"level_list":hound_chaotic_levels}

hound_suicide_levels = {2:bite,3:scratch,4:dust_blast,5:listener,7:bodycheck,10:ground_eating,15:massive_bite}
hound_suicide = {"name": "¤ HOUND","OG_NAME":"HOUND","type":"suicide","status":" OK","speed":2,"OG_speed":2,"atk":2,"OG_atk":2,"dfk":3,"OG_dfk":3, "hp": 43,"base_hp": 43,"current_hp": 43,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":4,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [headbutt],
"level_list":hound_suicide_levels}


# BADGER
badger_natural_levels = {2:resting,3:slash,4:claws_sharpening,5:furball,6:dust_blast,9:clawstorm,12:earthquake}
badger_natural = {"name": "≡ BADGER","OG_NAME":"BADGER","type":"natural","status":" OK","speed":1,"OG_speed":1,"atk":3,"OG_atk":3,"dfk":4,"OG_dfk":4, "hp": 56,"base_hp": 56,"current_hp": 56,"hp_coef": 1.4, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":4,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [scratch, mudshot],
"level_list":badger_natural_levels}

badger_violent_levels = {2:slash,3:furball,5:bite,6:rage,8:earthquake,9:foulbreath,11:massive_bite}
badger_violent = {"name": "× BADGER","OG_NAME":"BADGER","type":"violent","status":" OK","speed":1,"OG_speed":1,"atk":4,"OG_atk":4,"dfk":3,"OG_dfk":3, "hp": 56,"base_hp": 56,"current_hp": 56,"hp_coef": 1.4, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":4,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [scratch, mudshot],
"level_list":badger_violent_levels}

badger_chaotic_levels = {3:claws_sharpening,4:grounddigger,6:paw_slap,7:earthquake,8:dust_blast,9:resting,10:massive_bite}
badger_chaotic = {"name": "▒ BADGER","OG_NAME":"BADGER","type":"chaotic","status":" OK","speed":1,"OG_speed":1,"atk":3,"OG_atk":3,"dfk":4,"OG_dfk":4, "hp": 52,"base_hp": 52,"current_hp": 56,"hp_coef": 1.4, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":4,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bite],
"level_list":badger_chaotic_levels}

badger_suicide_levels = {2:dust_blast,4:furball,5:paw_slap,6:squeak,7:fur_armor,8:clawstorm,10:earthquake}
badger_suicide = {"name": "¤ BADGER","OG_NAME":"BADGER","type":"suicide","status":" OK","speed":1,"OG_speed":1,"atk":2,"OG_atk":2,"dfk":5,"OG_dfk":5, "hp": 56,"base_hp": 56,"current_hp": 56,"hp_coef": 1.4, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":4,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [scratch, mudshot],
"level_list":badger_suicide_levels}


# CAT
cat_natural_levels = {2:resting,3:claws_sharpening,4:dust_blast, 6:tail_strangler,8: accelerate,9:slash, 11:clawstorm, 15: listener}
cat_natural = {"name": "≡ CAT","OG_NAME":"CAT","type":"natural","status":" OK","speed":4,"OG_speed":4,"atk":2,"OG_atk":2,"dfk":1,"OG_dfk":1, "hp": 23,"base_hp": 23,"current_hp": 23,"hp_coef": 1.5, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":4,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [scratch],
"level_list":cat_natural_levels}

cat_violent_levels = {2:paw_slap,3:tail_strangler,4:slash, 5:clawstorm,7: whip,8:bite, 12:massive_bite, 14: furball}
cat_violent = {"name": "× CAT","OG_NAME":"CAT","type":"violent","status":" OK","speed":3,"OG_speed":3,"atk":3,"OG_atk":3,"dfk":1,"OG_dfk":1, "hp": 23,"base_hp": 23,"current_hp": 23,"hp_coef": 1.5, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":4,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [scratch],
"level_list":cat_violent_levels}

cat_chaotic_levels = {2:ground_eating,3:accelerate,4:listener, 5:tail_strike,6: dust_blast,9:rage, 10:furball, 18: fur_armor, 21: foulbreath}
cat_chaotic = {"name": "▒ CAT","OG_NAME":"CAT","type":"chaotic","status":" OK","speed":4,"OG_speed":4,"atk":2,"OG_atk":2,"dfk":1,"OG_dfk":1, "hp": 20,"base_hp": 20,"current_hp": 20,"hp_coef": 1.5, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":4,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [scratch],
"level_list":cat_chaotic_levels}

cat_suicide_levels = {2:headbutt,3:claws_sharpening,4:tail_strangler, 6:headbutt,7: dust_blast,8:slash, 11:listener, 13: clawstorm}
cat_suicide = {"name": "¤ CAT","OG_NAME":"CAT","type":"suicide","status":" OK","speed":3,"OG_speed":3,"atk":1,"OG_atk":1,"dfk":2,"OG_dfk":2, "hp": 23,"base_hp": 23,"current_hp": 23,"hp_coef": 1.5, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":4,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [furball],
"level_list":cat_suicide_levels}


# GORILLA
gorilla_natural_levels = {2:roar,3:headbutt,4:inflate,5:accelerate,7:dust_blast,9:slash,10:earthquake,15:massive_bite}
gorilla_natural = {"name": "≡ GORILLA","OG_NAME":"GORILLA","type":"natural","status":" OK","speed":3,"OG_speed":3,"atk":5,"OG_atk":5,"dfk":3,"OG_dfk":3, "hp": 55,"base_hp": 55,"current_hp": 55,"hp_coef": 1.2, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":4,"attack_coef": 1.5,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [punch],
"level_list":gorilla_natural_levels}

gorilla_violent_levels = {2:bite,3:stonethrow,4:earthquake,5:slash,6:dust_blast,8:massive_bite,12:furball,16:rage}
gorilla_violent = {"name": "× GORILLA","OG_NAME":"GORILLA","type":"violent","status":" OK","speed":2,"OG_speed":2,"atk":5,"OG_atk":5,"dfk":2,"OG_dfk":2, "hp": 55,"base_hp": 55,"current_hp": 55,"hp_coef": 1.2, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":4,"attack_coef": 1.5,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [punch],
"level_list":gorilla_violent_levels}

gorilla_chaotic_levels = {3:rage,5:roar,6:furball,8:dust_blast,9:accelerate,10:bite,11:inflate,15:massive_bite}
gorilla_chaotic = {"name": "▒ GORILLA","OG_NAME":"GORILLA","type":"chaotic","status":" OK","speed":3,"OG_speed":3,"atk":5,"OG_atk":5,"dfk":3,"OG_dfk":3, "hp": 51,"base_hp": 51,"current_hp": 51,"hp_coef": 1.2, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":4,"attack_coef": 1.5,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [punch],
"level_list":gorilla_chaotic_levels}

gorilla_suicide_levels = {2:furball,3:punch,4:dust_blast,5:foulbreath,6:slash,8:stonethrow,10:earthquake,13:deathjump}
gorilla_suicide = {"name": "¤ GORILLA","OG_NAME":"GORILLA","type":"suicide","status":" OK","speed":2,"OG_speed":2,"atk":4,"OG_atk":4,"dfk":4,"OG_dfk":4, "hp": 55,"base_hp": 55,"current_hp": 55,"hp_coef": 1.2, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":4,"attack_coef": 1.5,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [headbutt],
"level_list":gorilla_suicide_levels}


# PLATYPUS
platypus_natural_levels = {2:headbutt,3:mudshot,4:dead_eyes,5:dust_blast,7:slash,9:cold_wind,10:furball,15:bodycheck,18:wet_darkness}
platypus_natural = {"name": "≡ PLATYPUS","OG_NAME":"PLATYPUS, PICO!","type":"natural","status":" OK","speed":1,"OG_speed":1,"atk":2,"OG_atk":2,"dfk":3,"OG_dfk":3, "hp": 35,"base_hp": 35,"current_hp": 35,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":11,"attack_coef": 1.2,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [slapping_flippers],
"level_list":platypus_natural_levels}

platypus_violent_levels = {2:bodycheck,3:headbutt,4:slash,5:dust_blast,6:furball,7:earthquake,10:mudshot,16:wet_darkness}
platypus_violent = {"name": "× PLATYPUS","OG_NAME":"PLATYPUS, PICO!","type":"violent","status":" OK","speed":1,"OG_speed":1,"atk":3,"OG_atk":3,"dfk":2,"OG_dfk":2, "hp": 35,"base_hp": 35,"current_hp": 35,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":4,"attack_coef": 1.2,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [slapping_flippers],
"level_list":platypus_violent_levels}

platypus_chaotic_levels = {3:furball,5:slapping_flippers,6:dead_eyes,7:headbutt,9:cold_wind,10:accelerate,11:rage,13:bloodshot,14:peck}
platypus_chaotic = {"name": "▒ PLATYPUS","OG_NAME":"PLATYPUS, PICO!","type":"chaotic","status":" OK","speed":1,"OG_speed":1,"atk":2,"OG_atk":2,"dfk":3,"OG_dfk":3, "hp": 32,"base_hp": 32,"current_hp": 32,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":11,"attack_coef": 1.2,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [wet_darkness],
"level_list":platypus_chaotic_levels}

platypus_suicide_levels = {2:furball,3:fur_armor,4:dead_eyes,5:dust_blast,7:cold_wind,9:headbutt,10:squeak,15:mudshot,18:wet_darkness}
platypus_suicide = {"name": "¤ PLATYPUS","OG_NAME":"PLATYPUS, PICO!","type":"suicide","status":" OK","speed":1,"OG_speed":1,"atk":1,"OG_atk":1,"dfk":4,"OG_dfk":4, "hp": 35,"base_hp": 35,"current_hp": 35,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":4,"attack_coef": 1.2,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [slapping_flippers],
"level_list":platypus_suicide_levels}


# PANDA
panda_natural_levels = {2:furball,3:dust_blast,4:headbutt,6:stonethrow,8:bite,9:slash,12:fur_armor}
panda_natural = {"name": "≡ PANDA","OG_NAME":"PANDA","type":"natural","status":" OK","speed":1,"OG_speed":1,"atk":3,"OG_atk":3,"dfk":2,"OG_dfk":2, "hp": 50,"base_hp": 50,"current_hp": 50,"hp_coef": 1.4, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":12,"attack_coef": 1.2,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [scratch,resting],
"level_list":panda_natural_levels}

panda_violent_levels = {3:furball,4:mudshot,5:headbutt,7:stonethrow,8:massive_bite,10:slash,11:punch}
panda_violent = {"name": "× PANDA","OG_NAME":"PANDA","type":"violent","status":" OK","speed":1,"OG_speed":1,"atk":4,"OG_atk":4,"dfk":1,"OG_dfk":1, "hp": 50,"base_hp": 50,"current_hp": 50,"hp_coef": 1.4, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":4,"attack_coef": 1.2,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [scratch,bite],
"level_list":panda_violent_levels}

panda_chaotic_levels = {3:fur_armor,4:headbutt,6:scratch,7:stonethrow,8:paw_slap,9:hypnosis,10:slash,14:deathjump}
panda_chaotic = {"name": "▒ PANDA","OG_NAME":"PANDA","type":"chaotic","status":" OK","speed":1,"OG_speed":1,"atk":3,"OG_atk":3,"dfk":2,"OG_dfk":2, "hp": 45,"base_hp": 45,"current_hp": 45,"hp_coef": 1.4, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":4,"attack_coef": 1.2,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [furball,resting],
"level_list":panda_chaotic_levels}

panda_suicide_levels = {2:furball,3:headbutt,4:dust_blast,6:deathjump,8:claws_sharpening,9:fur_armor,12:mudshot}
panda_suicide = {"name": "¤ PANDA","OG_NAME":"PANDA","type":"natural","status":" OK","speed":1,"OG_speed":1,"atk":2,"OG_atk":2,"dfk":3,"OG_dfk":3, "hp": 50,"base_hp": 50,"current_hp": 50,"hp_coef": 1.4, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":4,"attack_coef": 1.2,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [scratch,ground_eating],
"level_list":panda_suicide_levels}


# SCORPION
scorpion_natural_levels = {2:accelerate,3:detox,4:dead_eyes,6:shell_fortress,7:dust_blast,8:regenerate,9:mudshot,12:rain_of_poison}
scorpion_natural = {"name": "≡ SCORPION","OG_NAME":"SCORPION","type":"natural","status":" OK","speed":4,"OG_speed":4,"atk":4,"OG_atk":4,"dfk":1,"OG_dfk":1, "hp": 25,"base_hp": 25,"current_hp": 25,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":4,"attack_coef": 1.5,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [poison_sting],
"level_list":scorpion_natural_levels}

scorpion_violent_levels = {2:detox,3:mudshot,4:cold_wind,5:shell_fortress,6:dust_blast,9:rain_of_poison,10:regenerate}
scorpion_violent = {"name": "× SCORPION","OG_NAME":"SCORPION","type":"violent","status":" OK","speed":3,"OG_speed":3,"atk":5,"OG_atk":5,"dfk":1,"OG_dfk":1, "hp": 25,"base_hp": 25,"current_hp": 25,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":14,"attack_coef": 1.5,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [poison_sting],
"level_list":scorpion_violent_levels}

scorpion_chaotic_levels = {2:venom_fusion,3:detox,4:shell_fortress,5:bite,6:cold_wind,7:dust_blast,8:rain_of_poison,9:accelerate}
scorpion_chaotic = {"name": "▒ SCORPION","OG_NAME":"SCORPION","type":"chaotic","status":" OK","speed":4,"OG_speed":4,"atk":4,"OG_atk":4,"dfk":1,"OG_dfk":1, "hp": 20,"base_hp": 20,"current_hp": 20,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":14,"attack_coef": 1.5,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [poison_sting],
"level_list":scorpion_chaotic_levels}

scorpion_suicide_levels = {2:accelerate,3:detox,4:shell_fortress,6:dead_eyes,7:dust_blast,8:rain_of_poison,9:mudshot,12:bloodshot}
scorpion_suicide = {"name": "¤ SCORPION","OG_NAME":"SCORPION","type":"suicide","status":" OK","speed":3,"OG_speed":3,"atk":3,"OG_atk":3,"dfk":2,"OG_dfk":2, "hp": 25,"base_hp": 25,"current_hp": 25,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":4,"attack_coef": 1.5,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [poison_sting],
"level_list":scorpion_suicide_levels}


# ANTEATER
anteater_natural_levels = {2:scratch,3:furball,4:claws_sharpening,5:tongue_whip,6:dust_blast,9:grounddigger,12:clawstorm,17:earthquake}
anteater_natural = {"name": "≡ ANTEATER","OG_NAME":"ANTEATER","type":"natural","status":" OK","speed":2,"OG_speed":2,"atk":3,"OG_atk":3,"dfk":3,"OG_dfk":3, "hp": 47,"base_hp": 47,"current_hp": 47,"hp_coef": 1.4, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":4,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [mudshot],
"level_list":anteater_natural_levels}

anteater_violent_levels = {2:scratch,3:tongue_whip,4:bodycheck,5:furball,6:dust_blast,7:clawstorm,9:earthquake,15:cold_wind}
anteater_violent = {"name": "× ANTEATER","OG_NAME":"ANTEATER","type":"violent","status":" OK","speed":1,"OG_speed":1,"atk":4,"OG_atk":4,"dfk":2,"OG_dfk":2, "hp": 47,"base_hp": 47,"current_hp": 47,"hp_coef": 1.4, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":4,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [mudshot],
"level_list":anteater_violent_levels}

anteater_chaotic_levels = {2:furball,3:ground_eating,4:tongue_whip,5:bodycheck,7:dust_blast,8:kick,9:grounddigger,11:clawstorm,14:earthquake}
anteater_chaotic = {"name": "▒ ANTEATER","OG_NAME":"ANTEATER","type":"chaotic","status":" OK","speed":2,"OG_speed":2,"atk":3,"OG_atk":3,"dfk":3,"OG_dfk":3, "hp": 47,"base_hp": 43,"current_hp": 43,"hp_coef": 1.4, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":14,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [mudshot],
"level_list":anteater_chaotic_levels}

anteater_suicide_levels = {2:bloodshot,3:furball,4:ground_eating,5:tongue_whip,6:fur_armor,8:slash,10:clawstorm,15:earthquake}
anteater_suicide = {"name": "¤ ANTEATER","OG_NAME":"ANTEATER","type":"suicide","status":" OK","speed":1,"OG_speed":1,"atk":2,"OG_atk":2,"dfk":4,"OG_dfk":4, "hp": 47,"base_hp": 47,"current_hp": 47,"hp_coef": 1.4, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":4,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [mudshot],
"level_list":anteater_suicide_levels}


# BUFFALO
buffalo_natural_levels = {3:stomp,5:bodycheck,6:earthquake,9:dust_blast,10:fur_armor,14:resting,18: rage}
buffalo_natural = {"name": "≡ BUFFALO","OG_NAME":"BUFFALO","type":"natural","status":" OK","speed":2,"OG_speed":2,"atk":4,"OG_atk":4,"dfk":5,"OG_dfk":5, "hp": 80,"base_hp": 80,"current_hp": 80,"hp_coef": 1.4, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [horn_attack],
"level_list":buffalo_natural_levels}

buffalo_violent_levels = {3:bodycheck,4:earthquake,5:kick,6:stomp,12:rage,13:bite,14: massive_bite}
buffalo_violent = {"name": "× BUFFALO","OG_NAME":"BUFFALO","type":"violent","status":" OK","speed":1,"OG_speed":1,"atk":5,"OG_atk":5,"dfk":3,"OG_dfk":3, "hp": 80,"base_hp": 80,"current_hp": 80,"hp_coef": 1.4, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [horn_attack],
"level_list":buffalo_violent_levels}

buffalo_chaotic_levels = {2:fur_armor,4:bite,7:kick,8:resting,11:stomp,15:accelerate,16: earthquake}
buffalo_chaotic = {"name": "▒ BUFFALO","OG_NAME":"BUFFALO","type":"chaotic","status":" OK","speed":2,"OG_speed":2,"atk":4,"OG_atk":4,"dfk":5,"OG_dfk":5, "hp": 76,"base_hp": 76,"current_hp": 76,"hp_coef": 1.4, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [horn_attack],
"level_list":buffalo_chaotic_levels}

buffalo_suicide_levels = {3:stomp,5:cold_wind,6:dust_blast,9:earthquake,10:rage,14:fur_armor,18: rage}
buffalo_suicide = {"name": "¤ BUFFALO","OG_NAME":"BUFFALO","type":"suicide","status":" OK","speed":1,"OG_speed":1,"atk":3,"OG_atk":3,"dfk":5,"OG_dfk":5, "hp": 80,"base_hp": 80,"current_hp": 80,"hp_coef": 1.4, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [horn_attack],
"level_list":buffalo_suicide_levels}


# ALLIGATOR
alligator_natural_levels = {2:dead_eyes,3:mudshot,5:massive_bite,7:harding_scales,10:resting,13:wet_darkness,16: tail_strike}
alligator_natural = {"name": "≡ ALLIGATOR","OG_NAME":"ALLIGATOR","type":"natural","status":" OK","speed":3,"OG_speed":3,"atk":5,"OG_atk":5,"dfk":3,"OG_dfk":3, "hp": 60,"base_hp": 60,"current_hp": 60,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.5,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bite],
"level_list":alligator_natural_levels}

alligator_violent_levels = {2:slash,3:mudshot,4:massive_bite,6:earthquake,9:cold_wind,13:wet_darkness}
alligator_violent = {"name": "× ALLIGATOR","OG_NAME":"ALLIGATOR","type":"violent","status":" OK","speed":2,"OG_speed":2,"atk":5,"OG_atk":5,"dfk":2,"OG_dfk":2, "hp": 60,"base_hp": 60,"current_hp": 60,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.5,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bite],
"level_list":alligator_violent_levels}

alligator_chaotic_levels = {2:bodycheck,3:accelerate,4:bite,6:dead_eyes,8:resting,10:harding_scales,12:massive_bite,14: wet_darkness}
alligator_chaotic = {"name": "▒ ALLIGATOR","OG_NAME":"ALLIGATOR","type":"chaotic","status":" OK","speed":3,"OG_speed":3,"atk":5,"OG_atk":5,"dfk":3,"OG_dfk":3, "hp": 55,"base_hp": 55,"current_hp": 55,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":15,"attack_coef": 1.5,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [scratch],
"level_list":alligator_chaotic_levels}

alligator_suicide_levels = {2:harding_scales,4:massive_bite,5:wet_darkness,7:environmentize,8:slash,13:clawstorm,15: cold_wind}
alligator_suicide = {"name": "¤ ALLIGATOR","OG_NAME":"ALLIGATOR","type":"suicide","status":" OK","speed":2,"OG_speed":2,"atk":4,"OG_atk":4,"dfk":4,"OG_dfk":4, "hp": 60,"base_hp": 60,"current_hp": 60,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.5,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bite],
"level_list":alligator_suicide_levels}


# SWAN
swan_natural_levels = {3:wing_slap,5:mudshot,7:headhammer,9:feather_tornado,11:air_bomb,13:kick,15: cold_wind}
swan_natural = {"name": "≡ SWAN","OG_NAME":"SWAN","type":"natural","status":" OK","speed":2,"OG_speed":2,"atk":3,"OG_atk":3,"dfk":3,"OG_dfk":3, "hp": 60,"base_hp": 60,"current_hp": 60,"hp_coef": 1.4, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.5,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [peck],
"level_list":swan_natural_levels}

swan_violent_levels = {2:wing_slap,4:mudshot,6:headhammer,8:bite,10:air_bomb,12:kick,14: cold_wind}
swan_violent = {"name": "× SWAN","OG_NAME":"SWAN","type":"violent","status":" OK","speed":1,"OG_speed":1,"atk":4,"OG_atk":4,"dfk":2,"OG_dfk":2, "hp": 60,"base_hp": 60,"current_hp": 60,"hp_coef": 1.4, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":16,"attack_coef": 1.5,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [peck],
"level_list":swan_violent_levels}

swan_chaotic_levels = {3:mudshot,4:feather_tornado,6:bite,7:air_bomb,9:wet_darkness,10:earthquake,12: peck,13:kick}
swan_chaotic = {"name": "▒ SWAN","OG_NAME":"SWAN","type":"chaotic","status":" OK","speed":2,"OG_speed":2,"atk":3,"OG_atk":3,"dfk":3,"OG_dfk":3, "hp": 54,"base_hp": 54,"current_hp": 54,"hp_coef": 1.4, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.5,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [headhammer],
"level_list":swan_chaotic_levels}

swan_suicide_levels = {3:feather_tornado,5:headhammer,7:air_bomb,9:kick,11:cold_wind,13:bloodshot,15: cold_wind}
swan_suicide = {"name": "¤ SWAN","OG_NAME":"SWAN","type":"suicide","status":" OK","speed":1,"OG_speed":1,"atk":2,"OG_atk":2,"dfk":4,"OG_dfk":4, "hp": 60,"base_hp": 60,"current_hp": 60,"hp_coef": 1.4, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.5,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [peck],
"level_list":swan_suicide_levels}


# KOMODO DRAGON
komodo_dragon_natural_levels = {3:toxic_spit,6:harding_scales,9:tail_strike,12:detox,15:regenerate,18:massive_bite,21: accelerate}
komodo_dragon_natural = {"name": "≡ KOMODO DRAGON","OG_NAME":"KOMODO DRAGON","type":"natural","status":" OK","speed":3,"OG_speed":3,"atk":4,"OG_atk":4,"dfk":4,"OG_dfk":4, "hp": 55,"base_hp": 55,"current_hp": 55,"hp_coef": 1.4, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.4,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bite],
"level_list":komodo_dragon_natural_levels}

komodo_dragon_violent_levels = {2:toxic_spit,6:massive_bite,8:cold_wind,12:detox,14:tail_strike,18:regenerate,20: detox}
komodo_dragon_violent = {"name": "× KOMODO DRAGON","OG_NAME":"KOMODO DRAGON","type":"violent","status":" OK","speed":2,"OG_speed":2,"atk":5,"OG_atk":5,"dfk":3,"OG_dfk":3, "hp": 55,"base_hp": 55,"current_hp": 55,"hp_coef": 1.4, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.4,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bite],
"level_list":komodo_dragon_violent_levels}

komodo_dragon_chaotic_levels = {2:cold_wind,5:earthquake,6:detox,9:massive_bite,10:mudshot,14:accelerate,15: regenerate,19:accelerate}
komodo_dragon_chaotic = {"name": "▒ KOMODO DRAGON","OG_NAME":"KOMODO DRAGON","type":"chaotic","status":" OK","speed":3,"OG_speed":3,"atk":4,"OG_atk":4,"dfk":4,"OG_dfk":4, "hp": 52,"base_hp": 52,"current_hp": 52,"hp_coef": 1.4, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.4,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [toxic_spit],
"level_list":komodo_dragon_chaotic_levels}

komodo_dragon_suicide_levels = {3:harding_scales,6:massive_bite,9:tail_strike,12:headbutt,15:toxic_spit,18:mudshot,21: dead_eyes}
komodo_dragon_suicide = {"name": "¤ KOMODO DRAGON","OG_NAME":"KOMODO DRAGON","type":"suicide","status":" OK","speed":2,"OG_speed":2,"atk":3,"OG_atk":3,"dfk":5,"OG_dfk":5, "hp": 55,"base_hp": 55,"current_hp": 55,"hp_coef": 1.4, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.4,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bite],
"level_list":komodo_dragon_suicide_levels}


# HORSE
horse_natural_levels = {4:bodycheck,8:stomp,12:bite,13:accelerate,16:ground_eating,18:horse_power_kick,23: deathjump}
horse_natural = {"name": "≡ HORSE","OG_NAME":"HORSE","type":"natural","status":" OK","speed":5,"OG_speed":5,"atk":4,"OG_atk":4,"dfk":3,"OG_dfk":3, "hp": 75,"base_hp": 75,"current_hp": 75,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.4,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [kick],
"level_list":horse_natural_levels}

horse_violent_levels = {3:bodycheck,7:stomp,11:bite,12:headbutt,15:massive_bite,17:horse_power_kick,22: deathjump}
horse_violent = {"name": "× HORSE","OG_NAME":"HORSE","type":"violent","status":" OK","speed":4,"OG_speed":4,"atk":5,"OG_atk":5,"dfk":2,"OG_dfk":2, "hp": 75,"base_hp": 75,"current_hp": 75,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.4,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [kick],
"level_list":horse_violent_levels}

horse_chaotic_levels = {4:bite,7:dead_eyes,8:ground_eating,12:accelerate,13:massive_bite,16:dust_blast,18:horse_power_kick,23: deathjump}
horse_chaotic = {"name": "▒ HORSE","OG_NAME":"HORSE","type":"chaotic","status":" OK","speed":5,"OG_speed":5,"atk":4,"OG_atk":4,"dfk":3,"OG_dfk":3, "hp": 72,"base_hp": 72,"current_hp": 72,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.4,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [headbutt],
"level_list":horse_chaotic_levels}

horse_suicide_levels = {3:ground_eating,7:headbutt,11:bodycheck,12:dead_eyes,15:deathjump,17:horse_power_kick,23: massive_bite}
horse_suicide = {"name": "¤ HORSE","OG_NAME":"HORSE","type":"suicide","status":" OK","speed":4,"OG_speed":4,"atk":3,"OG_atk":3,"dfk":4,"OG_dfk":4, "hp": 75,"base_hp": 75,"current_hp": 75,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.4,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [kick],
"level_list":horse_suicide_levels}


# WOLVERINE
wolverine_natural_levels = {3:regenerate,7:slash,9:claws_sharpening,11:accelerate,12:furball,14:massive_bite,15: detox}
wolverine_natural = {"name": "≡ WOLVERINE","OG_NAME":"WOLVERINE, THAT ANIMAL - NOT HUGH JACKMAN!","type":"natural","status":" OK","speed":4,"OG_speed":4,"atk":5,"OG_atk":5,"dfk":2,"OG_dfk":2, "hp": 40,"base_hp": 40,"current_hp": 40,"hp_coef": 1.2, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.4,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bite,scratch],
"level_list":wolverine_natural_levels}

wolverine_violent_levels = {3:regenerate,4:massive_bite,8:clawstorm,11:rage,12:furball,14:slash,15: detox}
wolverine_violent = {"name": "× WOLVERINE","OG_NAME":"WOLVERINE, THAT ANIMAL - NOT HUGH JACKMAN!","type":"violent","status":" OK","speed":3,"OG_speed":3,"atk":5,"OG_atk":5,"dfk":1,"OG_dfk":1, "hp": 40,"base_hp": 40,"current_hp": 40,"hp_coef": 1.2, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.4,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bite,scratch],
"level_list":wolverine_violent_levels}

wolverine_chaotic_levels = {3:dust_blast,5:slash,8:regenerate,10:detox,12:massive_bite,14:fur_armor,15: clawstorm}
wolverine_chaotic = {"name": "▒ WOLVERINE","OG_NAME":"WOLVERINE, THAT ANIMAL - NOT HUGH JACKMAN!","type":"chaotic","status":" OK","speed":4,"OG_speed":4,"atk":5,"OG_atk":5,"dfk":2,"OG_dfk":2, "hp": 36,"base_hp": 36,"current_hp": 36,"hp_coef": 1.2, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.4,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bite,furball],
"level_list":wolverine_chaotic_levels}

wolverine_suicide_levels = {3:fur_armor,4:furball,6:regenerate,10:massive_bite,11:clawstorm,13:dust_blast,15: ground_eating}
wolverine_suicide = {"name": "¤ WOLVERINE","OG_NAME":"WOLVERINE, THAT ANIMAL - NOT HUGH JACKMAN!","type":"suicide","status":" OK","speed":4,"OG_speed":4,"atk":5,"OG_atk":5,"dfk":2,"OG_dfk":2, "hp": 40,"base_hp": 40,"current_hp": 40,"hp_coef": 1.2, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":6,"attack_coef": 1.4,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bite,scratch],
"level_list":wolverine_suicide_levels}

# HELL KING
# WOLVERINE
python_natural_levels = {3:venom_fusion,5:rain_of_poison,6:tail_strangler,7:toxic_spit,9:snake_dance,11:detox}
python_natural = {"name": "≡ PYTHON","OG_NAME":"PYTHON","type":"natural","status":" OK","speed":3,"OG_speed":3,"atk":4,"OG_atk":4,"dfk":3,"OG_dfk":3, "hp": 80,"base_hp": 80,"current_hp": 40,"hp_coef": 1.3, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":19,"attack_coef": 1.4,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [massive_bite,regenerate],
"level_list":python_natural_levels}

retriever_chaotic_levels = {3:fur_armor,5:slash,6:tail_strike,7:accelerate,9:dust_blast,11:ground_eating}
retriever_chaotic = {"name": "▒ RETRIEVER","OG_NAME":"RETRIEVER","type":"chaotic","status":" OK","speed":3,"OG_speed":3,"atk":2,"OG_atk":2,"dfk":3,"OG_dfk":3, "hp": 35,"base_hp": 35,"current_hp": 35,"hp_coef": 1.4, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":16,"attack_coef": 1.2,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [bite,paw_slap],
"level_list":retriever_chaotic_levels}

pegasus_suicide_levels = {3:stomp,5:wing_slap,6:accelerate,7:moon_song,9:horse_power_kick,11:light_storm}
pegasus_suicide = {"name": "¤ PEGASUS","OG_NAME":"PEGASUS","type":"suicide","status":" OK","speed":4,"OG_speed":4,"atk":3,"OG_atk":3,"dfk":4,"OG_dfk":4, "hp": 70,"base_hp": 70,"current_hp": 70,"hp_coef": 1.4, "extra_hp": 0,"extra_def": 0,"extra_atk": 0,"extra_acc": 0,"extra_speed":0, "level":15,"attack_coef": 1.3,"exp": 0,"nature":"lost","DBP":"NO","attack_list": [kick,bite],
"level_list":pegasus_suicide_levels}




lost_souls = [polar_bear_natural,
            polar_bear_natural,
            polar_bear_natural,
            polar_bear_natural,
            polar_bear_violent,
            polar_bear_violent,
            polar_bear_violent,
            polar_bear_chaotic,
            polar_bear_chaotic,
            polar_bear_suicide,

            fox_natural,
            fox_natural,
            fox_natural,
            fox_natural,
            fox_violent,
            fox_violent,
            fox_violent,
            fox_chaotic,
            fox_chaotic,
            fox_suicide,

            viper_natural,
            viper_natural,
            viper_natural,
            viper_natural,
            viper_violent,
            viper_violent,
            viper_violent,
            viper_chaotic,
            viper_chaotic,
            viper_suicide,

            wolf_natural,
            wolf_natural,
            wolf_natural,
            wolf_natural,
            wolf_violent,
            wolf_violent,
            wolf_violent,
            wolf_chaotic,
            wolf_chaotic,
            wolf_suicide,

            eagle_natural,
            eagle_natural,
            eagle_natural,
            eagle_natural,
            eagle_violent,
            eagle_violent,
            eagle_violent,
            eagle_chaotic,
            eagle_chaotic,
            eagle_suicide,

            boar_natural,
            boar_natural,
            boar_natural,
            boar_natural,
            boar_violent,
            boar_violent,
            boar_violent,
            boar_chaotic,
            boar_chaotic,
            boar_suicide,

            stag_natural,
            stag_natural,
            stag_natural,
            stag_natural,
            stag_violent,
            stag_violent,
            stag_violent,
            stag_chaotic,
            stag_chaotic,
            stag_suicide,

            rat_natural,
            rat_natural,
            rat_natural,
            rat_natural,
            rat_violent,
            rat_violent,
            rat_violent,
            rat_chaotic,
            rat_chaotic,
            rat_suicide,

            hare_natural,
            hare_natural,
            hare_natural,
            hare_natural,
            hare_violent,
            hare_violent,
            hare_violent,
            hare_chaotic,
            hare_chaotic,
            hare_suicide,

            giraffe_natural,
            giraffe_natural,
            giraffe_natural,
            giraffe_natural,
            giraffe_violent,
            giraffe_violent,
            giraffe_violent,
            giraffe_chaotic,
            giraffe_chaotic,
            giraffe_suicide,

            bullfrog_natural,
            bullfrog_natural,
            bullfrog_natural,
            bullfrog_natural,
            bullfrog_violent,
            bullfrog_violent,
            bullfrog_violent,
            bullfrog_chaotic,
            bullfrog_chaotic,
            bullfrog_suicide,

            tortoise_natural,
            tortoise_natural,
            tortoise_natural,
            tortoise_natural,
            tortoise_violent,
            tortoise_violent,
            tortoise_violent,
            tortoise_chaotic,
            tortoise_chaotic,
            tortoise_suicide,

            rhino_natural,
            rhino_natural,
            rhino_natural,
            rhino_natural,
            rhino_violent,
            rhino_violent,
            rhino_violent,
            rhino_chaotic,
            rhino_chaotic,
            rhino_suicide,

            elephant_natural,
            elephant_natural,
            elephant_natural,
            elephant_natural,
            elephant_violent,
            elephant_violent,
            elephant_violent,
            elephant_chaotic,
            elephant_chaotic,
            elephant_suicide,

            lion_natural,
            lion_natural,
            lion_natural,
            lion_natural,
            lion_violent,
            lion_violent,
            lion_violent,
            lion_chaotic,
            lion_chaotic,
            lion_suicide,

            ostrich_natural,
            ostrich_natural,
            ostrich_natural,
            ostrich_natural,
            ostrich_violent,
            ostrich_violent,
            ostrich_violent,
            ostrich_chaotic,
            ostrich_chaotic,
            ostrich_suicide,

            pheasant_natural,
            pheasant_natural,
            pheasant_natural,
            pheasant_natural,
            pheasant_violent,
            pheasant_violent,
            pheasant_violent,
            pheasant_chaotic,
            pheasant_chaotic,
            pheasant_suicide,

            hound_natural,
            hound_natural,
            hound_natural,
            hound_natural,
            hound_violent,
            hound_violent,
            hound_violent,
            hound_chaotic,
            hound_chaotic,
            hound_suicide,

            badger_natural,
            badger_natural,
            badger_natural,
            badger_natural,
            badger_violent,
            badger_violent,
            badger_violent,
            badger_chaotic,
            badger_chaotic,
            badger_suicide,

            cat_natural,
            cat_natural,
            cat_natural,
            cat_natural,
            cat_violent,
            cat_violent,
            cat_violent,
            cat_chaotic,
            cat_chaotic,
            cat_suicide,

            gorilla_natural,
            gorilla_natural,
            gorilla_natural,
            gorilla_natural,
            gorilla_violent,
            gorilla_violent,
            gorilla_violent,
            gorilla_chaotic,
            gorilla_chaotic,
            gorilla_suicide,

            platypus_natural,
            platypus_natural,
            platypus_natural,
            platypus_natural,
            platypus_violent,
            platypus_violent,
            platypus_violent,
            platypus_chaotic,
            platypus_chaotic,
            platypus_suicide,

            panda_chaotic,
            panda_chaotic,
            panda_chaotic,
            panda_chaotic,
            panda_suicide,
            panda_suicide,
            panda_suicide,
            panda_natural,
            panda_natural,
            panda_violent,

            scorpion_natural,
            scorpion_natural,
            scorpion_natural,
            scorpion_natural,
            scorpion_violent,
            scorpion_violent,
            scorpion_violent,
            scorpion_chaotic,
            scorpion_chaotic,
            scorpion_suicide,

            anteater_natural,
            anteater_natural,
            anteater_natural,
            anteater_natural,
            anteater_violent,
            anteater_violent,
            anteater_violent,
            anteater_chaotic,
            anteater_chaotic,
            anteater_suicide,

            buffalo_natural,
            buffalo_natural,
            buffalo_natural,
            buffalo_natural,
            buffalo_violent,
            buffalo_violent,
            buffalo_violent,
            buffalo_chaotic,
            buffalo_chaotic,
            buffalo_suicide,

            alligator_natural,
            alligator_natural,
            alligator_natural,
            alligator_natural,
            alligator_violent,
            alligator_violent,
            alligator_violent,
            alligator_chaotic,
            alligator_chaotic,
            alligator_suicide,

            swan_natural,
            swan_natural,
            swan_natural,
            swan_natural,
            swan_violent,
            swan_violent,
            swan_violent,
            swan_chaotic,
            swan_chaotic,
            swan_suicide,

            komodo_dragon_natural,
            komodo_dragon_natural,
            komodo_dragon_natural,
            komodo_dragon_natural,
            komodo_dragon_violent,
            komodo_dragon_violent,
            komodo_dragon_violent,
            komodo_dragon_chaotic,
            komodo_dragon_chaotic,
            komodo_dragon_suicide,

            horse_natural,
            horse_natural,
            horse_natural,
            horse_natural,
            horse_violent,
            horse_violent,
            horse_violent,
            horse_chaotic,
            horse_chaotic,
            horse_suicide,

            wolverine_natural,
            wolverine_natural,
            wolverine_natural,
            wolverine_natural,
            wolverine_violent,
            wolverine_violent,
            wolverine_violent,
            wolverine_chaotic,
            wolverine_chaotic,
            wolverine_suicide,



            ]



level_attacks = []

