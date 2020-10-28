import math

PI = math.pi
EARTH_R = 6371

def get_rad_latitude(deg, min, sec, dir):
        lat = (deg + min/60.0 + sec/3600) * PI / 180.0
        return lat if dir.upper() == 'N' else -lat

def get_rad_longitude(deg, min, sec, dir):
        long = (deg + min/60.0 + sec/3600) * PI / 180.0
        return long if dir.upper() == 'E' else -long

def hav(num): # hav(phi) = (sin(phi/2))^2
        return (math.sin(num/2)) ** 2





def get_a(lat_a, lat_b, lat_diff, long_diff):
        return hav(lat_diff) + math.cos(lat_a) * math.cos(lat_b) * hav(long_diff)

def get_distance(a):
        return 2*math.asin(math.sqrt(a)) * EARTH_R

def calculate_distance_prog():
        # Location a
        print('Input name and coordinate of A:  ')
        name_a = str(input('>>> Input name: '))
        arr1 = input('Latitude [deg min sec dir]: ')
        arr1 = arr1.split()
        lat_a = get_rad_latitude(float(arr1[0]), float(arr1[1]), float(arr1[2]), str(arr1[3]))
        print(lat_a)
        arr2 = input('Longitude [deg min sec dir]: ')
        arr2 = arr2.split()
        long_a = get_rad_longitude(float(arr2[0]), float(arr2[1]), float(arr2[2]), str(arr2[3]))
        print(long_a)

        print('Input name and coordinate of B:  ')
        name_b = str(input('>>> Input name: '))
        arr3 = input('Latitude [deg-min-sec-dir]: ')
        arr3 = arr3.split()
        lat_b = get_rad_latitude(float(arr3[0]), float(arr3[1]), float(arr3[2]), str(arr3[3]))
        print(lat_b)

        arr4 = input('Longitude [deg-min-sec-dir]: ')
        arr4 = arr4.split()
        long_b = get_rad_longitude(float(arr4[0]), float(arr4[1]), float(arr4[2]), str(arr4[3]))
        print(long_b)

        lat_diff = lat_b - lat_a
        long_diff = long_b - long_a

        a = get_a(lat_a, lat_b, lat_diff, long_diff)
        distance = get_distance(a)


        print('The distance from {} to {} is approximately: {:.2f}'.format(name_a, name_b, distance))

if __name__ == '__main__':

    calculate_distance_prog()
