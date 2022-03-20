import drown_time
import argparse
if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Calculate when the sea level will reach your location')
    parser.add_argument('latitude', type=float,
                    help='Latitude')
    parser.add_argument('longitude', type=float,
                    help='Longitude')

    args = parser.parse_args()
    print(drown_time.drown_time(args.latitude,args.longitude))

