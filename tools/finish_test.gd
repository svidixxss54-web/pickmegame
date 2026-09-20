extends SceneTree


func _initialize() -> void:
	call_deferred("_run")


func _run() -> void:
	var scene: Node2D = load("res://main.tscn").instantiate()
	root.add_child(scene)
	current_scene = scene
	var player: CharacterBody2D = scene.get_node("Player")
	var finish: Area2D = scene.get_node("Finish")
	player.global_position = finish.global_position
	for frame in range(3):
		await physics_frame
	if not scene.won or not scene.get_node("HUD/WinPanel").visible:
		_fail("Finish did not show the win screen")
		return
	if not scene.get_node("WinSound").playing:
		_fail("Victory sound did not play")
		return

	scene._restart()
	for frame in range(3):
		await process_frame
	if current_scene == scene:
		_fail("Restart did not work after winning")
		return

	scene = current_scene
	player = scene.get_node("Player")
	var hazard: Area2D = scene.get_node("Hazard01")
	player.global_position = hazard.global_position
	for frame in range(3):
		await physics_frame
	if not scene.restarting or not scene.get_node("HUD/Notice").visible:
		_fail("Hazard did not trigger a retry")
		return
	if not scene.get_node("HitSound").playing:
		_fail("Hit sound did not play")
		return
	for frame in range(40):
		await physics_frame
	if current_scene == scene:
		_fail("Hazard did not restart the level")
		return

	print("Finish and hazard test passed")
	quit()


func _fail(message: String) -> void:
	push_error(message)
	quit(1)
