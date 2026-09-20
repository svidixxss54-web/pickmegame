extends Area2D

signal touched

@export var patrol_distance := 35.0
@export var patrol_speed := 1.5
@export var phase := 0.0

var home_x := 0.0
var patrol_time := 0.0

@onready var sprite: Sprite2D = $Sprite2D


func _ready() -> void:
	home_x = position.x
	patrol_time = phase
	body_entered.connect(_on_body_entered)


func _process(delta: float) -> void:
	patrol_time += delta * patrol_speed
	position.x = home_x + sin(patrol_time) * patrol_distance
	sprite.flip_h = cos(patrol_time) < 0.0


func _on_body_entered(body: Node2D) -> void:
	if body is CharacterBody2D:
		set_deferred("monitoring", false)
		touched.emit()
