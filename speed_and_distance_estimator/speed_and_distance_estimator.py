import sys
sys.path.append('../')
from utils import measure_distance, get_foot_position
import cv2

class SpeedAndDistance_Estimator():
    def __init__(self):
        self.frame_window=5
        self.frame_rate = 24
        
    def add_speed_and_distance_to_tracks(self,tracks):
        total_distance = {}
        for object, object_tracks in tracks.items():
            if object == 'ball' or object == 'referee':
                continue
            number_of_frames = len(object_tracks)
            for frame_number in range(0,number_of_frames, self.frame_window):
                last_frame = min(frame_number + self.frame_window, number_of_frames - 1)

                
                for track_id,_ in object_tracks[frame_number].items():
                    if track_id not in object_tracks[last_frame]:
                        continue
                    
                    start_position = object_tracks[frame_number][track_id]['position_transformed']
                    end_position = object_tracks[last_frame][track_id]['position_transformed']
                
                    if start_position is None or end_position is None:
                        continue
                    
                    distance_covered = measure_distance(start_position,end_position)
                    time_elapsed = (last_frame-frame_number)/self.frame_rate
                    speed_meters_per_second = distance_covered/time_elapsed
                    speed_km_per_hour = speed_meters_per_second*3.6
                    
                    if object not in total_distance:
                        total_distance[object] = {}
                    
                    if track_id not in total_distance[object]:
                        total_distance[object][track_id] = 0
                        
                    total_distance[object][track_id] += distance_covered
                    
                    for frame_number_batch in range(frame_number,last_frame):
                        if track_id not in tracks[object][frame_number_batch]:
                            continue
                        object_tracks[frame_number_batch][track_id]['distance'] = total_distance[object][track_id]
                        tracks[object][frame_number_batch][track_id]['speed'] = speed_km_per_hour

    def draw_speed_and_distance(self,frames,tracks):
        output_frames = []
        for frame_number, frame in enumerate(frames):
            for object, object_tracks in tracks.items():
                if object == "ball" or object == "referee":
                    continue
                for _, track_info in object_tracks[frame_number].items():
                    if 'speed' in track_info:
                        speed = track_info.get('speed', None)
                        distance = track_info.get('distance', None)
                        if speed is None or distance is None:
                            continue
                        
                        bbox = track_info['bbox']
                        position = get_foot_position(bbox)
                        position = list(position)
                        position[1]+=40
                        position = tuple(map(int,position))
                        
                        text = f"Speed: {speed: .2f} km/h\nDistance: {distance: .2f} m"
                        frame = cv2.putText(frame,f"{speed: .2f} km/h",position, cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
                        frame = cv2.putText(frame,f"{distance: .2f} m",(position[0],position[1]+20), cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
                        
            output_frames.append(frame)        
        return output_frames            