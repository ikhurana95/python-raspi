import numpy as np
import random

colours = {}
classifiedColours = {}
e = [0, 0, 0]
darkColours = []

colorsFile = """air_force_blue_raf,93,138,168
air_force_blue_usaf,0,48,143
air_superiority_blue,114,160,193
alabama_crimson,163,38,56
alice_blue,240,248,255
alizarin_crimson,227,38,54
alloy_orange,196,98,16
almond,239,222,205
amaranth,229,43,80
amber,255,191,0
amber_sae_ece,255,126,0
american_rose,255,3,62
amethyst,153,102,204
android_green,164,198,57
anti_flash_white,242,243,244
antique_brass,205,149,117
antique_fuchsia,145,92,131
antique_ruby,132,27,45
antique_white,250,235,215
ao_english,0,128,0
apple_green,141,182,0
apricot,251,206,177
aqua,0,255,255
aquamarine,127,255,212
army_green,75,83,32
arsenic,59,68,75
arylide_yellow,233,214,107
ash_grey,178,190,181
asparagus,135,169,107
atomic_tangerine,255,153,102
auburn,165,42,42
aureolin,253,238,0
aurometalsaurus,110,127,128
avocado,86,130,3
azure,0,127,255
azure_mist_web,240,255,255
baby_blue,137,207,240
baby_blue_eyes,161,202,241
baby_pink,244,194,194
ball_blue,33,171,205
banana_mania,250,231,181
banana_yellow,255,225,53
barn_red,124,10,2
battleship_grey,132,132,130
bazaar,152,119,123
beau_blue,188,212,230
beaver,159,129,112
beige,245,245,220
big_dip_o_ruby,156,37,66
bisque,255,228,196
bistre,61,43,31
bittersweet,254,111,94
bittersweet_shimmer,191,79,81
black,0,0,0
black_bean,61,12,2
black_leather_jacket,37,53,41
black_olive,59,60,54
blanched_almond,255,235,205
blast_off_bronze,165,113,100
bleu_de_france,49,140,231
blizzard_blue,172,229,238
blond,250,240,190
blue,0,0,255
blue_bell,162,162,208
blue_crayola,31,117,254
blue_gray,102,153,204
blue_green,13,152,186
blue_munsell,0,147,175
blue_ncs,0,135,189
blue_pigment,51,51,153
blue_ryb,2,71,254
blue_sapphire,18,97,128
blue_violet,138,43,226
blush,222,93,131
bole,121,68,59
bondi_blue,0,149,182
bone,227,218,201
boston_university_red,204,0,0
bottle_green,0,106,78
boysenberry,135,50,96
brandeis_blue,0,112,255
brass,181,166,66
brick_red,203,65,84
bright_cerulean,29,172,214
bright_green,102,255,0
bright_lavender,191,148,228
bright_maroon,195,33,72
bright_pink,255,0,127
bright_turquoise,8,232,222
bright_ube,209,159,232
brilliant_lavender,244,187,255
brilliant_rose,255,85,163
brink_pink,251,96,127
british_racing_green,0,66,37
bronze,205,127,50
brown_traditional,150,75,0
brown_web,165,42,42
bubble_gum,255,193,204
bubbles,231,254,255
buff,240,220,130
bulgarian_rose,72,6,7
burgundy,128,0,32
burlywood,222,184,135
burnt_orange,204,85,0
burnt_sienna,233,116,81
burnt_umber,138,51,36
byzantine,189,51,164
byzantium,112,41,99
cadet,83,104,114
cadet_blue,95,158,160
cadet_grey,145,163,176
cadmium_green,0,107,60
cadmium_orange,237,135,45
cadmium_red,227,0,34
cadmium_yellow,255,246,0
caf_au_lait,166,123,91
caf_noir,75,54,33
cal_poly_green,30,77,43
cambridge_blue,163,193,173
camel,193,154,107
cameo_pink,239,187,204
camouflage_green,120,134,107
canary_yellow,255,239,0
candy_apple_red,255,8,0
candy_pink,228,113,122
capri,0,191,255
caput_mortuum,89,39,32
cardinal,196,30,58
caribbean_green,0,204,153
carmine,150,0,24
carmine_m_p,215,0,64
carmine_pink,235,76,66
carmine_red,255,0,56
carnation_pink,255,166,201
carnelian,179,27,27
carolina_blue,153,186,221
carrot_orange,237,145,33
catalina_blue,6,42,120
ceil,146,161,207
celadon,172,225,175
celadon_blue,0,123,167
celadon_green,47,132,124
celeste_colour,178,255,255
celestial_blue,73,151,208
cerise,222,49,99
cerise_pink,236,59,131
cerulean,0,123,167
cerulean_blue,42,82,190
cerulean_frost,109,155,195
cg_blue,0,122,165
cg_red,224,60,49
chamoisee,160,120,90
champagne,250,214,165
charcoal,54,69,79
charm_pink,230,143,172
chartreuse_traditional,223,255,0
chartreuse_web,127,255,0
cherry,222,49,99
cherry_blossom_pink,255,183,197
chestnut,205,92,92
china_pink,222,111,161
china_rose,168,81,110
chinese_red,170,56,30
chocolate_traditional,123,63,0
chocolate_web,210,105,30
chrome_yellow,255,167,0
cinereous,152,129,123
cinnabar,227,66,52
cinnamon,210,105,30
citrine,228,208,10
classic_rose,251,204,231
cobalt,0,71,171
cocoa_brown,210,105,30
coffee,111,78,55
columbia_blue,155,221,255
congo_pink,248,131,121
cool_black,0,46,99
cool_grey,140,146,172
copper,184,115,51
copper_crayola,218,138,103
copper_penny,173,111,105
copper_red,203,109,81
copper_rose,153,102,102
coquelicot,255,56,0
coral,255,127,80
coral_pink,248,131,121
coral_red,255,64,64
cordovan,137,63,69
corn,251,236,93
cornell_red,179,27,27
cornflower_blue,100,149,237
cornsilk,255,248,220
cosmic_latte,255,248,231
cotton_candy,255,188,217
cream,255,253,208
crimson,220,20,60
crimson_glory,190,0,50
cyan,0,255,255
cyan_process,0,183,235
daffodil,255,255,49
dandelion,240,225,48
dark_blue,0,0,139
dark_brown,101,67,33
dark_byzantium,93,57,84
dark_candy_apple_red,164,0,0
dark_cerulean,8,69,126
dark_chestnut,152,105,96
dark_coral,205,91,69
dark_cyan,0,139,139
dark_electric_blue,83,104,120
dark_goldenrod,184,134,11
dark_gray,169,169,169
dark_green,1,50,32
dark_imperial_blue,0,65,106
dark_jungle_green,26,36,33
dark_khaki,189,183,107
dark_lava,72,60,50
dark_lavender,115,79,150
dark_magenta,139,0,139
dark_midnight_blue,0,51,102
dark_olive_green,85,107,47
dark_orange,255,140,0
dark_orchid,153,50,204
dark_pastel_blue,119,158,203
dark_pastel_green,3,192,60
dark_pastel_purple,150,111,214
dark_pastel_red,194,59,34
dark_pink,231,84,128
dark_powder_blue,0,51,153
dark_raspberry,135,38,87
dark_red,139,0,0
dark_salmon,233,150,122
dark_scarlet,86,3,25
dark_sea_green,143,188,143
dark_sienna,60,20,20
dark_slate_blue,72,61,139
dark_slate_gray,47,79,79
dark_spring_green,23,114,69
dark_tan,145,129,81
dark_tangerine,255,168,18
dark_taupe,72,60,50
dark_terra_cotta,204,78,92
dark_turquoise,0,206,209
dark_violet,148,0,211
dark_yellow,155,135,12
dartmouth_green,0,112,60
davy_s_grey,85,85,85
debian_red,215,10,83
deep_carmine,169,32,62
deep_carmine_pink,239,48,56
deep_carrot_orange,233,105,44
deep_cerise,218,50,135
deep_champagne,250,214,165
deep_chestnut,185,78,72
deep_coffee,112,66,65
deep_fuchsia,193,84,193
deep_jungle_green,0,75,73
deep_lilac,153,85,187
deep_magenta,204,0,204
deep_peach,255,203,164
deep_pink,255,20,147
deep_ruby,132,63,91
deep_saffron,255,153,51
deep_sky_blue,0,191,255
deep_tuscan_red,102,66,77
denim,21,96,189
desert,193,154,107
desert_sand,237,201,175
dim_gray,105,105,105
dodger_blue,30,144,255
dogwood_rose,215,24,104
dollar_bill,133,187,101
drab,150,113,23
duke_blue,0,0,156
earth_yellow,225,169,95
ebony,85,93,80
ecru,194,178,128
eggplant,97,64,81
eggshell,240,234,214
egyptian_blue,16,52,166
electric_blue,125,249,255
electric_crimson,255,0,63
electric_cyan,0,255,255
electric_green,0,255,0
electric_indigo,111,0,255
electric_lavender,244,187,255
electric_lime,204,255,0
electric_purple,191,0,255
electric_ultramarine,63,0,255
electric_violet,143,0,255
electric_yellow,255,255,0
emerald,80,200,120
english_lavender,180,131,149
eton_blue,150,200,162
fallow,193,154,107
falu_red,128,24,24
fandango,181,51,137
fashion_fuchsia,244,0,161
fawn,229,170,112
feldgrau,77,93,83
fern_green,79,121,66
ferrari_red,255,40,0
field_drab,108,84,30
fire_engine_red,206,32,41
firebrick,178,34,34
flame,226,88,34
flamingo_pink,252,142,172
flavescent,247,233,142
flax,238,220,130
floral_white,255,250,240
fluorescent_orange,255,191,0
fluorescent_pink,255,20,147
fluorescent_yellow,204,255,0
folly,255,0,79
forest_green_traditional,1,68,33
forest_green_web,34,139,34
french_beige,166,123,91
french_blue,0,114,187
french_lilac,134,96,142
french_lime,204,255,0
french_raspberry,199,44,72
french_rose,246,74,138
fuchsia,255,0,255
fuchsia_crayola,193,84,193
fuchsia_pink,255,119,255
fuchsia_rose,199,67,117
fulvous,228,132,0
fuzzy_wuzzy,204,102,102
gainsboro,220,220,220
gamboge,228,155,15
ghost_white,248,248,255
ginger,176,101,0
glaucous,96,130,182
glitter,230,232,250
gold_metallic,212,175,55
gold_web_golden,255,215,0
golden_brown,153,101,21
golden_poppy,252,194,0
golden_yellow,255,223,0
goldenrod,218,165,32
granny_smith_apple,168,228,160
gray,128,128,128
gray_asparagus,70,89,69
gray_html_css_gray,128,128,128
gray_x11_gray,190,190,190
green_color_wheel_x11_green,0,255,0
green_crayola,28,172,120
green_html_css_green,0,128,0
green_munsell,0,168,119
green_ncs,0,159,107
green_pigment,0,165,80
green_ryb,102,176,50
green_yellow,173,255,47
grullo,169,154,134
guppie_green,0,255,127
halay_be,102,56,84
han_blue,68,108,207
han_purple,82,24,250
hansa_yellow,233,214,107
harlequin,63,255,0
harvard_crimson,201,0,22
harvest_gold,218,145,0
heart_gold,128,128,0
heliotrope,223,115,255
hollywood_cerise,244,0,161
honeydew,240,255,240
honolulu_blue,0,127,191
hooker_s_green,73,121,107
hot_magenta,255,29,206
hot_pink,255,105,180
hunter_green,53,94,59
iceberg,113,166,210
icterine,252,247,94
imperial_blue,0,35,149
inchworm,178,236,93
india_green,19,136,8
indian_red,205,92,92
indian_yellow,227,168,87
indigo,111,0,255
indigo_dye,0,65,106
indigo_web,75,0,130
international_klein_blue,0,47,167
international_orange_aerospace,255,79,0
international_orange_engineering,186,22,12
international_orange_golden_gate_bridge,192,54,44
iris,90,79,207
isabelline,244,240,236
islamic_green,0,144,0
ivory,255,255,240
jade,0,168,107
jasmine,248,222,126
jasper,215,59,62
jazzberry_jam,165,11,94
jet,52,52,52
jonquil,250,218,94
june_bud,189,218,87
jungle_green,41,171,135
kelly_green,76,187,23
kenyan_copper,124,28,5
khaki_html_css_khaki,195,176,145
khaki_x11_light_khaki,240,230,140
ku_crimson,232,0,13
la_salle_green,8,120,48
languid_lavender,214,202,221
lapis_lazuli,38,97,156
laser_lemon,254,254,34
laurel_green,169,186,157
lava,207,16,32
lavender_blue,204,204,255
lavender_blush,255,240,245
lavender_floral,181,126,220
lavender_gray,196,195,208
lavender_indigo,148,87,235
lavender_magenta,238,130,238
lavender_mist,230,230,250
lavender_pink,251,174,210
lavender_purple,150,123,182
lavender_rose,251,160,227
lavender_web,230,230,250
lawn_green,124,252,0
lemon,255,247,0
lemon_chiffon,255,250,205
lemon_lime,227,255,0
licorice,26,17,16
light_apricot,253,213,177
light_blue,173,216,230
light_brown,181,101,29
light_carmine_pink,230,103,113
light_coral,240,128,128
light_cornflower_blue,147,204,234
light_crimson,245,105,145
light_cyan,224,255,255
light_fuchsia_pink,249,132,239
light_goldenrod_yellow,250,250,210
light_gray,211,211,211
light_green,144,238,144
light_khaki,240,230,140
light_pastel_purple,177,156,217
light_pink,255,182,193
light_red_ochre,233,116,81
light_salmon,255,160,122
light_salmon_pink,255,153,153
light_sea_green,32,178,170
light_sky_blue,135,206,250
light_slate_gray,119,136,153
light_taupe,179,139,109
light_thulian_pink,230,143,172
light_yellow,255,255,224
lilac,200,162,200
lime_color_wheel,191,255,0
lime_green,50,205,50
lime_web_x11_green,0,255,0
limerick,157,194,9
lincoln_green,25,89,5
linen,250,240,230
lion,193,154,107
little_boy_blue,108,160,220
liver,83,75,79
lust,230,32,32
magenta,255,0,255
magenta_dye,202,31,123
magenta_process,255,0,144
magic_mint,170,240,209
magnolia,248,244,255
mahogany,192,64,0
maize,251,236,93
majorelle_blue,96,80,220
malachite,11,218,81
manatee,151,154,170
mango_tango,255,130,67
mantis,116,195,101
mardi_gras,136,0,133
maroon_crayola,195,33,72
maroon_html_css,128,0,0
maroon_x11,176,48,96
mauve,224,176,255
mauve_taupe,145,95,109
mauvelous,239,152,170
maya_blue,115,194,251
meat_brown,229,183,59
medium_aquamarine,102,221,170
medium_blue,0,0,205
medium_candy_apple_red,226,6,44
medium_carmine,175,64,53
medium_champagne,243,229,171
medium_electric_blue,3,80,150
medium_jungle_green,28,53,45
medium_lavender_magenta,221,160,221
medium_orchid,186,85,211
medium_persian_blue,0,103,165
medium_purple,147,112,219
medium_red_violet,187,51,133
medium_ruby,170,64,105
medium_sea_green,60,179,113
medium_slate_blue,123,104,238
medium_spring_bud,201,220,135
medium_spring_green,0,250,154
medium_taupe,103,76,71
medium_turquoise,72,209,204
medium_tuscan_red,121,68,59
medium_vermilion,217,96,59
medium_violet_red,199,21,133
mellow_apricot,248,184,120
mellow_yellow,248,222,126
melon,253,188,180
midnight_blue,25,25,112
midnight_green_eagle_green,0,73,83
mikado_yellow,255,196,12
mint,62,180,137
mint_cream,245,255,250
mint_green,152,255,152
misty_rose,255,228,225
moccasin,250,235,215
mode_beige,150,113,23
moonstone_blue,115,169,194
mordant_red_19,174,12,0
moss_green,173,223,173
mountain_meadow,48,186,143
mountbatten_pink,153,122,141
msu_green,24,69,59
mulberry,197,75,140
mustard,255,219,88
myrtle,33,66,30
nadeshiko_pink,246,173,198
napier_green,42,128,0
naples_yellow,250,218,94
navajo_white,255,222,173
navy_blue,0,0,128
neon_carrot,255,163,67
neon_fuchsia,254,65,100
neon_green,57,255,20
new_york_pink,215,131,127
non_photo_blue,164,221,237
north_texas_green,5,144,51
ocean_boat_blue,0,119,190
ochre,204,119,34
office_green,0,128,0
old_gold,207,181,59
old_lace,253,245,230
old_lavender,121,104,120
old_mauve,103,49,71
old_rose,192,128,129
olive,128,128,0
olive_drab_7,60,52,31
olive_drab_web_olive_drab_3,107,142,35
olivine,154,185,115
onyx,53,56,57
opera_mauve,183,132,167
orange_color_wheel,255,127,0
orange_peel,255,159,0
orange_red,255,69,0
orange_ryb,251,153,2
orange_web_color,255,165,0
orchid,218,112,214
otter_brown,101,67,33
ou_crimson_red,153,0,0
outer_space,65,74,76
outrageous_orange,255,110,74
oxford_blue,0,33,71
pakistan_green,0,102,0
palatinate_blue,39,59,226
palatinate_purple,104,40,96
pale_aqua,188,212,230
pale_blue,175,238,238
pale_brown,152,118,84
pale_carmine,175,64,53
pale_cerulean,155,196,226
pale_chestnut,221,173,175
pale_copper,218,138,103
pale_cornflower_blue,171,205,239
pale_gold,230,190,138
pale_goldenrod,238,232,170
pale_green,152,251,152
pale_lavender,220,208,255
pale_magenta,249,132,229
pale_pink,250,218,221
pale_plum,221,160,221
pale_red_violet,219,112,147
pale_robin_egg_blue,150,222,209
pale_silver,201,192,187
pale_spring_bud,236,235,189
pale_taupe,188,152,126
pale_violet_red,219,112,147
pansy_purple,120,24,74
papaya_whip,255,239,213
paris_green,80,200,120
pastel_blue,174,198,207
pastel_brown,131,105,83
pastel_gray,207,207,196
pastel_green,119,221,119
pastel_magenta,244,154,194
pastel_orange,255,179,71
pastel_pink,222,165,164
pastel_purple,179,158,181
pastel_red,255,105,97
pastel_violet,203,153,201
pastel_yellow,253,253,150
patriarch,128,0,128
payne_s_grey,83,104,120
peach,255,229,180
peach_crayola,255,203,164
peach_orange,255,204,153
peach_puff,255,218,185
peach_yellow,250,223,173
pear,209,226,49
pearl,234,224,200
pearl_aqua,136,216,192
pearly_purple,183,104,162
peridot,230,226,0
periwinkle,204,204,255
persian_blue,28,57,187
persian_green,0,166,147
persian_indigo,50,18,122
persian_orange,217,144,88
persian_pink,247,127,190
persian_plum,112,28,28
persian_red,204,51,51
persian_rose,254,40,162
persimmon,236,88,0
peru,205,133,63
phlox,223,0,255
phthalo_blue,0,15,137
phthalo_green,18,53,36
piggy_pink,253,221,230
pine_green,1,121,111
pink,255,192,203
pink_lace,255,221,244
pink_orange,255,153,102
pink_pearl,231,172,207
pink_sherbet,247,143,167
pistachio,147,197,114
platinum,229,228,226
plum_traditional,142,69,133
plum_web,221,160,221
portland_orange,255,90,54
powder_blue_web,176,224,230
princeton_orange,255,143,0
prune,112,28,28
prussian_blue,0,49,83
psychedelic_purple,223,0,255
puce,204,136,153
pumpkin,255,117,24
purple_heart,105,53,156
purple_html_css,128,0,128
purple_mountain_majesty,150,120,182
purple_munsell,159,0,197
purple_pizzazz,254,78,218
purple_taupe,80,64,77
purple_x11,160,32,240
quartz,81,72,79
rackley,93,138,168
radical_red,255,53,94
rajah,251,171,96
raspberry,227,11,93
raspberry_glace,145,95,109
raspberry_pink,226,80,152
raspberry_rose,179,68,108
raw_umber,130,102,68
razzle_dazzle_rose,255,51,204
razzmatazz,227,37,107
red,255,0,0
red_brown,165,42,42
red_devil,134,1,17
red_munsell,242,0,60
red_ncs,196,2,51
red_orange,255,83,73
red_pigment,237,28,36
red_ryb,254,39,18
red_violet,199,21,133
redwood,171,78,82
regalia,82,45,128
resolution_blue,0,35,135
rich_black,0,64,64
rich_brilliant_lavender,241,167,254
rich_carmine,215,0,64
rich_electric_blue,8,146,208
rich_lavender,167,107,207
rich_lilac,182,102,210
rich_maroon,176,48,96
rifle_green,65,72,51
robin_egg_blue,0,204,204
rose,255,0,127
rose_bonbon,249,66,158
rose_ebony,103,72,70
rose_gold,183,110,121
rose_madder,227,38,54
rose_pink,255,102,204
rose_quartz,170,152,169
rose_taupe,144,93,93
rose_vale,171,78,82
rosewood,101,0,11
rosso_corsa,212,0,0
rosy_brown,188,143,143
royal_azure,0,56,168
royal_blue_traditional,0,35,102
royal_blue_web,65,105,225
royal_fuchsia,202,44,146
royal_purple,120,81,169
royal_yellow,250,218,94
rubine_red,209,0,86
ruby,224,17,95
ruby_red,155,17,30
ruddy,255,0,40
ruddy_brown,187,101,40
ruddy_pink,225,142,150
rufous,168,28,7
russet,128,70,27
rust,183,65,14
rusty_red,218,44,67
sacramento_state_green,0,86,63
saddle_brown,139,69,19
safety_orange_blaze_orange,255,103,0
saffron,244,196,48
salmon,255,140,105
salmon_pink,255,145,164
sand,194,178,128
sand_dune,150,113,23
sandstorm,236,213,64
sandy_brown,244,164,96
sandy_taupe,150,113,23
sangria,146,0,10
sap_green,80,125,42
sapphire,15,82,186
sapphire_blue,0,103,165
satin_sheen_gold,203,161,53
scarlet,255,36,0
scarlet_crayola,253,14,53
school_bus_yellow,255,216,0
screamin_green,118,255,122
sea_blue,0,105,148
sea_green,46,139,87
seal_brown,50,20,20
seashell,255,245,238
selective_yellow,255,186,0
sepia,112,66,20
shadow,138,121,93
shamrock_green,0,158,96
shocking_pink,252,15,192
shocking_pink_crayola,255,111,255
sienna,136,45,23
silver,192,192,192
sinopia,203,65,11
skobeloff,0,116,116
sky_blue,135,206,235
sky_magenta,207,113,175
slate_blue,106,90,205
slate_gray,112,128,144
smalt_dark_powder_blue,0,51,153
smokey_topaz,147,61,65
smoky_black,16,12,8
snow,255,250,250
spiro_disco_ball,15,192,252
spring_bud,167,252,0
spring_green,0,255,127
st_patrick_s_blue,35,41,122
steel_blue,70,130,180
stil_de_grain_yellow,250,218,94
stizza,153,0,0
stormcloud,79,102,106
straw,228,217,111
sunglow,255,204,51
sunset,250,214,165
tan,210,180,140
tangelo,249,77,0
tangerine,242,133,0
tangerine_yellow,255,204,0
tango_pink,228,113,122
taupe,72,60,50
taupe_gray,139,133,137
tea_green,208,240,192
tea_rose_orange,248,131,121
tea_rose_rose,244,194,194
teal,0,128,128
teal_blue,54,117,136
teal_green,0,130,127
telemagenta,207,52,118
tenn_tawny,205,87,0
terra_cotta,226,114,91
thistle,216,191,216
thulian_pink,222,111,161
tickle_me_pink,252,137,172
tiffany_blue,10,186,181
tiger_s_eye,224,141,60
timberwolf,219,215,210
titanium_yellow,238,230,0
tomato,255,99,71
toolbox,116,108,192
topaz,255,200,124
tractor_red,253,14,53
trolley_grey,128,128,128
tropical_rain_forest,0,117,94
true_blue,0,115,207
tufts_blue,65,125,193
tumbleweed,222,170,136
turkish_rose,181,114,129
turquoise,48,213,200
turquoise_blue,0,255,239
turquoise_green,160,214,180
tuscan_red,124,72,72
twilight_lavender,138,73,107
tyrian_purple,102,2,60
ua_blue,0,51,170
ua_red,217,0,76
ube,136,120,195
ucla_blue,83,104,149
ucla_gold,255,179,0
ufo_green,60,208,112
ultra_pink,255,111,255
ultramarine,18,10,143
ultramarine_blue,65,102,245
umber,99,81,71
unbleached_silk,255,221,202
united_nations_blue,91,146,229
university_of_california_gold,183,135,39
unmellow_yellow,255,255,102
up_forest_green,1,68,33
up_maroon,123,17,19
upsdell_red,174,32,41
urobilin,225,173,33
usafa_blue,0,79,152
usc_cardinal,153,0,0
usc_gold,255,204,0
utah_crimson,211,0,63
vanilla,243,229,171
vegas_gold,197,179,88
venetian_red,200,8,21
verdigris,67,179,174
vermilion_cinnabar,227,66,52
vermilion_plochere,217,96,59
veronica,160,32,240
violet,143,0,255
violet_blue,50,74,178
violet_color_wheel,127,0,255
violet_ryb,134,1,175
violet_web,238,130,238
viridian,64,130,109
vivid_auburn,146,39,36
vivid_burgundy,159,29,53
vivid_cerise,218,29,129
vivid_tangerine,255,160,137
vivid_violet,159,0,255
warm_black,0,66,66
waterspout,164,244,249
wenge,100,84,82
wheat,245,222,179
white,255,255,255
white_smoke,245,245,245
wild_blue_yonder,162,173,208
wild_strawberry,255,67,164
wild_watermelon,252,108,133
wine,114,47,55
wine_dregs,103,49,71
wisteria,201,160,220
wood_brown,193,154,107
xanadu,115,134,120
yale_blue,15,77,146
yellow,255,255,0
yellow_green,154,205,50
yellow_munsell,239,204,0
yellow_ncs,255,211,0
yellow_orange,255,174,66
yellow_process,255,239,0
yellow_ryb,254,254,51
zaffre,0,20,168
zinnwaldite_brown,44,22,8"""

file = colorsFile.split()
for line in file:
    line.replace("\n", "")
    splitLine = line.split(",")
    name = splitLine[0]
    rgb = [int(splitLine[1]), int(splitLine[2]), int(splitLine[3])]

    colours[name] = rgb

for key in colours.keys():
    for intensity in colours[key]:
        if int(intensity) > 200:
            darkColours.append(colours[key])
            break


def randomDarkColour():
    return random.choice(darkColours)


def getColour(colourName):
    selectedColours = []

    for line in file:
        line.replace("\n", "")
        splitLine = line.split(",")
        name = splitLine[0]
        if colourName in name:
            rgb = [int(splitLine[1]), int(splitLine[2]), int(splitLine[3])]
            selectedColours.append(rgb)

    return selectedColours


basicColours = [
    "yellow", "blue", "red", "pink", "green", "orange", "violet", "purple", "gold"
]

for selectedColour in basicColours:
    classifiedColours[selectedColour] = getColour(selectedColour)


def randomBlue():
    return random.choice(classifiedColours['blue'])


def randomYellow():
    return random.choice(classifiedColours['yellow'])


def randomRed():
    return random.choice(classifiedColours['red'])


def randomGreen():
    return random.choice(classifiedColours['green'])


def randomShade(shade):
    return random.choice(classifiedColours[shade])


def getBlues():
    return classifiedColours['blue']


def colour(colourName):
    try:
        return colours[colourName]
    except:
        print("Invalid colour Entered")


def randomColour():
    key = random.choice(list(colours.keys()))

    return colours[key]


def raspi_logo(randomColours=False):
    if randomColours == True:
        G = randomGreen()
        R = randomRed()
    else:
        G = [0, 255, 0]
        R = [255, 0, 0]

    O = [0, 0, 0]
    logo = [
        O, G, G, O, O, G, G, O,
        O, O, G, G, G, G, O, O,
        O, O, R, R, R, R, O, O,
        O, R, R, R, R, R, R, O,
        R, R, R, R, R, R, R, R,
        R, R, R, R, R, R, R, R,
        O, R, R, R, R, R, R, O,
        O, O, R, R, R, R, O, O,
    ]
    return logo


def seven():
    g = colours['vegas_gold']
    p = colours['electric_purple']

    seven = [
        p, p, p, p, p, p, p, p,
        p, e, g, g, g, g, g, p,
        p, e, e, e, e, e, g, p,
        p, e, e, e, e, g, e, p,
        p, e, e, e, g, e, e, p,
        p, e, e, e, g, e, e, p,
        p, e, e, e, g, e, e, p,
        p, p, p, p, p, p, p, p,
    ]

    return seven


def five():
    g = colours['vegas_gold']
    p = colours['electric_purple']

    five = [
        p, p, p, p, p, p, p, p,
        p, e, g, g, g, g, g, p,
        p, e, e, e, e, e, g, p,
        p, e, e, e, e, g, e, p,
        p, e, e, e, g, e, e, p,
        p, e, e, e, g, e, e, p,
        p, e, e, e, g, e, e, p,
        p, p, p, p, p, p, p, p,
    ]

    return five


def ten(colour):
    c = colour

    ten = [
        e, e, e, e, e, e, e, e,
        e, c, e, e, e, c, c, e,
        c, c, e, e, c, e, e, c,
        e, c, e, e, c, e, e, c,
        e, c, e, e, c, e, e, c,
        e, c, e, e, c, e, e, c,
        c, c, c, e, e, c, c, e,
        e, e, e, e, e, e, e, e,
    ]

    return ten


def eleven(colour):
    c = colour

    eleven = [
        e, e, e, e, e, e, e, e,
        e, e, c, e, e, e, c, e,
        e, c, c, e, e, c, c, e,
        e, e, c, e, e, e, c, e,
        e, e, c, e, e, e, c, e,
        e, e, c, e, e, e, c, e,
        e, c, c, c, e, c, c, c,
        e, e, e, e, e, e, e, e,
    ]

    return eleven


def twelve(colour):
    c = colour

    twelve = [
        e, e, e, e, e, e, e, e,
        e, c, e, e, e, c, c, e,
        c, c, e, e, c, e, e, c,
        e, c, e, e, e, e, e, c,
        e, c, e, e, e, e, c, e,
        e, c, e, e, e, c, e, e,
        c, c, c, e, c, c, c, c,
        e, e, e, e, e, e, e, e,
    ]

    return twelve


def arrow(colour=None):
    if colour == None:
        c = colours['salmon']
    else:
        c = colour
    arrow = [
        e, e, e, c, e, e, e, e,
        e, e, c, c, c, e, e, e,
        e, c, c, c, c, c, e, e,
        e, e, e, c, e, e, e, e,
        e, e, e, c, e, e, e, e,
        e, e, e, c, e, e, e, e,
        e, e, e, c, e, e, e, e,
        e, e, e, c, e, e, e, e,
    ]

    return arrow


def upArrow(colour=None):
    upArrow = arrow(colour)
    return upArrow


def downArrow(colour=None):
    downArrow = arrow(colour)
    downArrow.reverse()
    return downArrow


def ticTacToeBoard():
    c = randomColour()

    board = []

    for i in range(8):
        for j in range(8):
            if i == 2 or i == 5:
                board.append(c)
            elif j == 2 or j == 5:
                board.append(c)
            else:
                board.append(e)

    return board


def mosaicGlitter(borders=None):
    glitter = []
    if borders == None:
        borders = [[0, 7], [1, 6], [2, 5]]

    for i in range(8):
        for j in range(8):
            if i in borders[0] or j in borders[0]:
                glitter.append(randomYellow())
            elif i in borders[1] or j in borders[1]:
                glitter.append(randomBlue())
            elif i in borders[2] or j in borders[2]:
                glitter.append(randomYellow())
            else:
                glitter.append(randomRed())

    return glitter