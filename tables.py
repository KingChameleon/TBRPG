#!/usr/bin/env python

# player tables in the form of dictionaries


player_strength_dict = {'strength': 1, 'damage_modifier': 1, 'carry_weight_modifier': 1}
player_dex_dict = {'dexterity': 1, 'evade_modifier': 1, 'ranged_modifier': 1}
player_constitution_dict = {'resist_modifier': 1, 'health_modifier': 1, 'stamina_modifier': 1}
player_intelligence_dict = {'spell_resist_modifier': 1, 'spell_power_modifier': 1, 'skill_point_modifier': 1}
player_wisdom_dict = {'willpower': 1, 'perception_modifier': 1, 'intuition_modifier': 1}
player_charisma_dict = {'persuasion_modifier': 1, 'diplomacy_modifier': 1, 'speech_modifier': 1}



def replace_value(dict_to_find, key_to_find, definition):
    for key in dict_to_find.keys():
        if key == key_to_find:
            dict_to_find[key] = definition

def find_value(dict_to_find, key_to_find):
    for key in dict_to_find.keys():
        if key == key_to_find:
            key_value = dict_to_find[key]
            return key_value