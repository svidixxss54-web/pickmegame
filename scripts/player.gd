extends CharacterBody2D

signal fell
signal jumped

const SPEED := 370.0
const ACCELERATION := 2400.0
const STOP_SPEED := 900.0
const JUMP_VELOCITY := -900.0
const COYOTE_TIME := 0.10
const JUMP_BUFFER := 0.12

var gravity: float = ProjectSettings.get_setting("physics/2d/default_gravity")
var coyote_timer := 0.0
var jump_timer := 0.0

@onready var visual: Node2D = $Visual


func _physics_process(delta: float) -> void:
	if is_on_floor():
		coyote_timer = COYOTE_TIME
	else:
		coyote_timer = maxf(coyote_timer - delta, 0.0)
		velocity.y += gravity * delta

	if Input.is_action_just_pressed("jump"):
		jump_timer = JUMP_BUFFER
	else:
		jump_timer = maxf(jump_timer - delta, 0.0)

	if jump_timer > 0.0 and coyote_timer > 0.0:
		velocity.y = JUMP_VELOCITY
		jump_timer = 0.0
		coyote_timer = 0.0
		jumped.emit()

	var direction := Input.get_axis("left", "right")
	if direction != 0.0:
		velocity.x = move_toward(velocity.x, direction * SPEED, ACCELERATION * delta)
		visual.scale.x = -1.0 if direction < 0.0 else 1.0
	else:
		velocity.x = move_toward(velocity.x, 0.0, STOP_SPEED * delta)

	move_and_slide()
	if global_position.y > 1050.0:
		fell.emit()
