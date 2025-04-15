base_monsters = {
	'Springheel': {
		'id': 'springheel',
		'locations': [
			"Cherry Cross Station",
			"Harbourtown Beach",
			"Harbourtown Outskirts"
		],
		'type': "beast",
		'stats': [90,130,80,80,90,130],
		},
	'Hopskin': {
		'id': 'hopskin',
		'locations': [
			"New London",
			"Cherry Cross Station",
			"remaster_Springheel"
		],
		'type': "beast",
		'stats': [90,170,100,90,100,150],
		},
	'Ripterra': {
		'id': 'ripterra',
		'locations': [
			"New London",
			"remaster_Hopskin"
		],
		'type': "beast",
		'stats': [120,200,100,90,120,170],
		},
	'Snoopin': {
		'id': 'snoopin',
		'locations': [
			"New London",
			"Cherry Cross Station",
			"remaster_Springheel"
		],
		'type': "beast",
		'stats': [90,160,80,150,90,130],
		},
	'Scampire': {
		'id': 'scampire',
		'locations': [
			"Lost Hearts Graveyard",
			"remaster_Snoopin"
		],
		'type': "beast",
		'stats': [120,160,80,180,90,170],
		},
	'Carniviper': {
		'id': 'carniviper',
		'locations': [
			"Harbourtown Beach",
			"Harbourtown Outskirts",
			"Glowcester Road Station",
			"New Wirral Park",
			"New London",
			"Deadlands",
			"Deadlands Coast"
		],
		'type': "poison",
		'stats': [60,120,80,120,80,140],
		},
	'Masquerattle': {
		'id': 'masquerattle',
		'locations': [
			"Autumn Hill",
			"Lakeside",
			"The Marshes",
			"remaster_Carniviper"
		],
		'type': "poison",
		'stats': [90,140,80,140,90,160],
		},
	'Jormungold': {
		'id': 'jormungold',
		'locations': [
			"Autumn Hill",
			"The Marshes",
			"remaster_Masquerattle",
		],
		'type': "poison",
		'stats': [100,155,100,155,100,190],
		},
	'Mardiusa': {
		'id': 'mardiusa',
		'locations': ["remaster_Masquerattle"],
		'type': "poison",
		'stats': [130,160,100,120,130,160],
		},
	'Aeroboros': {
		'id': 'aeroboros',
		'locations': ["remaster-Zephyr_Masquerattle"],
		'type': "air",
		'stats': [190,30,100,160,160,160],
		},
	'Traffikrab': {
		'id': 'traffikrab',
		'locations': [
			"Harbourtown Beach",
			"Harbourtown Outskirts",
			"Deadlands",
			"Deadlands Coast",
			"Southern Isles",
			"NE Mire Sea",
			"West Mire Sea",
			"Titania Shipwreck"
		],
		'type': "plastic",
		'stats': [80,120,80,120,110,90],
		},
	'Weevilite': {
		'id': 'weevilite',
		'locations': [
			"NE Mire Sea",
			"West Mire Sea",
			"Waterloop Station",
			"remaster_Traffikrab"
		],
		'type': "plastic",
		'stats': [120,120,120,160,120,160],
		},
	'Lobstacle': {
		'id': 'lobstacle',
		'locations': [
			"Thirstaton Lake",
			"Southern Isles",
			"Waterloop Station",
			"remaster_Traffikrab"
		],
		'type': "plastic",
		'stats': [150,120,160,120,160,90],
		},
	'Candevil': {
		'id': 'candevil',
		'locations': ["Funworld", "Postgame"],# dlc area, alse buy with ranger badge
		'type': "beast",
		'stats': [115,110,100,110,105,100],
		},
	'Malchemy': {
		'id': 'malchemy',
		'locations': ["remaster_Candevil"],
		'type': "poison",
		'stats': [120,125,110,145,110,130],
		},
	'Miasmodeus': {
		'id': 'miasmodeus',
		'locations': ["remaster_Malchemy"],
		'type': "poison",
		'stats': [130,150,120,170,120,150],
		},
	'Vendemon': {
		'id': 'vendemon',
		'locations': ["remaster_Candevil"],
		'type': "metal",
		'stats': [130,110,130,120,130,120],
		},
	'Gumbaal': {
		'id': 'gumbaal',
		'locations': ["remaster_Vendemon"],
		'type': "metal",
		'stats': [150,110,160,130,160,130],
		},
	'Bansheep': {
		'id': 'bansheep',
		'locations': ["The Witch House", "Postgame"],# dlc area, alse buy with ranger badge
		'type': "beast",
		'stats': [115,110,105,110,100,100],
		},
	'Wooltergeist': {
		'id': 'wooltergeist',
		'locations': ["remaster_Bansheep"],
		'type': "astral",
		'stats': [120,145,110,125,110,130],
		},
	'Ramtasm': {
		'id': 'ramtasm',
		'locations': ["remaster_Wooltergeist"],
		'type': "astral",
		'stats': [130,170,120,150,120,150],
		},
	'Zombleat': {
		'id': 'zombleat',
		'locations': ["remaster_Bansheep"],
		'type': "earth",
		'stats': [130,130,130,110,130,110],
		},
	'Capricorpse': {
		'id': 'capricorpse',
		'locations': ["remaster_Zombleat"],
		'type': "earth",
		'stats': [160,140,160,110,160,110],
		},
	'Sirenade': {
		'id': 'sirenade',
		'locations': [
			"Recruited Kayleigh",
			"Brokenhead"
		],
		'type': "air",
		'stats': [110,70,80,130,120,90],
		},
	'Decibelle': {
		'id': 'decibelle',
		'locations': ["remaster_Sirenade"],
		'type': "air",
		'stats': [135,100,110,170,160,125],
		},
	'Dandylion': {
		'id': 'dandylion',
		'locations': [
			"Harbourtown Outskirts",
			"New Wirral Park",
			"Thirstaton Lake",
			"Cherry Meadow",
			"Mt Wirral",
			"Lost Hearts Graveyard"
		],
		'type': "plant",
		'stats': [120,80,120,100,120,60],
		},
	'Blossomaw': {
		'id': 'blossomaw',
		'locations': [
			"Cherry Meadow",
			"remaster_Dandylion"
		],
		'type': "plant",
		'stats': [160,100,160,130,160,90],
		},
	'Macabra': {
		'id': 'macabra',
		'locations': [
			"Autumn Hill",
			"New Wirral Park",
			"Lakeside",
			"The Marshes",
			"Ham"
		],
		'type': "beast",
		'stats': [140,120,60,100,100,120],
		},
	'Folklord': {
		'id': 'folklord',
		'locations': [
			"Autumn Hill",
			"The Marshes",
			"Ham",
			"remaster_Macabra"
		],
		'type': "beast",
		'stats': [140,135,135,100,120,120],
		},
	'Dominoth': {
		'id': 'dominoth',
		'locations': [
			"New Wirral Park",
			"Eastham Woods",
			"Eastham Woods Cliff",
			"Ham",
			"Falldown Mall",
			"Lakeside",
			"Cherry Meadow",
			"Cherry Cross Station"
		],
		'type': "air",
		'stats': [100,100,100,100,120,80],
		},
	'Wingloom': {
		'id': 'wingloom',
		'locations': [
			"Cherry Meadow",
			"Cherry Cross Station",
			"Eastham Woods",
			"Eastham Woods Cliff"
			"Ham",
			"Falldown Mall",
			"remaster_Dominoth"
		],
		'type': "lightning",
		'stats': [120,100,120,100,120,90],
		},
	'Mothmanic': {
		'id': 'mothmanic',
		'locations': [
			"Falldown Mall",
			"Cherry Meadow",
			"Cherry Cross Station",
			"Mt Wirral",
			"remaster_Wingloom"
		],
		'type': "lightning",
		'stats': [130,110,120,180,140,120],
		},
	'Tokusect': {
		'id': 'tokusect',
		'locations': ["remaster_Dominoth"],
		'type': "air",
		'stats': [120,170,120,100,120,170],
		},
	'Squirey': {
		'id': 'squirey',
		'locations': [
			"New Wirral Park",
			"Lakeside",
			"Deadlands",
			"Deadlands Coast",
			"Ham",
			"Harbourtown Outskirts",
			"Southern Isles",
			"Dino Quarry"
		],
		'type': "beast",
		'stats': [90,110,110,100,90,100],
		},
	'Manispear': {
		'id': 'manispear',
		'locations': [
			"Lakeside",
			"Ham",
			"Deadlands",
			"Deadlands Coast",
			"remaster_Squirey"
		],
		'type': "metal",
		'stats': [110,120,170,100,150,100],
		},
	'Palangolin': {
		'id': 'palangolin',
		'locations': ["remaster_Squirey"],
		'type': "metal",
		'stats': [150,120,120,100,100,160],
		},
	'Kittelly': {
		'id': 'kittelly',
		'locations': [
			"Recruited Meredith",
			"Brokenhead"
		],
		'type': "lightning",
		'stats': [100,110,90,110,90,100],
		},
	'Cat-5': {
		'id': 'cat-5',
		'locations': ["remaster_Kittelly"],
		'type': "lightning",
		'stats': [150,160,100,120,120,150],
		},
	'Puppercut': {
		'id': 'puppercut',
		'locations': [
			"Cherry Meadow",
			"Lakeside",
			"Lost Hearts Graveyard",
			"Ham",
			"New Wirral Park",
			"The Marshes"
		],
		'type': "metal",
		'stats': [100,120,110,80,80,110],
		},
	'Southpaw': {
		'id': 'southpaw',
		'locations': [
			"Lost Hearts Graveyard",
			"remaster_Puppercut"
		],
		'type': "metal",
		'stats': [130,160,140,110,110,150],
		},
	'Bulletino': {
		'id': 'bulletino',
		'locations': [
			"Lakeside",
			"Autumn Hill",
			"Dino Quarry"
		],
		'type': "fire",
		'stats': [80,70,70,100,70,200],
		},
	'Velocirifle': {
		'id': 'velocirifle',
		'locations': [
			"Autumn Hill",
			"Lakeside",
			"remaster_Bulletino"
		],
		'type': "fire",
		'stats': [100,100,100,140,100,160],
		},
	'Artillerex': {
		'id': 'artillerex',
		'locations': ["remaster_Velocirifle"],
		'type': "fire",
		'stats': [110,170,120,170,110,120],
		},
	'Gearyu': {
		'id': 'gearyu',
		'locations': ["remaster-Gear Shear_Velocirifle"],
		'type': "metal",
		'stats': [110,120,170,170,110,120],
		},
	'Diveal': {
		'id': 'diveal',
		'locations': [
			"Thirstaton Lake",
			"NE Mire Sea",
			"West Mire Sea",
			"The Marshes"
		],
		'type': "water",
		'stats': [100,100,125,125,100,50],
		},
	'Scubalrus': {
		'id': 'scubalrus',
		'locations': [
			"NE Mire Sea",
			"West Mire Sea",
			"Thirstaton Lake"
			"remaster_Diveal"
		],
		'type': "water",
		'stats': [130,125,160,160,125,100],
		},
	'Nevermort': {
		'id': 'nevermort',
		'locations': [
			"Piper Farm",
			"Deadlands",
			"Deadlands Coast",
			"New London",
			"Dino Quarry"
		],
		'type': "poison",
		'stats': [150,70,75,80,75,150],
		},
	'Apocrowlypse': {
		'id': 'apocrowlypse',
		'locations': ["remaster_Nevermort"],
		'type': "poison",
		'stats': [160,120,120,120,120,160],
		},
	'Clocksley': {
		'id': 'clocksley',
		'locations': [
			"Recruited Eugene",
			"Brokenhead"
		],
		'type': "plastic",
		'stats': [80,80,80,150,130,80],
		},
	'Robindam': {
		'id': 'robindam',
		'locations': ["remaster_Clocksley"],
		'type': "plastic",
		'stats': [110,110,110,200,150,120],
		},
	'Thwackalope': {
		'id': 'thwackalope',
		'locations': ["Autumn Hill"],
		'type': "air",
		'stats': [110,180,110,110,110,180],
		},
	'Allseer': {
		'id': 'allseer',
		'locations': [
			"NE Mire Sea",
			"West Mire Sea",
			"Autumn Hill",
			"Thirstaton Lake",
			"Eastham Woods",
			"Eastham Woods Cliff",
			"Southern Isles"
		],
		'type': "metal",
		'stats': [100,50,120,150,80,100],
		},
	'Khufo': {
		'id': 'khufo',
		'locations': ["remaster-Close Encounter_Allseer"],
		'type': "astral",
		'stats': [120,160,140,160,100,120],
		},
	'Triphinx': {
		'id': 'triphinx',
		'locations': [
			"Autumn Hill",
			"NE Mire Sea",
			"West Mire Sea",
			"Thirstaton Lake",
			"remaster_Allseer"
		],
		'type': "metal",
		'stats': [140,50,140,190,140,140],
		},
	'Braxsuit': {
		'id': 'braxsuit',
		'locations': [
			"Eastham Woods",
			"Eastham Woods Cliff"
		],
		'type': "air",
		'stats': [100,100,70,100,90,140],
		},
	'Flapwoods': {
		'id': 'flapwoods',
		'locations': [
			"Eastham Woods",
			"Eastham Woods Cliff",
			"remaster_Braxsuit"
		],
		'type': "air",
		'stats': [140,140,100,140,100,180],
		},
	'Sanzatime': {
		'id': 'sanzatime',
		'locations': [
			"Lost Hearts Graveyard",
			"New London",
			"The Marshes"
		],
		'type': "plastic",
		'stats': [100,120,120,100,110,50],
		},
	'Fortiwinx': {
		'id': 'fortiwinx',
		'locations': ["remaster_Sanzatime"],
		'type': "plastic",
		'stats': [130,165,155,130,140,80],
		},
	'Salamagus': {
		'id': 'salamagus',
		'locations': [
			"Waterloop Station",
			"Autumn Hill",
			"Lakeside"
		],
		'type': "fire",
		'stats': [100,50,80,150,120,100],
		},
	'Pyromeleon': {
		'id': 'pyromeleon',
		'locations': ["remaster_Salamagus"],
		'type': "fire",
		'stats': [150,60,100,200,150,140],
		},
	'Muskrateer': {
		'id': 'muskrateer',
		'locations': [
			"Falldown Mall",
			"New Wirral Park",
			"Autumn Hill",
			"Lakeside"
		],
		'type': "beast",
		'stats': [80,100,80,80,80,120],
		},
	'Ratcousel': {
		'id': 'ratcousel',
		'locations': [
			"Falldown Mall",
			"Mt Wirral",
			"remaster_Muskrateer"
		],
		'type': "plastic",
		'stats': [136,136,136,136,136,120],
		},
	'Padpole': {
		'id': 'padpole',
		'locations': ["Thirstaton Lake"],
		'type': "water",
		'stats': [120,120,80,80,80,120],
		},
	'Frillypad': {
		'id': 'frillypad',
		'locations': [
			"Thirstaton Lake",
			"Cherry Meadow",
			"remaster_Padpole"
		],
		'type': "water",
		'stats': [140,180,100,100,100,140],
		},
	'Liligator': {
		'id': 'liligator',
		'locations': [
			"Cherry Meadow",
			"remaster_Frillypad"
		],
		'type': "water",
		'stats': [150,200,100,100,100,150],
		},
	'Elfless': {
		'id': 'elfless',
		'locations': [
			"Cherry Cross Station",
			"Brokenhead",
			"Eastham Woods",
			"Eastham Woods Cliff",
			"New Wirral Park",
			"Cherry Meadow"
		],
		'type': "ice",
		'stats': [100,100,100,100,100,100],
		},
	'Grampus': {
		'id': 'grampus',
		'locations': [
			"Mt Wirral",
			"remaster_Elfless"
		],
		'type': "ice",
		'stats': [160,150,160,100,130,100],
		},
	'Faerious': {
		'id': 'faerious',
		'locations': ["remaster-Toy Hammer_Elfless"],
		'type': "ice",
		'stats': [160,160,100,120,100,160],
		},
	'Brushroom': {
		'id': 'brushroom',
		'locations': [
			"Recruited Felix",
			"Brokenhead"
		],
		'type': "plant",
		'stats': [100,100,100,90,110,100],
		},
	'Fungogh': {
		'id': 'fungogh',
		'locations': ["remaster_Brushroom"],
		'type': "plant",
		'stats': [120,160,160,100,140,120],
		},
	'Boltam': {
		'id': 'boltam',
		'locations': [
			"Eastham Woods",
			"Eastham Woods Cliff"
		],
		'type': "lightning",
		'stats': [90,90,90,90,90,150],
		},
	'Plasmantler': {
		'id': 'plasmantler',
		'locations': [
			"Mt Wirral",
			"Eastham Woods",
			"Eastham Woods Cliff",
			"remaster_Boltam"
		],
		'type': "lightning",
		'stats': [120,120,120,120,160,160],
		},
	'Busheye': {
		'id': 'busheye',
		'locations': [
			"Eastham Woods",
			"Eastham Woods Cliff"
		],
		'type': "plant",
		'stats': [150,90,90,90,90,90],
		},
	'Huntorch': {
		'id': 'huntorch',
		'locations': [
			"Eastham Woods",
			"Eastham Woods Cliff",
			"remaster_Busheye"
		],
		'type': "plant",
		'stats': [150,140,90,90,90,140],
		},
	'Hedgeherne': {
		'id': 'hedgeherne',
		'locations': ["remaster_Huntorch"],
		'type': "plant",
		'stats': [150,140,110,140,110,150],
		},
	'Terracooka': {
		'id': 'terracooka',
		'locations': [
			"Lakeside",
			"Mt Wirral",
			"Spider Cave",
			"New Wirral Park",
			"Autumn Hill",
			"Glowcester Road Station"
		],
		'type': "earth",
		'stats': [100,110,110,100,100,80],
		},
	'Coaldron': {
		'id': 'coaldron',
		'locations': [
			"Mt Wirral",
			"remaster_Terracooka"
		],
		'type': "earth",
		'stats': [160,110,140,160,140,90],
		},
	'Stardigrade': {
		'id': 'stardigrade',
		'locations': [
			"NE Mire Sea",
			"West Mire Sea",
			"Thirstaton Lake",
			"Autumn Hill",
			"New Wirral Park"
		],
		'type': "astral",
		'stats': [180,40,150,40,150,40],
		},
	'Galagor': {
		'id': 'galagor',
		'locations': ["remaster_Stardigrade"],
		'type': "astral",
		'stats': [200,60,180,150,150,60],
		},
	'Mascotoy': {
		'id': 'mascotoy',
		'locations': ["Falldown Mall"],
		'type': "plastic",
		'stats': [120,150,100,80,80,70],
		},
	'Mascotorn': {
		'id': 'mascotorn',
		'locations': ["remaster_Mascotoy"],
		'type': "plastic",
		'stats': [150,200,150,100,110,90],
		},
	'Binvader': {
		'id': 'binvader',
		'locations': ["Falldown Mall"],
		'type': "metal",
		'stats': [90,90,140,140,90,50],
		},
	'Binterloper': {
		'id': 'binterloper',
		'locations': ["remaster_Binvader"],
		'type': "plastic",
		'stats': [110,110,170,170,110,110],
		},
	'Twirligig': {
		'id': 'twirligig',
		'locations': ["Cherry Meadow"],
		'type': "plant",
		'stats': [190,50,150,50,150,10],
		},
	'Kirikuri': {
		'id': 'kirikuri',
		'locations': ["remaster_Twirligig"],
		'type': "plant",
		'stats': [190,160,150,70,110,120],
		},
	'Jellyton': {
		'id': 'jellyton',
		'locations': [
			"Lost Hearts Graveyard",
			"The Marshes"
		],
		'type': "poison",
		'stats': [120,200,130,150,90,110],
		},
	'Spirouette': {
		'id': 'spirouette',
		'locations': [
			"Recruited Viola",
			"Brokenhead"
		],
		'type': "water",
		'stats': [140,70,70,110,70,140],
		},
	'Regensea': {
		'id': 'regensea',
		'locations': ["remaster_Spirouette"],
		'type': "water",
		'stats': [170,115,100,145,100,170],
		},
	'Jumpkin': {
		'id': 'jumpkin',
		'locations': ["Piper Farm"],# also requires skelly jelly
		'type': "plant",
		'stats': [130,100,100,75,100,140],
		},
	'Beanstalker': {
		'id': 'beanstalker',
		'locations': ["remaster_Jumpkin"],
		'type': "plant",
		'stats': [140,185,110,100,100,165],
		},
	'Draculeaf': {
		'id': 'draculeaf',
		'locations': ["remaster_Jumpkin"],
		'type': "plant",
		'stats': [160,125,125,125,125,140],
		},
	'Pawndead': {
		'id': 'pawndead',
		'locations': ["Lost Hearts Graveyard"],
		'type': "earth",
		'stats': [90,90,90,90,90,90],
		},
	'Skelevangelist': {
		'id': 'skelevangelist',
		'locations': [
			"Lost Hearts Graveyard",
			"remaster_Pawndead"
		],
		'type': "earth",
		'stats': [110,110,110,110,110,110],
		},
	'Kingrave': {
		'id': 'kingrave',
		'locations': ["remaster_Skelevangelist"],
		'type': "earth",
		'stats': [110,220,110,160,110,110],
		},
	'Queenyx': {
		'id': 'queenyx',
		'locations': [
			"Night's Bridge Station",
			"remaster_Skelevangelist"
		],
		'type': "earth",
		'stats': [180,110,110,110,110,200],
		},
	'Burnace': {
		'id': 'burnace',
		'locations': [
			"Glowcester Road Station",
			"Waterloop Station",
			"Titania Shipwreck"
		],
		'type': "fire",
		'stats': [100,60,150,100,150,40],
		},
	'Smogmagog': {
		'id': 'smogmagog',
		'locations': [
			"Icelington Station",
			"Night's Bridge Station",
			"remaster_Burnace"
		],
		'type': "fire",
		'stats': [140,110,195,110,195,50],
		},
	'Faucetear': {
		'id': 'faucetear',
		'locations': [
			"Glowcester Road Station",
			"Falldown Mall",
			"Waterloop Station"
		],
		'type': "water",
		'stats': [90,100,90,110,100,90],
		},
	'Fountess': {
		'id': 'fountess',
		'locations': [
			"Titania Shipwreck",
			"Waterloop Station",
			"Night's Bridge Station",
			"remaster_Faucetear"],
		'type': "water",
		'stats': [125,135,125,155,135,125],
		},
	'Cluckabilly': {
		'id': 'cluckabilly',
		'locations': ["Piper Farm"],
		'type': "air",
		'stats': [100,115,90,105,90,100],
		},
	'Rockertrice': {
		'id': 'rockertrice',
		'locations': ["remaster_Cluckabilly"],
		'type': "air",
		'stats': [130,145,130,135,130,130],
		},
	'Pondwalker': {
		'id': 'pondwalker',
		'locations': [
			"Thirstaton Lake",
			"Waterloop Station"
		],
		'type': 'water',
		'stats': [100,100,100,100,100,100],
		},
	'Sharktanker': {
		'id': 'sharktanker',
		'locations': [
			"NE Mire Sea",
			"West Mire Sea",
			"remaster_Pondwalker"
		],
		'type': 'water',
		'stats': [130,150,140,130,140,110],
		},
	'Pombomb': {
		'id': 'pombomb',
		'locations': [
			"Harbourtown Outskirts",
			"Brokenhead",
			"Recruited Barkley"
		],
		'type': "fire",
		'stats': [100,90,90,100,120,100],
		},
	'Spitzfyre': {
		'id': 'spitzfyre',
		'locations': ["remaster_Pombomb"],
		'type': "fire",
		'stats': [140,110,110,160,150,130],
		},
	'Icepeck': {
		'id': 'icepeck',
		'locations': [
			"NE Mire Sea",
			"West Mire Sea",
			"Mt Wirral"
		],
		'type': "ice",
		'stats': [80,150,80,80,80,190],
		},
	'Cryoshear': {
		'id': 'cryoshear',
		'locations': [
			"Mt Wirral",
			"Icelington Station",
			"remaster_Icepeck"
		],
		'type': "ice",
		'stats': [150,180,90,90,90,200],
		},
	'Sparktan': {
		'id': 'sparktan',
		'locations': ["Mt Wirral"],
		'type': "lightning",
		'stats': [100,80,90,90,90,150],
		},
	'Zeustrike': {
		'id': 'zeustrike',
		'locations': [
			"Mt Wirral",
			"remaster_Sparktan"
		],
		'type': "lightning",
		'stats': [140,100,110,120,130,200],
		},
	'Kuneko': {
		'id': 'kuneko',
		'locations': ["Defeat Shining Kuneko"],
		'type': "air",
		'stats': [115,115,115,115,115,115],
		},
	'Shining Kuneko': {
		'id': 'shining_kuneko',
		'locations': ["remaster_Kuneko"],
		'type': "astral",
		'stats': [140,140,140,140,140,140],
		},
	'Djinn Entonic': {
		'id': 'djinn_entonic',
		'locations': [
			"New London",
			"Night's Bridge Station"
		],
		'type': "astral",
		'stats': [150,100,150,150,100,150],
		},
	'Arkidd': {
		'id': 'arkidd',
		'locations': ["Falldown Mall"],
		'type': "lightning",
		'stats': [100,150,100,100,100,250],
		},
	'Undyin': {
		'id': 'undyin',
		'locations': [
			"Cast Iron Shore",
			"Titania Shipwreck"
		],
		'type': "water",
		'stats': [200,110,110,160,110,110],
		},
	'Spooki-onna': {
		'id': 'spooki-onna',
		'locations': [
			"Mt Wirral",
			"Icelington Station"
		],
		'type': "ice",
		'stats': [190,120,130,130,130,100],
		},
	'Khepri': {
		'id': 'khepri',
		'locations': ["Mt Wirral"],
		'type': "fire",
		'stats': [100,1,100,300,250,79],
		},
	'Averevoir': {
		'id': 'averevoir',
		'locations': ["Recruited Barkley"],
		'type': "air",
		'stats': [150,100,150,100,150,190],
		},
	'Glaistain': {
		'id': 'glaistain',
		'locations': ["Cherry Meadow"],# also magnet?
		'type': "glass",
		'stats': [120,160,90,160,90,220],
		},
	'Miss Mimic': {
		'id': 'miss_mimic',
		'locations': ["Postgame"],# technically level 50 or level 65
		'type': "metal",
		'stats': [110,210,110,110,110,150],
		},
	'Anathema': {
		'id': 'anathema',
		'locations': ["Postgame"],
		'type': "beast",
		'stats': [150,155,140,140,130,85],
		},
	'Pinbolt': {
		'id': 'pinbolt',
		'locations': ["remaster_Boltam"],
		'type': "lightning",
		'stats': [120,120,105,160,105,190],
		},
	'Diveberg': {
		'id': 'diveberg',
		'locations': ["remaster-Ice Coating_Diveal"],
		'type': "ice",
		'stats': [100,160,150,125,135,130],
		},
	'Adeptile': {
		'id': 'adeptile',
		'locations': ["remaster-Magic Tome_Salamagus"],
		'type': "astral",
		'stats': [110,80,180,150,180,100],
		},
	'Trapwurm': {
		'id': 'trapwurm',
		'locations': [
			"The Marshes",
			"Spider Cave"
		],
		'type': "earth",
		'stats': [120,150,120,90,120,90],
		},
	'Wyrmaw': {
		'id': 'wyrmaw',
		'locations': ["remaster_Trapwurm"],
		'type': "earth",
		'stats': [150,180,130,110,130,100],
		},
	'Ferriclaw': {
		'id': 'ferriclaw',
		'locations': ["Spider Cave"],
		'type': "metal",
		'stats': [90,140,100,90,140,140],
		},
	'Auriclaw': {
		'id': 'auriclaw',
		'locations': ["remaster_Ferriclaw"],
		'type': "metal",
		'stats': [100,170,100,100,170,160],
		},
	'Picksie': {
		'id': 'picksie',
		'locations': ["Spider Cave"],
		'type': "earth",
		'stats': [130,130,130,130,130,150],
		},
	'Pawper': {
		'id': 'bear1',
		'locations': [
			"Recruited Sunny",
			"New Landkeeper Hideout"
		],
		'type': "beast",
		'stats': [120,130,100,100,120,130],
		},
	'Pawprince': {
		'id': 'bear1',
		'locations': ["reamster_Pawper"],
		'type': "beast",
		'stats': [140,160,110,110,140,140],	
		},
	'Minosteam': {
		'id': 'minosteam',
		'locations': ["Quest People are People"],
		'type': "beast",
		'stats': [140,160,110,110,140,140],	
		},
}
for data in base_monsters.values():
	data['dlc'] = None

other_monsters = {
	"Magikrab": {
		'id': "magikrab",
		'locations': ["remaster-astral_Traffikrab"],
		'type': "astral",
		'stats': [105,160,105,160,150,120],
		'dlc': None,
		},
}

pier_monsters = {
	"Amphare": {
		'id': "amphare",
		'locations': ["Funworld"],
		'type': "lightning",
		'stats': [120,100,120,100,80,80],
	},
	"Blunderbusk": {
		'id': "blunderbusk",
		'locations': ["remaster_Charlequin"],
		'type': "fire",
		'stats': [150,120,150,150,100,130],
		},
	"Charlequin": {
		'id': "charlequin",
		'locations': [
			"The Witch House",
			"Cosmic Zone",
			"Funworld"
		],
		'type': "fire",
		'stats': [80,110,80,120,100,110],
		},
	"Fragliacci": {
		'id': "fragliacci",
		'locations': ["remaster_Charlequin"],
		'type': "fire",
		'stats': [100,140,100,170,160,130],
		},
	"Hauntome": {
		'id': "hauntome",
		'locations': ["The Witch House"],
		'type': "air",
		'stats': [110,180,150,180,80,100],
		},
	"Lapacitor": {
		'id': "lapacitor",
		'locations': ["remaster_Amphare"],
		'type': "lightning",
		'stats': [150,125,150,125,150,100],
		},
	"Littlered": {
		'id': "littlered",
		'locations': ["The Witch House"],
		'type': "beast",
		'stats': [100,100,100,100,100,100],
		},
	"Majortom": {
		'id': "majortom",
		'locations': ["remaster_Minortom"],
		'type': "metal",
		'stats': [150,150,150,110,110,130],
		},
	"Minortom": {
		'id': "minortom",
		'locations': ["Cosmic Zone"],
		'type': "metal",
		'stats': [130,130,130,70,70,70],
		},
	"Rosehood": {
		'id': "rosehood",
		'locations': ["remaster_Littlered"],
		'type': "plant",
		'stats': [160,110,100,160,110,160],
		},
	"Scarleteeth": {
		'id': "scarleteeth",
		'locations': ["remaster-Carnivore_Littlered"],
		'type': "beast",
		'stats': [110,160,160,100,160,110],
		},
	"Umbrahella": {
		'id': "umbrahella",
		'locations': ["Warehouse Key"],# this is a special case, needs work in rules
		'type': "poison",
		'stats': [150,120,140,170,200,60],
		},
}
for data in pier_monsters.values():
	data['dlc'] = "pier"

types = [
	"air",
	"astral",
	"beast",
	"earth",
	"fire",
	"glass",
	"glitter",
	"ice",
	"lightning",
	"metal",
	"plant",
	"plastic",
	"poison",
	"water"
	]

def monsters(options=None):# None for options means just give full monster list
	if options:
		if not options.use_pier:
			return base_monsters
	return base_monsters|pier_monsters

def monsterCount(options=None):# None for options means just give full monster count
	return len(monsters(options))