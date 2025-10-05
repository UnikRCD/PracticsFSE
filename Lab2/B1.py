# -*- coding: utf-8 -*-

def main():
    with open('inmap1.dat', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    first_line = lines[0].strip().split()
    num_locations = int(first_line[0])
    scale_factor = float(first_line[1])
    
    map_distances = []
    for i in range(1, len(lines)):
        line = lines[i].strip()
        if line: 
            map_distances.extend([float(x) for x in line.split()])
    
    filtered_distances = [map_distances[0]]
    for dist in map_distances[1:]:
        if dist > 0:
            filtered_distances.append(dist)
    
    mileage_distances = [dist * scale_factor for dist in filtered_distances]
    

    print("Alexandr Zhurko")
    print("Simple Map Distance Computations")
    print(f"Map Scale Factor: {scale_factor:.2f} miles per inch")
    print("Map\t| Mileage")
    print("Measure\t| Distance")
    print("-" * 20)
    
    total_map_distance = 0
    total_mileage = 0
    
    for i, (map_dist, mile_dist) in enumerate(zip(filtered_distances, mileage_distances), 1):
        print(f"+ {i}\t| {map_dist}\t| {mile_dist:.1f}")
        total_map_distance += map_dist
        total_mileage += mile_dist
    
    print(f"Total Distance: {total_mileage:.1f} miles")

if __name__ == "__main__":

    main()
