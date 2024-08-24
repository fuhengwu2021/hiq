import numpy as np


#--------------------- FashionMINST ----------------------------
CLS_FMNIST= ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

#--------------------- ImageNet-1K ----------------------------
IN_MEAN = np.array([0.485, 0.456, 0.406])
IN_STD = np.array([0.229, 0.224, 0.225])
# imagenet class to folder and label name, ie. 0 => ["n01440764", "tench"]
IN_CAT = [['n01440764', 'tench'],
          ['n01443537', 'goldfish'],
          ['n01484850', 'great_white_shark'],
          ['n01491361', 'tiger_shark'],
          ['n01494475', 'hammerhead'],
          ['n01496331', 'electric_ray'],
          ['n01498041', 'stingray'],
          ['n01514668', 'cock'],
          ['n01514859', 'hen'],
          ['n01518878', 'ostrich'],
          ['n01530575', 'brambling'],
          ['n01531178', 'goldfinch'],
          ['n01532829', 'house_finch'],
          ['n01534433', 'junco'],
          ['n01537544', 'indigo_bunting'],
          ['n01558993', 'robin'],
          ['n01560419', 'bulbul'],
          ['n01580077', 'jay'],
          ['n01582220', 'magpie'],
          ['n01592084', 'chickadee'],
          ['n01601694', 'water_ouzel'],
          ['n01608432', 'kite'],
          ['n01614925', 'bald_eagle'],
          ['n01616318', 'vulture'],
          ['n01622779', 'great_grey_owl'],
          ['n01629819', 'European_fire_salamander'],
          ['n01630670', 'common_newt'],
          ['n01631663', 'eft'],
          ['n01632458', 'spotted_salamander'],
          ['n01632777', 'axolotl'],
          ['n01641577', 'bullfrog'],
          ['n01644373', 'tree_frog'],
          ['n01644900', 'tailed_frog'],
          ['n01664065', 'loggerhead'],
          ['n01665541', 'leatherback_turtle'],
          ['n01667114', 'mud_turtle'],
          ['n01667778', 'terrapin'],
          ['n01669191', 'box_turtle'],
          ['n01675722', 'banded_gecko'],
          ['n01677366', 'common_iguana'],
          ['n01682714', 'American_chameleon'],
          ['n01685808', 'whiptail'],
          ['n01687978', 'agama'],
          ['n01688243', 'frilled_lizard'],
          ['n01689811', 'alligator_lizard'],
          ['n01692333', 'Gila_monster'],
          ['n01693334', 'green_lizard'],
          ['n01694178', 'African_chameleon'],
          ['n01695060', 'Komodo_dragon'],
          ['n01697457', 'African_crocodile'],
          ['n01698640', 'American_alligator'],
          ['n01704323', 'triceratops'],
          ['n01728572', 'thunder_snake'],
          ['n01728920', 'ringneck_snake'],
          ['n01729322', 'hognose_snake'],
          ['n01729977', 'green_snake'],
          ['n01734418', 'king_snake'],
          ['n01735189', 'garter_snake'],
          ['n01737021', 'water_snake'],
          ['n01739381', 'vine_snake'],
          ['n01740131', 'night_snake'],
          ['n01742172', 'boa_constrictor'],
          ['n01744401', 'rock_python'],
          ['n01748264', 'Indian_cobra'],
          ['n01749939', 'green_mamba'],
          ['n01751748', 'sea_snake'],
          ['n01753488', 'horned_viper'],
          ['n01755581', 'diamondback'],
          ['n01756291', 'sidewinder'],
          ['n01768244', 'trilobite'],
          ['n01770081', 'harvestman'],
          ['n01770393', 'scorpion'],
          ['n01773157', 'black_and_gold_garden_spider'],
          ['n01773549', 'barn_spider'],
          ['n01773797', 'garden_spider'],
          ['n01774384', 'black_widow'],
          ['n01774750', 'tarantula'],
          ['n01775062', 'wolf_spider'],
          ['n01776313', 'tick'],
          ['n01784675', 'centipede'],
          ['n01795545', 'black_grouse'],
          ['n01796340', 'ptarmigan'],
          ['n01797886', 'ruffed_grouse'],
          ['n01798484', 'prairie_chicken'],
          ['n01806143', 'peacock'],
          ['n01806567', 'quail'],
          ['n01807496', 'partridge'],
          ['n01817953', 'African_grey'],
          ['n01818515', 'macaw'],
          ['n01819313', 'sulphur-crested_cockatoo'],
          ['n01820546', 'lorikeet'],
          ['n01824575', 'coucal'],
          ['n01828970', 'bee_eater'],
          ['n01829413', 'hornbill'],
          ['n01833805', 'hummingbird'],
          ['n01843065', 'jacamar'],
          ['n01843383', 'toucan'],
          ['n01847000', 'drake'],
          ['n01855032', 'red-breasted_merganser'],
          ['n01855672', 'goose'],
          ['n01860187', 'black_swan'],
          ['n01871265', 'tusker'],
          ['n01872401', 'echidna'],
          ['n01873310', 'platypus'],
          ['n01877812', 'wallaby'],
          ['n01882714', 'koala'],
          ['n01883070', 'wombat'],
          ['n01910747', 'jellyfish'],
          ['n01914609', 'sea_anemone'],
          ['n01917289', 'brain_coral'],
          ['n01924916', 'flatworm'],
          ['n01930112', 'nematode'],
          ['n01943899', 'conch'],
          ['n01944390', 'snail'],
          ['n01945685', 'slug'],
          ['n01950731', 'sea_slug'],
          ['n01955084', 'chiton'],
          ['n01968897', 'chambered_nautilus'],
          ['n01978287', 'Dungeness_crab'],
          ['n01978455', 'rock_crab'],
          ['n01980166', 'fiddler_crab'],
          ['n01981276', 'king_crab'],
          ['n01983481', 'American_lobster'],
          ['n01984695', 'spiny_lobster'],
          ['n01985128', 'crayfish'],
          ['n01986214', 'hermit_crab'],
          ['n01990800', 'isopod'],
          ['n02002556', 'white_stork'],
          ['n02002724', 'black_stork'],
          ['n02006656', 'spoonbill'],
          ['n02007558', 'flamingo'],
          ['n02009229', 'little_blue_heron'],
          ['n02009912', 'American_egret'],
          ['n02011460', 'bittern'],
          ['n02012849', 'crane'],
          ['n02013706', 'limpkin'],
          ['n02017213', 'European_gallinule'],
          ['n02018207', 'American_coot'],
          ['n02018795', 'bustard'],
          ['n02025239', 'ruddy_turnstone'],
          ['n02027492', 'red-backed_sandpiper'],
          ['n02028035', 'redshank'],
          ['n02033041', 'dowitcher'],
          ['n02037110', 'oystercatcher'],
          ['n02051845', 'pelican'],
          ['n02056570', 'king_penguin'],
          ['n02058221', 'albatross'],
          ['n02066245', 'grey_whale'],
          ['n02071294', 'killer_whale'],
          ['n02074367', 'dugong'],
          ['n02077923', 'sea_lion'],
          ['n02085620', 'Chihuahua'],
          ['n02085782', 'Japanese_spaniel'],
          ['n02085936', 'Maltese_dog'],
          ['n02086079', 'Pekinese'],
          ['n02086240', 'Shih-Tzu'],
          ['n02086646', 'Blenheim_spaniel'],
          ['n02086910', 'papillon'],
          ['n02087046', 'toy_terrier'],
          ['n02087394', 'Rhodesian_ridgeback'],
          ['n02088094', 'Afghan_hound'],
          ['n02088238', 'basset'],
          ['n02088364', 'beagle'],
          ['n02088466', 'bloodhound'],
          ['n02088632', 'bluetick'],
          ['n02089078', 'black-and-tan_coonhound'],
          ['n02089867', 'Walker_hound'],
          ['n02089973', 'English_foxhound'],
          ['n02090379', 'redbone'],
          ['n02090622', 'borzoi'],
          ['n02090721', 'Irish_wolfhound'],
          ['n02091032', 'Italian_greyhound'],
          ['n02091134', 'whippet'],
          ['n02091244', 'Ibizan_hound'],
          ['n02091467', 'Norwegian_elkhound'],
          ['n02091635', 'otterhound'],
          ['n02091831', 'Saluki'],
          ['n02092002', 'Scottish_deerhound'],
          ['n02092339', 'Weimaraner'],
          ['n02093256', 'Staffordshire_bullterrier'],
          ['n02093428', 'American_Staffordshire_terrier'],
          ['n02093647', 'Bedlington_terrier'],
          ['n02093754', 'Border_terrier'],
          ['n02093859', 'Kerry_blue_terrier'],
          ['n02093991', 'Irish_terrier'],
          ['n02094114', 'Norfolk_terrier'],
          ['n02094258', 'Norwich_terrier'],
          ['n02094433', 'Yorkshire_terrier'],
          ['n02095314', 'wire-haired_fox_terrier'],
          ['n02095570', 'Lakeland_terrier'],
          ['n02095889', 'Sealyham_terrier'],
          ['n02096051', 'Airedale'],
          ['n02096177', 'cairn'],
          ['n02096294', 'Australian_terrier'],
          ['n02096437', 'Dandie_Dinmont'],
          ['n02096585', 'Boston_bull'],
          ['n02097047', 'miniature_schnauzer'],
          ['n02097130', 'giant_schnauzer'],
          ['n02097209', 'standard_schnauzer'],
          ['n02097298', 'Scotch_terrier'],
          ['n02097474', 'Tibetan_terrier'],
          ['n02097658', 'silky_terrier'],
          ['n02098105', 'soft-coated_wheaten_terrier'],
          ['n02098286', 'West_Highland_white_terrier'],
          ['n02098413', 'Lhasa'],
          ['n02099267', 'flat-coated_retriever'],
          ['n02099429', 'curly-coated_retriever'],
          ['n02099601', 'golden_retriever'],
          ['n02099712', 'Labrador_retriever'],
          ['n02099849', 'Chesapeake_Bay_retriever'],
          ['n02100236', 'German_short-haired_pointer'],
          ['n02100583', 'vizsla'],
          ['n02100735', 'English_setter'],
          ['n02100877', 'Irish_setter'],
          ['n02101006', 'Gordon_setter'],
          ['n02101388', 'Brittany_spaniel'],
          ['n02101556', 'clumber'],
          ['n02102040', 'English_springer'],
          ['n02102177', 'Welsh_springer_spaniel'],
          ['n02102318', 'cocker_spaniel'],
          ['n02102480', 'Sussex_spaniel'],
          ['n02102973', 'Irish_water_spaniel'],
          ['n02104029', 'kuvasz'],
          ['n02104365', 'schipperke'],
          ['n02105056', 'groenendael'],
          ['n02105162', 'malinois'],
          ['n02105251', 'briard'],
          ['n02105412', 'kelpie'],
          ['n02105505', 'komondor'],
          ['n02105641', 'Old_English_sheepdog'],
          ['n02105855', 'Shetland_sheepdog'],
          ['n02106030', 'collie'],
          ['n02106166', 'Border_collie'],
          ['n02106382', 'Bouvier_des_Flandres'],
          ['n02106550', 'Rottweiler'],
          ['n02106662', 'German_shepherd'],
          ['n02107142', 'Doberman'],
          ['n02107312', 'miniature_pinscher'],
          ['n02107574', 'Greater_Swiss_Mountain_dog'],
          ['n02107683', 'Bernese_mountain_dog'],
          ['n02107908', 'Appenzeller'],
          ['n02108000', 'EntleBucher'],
          ['n02108089', 'boxer'],
          ['n02108422', 'bull_mastiff'],
          ['n02108551', 'Tibetan_mastiff'],
          ['n02108915', 'French_bulldog'],
          ['n02109047', 'Great_Dane'],
          ['n02109525', 'Saint_Bernard'],
          ['n02109961', 'Eskimo_dog'],
          ['n02110063', 'malamute'],
          ['n02110185', 'Siberian_husky'],
          ['n02110341', 'dalmatian'],
          ['n02110627', 'affenpinscher'],
          ['n02110806', 'basenji'],
          ['n02110958', 'pug'],
          ['n02111129', 'Leonberg'],
          ['n02111277', 'Newfoundland'],
          ['n02111500', 'Great_Pyrenees'],
          ['n02111889', 'Samoyed'],
          ['n02112018', 'Pomeranian'],
          ['n02112137', 'chow'],
          ['n02112350', 'keeshond'],
          ['n02112706', 'Brabancon_griffon'],
          ['n02113023', 'Pembroke'],
          ['n02113186', 'Cardigan'],
          ['n02113624', 'toy_poodle'],
          ['n02113712', 'miniature_poodle'],
          ['n02113799', 'standard_poodle'],
          ['n02113978', 'Mexican_hairless'],
          ['n02114367', 'timber_wolf'],
          ['n02114548', 'white_wolf'],
          ['n02114712', 'red_wolf'],
          ['n02114855', 'coyote'],
          ['n02115641', 'dingo'],
          ['n02115913', 'dhole'],
          ['n02116738', 'African_hunting_dog'],
          ['n02117135', 'hyena'],
          ['n02119022', 'red_fox'],
          ['n02119789', 'kit_fox'],
          ['n02120079', 'Arctic_fox'],
          ['n02120505', 'grey_fox'],
          ['n02123045', 'tabby'],
          ['n02123159', 'tiger_cat'],
          ['n02123394', 'Persian_cat'],
          ['n02123597', 'Siamese_cat'],
          ['n02124075', 'Egyptian_cat'],
          ['n02125311', 'cougar'],
          ['n02127052', 'lynx'],
          ['n02128385', 'leopard'],
          ['n02128757', 'snow_leopard'],
          ['n02128925', 'jaguar'],
          ['n02129165', 'lion'],
          ['n02129604', 'tiger'],
          ['n02130308', 'cheetah'],
          ['n02132136', 'brown_bear'],
          ['n02133161', 'American_black_bear'],
          ['n02134084', 'ice_bear'],
          ['n02134418', 'sloth_bear'],
          ['n02137549', 'mongoose'],
          ['n02138441', 'meerkat'],
          ['n02165105', 'tiger_beetle'],
          ['n02165456', 'ladybug'],
          ['n02167151', 'ground_beetle'],
          ['n02168699', 'long-horned_beetle'],
          ['n02169497', 'leaf_beetle'],
          ['n02172182', 'dung_beetle'],
          ['n02174001', 'rhinoceros_beetle'],
          ['n02177972', 'weevil'],
          ['n02190166', 'fly'],
          ['n02206856', 'bee'],
          ['n02219486', 'ant'],
          ['n02226429', 'grasshopper'],
          ['n02229544', 'cricket'],
          ['n02231487', 'walking_stick'],
          ['n02233338', 'cockroach'],
          ['n02236044', 'mantis'],
          ['n02256656', 'cicada'],
          ['n02259212', 'leafhopper'],
          ['n02264363', 'lacewing'],
          ['n02268443', 'dragonfly'],
          ['n02268853', 'damselfly'],
          ['n02276258', 'admiral'],
          ['n02277742', 'ringlet'],
          ['n02279972', 'monarch'],
          ['n02280649', 'cabbage_butterfly'],
          ['n02281406', 'sulphur_butterfly'],
          ['n02281787', 'lycaenid'],
          ['n02317335', 'starfish'],
          ['n02319095', 'sea_urchin'],
          ['n02321529', 'sea_cucumber'],
          ['n02325366', 'wood_rabbit'],
          ['n02326432', 'hare'],
          ['n02328150', 'Angora'],
          ['n02342885', 'hamster'],
          ['n02346627', 'porcupine'],
          ['n02356798', 'fox_squirrel'],
          ['n02361337', 'marmot'],
          ['n02363005', 'beaver'],
          ['n02364673', 'guinea_pig'],
          ['n02389026', 'sorrel'],
          ['n02391049', 'zebra'],
          ['n02395406', 'hog'],
          ['n02396427', 'wild_boar'],
          ['n02397096', 'warthog'],
          ['n02398521', 'hippopotamus'],
          ['n02403003', 'ox'],
          ['n02408429', 'water_buffalo'],
          ['n02410509', 'bison'],
          ['n02412080', 'ram'],
          ['n02415577', 'bighorn'],
          ['n02417914', 'ibex'],
          ['n02422106', 'hartebeest'],
          ['n02422699', 'impala'],
          ['n02423022', 'gazelle'],
          ['n02437312', 'Arabian_camel'],
          ['n02437616', 'llama'],
          ['n02441942', 'weasel'],
          ['n02442845', 'mink'],
          ['n02443114', 'polecat'],
          ['n02443484', 'black-footed_ferret'],
          ['n02444819', 'otter'],
          ['n02445715', 'skunk'],
          ['n02447366', 'badger'],
          ['n02454379', 'armadillo'],
          ['n02457408', 'three-toed_sloth'],
          ['n02480495', 'orangutan'],
          ['n02480855', 'gorilla'],
          ['n02481823', 'chimpanzee'],
          ['n02483362', 'gibbon'],
          ['n02483708', 'siamang'],
          ['n02484975', 'guenon'],
          ['n02486261', 'patas'],
          ['n02486410', 'baboon'],
          ['n02487347', 'macaque'],
          ['n02488291', 'langur'],
          ['n02488702', 'colobus'],
          ['n02489166', 'proboscis_monkey'],
          ['n02490219', 'marmoset'],
          ['n02492035', 'capuchin'],
          ['n02492660', 'howler_monkey'],
          ['n02493509', 'titi'],
          ['n02493793', 'spider_monkey'],
          ['n02494079', 'squirrel_monkey'],
          ['n02497673', 'Madagascar_cat'],
          ['n02500267', 'indri'],
          ['n02504013', 'Indian_elephant'],
          ['n02504458', 'African_elephant'],
          ['n02509815', 'lesser_panda'],
          ['n02510455', 'giant_panda'],
          ['n02514041', 'barracouta'],
          ['n02526121', 'eel'],
          ['n02536864', 'coho'],
          ['n02606052', 'rock_beauty'],
          ['n02607072', 'anemone_fish'],
          ['n02640242', 'sturgeon'],
          ['n02641379', 'gar'],
          ['n02643566', 'lionfish'],
          ['n02655020', 'puffer'],
          ['n02666196', 'abacus'],
          ['n02667093', 'abaya'],
          ['n02669723', 'academic_gown'],
          ['n02672831', 'accordion'],
          ['n02676566', 'acoustic_guitar'],
          ['n02687172', 'aircraft_carrier'],
          ['n02690373', 'airliner'],
          ['n02692877', 'airship'],
          ['n02699494', 'altar'],
          ['n02701002', 'ambulance'],
          ['n02704792', 'amphibian'],
          ['n02708093', 'analog_clock'],
          ['n02727426', 'apiary'],
          ['n02730930', 'apron'],
          ['n02747177', 'ashcan'],
          ['n02749479', 'assault_rifle'],
          ['n02769748', 'backpack'],
          ['n02776631', 'bakery'],
          ['n02777292', 'balance_beam'],
          ['n02782093', 'balloon'],
          ['n02783161', 'ballpoint'],
          ['n02786058', 'Band_Aid'],
          ['n02787622', 'banjo'],
          ['n02788148', 'bannister'],
          ['n02790996', 'barbell'],
          ['n02791124', 'barber_chair'],
          ['n02791270', 'barbershop'],
          ['n02793495', 'barn'],
          ['n02794156', 'barometer'],
          ['n02795169', 'barrel'],
          ['n02797295', 'barrow'],
          ['n02799071', 'baseball'],
          ['n02802426', 'basketball'],
          ['n02804414', 'bassinet'],
          ['n02804610', 'bassoon'],
          ['n02807133', 'bathing_cap'],
          ['n02808304', 'bath_towel'],
          ['n02808440', 'bathtub'],
          ['n02814533', 'beach_wagon'],
          ['n02814860', 'beacon'],
          ['n02815834', 'beaker'],
          ['n02817516', 'bearskin'],
          ['n02823428', 'beer_bottle'],
          ['n02823750', 'beer_glass'],
          ['n02825657', 'bell_cote'],
          ['n02834397', 'bib'],
          ['n02835271', 'bicycle-built-for-two'],
          ['n02837789', 'bikini'],
          ['n02840245', 'binder'],
          ['n02841315', 'binoculars'],
          ['n02843684', 'birdhouse'],
          ['n02859443', 'boathouse'],
          ['n02860847', 'bobsled'],
          ['n02865351', 'bolo_tie'],
          ['n02869837', 'bonnet'],
          ['n02870880', 'bookcase'],
          ['n02871525', 'bookshop'],
          ['n02877765', 'bottlecap'],
          ['n02879718', 'bow'],
          ['n02883205', 'bow_tie'],
          ['n02892201', 'brass'],
          ['n02892767', 'brassiere'],
          ['n02894605', 'breakwater'],
          ['n02895154', 'breastplate'],
          ['n02906734', 'broom'],
          ['n02909870', 'bucket'],
          ['n02910353', 'buckle'],
          ['n02916936', 'bulletproof_vest'],
          ['n02917067', 'bullet_train'],
          ['n02927161', 'butcher_shop'],
          ['n02930766', 'cab'],
          ['n02939185', 'caldron'],
          ['n02948072', 'candle'],
          ['n02950826', 'cannon'],
          ['n02951358', 'canoe'],
          ['n02951585', 'can_opener'],
          ['n02963159', 'cardigan'],
          ['n02965783', 'car_mirror'],
          ['n02966193', 'carousel'],
          ['n02966687', "carpenter's_kit"],
          ['n02971356', 'carton'],
          ['n02974003', 'car_wheel'],
          ['n02977058', 'cash_machine'],
          ['n02978881', 'cassette'],
          ['n02979186', 'cassette_player'],
          ['n02980441', 'castle'],
          ['n02981792', 'catamaran'],
          ['n02988304', 'CD_player'],
          ['n02992211', 'cello'],
          ['n02992529', 'cellular_telephone'],
          ['n02999410', 'chain'],
          ['n03000134', 'chainlink_fence'],
          ['n03000247', 'chain_mail'],
          ['n03000684', 'chain_saw'],
          ['n03014705', 'chest'],
          ['n03016953', 'chiffonier'],
          ['n03017168', 'chime'],
          ['n03018349', 'china_cabinet'],
          ['n03026506', 'Christmas_stocking'],
          ['n03028079', 'church'],
          ['n03032252', 'cinema'],
          ['n03041632', 'cleaver'],
          ['n03042490', 'cliff_dwelling'],
          ['n03045698', 'cloak'],
          ['n03047690', 'clog'],
          ['n03062245', 'cocktail_shaker'],
          ['n03063599', 'coffee_mug'],
          ['n03063689', 'coffeepot'],
          ['n03065424', 'coil'],
          ['n03075370', 'combination_lock'],
          ['n03085013', 'computer_keyboard'],
          ['n03089624', 'confectionery'],
          ['n03095699', 'container_ship'],
          ['n03100240', 'convertible'],
          ['n03109150', 'corkscrew'],
          ['n03110669', 'cornet'],
          ['n03124043', 'cowboy_boot'],
          ['n03124170', 'cowboy_hat'],
          ['n03125729', 'cradle'],
          ['n03126707', 'crane'],
          ['n03127747', 'crash_helmet'],
          ['n03127925', 'crate'],
          ['n03131574', 'crib'],
          ['n03133878', 'Crock_Pot'],
          ['n03134739', 'croquet_ball'],
          ['n03141823', 'crutch'],
          ['n03146219', 'cuirass'],
          ['n03160309', 'dam'],
          ['n03179701', 'desk'],
          ['n03180011', 'desktop_computer'],
          ['n03187595', 'dial_telephone'],
          ['n03188531', 'diaper'],
          ['n03196217', 'digital_clock'],
          ['n03197337', 'digital_watch'],
          ['n03201208', 'dining_table'],
          ['n03207743', 'dishrag'],
          ['n03207941', 'dishwasher'],
          ['n03208938', 'disk_brake'],
          ['n03216828', 'dock'],
          ['n03218198', 'dogsled'],
          ['n03220513', 'dome'],
          ['n03223299', 'doormat'],
          ['n03240683', 'drilling_platform'],
          ['n03249569', 'drum'],
          ['n03250847', 'drumstick'],
          ['n03255030', 'dumbbell'],
          ['n03259280', 'Dutch_oven'],
          ['n03271574', 'electric_fan'],
          ['n03272010', 'electric_guitar'],
          ['n03272562', 'electric_locomotive'],
          ['n03290653', 'entertainment_center'],
          ['n03291819', 'envelope'],
          ['n03297495', 'espresso_maker'],
          ['n03314780', 'face_powder'],
          ['n03325584', 'feather_boa'],
          ['n03337140', 'file'],
          ['n03344393', 'fireboat'],
          ['n03345487', 'fire_engine'],
          ['n03347037', 'fire_screen'],
          ['n03355925', 'flagpole'],
          ['n03372029', 'flute'],
          ['n03376595', 'folding_chair'],
          ['n03379051', 'football_helmet'],
          ['n03384352', 'forklift'],
          ['n03388043', 'fountain'],
          ['n03388183', 'fountain_pen'],
          ['n03388549', 'four-poster'],
          ['n03393912', 'freight_car'],
          ['n03394916', 'French_horn'],
          ['n03400231', 'frying_pan'],
          ['n03404251', 'fur_coat'],
          ['n03417042', 'garbage_truck'],
          ['n03424325', 'gasmask'],
          ['n03425413', 'gas_pump'],
          ['n03443371', 'goblet'],
          ['n03444034', 'go-kart'],
          ['n03445777', 'golf_ball'],
          ['n03445924', 'golfcart'],
          ['n03447447', 'gondola'],
          ['n03447721', 'gong'],
          ['n03450230', 'gown'],
          ['n03452741', 'grand_piano'],
          ['n03457902', 'greenhouse'],
          ['n03459775', 'grille'],
          ['n03461385', 'grocery_store'],
          ['n03467068', 'guillotine'],
          ['n03476684', 'hair_slide'],
          ['n03476991', 'hair_spray'],
          ['n03478589', 'half_track'],
          ['n03481172', 'hammer'],
          ['n03482405', 'hamper'],
          ['n03483316', 'hand_blower'],
          ['n03485407', 'hand-held_computer'],
          ['n03485794', 'handkerchief'],
          ['n03492542', 'hard_disc'],
          ['n03494278', 'harmonica'],
          ['n03495258', 'harp'],
          ['n03496892', 'harvester'],
          ['n03498962', 'hatchet'],
          ['n03527444', 'holster'],
          ['n03529860', 'home_theater'],
          ['n03530642', 'honeycomb'],
          ['n03532672', 'hook'],
          ['n03534580', 'hoopskirt'],
          ['n03535780', 'horizontal_bar'],
          ['n03538406', 'horse_cart'],
          ['n03544143', 'hourglass'],
          ['n03584254', 'iPod'],
          ['n03584829', 'iron'],
          ['n03590841', "jack-o'-lantern"],
          ['n03594734', 'jean'],
          ['n03594945', 'jeep'],
          ['n03595614', 'jersey'],
          ['n03598930', 'jigsaw_puzzle'],
          ['n03599486', 'jinrikisha'],
          ['n03602883', 'joystick'],
          ['n03617480', 'kimono'],
          ['n03623198', 'knee_pad'],
          ['n03627232', 'knot'],
          ['n03630383', 'lab_coat'],
          ['n03633091', 'ladle'],
          ['n03637318', 'lampshade'],
          ['n03642806', 'laptop'],
          ['n03649909', 'lawn_mower'],
          ['n03657121', 'lens_cap'],
          ['n03658185', 'letter_opener'],
          ['n03661043', 'library'],
          ['n03662601', 'lifeboat'],
          ['n03666591', 'lighter'],
          ['n03670208', 'limousine'],
          ['n03673027', 'liner'],
          ['n03676483', 'lipstick'],
          ['n03680355', 'Loafer'],
          ['n03690938', 'lotion'],
          ['n03691459', 'loudspeaker'],
          ['n03692522', 'loupe'],
          ['n03697007', 'lumbermill'],
          ['n03706229', 'magnetic_compass'],
          ['n03709823', 'mailbag'],
          ['n03710193', 'mailbox'],
          ['n03710637', 'maillot'],
          ['n03710721', 'maillot'],
          ['n03717622', 'manhole_cover'],
          ['n03720891', 'maraca'],
          ['n03721384', 'marimba'],
          ['n03724870', 'mask'],
          ['n03729826', 'matchstick'],
          ['n03733131', 'maypole'],
          ['n03733281', 'maze'],
          ['n03733805', 'measuring_cup'],
          ['n03742115', 'medicine_chest'],
          ['n03743016', 'megalith'],
          ['n03759954', 'microphone'],
          ['n03761084', 'microwave'],
          ['n03763968', 'military_uniform'],
          ['n03764736', 'milk_can'],
          ['n03769881', 'minibus'],
          ['n03770439', 'miniskirt'],
          ['n03770679', 'minivan'],
          ['n03773504', 'missile'],
          ['n03775071', 'mitten'],
          ['n03775546', 'mixing_bowl'],
          ['n03776460', 'mobile_home'],
          ['n03777568', 'Model_T'],
          ['n03777754', 'modem'],
          ['n03781244', 'monastery'],
          ['n03782006', 'monitor'],
          ['n03785016', 'moped'],
          ['n03786901', 'mortar'],
          ['n03787032', 'mortarboard'],
          ['n03788195', 'mosque'],
          ['n03788365', 'mosquito_net'],
          ['n03791053', 'motor_scooter'],
          ['n03792782', 'mountain_bike'],
          ['n03792972', 'mountain_tent'],
          ['n03793489', 'mouse'],
          ['n03794056', 'mousetrap'],
          ['n03796401', 'moving_van'],
          ['n03803284', 'muzzle'],
          ['n03804744', 'nail'],
          ['n03814639', 'neck_brace'],
          ['n03814906', 'necklace'],
          ['n03825788', 'nipple'],
          ['n03832673', 'notebook'],
          ['n03837869', 'obelisk'],
          ['n03838899', 'oboe'],
          ['n03840681', 'ocarina'],
          ['n03841143', 'odometer'],
          ['n03843555', 'oil_filter'],
          ['n03854065', 'organ'],
          ['n03857828', 'oscilloscope'],
          ['n03866082', 'overskirt'],
          ['n03868242', 'oxcart'],
          ['n03868863', 'oxygen_mask'],
          ['n03871628', 'packet'],
          ['n03873416', 'paddle'],
          ['n03874293', 'paddlewheel'],
          ['n03874599', 'padlock'],
          ['n03876231', 'paintbrush'],
          ['n03877472', 'pajama'],
          ['n03877845', 'palace'],
          ['n03884397', 'panpipe'],
          ['n03887697', 'paper_towel'],
          ['n03888257', 'parachute'],
          ['n03888605', 'parallel_bars'],
          ['n03891251', 'park_bench'],
          ['n03891332', 'parking_meter'],
          ['n03895866', 'passenger_car'],
          ['n03899768', 'patio'],
          ['n03902125', 'pay-phone'],
          ['n03903868', 'pedestal'],
          ['n03908618', 'pencil_box'],
          ['n03908714', 'pencil_sharpener'],
          ['n03916031', 'perfume'],
          ['n03920288', 'Petri_dish'],
          ['n03924679', 'photocopier'],
          ['n03929660', 'pick'],
          ['n03929855', 'pickelhaube'],
          ['n03930313', 'picket_fence'],
          ['n03930630', 'pickup'],
          ['n03933933', 'pier'],
          ['n03935335', 'piggy_bank'],
          ['n03937543', 'pill_bottle'],
          ['n03938244', 'pillow'],
          ['n03942813', 'ping-pong_ball'],
          ['n03944341', 'pinwheel'],
          ['n03947888', 'pirate'],
          ['n03950228', 'pitcher'],
          ['n03954731', 'plane'],
          ['n03956157', 'planetarium'],
          ['n03958227', 'plastic_bag'],
          ['n03961711', 'plate_rack'],
          ['n03967562', 'plow'],
          ['n03970156', 'plunger'],
          ['n03976467', 'Polaroid_camera'],
          ['n03976657', 'pole'],
          ['n03977966', 'police_van'],
          ['n03980874', 'poncho'],
          ['n03982430', 'pool_table'],
          ['n03983396', 'pop_bottle'],
          ['n03991062', 'pot'],
          ['n03992509', "potter's_wheel"],
          ['n03995372', 'power_drill'],
          ['n03998194', 'prayer_rug'],
          ['n04004767', 'printer'],
          ['n04005630', 'prison'],
          ['n04008634', 'projectile'],
          ['n04009552', 'projector'],
          ['n04019541', 'puck'],
          ['n04023962', 'punching_bag'],
          ['n04026417', 'purse'],
          ['n04033901', 'quill'],
          ['n04033995', 'quilt'],
          ['n04037443', 'racer'],
          ['n04039381', 'racket'],
          ['n04040759', 'radiator'],
          ['n04041544', 'radio'],
          ['n04044716', 'radio_telescope'],
          ['n04049303', 'rain_barrel'],
          ['n04065272', 'recreational_vehicle'],
          ['n04067472', 'reel'],
          ['n04069434', 'reflex_camera'],
          ['n04070727', 'refrigerator'],
          ['n04074963', 'remote_control'],
          ['n04081281', 'restaurant'],
          ['n04086273', 'revolver'],
          ['n04090263', 'rifle'],
          ['n04099969', 'rocking_chair'],
          ['n04111531', 'rotisserie'],
          ['n04116512', 'rubber_eraser'],
          ['n04118538', 'rugby_ball'],
          ['n04118776', 'rule'],
          ['n04120489', 'running_shoe'],
          ['n04125021', 'safe'],
          ['n04127249', 'safety_pin'],
          ['n04131690', 'saltshaker'],
          ['n04133789', 'sandal'],
          ['n04136333', 'sarong'],
          ['n04141076', 'sax'],
          ['n04141327', 'scabbard'],
          ['n04141975', 'scale'],
          ['n04146614', 'school_bus'],
          ['n04147183', 'schooner'],
          ['n04149813', 'scoreboard'],
          ['n04152593', 'screen'],
          ['n04153751', 'screw'],
          ['n04154565', 'screwdriver'],
          ['n04162706', 'seat_belt'],
          ['n04179913', 'sewing_machine'],
          ['n04192698', 'shield'],
          ['n04200800', 'shoe_shop'],
          ['n04201297', 'shoji'],
          ['n04204238', 'shopping_basket'],
          ['n04204347', 'shopping_cart'],
          ['n04208210', 'shovel'],
          ['n04209133', 'shower_cap'],
          ['n04209239', 'shower_curtain'],
          ['n04228054', 'ski'],
          ['n04229816', 'ski_mask'],
          ['n04235860', 'sleeping_bag'],
          ['n04238763', 'slide_rule'],
          ['n04239074', 'sliding_door'],
          ['n04243546', 'slot'],
          ['n04251144', 'snorkel'],
          ['n04252077', 'snowmobile'],
          ['n04252225', 'snowplow'],
          ['n04254120', 'soap_dispenser'],
          ['n04254680', 'soccer_ball'],
          ['n04254777', 'sock'],
          ['n04258138', 'solar_dish'],
          ['n04259630', 'sombrero'],
          ['n04263257', 'soup_bowl'],
          ['n04264628', 'space_bar'],
          ['n04265275', 'space_heater'],
          ['n04266014', 'space_shuttle'],
          ['n04270147', 'spatula'],
          ['n04273569', 'speedboat'],
          ['n04275548', 'spider_web'],
          ['n04277352', 'spindle'],
          ['n04285008', 'sports_car'],
          ['n04286575', 'spotlight'],
          ['n04296562', 'stage'],
          ['n04310018', 'steam_locomotive'],
          ['n04311004', 'steel_arch_bridge'],
          ['n04311174', 'steel_drum'],
          ['n04317175', 'stethoscope'],
          ['n04325704', 'stole'],
          ['n04326547', 'stone_wall'],
          ['n04328186', 'stopwatch'],
          ['n04330267', 'stove'],
          ['n04332243', 'strainer'],
          ['n04335435', 'streetcar'],
          ['n04336792', 'stretcher'],
          ['n04344873', 'studio_couch'],
          ['n04346328', 'stupa'],
          ['n04347754', 'submarine'],
          ['n04350905', 'suit'],
          ['n04355338', 'sundial'],
          ['n04355933', 'sunglass'],
          ['n04356056', 'sunglasses'],
          ['n04357314', 'sunscreen'],
          ['n04366367', 'suspension_bridge'],
          ['n04367480', 'swab'],
          ['n04370456', 'sweatshirt'],
          ['n04371430', 'swimming_trunks'],
          ['n04371774', 'swing'],
          ['n04372370', 'switch'],
          ['n04376876', 'syringe'],
          ['n04380533', 'table_lamp'],
          ['n04389033', 'tank'],
          ['n04392985', 'tape_player'],
          ['n04398044', 'teapot'],
          ['n04399382', 'teddy'],
          ['n04404412', 'television'],
          ['n04409515', 'tennis_ball'],
          ['n04417672', 'thatch'],
          ['n04418357', 'theater_curtain'],
          ['n04423845', 'thimble'],
          ['n04428191', 'thresher'],
          ['n04429376', 'throne'],
          ['n04435653', 'tile_roof'],
          ['n04442312', 'toaster'],
          ['n04443257', 'tobacco_shop'],
          ['n04447861', 'toilet_seat'],
          ['n04456115', 'torch'],
          ['n04458633', 'totem_pole'],
          ['n04461696', 'tow_truck'],
          ['n04462240', 'toyshop'],
          ['n04465501', 'tractor'],
          ['n04467665', 'trailer_truck'],
          ['n04476259', 'tray'],
          ['n04479046', 'trench_coat'],
          ['n04482393', 'tricycle'],
          ['n04483307', 'trimaran'],
          ['n04485082', 'tripod'],
          ['n04486054', 'triumphal_arch'],
          ['n04487081', 'trolleybus'],
          ['n04487394', 'trombone'],
          ['n04493381', 'tub'],
          ['n04501370', 'turnstile'],
          ['n04505470', 'typewriter_keyboard'],
          ['n04507155', 'umbrella'],
          ['n04509417', 'unicycle'],
          ['n04515003', 'upright'],
          ['n04517823', 'vacuum'],
          ['n04522168', 'vase'],
          ['n04523525', 'vault'],
          ['n04525038', 'velvet'],
          ['n04525305', 'vending_machine'],
          ['n04532106', 'vestment'],
          ['n04532670', 'viaduct'],
          ['n04536866', 'violin'],
          ['n04540053', 'volleyball'],
          ['n04542943', 'waffle_iron'],
          ['n04548280', 'wall_clock'],
          ['n04548362', 'wallet'],
          ['n04550184', 'wardrobe'],
          ['n04552348', 'warplane'],
          ['n04553703', 'washbasin'],
          ['n04554684', 'washer'],
          ['n04557648', 'water_bottle'],
          ['n04560804', 'water_jug'],
          ['n04562935', 'water_tower'],
          ['n04579145', 'whiskey_jug'],
          ['n04579432', 'whistle'],
          ['n04584207', 'wig'],
          ['n04589890', 'window_screen'],
          ['n04590129', 'window_shade'],
          ['n04591157', 'Windsor_tie'],
          ['n04591713', 'wine_bottle'],
          ['n04592741', 'wing'],
          ['n04596742', 'wok'],
          ['n04597913', 'wooden_spoon'],
          ['n04599235', 'wool'],
          ['n04604644', 'worm_fence'],
          ['n04606251', 'wreck'],
          ['n04612504', 'yawl'],
          ['n04613696', 'yurt'],
          ['n06359193', 'web_site'],
          ['n06596364', 'comic_book'],
          ['n06785654', 'crossword_puzzle'],
          ['n06794110', 'street_sign'],
          ['n06874185', 'traffic_light'],
          ['n07248320', 'book_jacket'],
          ['n07565083', 'menu'],
          ['n07579787', 'plate'],
          ['n07583066', 'guacamole'],
          ['n07584110', 'consomme'],
          ['n07590611', 'hot_pot'],
          ['n07613480', 'trifle'],
          ['n07614500', 'ice_cream'],
          ['n07615774', 'ice_lolly'],
          ['n07684084', 'French_loaf'],
          ['n07693725', 'bagel'],
          ['n07695742', 'pretzel'],
          ['n07697313', 'cheeseburger'],
          ['n07697537', 'hotdog'],
          ['n07711569', 'mashed_potato'],
          ['n07714571', 'head_cabbage'],
          ['n07714990', 'broccoli'],
          ['n07715103', 'cauliflower'],
          ['n07716358', 'zucchini'],
          ['n07716906', 'spaghetti_squash'],
          ['n07717410', 'acorn_squash'],
          ['n07717556', 'butternut_squash'],
          ['n07718472', 'cucumber'],
          ['n07718747', 'artichoke'],
          ['n07720875', 'bell_pepper'],
          ['n07730033', 'cardoon'],
          ['n07734744', 'mushroom'],
          ['n07742313', 'Granny_Smith'],
          ['n07745940', 'strawberry'],
          ['n07747607', 'orange'],
          ['n07749582', 'lemon'],
          ['n07753113', 'fig'],
          ['n07753275', 'pineapple'],
          ['n07753592', 'banana'],
          ['n07754684', 'jackfruit'],
          ['n07760859', 'custard_apple'],
          ['n07768694', 'pomegranate'],
          ['n07802026', 'hay'],
          ['n07831146', 'carbonara'],
          ['n07836838', 'chocolate_sauce'],
          ['n07860988', 'dough'],
          ['n07871810', 'meat_loaf'],
          ['n07873807', 'pizza'],
          ['n07875152', 'potpie'],
          ['n07880968', 'burrito'],
          ['n07892512', 'red_wine'],
          ['n07920052', 'espresso'],
          ['n07930864', 'cup'],
          ['n07932039', 'eggnog'],
          ['n09193705', 'alp'],
          ['n09229709', 'bubble'],
          ['n09246464', 'cliff'],
          ['n09256479', 'coral_reef'],
          ['n09288635', 'geyser'],
          ['n09332890', 'lakeside'],
          ['n09399592', 'promontory'],
          ['n09421951', 'sandbar'],
          ['n09428293', 'seashore'],
          ['n09468604', 'valley'],
          ['n09472597', 'volcano'],
          ['n09835506', 'ballplayer'],
          ['n10148035', 'groom'],
          ['n10565667', 'scuba_diver'],
          ['n11879895', 'rapeseed'],
          ['n11939491', 'daisy'],
          ['n12057211', "yellow_lady's_slipper"],
          ['n12144580', 'corn'],
          ['n12267677', 'acorn'],
          ['n12620546', 'hip'],
          ['n12768682', 'buckeye'],
          ['n12985857', 'coral_fungus'],
          ['n12998815', 'agaric'],
          ['n13037406', 'gyromitra'],
          ['n13040303', 'stinkhorn'],
          ['n13044778', 'earthstar'],
          ['n13052670', 'hen-of-the-woods'],
          ['n13054560', 'bolete'],
          ['n13133613', 'ear'],
          ['n15075141', 'toilet_tissue']]
