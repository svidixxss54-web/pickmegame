extends SceneTree


func _initialize() -> void:
	call_deferred("_run")


func _run() -> void:
	for action in ["left", "right", "jump"]:
		if not InputMap.has_action(action) or InputMap.action_get_events(action).size() < 2:
			_fail("Missing input action: %s" % action)
			return

	var scene: Node2D = load("res://main.tscn").instantiate()
	root.add_child(scene)
	current_scene = scene
	var player: CharacterBody2D = scene.get_node("Player")
	for frame in range(20):
		await physics_frame
	if not player.is_on_floor():
		_fail("Player did not land")
		return

	var starting_x := player.position.x
	Input.action_press("right")
	for frame in range(20):
		await physics_frame
	Input.action_release("right")
	if player.position.x < starting_x + 40.0:
		_fail("Player did not move right")
		return

	Input.action_press("jump")
	await physics_frame
	await physics_frame
	Input.action_release("jump")
	if player.velocity.y >= -100.0:
		_fail("Player did not jump")
		return
	if not scene.get_node("JumpSound").playing:
		_fail("Jump sound did not play")
		return

	print("Movement test passed")
	quit()


func _fail(message: String) -> void:
	push_error(message)
	quit(1)
