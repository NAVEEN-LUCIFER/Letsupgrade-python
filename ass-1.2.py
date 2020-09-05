altitude=int(input("ENTER THE CURRENT ALTITUDE OF THE PLANE (in ft.) :"))
if(altitude<=1000):
    print("PILOT! LAND THE PLANE SAFELY")
elif(altitude>1000 and altitude<=5000):
    print("PILOT! PLEASE COME DOWN FOR 1000ft  FOR A SAFE LANDING")
else:
    print("PILOT! PLEASE TURN AROUND THE PLANE AND COME DOWN TO 1000 ft FOR A SAFE LANDING")
