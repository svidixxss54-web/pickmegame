extends Node2D

var hearts_collected := 0
var hearts_total := 0
var restarting := false
var won := false

@onready var score_label: Label = $HUD/Score
@onready var notice_label: Label = $HUD/Notice
@onready var win_panel: Control = $HUD/WinPanel
@onready var win_detail: Label = $HUD/WinPanel/WinDetail
@onready var player: CharacterBody2D = $Player
@onready var jump_sound: AudioStreamPlayer = $JumpSound
@onready var heart_sound: AudioStreamPlayer = $HeartSound
@onready var hit_sound: AudioStreamPlayer = $HitSound
@onready var win_sound: AudioStreamPlayer = $WinSound


func _ready() -> void:
	var hearts := get_tree().get_nodes_in_group("hearts")
	hearts_total = hearts.size()
	for heart in hearts:
		heart.collected.connect(_on_heart_collected)
	for hazard in get_tree().get_nodes_in_group("hazards"):
		hazard.touched.connect(_on_player_hit)
	$Finish.reached.connect(_on_finish_reached)
	player.fell.connect(_on_player_hit)
	player.jumped.connect(_on_player_jumped)
	_update_score()


func _on_heart_collected() -> void:
	hearts_collected += 1
	heart_sound.play()
	_update_score()


func _update_score() -> void:
	score_label.text = "HEARTS  %d / %d" % [hearts_collected, hearts_total]


func _on_player_jumped() -> void:
	if not restarting and not won:
		jump_sound.play()


func _on_player_hit() -> void:
	if restarting or won:
		return
	restarting = true
	player.set_physics_process(false)
	player.velocity = Vector2.ZERO
	notice_label.show()
	hit_sound.play()
	await get_tree().create_timer(0.55).timeout
	get_tree().reload_current_scene()


func _on_finish_reached() -> void:
	if restarting or won:
		return
	won = true
	player.set_physics_process(false)
	player.velocity = Vector2.ZERO
	for hazard in get_tree().get_nodes_in_group("hazards"):
		hazard.set_process(false)
	win_detail.text = "You found %d of %d hearts!" % [hearts_collected, hearts_total]
	win_panel.show()
	win_sound.play()


func _restart() -> void:
	if restarting:
		return
	restarting = true
	get_tree().call_deferred("reload_current_scene")


func _unhandled_input(event: InputEvent) -> void:
	if event is InputEventKey and event.pressed and not event.echo and event.keycode == KEY_R:
		_restart()
