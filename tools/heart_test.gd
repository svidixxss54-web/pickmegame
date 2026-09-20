extends SceneTree


func _initialize() -> void:
	call_deferred("_run")


func _run() -> void:
	var scene: Node2D = load("res://main.tscn").instantiate()
	root.add_child(scene)
	current_scene = scene
	var player: CharacterBody2D = scene.get_node("Player")
	var heart: Area2D = scene.get_node("Heart01")
	for frame in range(5):
		await physics_frame
	heart.global_position = player.global_position
	for frame in range(3):
		await physics_frame
	if scene.hearts_collected != 1:
		push_error("Heart pickup did not update the score")
		quit(1)
		return
	if scene.get_node("HUD/Score").text != "HEARTS  1 / 8":
		push_error("Score label is out of sync")
		quit(1)
		return
	if not scene.get_node("HeartSound").playing:
		push_error("Heart pickup sound did not play")
		quit(1)
		return
	print("Heart pickup test passed")
	quit()
