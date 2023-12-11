import time


def animate_frames(frames):

    for frame in frames:
        print(frame)
        time.sleep(1.05)


if __name__ == "__main__":
    animation_frames = ["i am Eli Kiprop ", "pursuing BSC in Information Technology ", "Year 3", "Maseno University", "Thank you!"]

    animate_frames(animation_frames)
