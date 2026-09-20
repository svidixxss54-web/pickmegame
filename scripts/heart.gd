extends Area2D

signal collected

var start_y := 0.0
var float_time := 0.0


func _ready() -> void:
	start_y = position.y
	float_time = position.x * 0.01
	body_entered.connect(_on_body_entered)


func _process(delta: float) -> void:
	float_time += delta * 2.5
	position.y = start_y + sin(float_time) * 6.0


func _on_body_entered(body: Node2D) -> void:
	if body is CharacterBody2D:
		set_deferred("monitoring", false)
		collected.emit()
		queue_free()
