extends Battle


func increase_stamina():
	print("increase stamina bypass")
	yield(get_tree(), "idle_frame")
	# stamina increases shuffled into AP item pool
