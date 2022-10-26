from draw2d import start_drawing, draw_line, draw_text, finish_drawing, draw_oval
def main():
          scene_width = 600
          scene_height = 375

          canvas = start_drawing('Grid', scene_width, scene_height)
          draw_grid(canvas, scene_width, scene_height, 50)

          finish_drawing(canvas)
def draw_grid(canvas, width, height, interval, color='blue'):
          #Draw a vertical line at every interval
          label_y = 15
          for x in range(interval, width, interval):
                    draw_line(canvas, x, 0, x, height, fill=color)
                    draw_text(canvas, x, label_y, f'{x}', fill=color)

          label_x = 15
          for y in range(interval, height, interval):
                    draw_line(canvas, 0, y, width, y, fill=color)
                    draw_text(canvas, label_x, y, f'{y}', fill=color)

main()