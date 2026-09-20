extends Node2D

var hearts_collected := 0
var hearts_total := 0
var restarting := false

@onready var score_label: Label = $HUD/Score
@onready var player: CharacterBody2D = $Player


func _ready() -> void:
	var hearts := get_tree().get_nodes_in_group("hearts")
	hearts_total = hearts.size()
	for heart in hearts:
		heart.collected.connect(_on_heart_collected)
	player.fell.connect(_restart)
	_update_score()


func _on_heart_collected() -> void:
	hearts_collected += 1
	_update_score()


func _update_score() -> void:
	score_label.text = "HEARTS  %d / %d" % [hearts_collected, hearts_total]


func _restart() -> void:
	if restarting:
		return
	restarting = true
	get_tree().call_deferred("reload_current_scene")


func _unhandled_input(event: InputEvent) -> void:
	if event is InputEventKey and event.pressed and not event.echo and event.keycode == KEY_R:
		_restart()
