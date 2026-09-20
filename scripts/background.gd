extends Node2D

const SKY_TOP := Color("#ffeaf5")
const SKY_BOTTOM := Color("#f6a5cb")
const CLOUD := Color("#fff6fb")


func _draw() -> void:
	for strip in range(36):
		var color := SKY_TOP.lerp(SKY_BOTTOM, strip / 35.0)
		draw_rect(Rect2(-200, strip * 24 - 120, 5600, 24), color)

	for i in range(17):
		var x := i * 330.0 - 100.0
		var y := 120.0 + float((i * 67) % 150)
		_draw_cloud(Vector2(x, y))

	for i in range(13):
		var x := i * 420.0 - 260.0
		draw_colored_polygon(PackedVector2Array([
			Vector2(x, 760), Vector2(x + 210, 470 + (i % 3) * 25),
			Vector2(x + 440, 760)
		]), Color("#ee9fc5"))

	for i in range(18):
		var x := i * 285.0 + 80.0
		var y := 205.0 + float((i * 83) % 220)
		_draw_heart(Vector2(x, y), 0.6 + (i % 3) * 0.2)


func _draw_cloud(center: Vector2) -> void:
	draw_circle(center + Vector2(-30, 8), 23, CLOUD)
	draw_circle(center + Vector2(0, -7), 32, CLOUD)
	draw_circle(center + Vector2(31, 7), 25, CLOUD)
	draw_rect(Rect2(center + Vector2(-42, 5), Vector2(86, 22)), CLOUD)


func _draw_heart(center: Vector2, scale_factor: float) -> void:
	var points := PackedVector2Array()
	for i in range(33):
		var angle := i * TAU / 32.0
		var x := 16.0 * pow(sin(angle), 3)
		var y := -(13.0 * cos(angle) - 5.0 * cos(2.0 * angle)
			- 2.0 * cos(3.0 * angle) - cos(4.0 * angle))
		points.append(center + Vector2(x, y) * scale_factor)
	draw_colored_polygon(points, Color(1.0, 1.0, 1.0, 0.36))
