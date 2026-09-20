extends Node2D

var hearts_collected := 0
var hearts_total := 0

@onready var score_label: Label = $HUD/Score


func _ready() -> void:
	var hearts := get_tree().get_nodes_in_group("hearts")
	hearts_total = hearts.size()
	for heart in hearts:
		heart.collected.connect(_on_heart_collected)
	_update_score()


func _on_heart_collected() -> void:
	hearts_collected += 1
	_update_score()


func _update_score() -> void:
	score_label.text = "HEARTS  %d / %d" % [hearts_collected, hearts_total]
