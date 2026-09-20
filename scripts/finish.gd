extends Area2D

signal reached

var pulse_time := 0.0

@onready var sprite: Sprite2D = $Sprite2D


func _ready() -> void:
	body_entered.connect(_on_body_entered)


func _process(delta: float) -> void:
	pulse_time += delta * 3.0
	sprite.scale = Vector2.ONE * (1.0 + sin(pulse_time) * 0.035)


func _on_body_entered(body: Node2D) -> void:
	if body is CharacterBody2D:
		set_deferred("monitoring", false)
		reached.emit()
