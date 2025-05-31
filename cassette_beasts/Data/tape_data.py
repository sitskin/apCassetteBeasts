from typing import NamedTuple, Optional

class MonsterData(NamedTuple):
	id: str
	type: str
	stats: list[int]
	locations: list[callable]
	tapesanity_item: Optional[str] = None
	bootlegsanity_item: Optional[str] = None
	requires: Optional[callable] = None

monster_data_table = {
	"Springheel": MonsterData(
		"springheel",
		"beast",
		[90,130,80,80,90,130],
		[
			"Cherry Cross Station",
			"Harbourtown Beach",
			"Harbourtown Outskirts"
		],
		"Basic Tape",
		"bootleg_tape"
	),
	"Hopskin": MonsterData(
		"hopskin",
		"beast",
		[90,170,100,90,100,150],
		[
			"New London",
			"Cherry Cross Station",
			"remaster_Springheel"
		],
		"Basic Tape",
		"bootleg_tape"# same as Springheel for split remaster
	),
	"Ripterra": MonsterData(
		"ripterra",
		"beast",
		[120,200,100,90,120,170],
		[
			"New London",
			"remaster_Hopskin"
		],
		None,
		None
	),
	"Snoopin": MonsterData(
		"snoopin",
		"beast",
		[90,160,80,150,90,130],
		[
			"New London",
			"Cherry Cross Station",
			"remaster_Springheel"
		],
		None,
		None
	),
	"Scampire": MonsterData(
		"scampire",
		"beast",
		[120,160,80,180,90,170],
		[
			"Lost Hearts Graveyard",
			"remaster_Snoopin"
		],
		None,
		None
	),
	"Carniviper": MonsterData(
		"carniviper",
		"poison",
		[60,120,80,120,80,140],
		[
			"Harbourtown Beach",
			"Harbourtown Outskirts",
			"Glowcester Road Station",
			"New Wirral Park",
			"New London",
			"Deadlands",
			"Deadlands Coast"
		],
		"Basic Tape",
		"bootleg_tape"
	),
	"Masquerattle": MonsterData(
		"masquerattle",
		"poison",
		[90,140,80,140,90,160],
		[
			"Autumn Hill",
			"Lakeside",
			"The Marshes",
			"remaster_Carniviper"
		],
		"Basic Tape",
		"bootleg_tape"# same as Carniviper for split remaster
	),
	"Jormungold": MonsterData(
		"jormungold",
		"poison",
		[100,155,100,155,100,190],
		[
			"Autumn Hill",
			"The Marshes",
			"remaster_Masquerattle",
		],
		"Basic Tape",
		"bootleg_tape"# same as Carniviper for split remaster
	),
	"Mardiusa": MonsterData(
		"mardiusa",
		"poison",
		[130,160,100,120,130,160],
		[
			"remaster_Masquerattle",
		],
		None,
		None
	),
	"Aeroboros": MonsterData(
		"aeroboros",
		"air",
		[190,30,100,160,160,160],
		[
			"remaster-Zephyr_Masquerattle",
		],
		"Zephyr Sticker",
		"Zephyr Sticker"
	),
	"Traffikrab": MonsterData(
		"traffikrab",
		"plastic",
		[80,120,80,120,110,90],
		[
			"Harbourtown Beach",
			"Harbourtown Outskirts",
			"Deadlands",
			"Deadlands Coast",
			"Southern Isles",
			"NE Mire Sea",
			"West Mire Sea",
			"Titania Shipwreck"
		],
		"Basic Tape",
		"bootleg_tape"
	),
	"Weevilite": MonsterData(
		"weevilite",
		"plastic",
		[120,120,120,160,120,160],
		[
			"NE Mire Sea",
			"West Mire Sea",
			"Waterloop Station",
			"remaster_Traffikrab"
		],
		"Basic Tape",
		"bootleg_tape"# same as Traffikrab for split remaster
	),
	"Lobstacle": MonsterData(
		"lobstacle",
		"plastic",
		[150,120,160,120,160,90],
		[
			"Thirstaton Lake",
			"Southern Isles",
			"Waterloop Station",
			"remaster_Traffikrab"
		],
		None,
		None
	),
	"Candevil": MonsterData(
		"candevil",
		"beast",
		[115,110,100,110,105,100],
		[
			"Funworld",
			"Postgame"
		],
		"Fused Material x20",
		"Ritual Candle"
	),
	"Malchemy": MonsterData(
		"malchemy",
		"poison",
		[120,125,110,145,110,130],
		[
			"remaster_Candevil",
		],
		"Fused Material x20",
		"Ritual Candle"# same as Candevil for split remaster
	),
	"Miasmodeus": MonsterData(
		"miasmodeus",
		"poison",
		[130,150,120,170,120,150],
		[
			"remaster_Malchemy",
		],
		None,
		None
	),
	"Vendemon": MonsterData(
		"vendemon",
		"metal",
		[130,110,130,120,130,120],
		[
			"remaster_Candevil",
		],
		None,
		None
	),
	"Gumbaal": MonsterData(
		"gumbaal",
		"metal",
		[150,110,160,130,160,130],
		[
			"remaster_Vendemon",
		],
		None,
		None
	),
	"Bansheep": MonsterData(
		"bansheep",
		"beast",
		[115,110,105,110,100,100],
		[
			"The Witch House",
			"Postgame",
		],
		"Fused Material x20",
		"Ritual Candle"
	),
	"Wooltergeist": MonsterData(
		"wooltergeist",
		"astral",
		[120,145,110,125,110,130],
		[
			"remaster_Bansheep"
		],
		"Fused Material x20",
		"Ritual Candle"# same as Bansheep for split remaster
	),
	"Ramtasm": MonsterData(
		"ramtasm",
		"astral",
		[130,170,120,150,120,150],
		[
			"remaster_Wooltergeist"
		],
		None,
		None
	),
	"Zombleat": MonsterData(
		"zombleat",
		"earth",
		[130,130,130,110,130,110],
		[
			"remaster_Bansheep"
		],
		None,
		None
	),
	"Capricorpse": MonsterData(
		"capricorpse",
		"earth",
		[160,140,160,110,160,110],
		[
			"remaster_Zombleat"
		],
		None,
		None
	),
	"Sirenade": MonsterData(
		"sirenade",
		"air",
		[110,70,80,130,120,90],
		[
			"Recruited Kayleigh",
			"Brokenhead"
		],
		None,
		"Ritual Candle"
	),
	"Decibelle": MonsterData(
		"decibelle",
		"air",
		[135,100,110,170,160,125],
		[
			"remaster_Sirenade"
		],
		None,
		None
	),
	"Dandylion": MonsterData(
		"dandylion",
		"plant",
		[120,80,120,100,120,60],
		[
			"Harbourtown Outskirts",
			"New Wirral Park",
			"Thirstaton Lake",
			"Cherry Meadow",
			"Mt Wirral",
			"Lost Hearts Graveyard"
		],
		"Basic Tape",
		"bootleg_tape"
	),
	"Blossomaw": MonsterData(
		"blossomaw",
		"plant",
		[160,100,160,130,160,90],
		[
			"Cherry Meadow",
			"remaster_Dandylion"
		],
		None,
		None
	),
	"Macabra": MonsterData(
		"macabra",
		"beast",
		[140,120,60,100,100,120],
		[
			"Autumn Hill",
			"New Wirral Park",
			"Lakeside",
			"The Marshes",
			"Ham"
		],
		"Basic Tape",
		"bootleg_tape"
	),
	"Folklord": MonsterData(
		"folklord",
		"beast",
		[140,135,135,100,120,120],
		[
			"Autumn Hill",
			"The Marshes",
			"Ham",
			"remaster_Macabra"
		],
		None,
		None
	),
	"Dominoth": MonsterData(
		"dominoth",
		"air",
		[100,100,100,100,120,80],
		[
			"New Wirral Park",
			"Eastham Woods",
			"Eastham Woods Cliff",
			"Ham",
			"Falldown Mall",
			"Lakeside",
			"Cherry Meadow",
			"Cherry Cross Station"
		],
		"Basic Tape",
		"bootleg_tape"
	),
	"Wingloom": MonsterData(
		"wingloom",
		"lightning",
		[120,100,120,100,120,90],
		[
			"Cherry Meadow",
			"Cherry Cross Station",
			"Eastham Woods",
			"Eastham Woods Cliff"
			"Ham",
			"Falldown Mall",
			"remaster_Dominoth"
		],
		"Basic Tape",
		"bootleg_tape"# same as Dominoth for split remaster
	),
	"Mothmanic": MonsterData(
		"mothmanic",
		"lightning",
		[130,110,120,180,140,120],
		[
			"Falldown Mall",
			"Cherry Meadow",
			"Cherry Cross Station",
			"Mt Wirral",
			"remaster_Wingloom"
		],
		None,
		None
	),
	"Tokusect": MonsterData(
		"tokusect",
		"air",
		[120,170,120,100,120,170],
		[
			"remaster_Dominoth"
		],
		None,
		None
	),
	"Squirey": MonsterData(
		"squirey",
		"beast",
		[90,110,110,100,90,100],
		[
			"New Wirral Park",
			"Lakeside",
			"Deadlands",
			"Deadlands Coast",
			"Ham",
			"Harbourtown Outskirts",
			"Southern Isles",
			"Dino Quarry"
		],
		"Basic Tape",
		"bootleg_tape"
	),
	"Manispear": MonsterData(
		"manispear",
		"metal",
		[110,120,170,100,150,100],
		[
			"Lakeside",
			"Ham",
			"Deadlands",
			"Deadlands Coast",
			"remaster_Squirey"
		],
		"Basic Tape",
		"bootleg_tape"# same as Squirey for split remaster
	),
	"Palangolin": MonsterData(
		"palangolin",
		"metal",
		[150,120,120,100,100,160],
		[
			"remaster_Squirey"
		],
		None,
		None
	),
	"Kittelly": MonsterData(
		"kittelly",
		"lightning",
		[100,110,90,110,90,100],
		[
			"Recruited Meredith",
			"Brokenhead"
		],
		None,
		"Ritual Candle"
	),
	"Cat-5": MonsterData(
		"cat-5",
		"lightning",
		[150,160,100,120,120,150],
		[
			"remaster_Kittelly"
		],
		None,
		None
	),
	"Puppercut": MonsterData(
		"puppercut",
		"metal",
		[100,120,110,80,80,110],
		[
			"Cherry Meadow",
			"Lakeside",
			"Lost Hearts Graveyard",
			"Ham",
			"New Wirral Park",
			"The Marshes"
		],
		"Basic Tape",
		"bootleg_tape"
	),
	"Southpaw": MonsterData(
		"southpaw",
		"metal",
		[130,160,140,110,110,150],
		[
			"Lost Hearts Graveyard",
			"remaster_Puppercut"
		],
		None,
		None
	),
	"Bulletino": MonsterData(
		"bulletino",
		"fire",
		[80,70,70,100,70,200],
		[
			"Lakeside",
			"Autumn Hill",
			"Dino Quarry"
		],
		"Basic Tape",
		"bootleg_tape"
	),
	"Velocirifle": MonsterData(
		"velocirifle",
		"fire",
		[100,100,100,140,100,160],
		[
			"Autumn Hill",
			"Lakeside",
			"remaster_Bulletino"
		],
		"Basic Tape",
		"bootleg_tape"# same as Bulletino for split remaster
	),
	"Artillerex": MonsterData(
		"artillerex",
		"fire",
		[110,170,120,170,110,120],
		[
			"remaster_Velocirifle"
		],
		None,
		None
	),
	"Gearyu": MonsterData(
		"gearyu",
		"metal",
		[110,120,170,170,110,120],
		[
			"remaster-Gear Shear_Velocirifle"
		],
		"Gear Shear Sticker",
		None
	),
	"Diveal": MonsterData(
		"diveal",
		"water",
		[100,100,125,125,100,50],
		[
			"Thirstaton Lake",
			"NE Mire Sea",
			"West Mire Sea",
			"The Marshes"
		],
		"Basic Tape",
		"bootleg_tape"
	),
	"Scubalrus": MonsterData(
		"scubalrus",
		"water",
		[130,125,160,160,125,100],
		[
			"NE Mire Sea",
			"West Mire Sea",
			"Thirstaton Lake"
			"remaster_Diveal"
		],
		"Basic Tape",
		"bootleg_tape"# same as Diveal for split remaster
	),
	"Nevermort": MonsterData(
		"nevermort",
		"poison",
		[150,70,75,80,75,150],
		[
			"Piper Farm",
			"Deadlands",
			"Deadlands Coast",
			"New London",
			"Dino Quarry"
		],
		"Basic Tape",
		"bootleg_tape"
	),
	"Apocrowlypse": MonsterData(
		"apocrowlypse",
		"poison",
		[160,120,120,120,120,160],
		[
			"remaster_Nevermort"
		],
		None,
		None
	),
	"Clocksley": MonsterData(
		"clocksley",
		"plastic",
		[80,80,80,150,130,80],
		[
			"Recruited Eugene",
			"Brokenhead"
		],
		None,
		"Ritual Candle"
	),
	"Robindam": MonsterData(
		"robindam",
		"plastic",
		[110,110,110,200,150,120],
		[
			"remaster_Clocksley"
		],
		None,
		None
	),
	"Thwackalope": MonsterData(
		"thwackalope",
		"air",
		[110,180,110,110,110,180],
		[
			"Autumn Hill"
		],
		"Chrome Tape",
		"bootleg_tape"
	),
	"Allseer": MonsterData(
		"allseer",
		"metal",
		[100,50,120,150,80,100],
		[
			"NE Mire Sea",
			"West Mire Sea",
			"Autumn Hill",
			"Thirstaton Lake",
			"Eastham Woods",
			"Eastham Woods Cliff",
			"Southern Isles"
		],
		"Basic Tape",
		"bootleg_tape"
	),
	"Khufo": MonsterData(
		"khufo",
		"astral",
		[120,160,140,160,100,120],
		[
			"remaster-Close Encounter_Allseer"
		],
		"Close Encounter Sticker",
		None
	),
	"Triphinx": MonsterData(
		"triphinx",
		"metal",
		[140,50,140,190,140,140],
		[
			"Autumn Hill",
			"NE Mire Sea",
			"West Mire Sea",
			"Thirstaton Lake",
			"remaster_Allseer"
		],
		"Basic Tape",
		"bootleg_tape"# same as Allseer for split remaster
	),
	"Braxsuit": MonsterData(
		"braxsuit",
		"air",
		[100,100,70,100,90,140],
		[
			"Eastham Woods",
			"Eastham Woods Cliff"
		],
		"Basic Tape",
		"bootleg_tape"
	),
	"Flapwoods": MonsterData(
		"flapwoods",
		"air",
		[140,140,100,140,100,180],
		[
			"Eastham Woods",
			"Eastham Woods Cliff",
			"remaster_Braxsuit"
		],
		None,
		None
	),
	"Sanzatime": MonsterData(
		"sanzatime",
		"earth",
		[100,120,120,100,110,50],
		[
			"Lost Hearts Graveyard",
			"New London",
			"The Marshes"
		],
		"Basic Tape",
		"bootleg_tape"
	),
	"Fortiwinx": MonsterData(
		"fortiwinx",
		"earth",
		[130,165,155,130,140,80],
		[
			"remaster_Sanzatime"
		],
		None,
		None
	),
	"Salamagus": MonsterData(
		"salamagus",
		"fire",
		[100,50,80,150,120,100],
		[
			"Waterloop Station",
			"Autumn Hill",
			"Lakeside"
		],
		"Basic Tape",
		"bootleg_tape"
	),
	"Pyromeleon": MonsterData(
		"pyromeleon",
		"fire",
		[150,60,100,200,150,140],
		[
			"remaster_Salamagus"
		],
		"Basic Tape",
		"bootleg_tape"# same as salamagus for split remaster
	),
	"Muskrateer": MonsterData(
		"muskrateer",
		"beast",
		[80,100,80,80,80,120],
		[
			"Falldown Mall",
			"New Wirral Park",
			"Autumn Hill",
			"Lakeside"
		],
		"Basic Tape",
		"bootleg_tape"
	),
	"Ratcousel": MonsterData(
		"ratcousel",
		"plastic",
		[136,136,136,136,136,120],
		[
			"Falldown Mall",
			"Mt Wirral",
			"remaster_Muskrateer"
		],
		None,
		None
	),
	"Padpole": MonsterData(
		"padpole",
		"water",
		[120,120,80,80,80,120],
		[
			"Thirstaton Lake"
		],
		"Basic Tape",
		"bootleg_tape"
	),
	"Frillypad": MonsterData(
		"frillypad",
		"water",
		[140,180,100,100,100,140],
		[
			"Thirstaton Lake",
			"Cherry Meadow",
			"remaster_Padpole"
		],
		None,
		None
	),
	"Liligator": MonsterData(
		"liligator",
		"water",
		[150,200,100,100,100,150],
		[
			"Cherry Meadow",
			"remaster_Frillypad"
		],
		None,
		None
	),
	"Elfless": MonsterData(
		"elfless",
		"ice",
		[100,100,100,100,100,100],
		[
			"Cherry Cross Station",
			"Brokenhead",
			"Eastham Woods",
			"Eastham Woods Cliff",
			"New Wirral Park",
			"Cherry Meadow"
		],
		"Basic Tape",
		"bootleg_tape"
	),
	"Grampus": MonsterData(
		"grampus",
		"ice",
		[160,150,160,100,130,100],
		[
			"Mt Wirral",
			"remaster_Elfless"
		],
		"Basic Tape",
		"bootleg_tape"# same as Elfless for split remaster
	),
	"Faerious": MonsterData(
		"faerious",
		"ice",
		[160,160,100,120,100,160],
		[
			"remaster-Toy Hammer_Elfless"
		],
		"Toy Hammer Sticker",
		None
	),
	"Brushroom": MonsterData(
		"brushroom",
		"plant",
		[100,100,100,90,110,100],
		[
			"Recruited Felix",
			"Brokenhead"
		],
		None,
		"Ritual Candle"
	),
	"Fungogh": MonsterData(
		"fungogh",
		"plant",
		[120,160,160,100,140,120],
		[
			"remaster_Brushroom"
		],
		None,
		None
	),
	"Boltam": MonsterData(
		"boltam",
		"lightning",
		[90,90,90,90,90,150],
		[
			"Eastham Woods",
			"Eastham Woods Cliff"
		],
		"Basic Tape",
		"bootleg_tape"
	),
	"Plasmantler": MonsterData(
		"plasmantler",
		"lightning",
		[120,120,120,120,160,160],
		[
			"Mt Wirral",
			"Eastham Woods",
			"Eastham Woods Cliff",
			"remaster_Boltam"
		],
		"Basic Tape",
		"bootleg_tape"# same as Boltam for split remaster
	),
	"Busheye": MonsterData(
		"busheye",
		"plant",
		[150,90,90,90,90,90],
		[
			"Eastham Woods",
			"Eastham Woods Cliff"
		],
		"Basic Tape",
		"bootleg_tape"
	),
	"Huntorch": MonsterData(
		"huntorch",
		"plant",
		[150,140,90,90,90,140],
		[
			"Eastham Woods",
			"Eastham Woods Cliff",
			"remaster_Busheye"
		],
		None,
		None
	),
	"Hedgeherne": MonsterData(
		"hedgeherne",
		"plant",
		[150,140,110,140,110,150],
		[
			"remaster_Huntorch"
		],
		None,
		None
	),
	"Terracooka": MonsterData(
		"terracooka",
		"earth",
		[100,110,110,100,100,80],
		[
			"Lakeside",
			"Mt Wirral",
			"Spider Cave",
			"New Wirral Park",
			"Autumn Hill",
			"Glowcester Road Station"
		],
		"Basic Tape",
		"bootleg_tape"
	),
	"Coaldron": MonsterData(
		"coaldron",
		"earth",
		[160,110,140,160,140,90],
		[
			"Mt Wirral",
			"remaster_Terracooka"
		],
		None,
		None
	),
	"Stardigrade": MonsterData(
		"stardigrade",
		"astral",
		[180,40,150,40,150,40],
		[
			"NE Mire Sea",
			"West Mire Sea",
			"Thirstaton Lake",
			"Autumn Hill",
			"New Wirral Park"
		],
		"Basic Tape",
		"bootleg_tape"
	),
	"Galagor": MonsterData(
		"galagor",
		"astral",
		[200,60,180,150,150,60],
		[
			"remaster_Stardigrade"
		],
		None,
		None
	),
	"Mascotoy": MonsterData(
		"mascotoy",
		"plastic",
		[120,150,100,80,80,70],
		[
			"Falldown Mall"
		],
		"Basic Tape",
		"bootleg_tape"
	),
	"Mascotorn": MonsterData(
		"mascotorn",
		"plastic",
		[150,200,150,100,110,90],
		[
			"remaster_Mascotoy"
		],
		None,
		None
	),
	"Binvader": MonsterData(
		"binvader",
		"metal",
		[90,90,140,140,90,50],
		[
			"Falldown Mall"
		],
		"Basic Tape",
		"bootleg_tape"
	),
	"Binterloper": MonsterData(
		"binterloper",
		"plastic",
		[110,110,170,170,110,110],
		[
			"remaster_Binvader"
		],
		None,
		None
	),
	"Twirligig": MonsterData(
		"twirligig",
		"plant",
		[190,50,150,50,150,10],
		[
			"Cherry Meadow"
		],
		"Basic Tape",
		"bootleg_tape"
	),
	"Kirikuri": MonsterData(
		"kirikuri",
		"plant",
		[190,160,150,70,110,120],
		[
			"remaster_Twirligig"
		],
		None,
		None
	),
	"Jellyton": MonsterData(
		"jellyton",
		"poison",
		[120,200,130,150,90,110],
		[
			"Lost Hearts Graveyard",
			"The Marshes"
		],
		"Chrome Tape",
		"bootleg_tape"
	),
	"Spirouette": MonsterData(
		"spirouette",
		"water",
		[140,70,70,110,70,140],
		[
			"Recruited Viola",
			"Brokenhead"
		],
		None,
		"Ritual Candle"
	),
	"Regensea": MonsterData(
		"regensea",
		"water",
		[170,115,100,145,100,170],
		[
			"remaster_Spirouette"
		],
		None,
		None
	),
	"Jumpkin": MonsterData(
		"jumpkin",
		"plant",
		[130,100,100,75,100,140],
		[
			"farm_jelly"
		],
		"Basic Tape",
		"bootleg_tape"
	),
	"Beanstalker": MonsterData(
		"beanstalker",
		"plant",
		[140,185,110,100,100,165],
		[
			"remaster_Jumpkin"
		],
		"Basic Tape",
		"bootleg_tape"# same as Jumpkin for split remaster
	),
	"Draculeaf": MonsterData(
		"draculeaf",
		"plant",
		[160,125,125,125,125,140],
		[
			"remaster_Jumpkin"
		],
		None,
		None
	),
	"Pawndead": MonsterData(
		"pawndead",
		"earth",
		[90,90,90,90,90,90],
		[
			"Lost Hearts Graveyard"
		],
		"Basic Tape",
		"bootleg_tape"
	),
	"Skelevangelist": MonsterData(
		"skelevangelist",
		"earth",
		[110,110,110,110,110,110],
		[
			"Lost Hearts Graveyard",
			"remaster_Pawndead"
		],
		"Basic Tape",
		"bootleg_tape"# same as Pawndead for split remaster
	),
	"Kingrave": MonsterData(
		"kingrave",
		"earth",
		[110,220,110,160,110,110],
		[
			"New Landkeeper Hideout",
			"remaster_Skelevangelist"
		],
		None,
		None
	),
	"Queenyx": MonsterData(
		"queenyx",
		"earth",
		[180,110,110,110,110,200],
		[
			"Night's Bridge Station",
			"New Landkeeper Hideout",
			"remaster_Skelevangelist"
		],
		None,
		None
	),
	"Burnace": MonsterData(
		"burnace",
		"fire",
		[100,60,150,100,150,40],
		[
			"Glowcester Road Station",
			"Waterloop Station",
			"Titania Shipwreck"
		],
		"Basic Tape",
		"bootleg_tape"
	),
	"Smogmagog": MonsterData(
		"smogmagog",
		"fire",
		[140,110,195,110,195,50],
		[
			"Icelington Station",
			"Night's Bridge Station",
			"remaster_Burnace"
		],
		None,
		None
	),
	"Faucetear": MonsterData(
		"faucetear",
		"water",
		[90,100,90,110,100,90],
		[
			"Glowcester Road Station",
			"Falldown Mall",
			"Waterloop Station"
		],
		"Basic Tape",
		"bootleg_tape"
	),
	"Fountess": MonsterData(
		"fountess",
		"water",
		[125,135,125,155,135,125],
		[
			"Titania Shipwreck",
			"Waterloop Station",
			"Night's Bridge Station",
			"remaster_Faucetear"
		],
		None,
		None
	),
	"Cluckabilly": MonsterData(
		"cluckabilly",
		"air",
		[100,115,90,105,90,100],
		[
			"Piper Farm"
		],
		"Basic Tape",
		"bootleg_tape"
	),
	"Rockertrice": MonsterData(
		"rockertrice",
		"air",
		[130,145,130,135,130,130],
		[
			"remaster_Cluckabilly"
		],
		None,
		None
	),
	"Pondwalker": MonsterData(
		"pondwalker",
		"water",
		[100,100,100,100,100,100],
		[
			"Thirstaton Lake",
			"Waterloop Station"
		],
		"Basic Tape",
		"bootleg_tape"
	),
	"Sharktanker": MonsterData(
		"sharktanker",
		"water",
		[130,150,140,130,140,110],
		[
			"NE Mire Sea",
			"West Mire Sea",
			"remaster_Pondwalker"
		],
		None,
		None
	),
	"Pombomb": MonsterData(
		"pombomb",
		"fire",
		[100,90,90,100,120,100],
		[
			"Harbourtown Outskirts",
			"Brokenhead",
			"Recruited Barkley"
		],
		"Basic Tape",
		"bootleg_tape"
	),
	"Spitzfyre": MonsterData(
		"spitzfyre",
		"fire",
		[140,110,110,160,150,130],
		[
			"remaster_Pombomb"
		],
		None,
		None
	),
	"Icepeck": MonsterData(
		"icepeck",
		"ice",
		[80,150,80,80,80,190],
		[
			"NE Mire Sea",
			"West Mire Sea",
			"Mt Wirral"
		],
		"Basic Tape",
		"bootleg_tape"
	),
	"Cryoshear": MonsterData(
		"cryoshear",
		"ice",
		[150,180,90,90,90,200],
		[
			"Mt Wirral",
			"Icelington Station",
			"remaster_Icepeck"
		],
		None,
		None
	),
	"Sparktan": MonsterData(
		"sparktan",
		"lightning",
		[100,80,90,90,90,150],
		[
			"Mt Wirral"
		],
		"Basic Tape",
		"bootleg_tape"
	),
	"Zeustrike": MonsterData(
		"zeustrike",
		"lightning",
		[140,100,110,120,130,200],
		[
			"Mt Wirral",
			"remaster_Sparktan"
		],
		None,
		None
	),
	"Kuneko": MonsterData(
		"kuneko",
		"air",
		[115,115,115,115,115,115],
		[
			"Defeated Shining Kuneko"
		],
		None,
		"bootleg_tape"
	),
	"Shining Kuneko": MonsterData(
		"shining_kuneko",
		"astral",
		[140,140,140,140,140,140],
		[
			"remaster_Kuneko"
		],
		None,
		None
	),
	"Djinn Entonic": MonsterData(
		"djinn_entonic",
		"astral",
		[150,100,150,150,100,150],
		[
			"New London",
			"Night's Bridge Station"
		],
		"Chrome Tape",
		"bootleg_tape"
	),
	"Arkidd": MonsterData(
		"arkidd",
		"lightning",
		[100,150,100,100,100,250],
		[
			"Falldown Mall"
		],
		"Chrome Tape",
		"bootleg_tape"
	),
	"Undyin": MonsterData(
		"undyin",
		"water",
		[200,110,110,160,110,110],
		[
			"Cast Iron Shore",
			"Titania Shipwreck"
		],
		"Chrome Tape",
		"bootleg_tape"
	),
	"Spooki-onna": MonsterData(
		"spooki-onna",
		"ice",
		[190,120,130,130,130,100],
		[
			"Mt Wirral",
			"Icelington Station"
		],
		"Chrome Tape",
		"bootleg_tape"
	),
	"Khepri": MonsterData(
		"khepri",
		"fire",
		[100,1,100,300,250,79],
		[
			"Mt Wirral"
		],
		"Optical Laser Tape",
		"bootleg_tape"
	),
	"Averevoir": MonsterData(
		"averevoir",
		"air",
		[150,100,150,100,150,190],
		[
			"Recruited Barkley"
		],
		"Optical Laser Tape",
		"bootleg_tape"
	),
	"Glaistain": MonsterData(
		"glaistain",
		"glass",
		[120,160,90,160,90,220],
		[
			"Glaistainbury Abbey"
		],
		"Optical Laser Tape",
		"bootleg_tape"
	),
	"Miss Mimic": MonsterData(
		"miss_mimic",
		"metal",
		[110,210,110,110,110,150],
		[
			"Postgame"
		],
		"Optical Laser Tape",
		"bootleg_tape"
	),
	"Anathema": MonsterData(
		"anathema",
		"beast",
		[150,155,140,140,130,85],
		[
			"Postgame"
		],
		"Optical Laser Tape",
		"bootleg_tape"
	),
	"Pinbolt": MonsterData(
		"pinbolt",
		"lightning",
		[120,120,105,160,105,190],
		[
			"remaster_Boltam"
		],
		None,
		None
	),
	"Diveberg": MonsterData(
		"diveberg",
		"ice",
		[100,160,150,125,135,130],
		[
			"remaster-Ice Coating_Diveal"
		],
		"Ice Coating Sticker",
		None
	),
	"Adeptile": MonsterData(
		"adeptile",
		"astral",
		[110,80,180,150,180,100],
		[
			"remaster-Magic Tome_Salamagus"
		],
		"Magic Tome Sticker",
		None
	),
	"Trapwurm": MonsterData(
		"trapwurm",
		"earth",
		[120,150,120,90,120,90],
		[
			"The Marshes",
			"Spider Cave"
		],
		"Basic Tape",
		"bootleg_tape"
	),
	"Wyrmaw": MonsterData(
		"wyrmaw",
		"earth",
		[150,180,130,110,130,100],
		[
			"New Landkeeper Hideout",
			"remaster_Trapwurm"
		],
		None,
		None
	),
	"Ferriclaw": MonsterData(
		"ferriclaw",
		"metal",
		[90,140,100,90,140,140],
		[
			"Spider Cave"
		],
		"Basic Tape",
		"bootleg_tape"
	),
	"Auriclaw": MonsterData(
		"auriclaw",
		"metal",
		[100,170,100,100,170,160],
		[
			"remaster_Ferriclaw"
		],
		None,
		None
	),
	"Picksie": MonsterData(
		"picksie",
		"earth",
		[130,130,130,130,130,150],
		[
			"Spider Cave"
		],
		"Optical Laser Tape",
		"bootleg_tape"
	),
	"Pawper": MonsterData(
		"bear1",
		"beast",
		[120,130,100,100,120,130],
		[
			"Recruited Sunny",
			"New Landkeeper Hideout"
		],
		None,
		"bootleg_tape"
	),
	"Pawprince": MonsterData(
		"bear2",
		"beast",
		[140,160,110,110,140,140],
		[
			"remaster_Pawper"
		],
		None,
		None
	),
	"Minosteam": MonsterData(
		"minosteam",
		"metal",
		[150,180,180,120,120,90],
		[
			"Quest People are People"
		],
		"Optical Laser Tape",
		"bootleg_tape"
	),
	"Magikrab": MonsterData(
		"magikrab",
		"astral",
		[105,160,105,160,150,120],
		[
			"remaster-astral_Traffikrab"
		],
		"Black Shuck's Tape",
		"Ritual Candle",
		lambda options: options.special_monsters == True
	),
	"Amphare": MonsterData(
		"amphare",
		"lightning",
		[120,100,120,100,80,80],
		[
			"Funworld"
		],
		"Basic Tape",
		"bootleg_tape",
		lambda options: options.use_pier == True
	),
	"Blunderbusk": MonsterData(
		"blunderbusk",
		"fire",
		[150,120,150,150,100,130],
		[
			"remaster_Charlequin"
		],
		"Basic Tape",
		"bootleg_tape",# same as Charlequin for split remaster
		lambda options: options.use_pier == True
	),
	"Charlequin": MonsterData(
		"charlequin",
		"fire",
		[80,110,80,120,100,110],
		[
			"The Witch House",
			"Cosmic Zone",
			"Funworld"
		],
		"Basic Tape",
		"bootleg_tape",
		lambda options: options.use_pier == True
	),
	"Fragliacci": MonsterData(
		"fragliacci",
		"fire",
		[100,140,100,170,160,130],
		[
			"remaster_Charlequin"
		],
		None,
		None,
		lambda options: options.use_pier == True
	),
	"Hauntome": MonsterData(
		"hauntome",
		"air",
		[110,180,150,180,80,100],
		[
			"The Witch House"
		],
		"Chrome Tape",
		"bootleg_tape",
		lambda options: options.use_pier == True
	),
	"Lapacitor": MonsterData(
		"lapacitor",
		"lightning",
		[150,125,150,125,150,100],
		[
			"remaster_Amphare"
		],
		None,
		None,
		lambda options: options.use_pier == True
	),
	"Littlered": MonsterData(
		"littlered",
		"beast",
		[100,100,100,100,100,100],
		[
			"The Witch House"
		],
		None,
		None,
		lambda options: options.use_pier == True
	),
	"Majortom": MonsterData(
		"majortom",
		"metal",
		[150,150,150,110,110,130],
		[
			"remaster_Minortom"
		],
		None,
		None,
		lambda options: options.use_pier == True
	),
	"Minortom": MonsterData(
		"minortom",
		"metal",
		[130,130,130,70,70,70],
		[
			"Cosmic Zone"
		],
		"Basic Tape",
		"bootleg_tape",
		lambda options: options.use_pier == True
	),
	"Rosehood": MonsterData(
		"rosehood",
		"plant",
		[160,110,100,160,110,160],
		[
			"remaster_Littlered"
		],
		None,
		None,
		lambda options: options.use_pier == True
	),
	"Scarleteeth": MonsterData(
		"scarleteeth",
		"beast",
		[110,160,160,100,160,110],
		[
			"remaster-Carnivore_Littlered"
		],
		"Carnivore Sticker",
		None,
		lambda options: options.use_pier == True
	),
	"Umbrahella": MonsterData(
		"umbrahella",
		"poison",
		[150,120,140,170,200,60],
		[
			"warehouse"
		],
		"Optical Laser Tape",
		"bootleg_tape",
		lambda options: options.use_pier == True
	),
}

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

def monsters(options=None) -> dict:
	if not options:
		return monster_data_table
	return {key: value for key, value in monster_data_table.items() if
		(value.requires and value.requires(options)) or not value.requires}

def monsterCount(options=None) -> int:
	return len(monsters(options))