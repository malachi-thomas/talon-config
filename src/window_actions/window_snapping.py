from talon import Context, Module, ui

mod, ctx = Module(), Context()

mod.list("window_snap_positions")

def window_snapper(window, pos):
  screen = window.screen.visible_rect
  x=screen.x + (screen.width * pos.left)
  y=screen.y + (screen.height * pos.top)
  width=screen.width * (pos.right - pos.left)
  height=screen.height * (pos.bottom - pos.top)
  window.rect = ui.Rect(round(x), round(y), round(width), round(height))

class Rect:
  def __init__(self, left, top, right, bottom):
    self.left = left
    self.top = top
    self.bottom = bottom
    self.right = right

window_positions = {
  "left": Rect(0, 0, 0.5, 1),
  "right": Rect(0.5, 0, 1, 1),
  "up": Rect(0, 0, 1, 0.5),
  "down": Rect(0, 0.5, 1, 1),
  "center": Rect(1 / 3, 0, 2 / 3, 1),
  "left small": Rect(0, 0, 1 / 3, 1),
  "right small": Rect(2 / 3, 0, 1, 1),
  "left large": Rect(0, 0, 2 / 3, 1),
  "right large": Rect(1 / 3, 0, 1, 1),
  "up left": Rect(0, 0, 0.5, 0.5),
  "up right": Rect(0.5, 0, 1, 0.5),
  "down left": Rect(0, 0.5, 0.5, 1),
  "down right": Rect(0.5, 0.5, 1, 1),
  "up left small": Rect(0, 0, 1 / 3, 0.5),
  "up right small": Rect(2 / 3, 0, 1, 0.5),
  "up left large": Rect(0, 0, 2 / 3, 0.5),
  "up right large": Rect(1 / 3, 0, 1, 0.5),
  "up center small": Rect(1 / 3, 0, 2 / 3, 0.5),
  "down left small": Rect(0, 0.5, 1 / 3, 1),
  "down right small": Rect(2 / 3, 0.5, 1, 1),
  "down left large": Rect(0, 0.5, 2 / 3, 1),
  "down right large": Rect(1 / 3, 0.5, 1, 1),
  "down center small": Rect(1 / 3, 0.5, 2 / 3, 1),
  "center": Rect(1 / 8, 1 / 6, 7 / 8, 5 / 6),
  "full": Rect(0, 0, 1, 1),
  "fullscreen": Rect(0, 0, 1, 1),
}

ctx.lists["user.window_snap_positions"] = window_positions.keys()

@mod.capture(rule="{user.window_snap_positions}")
def window_snap_position(m) -> Rect:
    return window_positions[m.window_snap_positions]

@mod.action_class
class Actions:
  def snap_window(position: Rect) -> None:
    ""
    window_snapper(ui.active_window(), position)