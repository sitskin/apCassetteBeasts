extends UnlockPartnerAction

func _run():
	SaveState.set_flag("ap_event_recruited_%s" % partner_id, true)
	return ._run()
