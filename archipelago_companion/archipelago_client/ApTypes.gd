## Mostly copied from Rampaging Hippy's Brotato implementation
extends Object

enum SlotType {
	SPECTATOR = 0b00
	PLAYER = 0b01
	GROUP = 0b10
}

enum Permission {
	DISABLED = 0b000
	ENABLED = 0b001
	GOAL = 0b010
	AUTO = 0b110
	AUTO_ENABLED = 0b111
}

enum NetworkItemFlags {
	NORMAL = 0
	PROGRESSION = 0b001
	IMPORTANT = 0b010
	TRAP = 0b100
}

enum ClientStatus {
	CLIENT_UNKOWN = 0
	CLIENT_CONNECTED = 5
	CLIENT_READY = 10
	CLIENT_PLAYING = 20
	CLIENT_GOAL = 30
}

enum DataStorageOperationType {
	REPLACE = 0
	DEFAULT = 1
	ADD = 2
	MUL = 3
	POW = 4
	MOD = 5
	FLOOR = 6
	CEIL = 7
	MAX = 8
	MIN = 9
	AND = 10
	OR = 11
	XOR = 12
	LEFT_SHIFT = 13
	RIGHT_SHIFT = 14
	REMOVE = 15
	POP = 16
	UPDATE = 17

}

const data_storage_operation_to_name = {
	DataStorageOperationType.REPLACE: "replace",
	DataStorageOperationType.DEFAULT: "default",
	DataStorageOperationType.ADD: "add",
	DataStorageOperationType.MUL: "mul",
	DataStorageOperationType.POW: "pow",
	DataStorageOperationType.MOD: "mod",
	DataStorageOperationType.FLOOR: "floor",
	DataStorageOperationType.CEIL: "ceil",
	DataStorageOperationType.MAX: "max",
	DataStorageOperationType.MIN: "min",
	DataStorageOperationType.AND: "and",
	DataStorageOperationType.OR: "or",
	DataStorageOperationType.XOR: "xor",
	DataStorageOperationType.LEFT_SHIFT: "left_shift",
	DataStorageOperationType.RIGHT_SHIFT: "right_shift",
	DataStorageOperationType.REMOVE: "remove",
	DataStorageOperationType.POP: "pop",
	DataStorageOperationType.UPDATE: "update",
}

class NetworkVersion:
	var major: int
	var minor: int
	var build: int

	static func from_command_data(data: Dictionary) -> NetworkVersion:
		var network_version = NetworkVersion.new()
		network_version.major = data["major"]
		network_version.minor = data["minor"]
		network_version.build = data["build"]

		return network_version

class NetworkPlayer:
	var team: int
	var slot: int
	var alias: String
	var name: String

class NetworkItem:
	var item: int
	var location: int
	var player: int
	var flags: int

class NetworkPlayerCon:
	var team: int
	var slot: int
	var players: Array
	var missing_locations: PoolIntArray
	var checked_locations: PoolIntArray
	var slot_data: Dictionary
	var slot_info: Dictionary
	var hint_points: int

class NetworkSlot:
	var name: String
	var game: String
	var type: int
	var group_members: PoolIntArray

class Hint:
	var receiving_player: int
	var finding_player: int
	var location: int
	var item: int
	var found: bool
	var entrance: String = ""
	var item_flags: int = 0

class JsonMessagePart:
	var type: String
	var text: String
	var color: String
	var flags: int
	var player: int

class DataPackageContents:
	var games: Dictionary

class GameData:
	var item_name_to_id: Dictionary
	var location_name_to_id: Dictionary
	var version: int
	var checksum: String

class DeathLinkData:
	var time: float
	var cause: String
	var source: String

class RoomInfo:
	var version: NetworkVersion
	var generator_version: NetworkVersion
	var tags: PoolIntArray
	var password: bool
	var permissions: Dictionary
	var hint_cost: int
	var location_check_points: int
	var games: PoolStringArray
	var datapackage_versions: Dictionary
	var datapackage_checksums: Dictionary
	var seed_name: String
	var time: float

	static func from_command(command: Dictionary) -> RoomInfo:
		if command["cmd"] != "RoomInfo":
			return null

		var room_info = RoomInfo.new()
		room_info.version = NetworkVersion.from_command_data(command["version"])
		room_info.generator_version = NetworkVersion.from_command_data(command["generator_version"])
		room_info.tags = PoolIntArray(command["tags"])
		room_info.password = command["password"]
		room_info.permissions = command["permissions"]
		room_info.hint_cost = command["hint_cost"]
		room_info.location_check_points = command["location_check_points"]
		room_info.games = PoolStringArray(command["games"])
		room_info.datapackage_versions = command["datapackage_versions"]
		room_info.datapackage_checksums = command["datapackage_checksums"]
		room_info.seed_name = command["seed_name"]
		room_info.time = command["time"]
		return room_info

class ConnectionRefused:
	var errors: PoolStringArray

class Connected:
	var team: int
	var slot: int
	var players: Array
	var missing_locations: PoolIntArray
	var checked_locations: PoolIntArray
	var slot_data: Dictionary
	var slot_info: Dictionary
	var hint_points: int

class ReceivedItems:
	var index: int
	var items: Array

class LocationInfo:
	var locations: Array

class RoomUpdate:
	var players: Array
	var checked_locations: PoolIntArray
	var missing_locations = null

class PrintJson:
	var data: Array
	var type: String
	var receiving: int
	var item: NetworkItem
	var found: bool
	var team: int
	var slot: int
	var message: String
	var tags: PoolStringArray
	var countdown: int

class DataPackage:
	var data: DataPackageContents

class Bounced:
	var games: PoolStringArray
	var slots: PoolIntArray
	var tags: PoolStringArray
	var data: Dictionary

class InvalidPacket:
	var type: String
	var original_cmd: String
	var text: String

class Retrieved:
	var keys: Dictionary

class SetReply:
	var key: String
	var value
	var original_value
