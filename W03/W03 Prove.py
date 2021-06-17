import tkinter as tk


def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.

    draw_sky(canvas, 0, 0)


    draw_ground(canvas, 800, 75, 500)

    draw_sun(canvas, 100, 700, 50)

    draw_cloud(canvas, 100, 100, 120, 60)
    draw_cloud(canvas, 150, 125, 110, 55)
    draw_cloud(canvas, 400, 160, 200, 75)

    x = 10
    while x < 810:
        draw_fence_post(canvas, x, 525, 165)
        x = x + 30


# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.

def draw_sky(canvas, width, height):

    sky_left = -height
    sky_top = -width
    sky_right = -height
    sky_bottom = -width

    canvas.create_rectangle(sky_left, sky_top, sky_right, sky_bottom, outline="lightblue1", width=10000)

def draw_ground(canvas, width, ground_height, height):
    ground_left = 0
    ground_top = height
    ground_right = width
    ground_bottom = height - ground_height

    canvas.create_rectangle(ground_left, ground_top, ground_right, ground_bottom, outline="green", width=2, fill="lightgreen")


def draw_sun(canvas, center_x, center_y, radius):

    sun_left = center_y - radius
    sun_right = center_y + radius
    sun_top = center_x - radius
    sun_bottom = center_x + radius

    canvas.create_oval(sun_left, sun_top, sun_right, sun_bottom, outline="orange", width=3, fill="yellow")

def draw_cloud(canvas, center_x, center_y, width_x, width_y):
    cloud_left = center_x - (width_x / 2)
    cloud_right = center_x + (width_x / 2)
    cloud_top = center_y - (width_y / 2)
    cloud_bottom = center_y + (width_y / 2)

    canvas.create_oval(cloud_left, cloud_top, cloud_right, cloud_bottom, outline="gray", width=0, fill="white")

def draw_fence_post(canvas, topright_x, topright_y, post_height):

    post_width = post_height / 8
    post_height = post_height
    post_left = topright_x - post_width / 2
    post_right = topright_x + post_width / 2
    post_bottom = topright_y - post_height
    post_top = topright_y

    canvas.create_rectangle(post_left, post_top, post_right, post_bottom, outline="gray20", width=1, fill="white")

# Call the main function so that
# this program will start executing.
main()