extends SceneTree


func _initialize() -> void:
	call_deferred("_build")


func _build() -> void:
	var tile_set := TileSet.new()
	tile_set.tile_size = Vector2i(80, 80)
	tile_set.add_physics_layer()
	var atlas := TileSetAtlasSource.new()
	atlas.texture = load("res://assets/platform.png")
	atlas.texture_region_size = Vector2i(80, 80)
	tile_set.add_source(atlas, 0)
	atlas.create_tile(Vector2i.ZERO)
	var tile_data := atlas.get_tile_data(Vector2i.ZERO, 0)
	tile_data.set_collision_polygons_count(0, 1)
	tile_data.set_collision_polygon_points(0, 0, PackedVector2Array([
		Vector2(-40, -40), Vector2(40, -40),
		Vector2(40, 40), Vector2(-40, 40)
	]))
	var result := ResourceSaver.save(tile_set, "res://tileset.tres")
	if result != OK:
		push_error("Could not save TileSet")
		quit(1)
		return

	var level: Node2D = load("res://main.tscn").instantiate()
	var ground := level.get_node("Ground")
	level.remove_child(ground)
	ground.free()

	var map := TileMapLayer.new()
	map.name = "TileMap"
	map.tile_set = load("res://tileset.tres")
	level.add_child(map)
	map.owner = level
	for x in range(16):
		map.set_cell(Vector2i(x, 7), 0, Vector2i.ZERO)

	var heart := Sprite2D.new()
	heart.name = "Heart"
	heart.position = Vector2(440, 490)
	heart.texture = load("res://assets/heart.png")
	heart.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	level.add_child(heart)
	heart.owner = level

	var scene := PackedScene.new()
	result = scene.pack(level)
	if result == OK:
		result = ResourceSaver.save(scene, "res://main.tscn")
	if result != OK:
		push_error("Could not save main scene")
		quit(1)
		return
	quit()
