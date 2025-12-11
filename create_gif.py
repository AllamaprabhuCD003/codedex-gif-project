import imageio.v3 as iio
files=["team-pic1.png","team-pic2.png"]
images=[iio.imread(f"images/{x}") for x in files]
iio.imwrite("team.gif",images,duration=500,loop=0)