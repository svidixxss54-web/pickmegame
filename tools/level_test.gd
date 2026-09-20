extends SceneTree


func _initialize() -> void:
	call_deferred("_run")


func _run() -> void:
	var scene: Node2D = load("res://main.tscn").instantiate()
	root.add_child(scene)
	current_scene = scene

	var tiles: TileMapLayer = scene.get_node("TileMap")
	var camera: Camera2D = scene.get_node("Player/Camera2D")
	if tiles.get_used_cells().size() < 150:
		_fail("The extended level is missing platforms")
		return
	if scene.hearts_total != 8:
		_fail("The level should contain eight hearts")
		return

	var player: CharacterBody2D = scene.get_node("Player")
	player.global_position = Vector2(2500, 500)
	for frame in range(40):
		await process_frame
	if camera.get_screen_center_position().x < 1000.0:
		_fail("Camera did not follow the player")
		return

	player.global_position = Vector2(740, 1100)
	for frame in range(5):
		await physics_frame
	if current_scene == scene or current_scene.hearts_collected != 0:
		_fail("Falling did not restart the level")
		return

	print("Level and camera test passed")
	quit()


func _fail(message: String) -> void:
	push_error(message)
	quit(1)
