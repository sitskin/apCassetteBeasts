-- this is an example/default implementation for AP autotracking
-- it will use the mappings defined in item_mapping.lua and location_mapping.lua to track items and locations via their ids
-- it will also keep track of the current index of on_item messages in CUR_INDEX
-- addition it will keep track of what items are local items and which one are remote using the globals LOCAL_ITEMS and GLOBAL_ITEMS
-- this is useful since remote items will not reset but local items might
-- if you run into issues when touching A LOT of items/locations here, see the comment about Tracker.AllowDeferredLogicUpdate in autotracking.lua
ScriptHost:LoadScript("scripts/autotracking/item_mapping.lua")
ScriptHost:LoadScript("scripts/autotracking/location_mapping.lua")
ScriptHost:LoadScript("scripts/autotracking/event_mapping.lua")

CUR_INDEX = -1
LOCAL_ITEMS = {}
GLOBAL_ITEMS = {}
OBTAINED_ITEMS = {}

EVENTS = {
	"Recruited Kayleigh",
	"Recruited Eugene",
	"Recruited Meredith",
	"Recruited Felix",
	"Recruited Viola",
	"Recruited Barkley",
	"Defeated Oldgante",
	"Defeated Poppetox",
	"Defeated Mourningstar",
	"Defeated Nowhere Monarch",
	"Defeated Heckahedron",
	"Defeated Alice",
	"Defeated Robin Goodfellow",
	"Defeated Mammon",
	"Defeated Lamento Mori",
	"Defeated Babelith",
	"Defeated Shining Kuneko",
	"Defeated Morgante",
	"Defeated Helia",
	"Defeated Lenna",
	"Defeated Gwenivar",
	"Defeated Averevoir",
	"Met Ianthe",
	"Met Meredith",
	"Cleared Landkeeper Offices",
	"Defeated Aleph",
	"Became Captain",
	"Recruited Sunny",
	"Quest People are People"
}


function resetItems()
	for _, value in pairs(ITEM_MAPPING) do
		if value[1] then
			local obj = Tracker:FindObjectForCode(value[1])
			if obj then
				obj.Active = false
			end
		else
			print(string.format("resetItems: bad item code %s", value[1]))
		end
	end
end

function resetLocations()
	for id, value in pairs(LOCATION_MAPPING) do
		if id > 517 then goto continue end-- hardcoded skipping of unimplemented locations
		--print("loc_map", id, value)
		for _, code in pairs(value) do
			--print("value", _, code)
			--print(id, code)
			local obj = Tracker:FindObjectForCode(code)
			if obj then
				if code:sub(1,1) == "@" then
					obj.AvailableChestCount = obj.ChestCount
				else
					obj.Active = false
				end
			end
		end
		::continue::
	end
end

function resetEvents()
	for _, code in pairs(EVENT_MAPPING) do
		Tracker:FindObjectForCode(code).Active = false
	end
end


function onClear(slot_data)
	Tracker.BulkUpdate = true	
	if AUTOTRACKER_ENABLE_DEBUG_LOGGING_AP then
		print(string.format("called onClear, slot_data:\n%s", dump_table(slot_data)))
	end
	PLAYER_NUMBER = Archipelago.PlayerNumber or -1
	TEAM_NUMBER = Archipelago.TeamNumber or 0
	CUR_INDEX = -1
	resetItems()
	resetLocations()
	if PLAYER_NUMBER > -1 then
		resetEvents()
		for _, event in ipairs(EVENTS) do
			Archipelago:SetNotify({event})
			Archipelago:Get({event})
		end
	end
	Tracker.BulkUpdate = false
end

function onItem(index, item_id, item_name, player_number)
	if AUTOTRACKER_ENABLE_DEBUG_LOGGING_AP then
		print(string.format("called onItem, index: %s item_id %s item_name %s player_number %s", index, item_id, item_name, player_number))
	end
	if index <= CUR_INDEX then
		return
	end
	CUR_INDEX = index
	local value = ITEM_MAPPING[item_id]
	if not value then
		return
	end
	if not value[1] then
		if AUTOTRACKER_ENABLE_DEBUG_LOGGING_AP then
			print(string.format("onItem: could not find code for item id %s", item_id))
		end
		return
	end
	local obj = Tracker:FindObjectForCode(value[1])
	if obj then
		obj.Active = true
		table.insert(OBTAINED_ITEMS, value[1])
	elseif AUTOTRACKER_ENABLE_DEBUG_LOGGING_AP then
		print(string.format("onItem: could not object for code %s", value[1]))
	end
end

function onLocation(location_id, location_name)
	local value = LOCATION_MAPPING[location_id]
	if not value then
		if AUTOTRACKER_ENABLE_DEBUG_LOGGING_AP then
			print(string.format("onLocation: could not find location mapping for id %s", location_id))
		end
		return
	end
	for _, code in pairs(value) do
		local obj = Tracker:FindObjectForCode(code)
		if obj then
			if code:sub(1, 1) == "@" then
				obj.AvailableChestCount = obj.AvailableChestCount - 1
			else
				obj.Active = true
			end
		elseif AUTOTRACKER_ENABLE_DEBUG_LOGGING_AP then
			print(string.format("onLocation: could not find object for code %s", code))
		end
	end
end

-- apply everything needed from slot_data, called from onClear
function apply_slot_data(slot_data)
	-- put any code here that slot_data should affect (toggling setting items for example)
end

-- called when a locations is scouted
function onScout(location_id, location_name, item_id, item_name, item_player)
	if AUTOTRACKER_ENABLE_DEBUG_LOGGING_AP then
		print(string.format("called onScout: %s, %s, %s, %s, %s", location_id, location_name, item_id, item_name,
			item_player))
	end
	-- not implemented yet :(
end

-- called when a bounce message is received
function onBounce(json)
	if AUTOTRACKER_ENABLE_DEBUG_LOGGING_AP then
		print(string.format("called onBounce: %s", dump_table(json)))
	end
	-- your code goes here
end

function onNotify(key, value, old_value)
	if value ~= old_value then
		if AUTOTRACKER_ENABLE_DEBUG_LOGGING_AP then
			print(string.format("called onNotify: %s, %s, %s", key, value, old_value))
		end
		updateEvent(key, value)
	end
end

function onNotifyLaunch(key, value)
	if AUTOTRACKER_ENABLE_DEBUG_LOGGING_AP then
		print(string.format("called onNotifyLaunch: %s, %s", key, value))
	end
	updateEvent(key, value)
end

function updateEvent(key, value)
	for event, code in pairs(EVENT_MAPPING) do
		if event == key then
			local obj = Tracker:FindObjectForCode(code)
			if value == 1 then
				obj.Active = true
			else
				obj.Active = false
			end
		end
	end
end

-- add AP callbacks
-- un-/comment as needed
Archipelago:AddClearHandler("clear handler", onClear)
--if AUTOTRACKER_ENABLE_ITEM_TRACKING then
--	Archipelago:AddItemHandler("item handler", onItem)
--end
--if AUTOTRACKER_ENABLE_LOCATION_TRACKING then
--	Archipelago:AddLocationHandler("location handler", onLocation)
--end
-- Archipelago:AddScoutHandler("scout handler", onScout)
-- Archipelago:AddBouncedHandler("bounce handler", onBounce)
Archipelago:AddItemHandler("item handler", onItem)
Archipelago:AddLocationHandler("location handler", onLocation)
Archipelago:AddSetReplyHandler("notify handler", onNotify)
Archipelago:AddRetrievedHandler("notify launch handler", onNotifyLaunch)